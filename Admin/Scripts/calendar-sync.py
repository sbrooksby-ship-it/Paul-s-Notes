#!/usr/bin/env python3
"""
Google Calendar → Obsidian sync script.
Fetches today's events from the user's primary Google Calendar
and writes them to a vault-usable markdown file.

Config:
  - VAULT_ADMIN_DIR: folder to write calendar files to (edit for your setup)
  - CREDENTIALS_FILE: path to credentials.json (from Google Cloud Console)
  - TOKEN_FILE: path to token.json (auto-created after first run)

Timezone: uses the system local timezone (Mountain Time on this machine).
"""

import datetime
import json
import os
import sys
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# ─── Configuration ───────────────────────────────────────────────────────────

VAULT_ADMIN_DIR = Path(
    os.environ.get(
        "VAULT_ADMIN_DIR",
        str(Path.home() / "Downloads" / "Team-Brain" / "Admin" / "Google-Calendar"),
    )
)
CREDENTIALS_FILE = os.environ.get(
    "GOOGLE_CALENDAR_CREDENTIALS",
    str(Path.home() / "Downloads" / "Team-Brain" / "Admin" / "credentials.json"),
)
TOKEN_FILE = os.environ.get(
    "GOOGLE_CALENDAR_TOKEN",
    str(Path.home() / "Downloads" / "Team-Brain" / "Admin" / "token.json"),
)

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

# ─── Auth ─────────────────────────────────────────────────────────────────────


def get_credentials() -> Credentials:
    """Load or obtain OAuth credentials. Returns valid Credentials object."""
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                print(
                    f"ERROR: credentials.json not found at {CREDENTIALS_FILE}",
                    file=sys.stderr,
                )
                print(
                    "Download it from Google Cloud Console and place it there.",
                    file=sys.stderr,
                )
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES
            )
            # port=0 lets the OS pick an open port; flow.print_server_thread
            # prints the URL. We suppress the thread output and let the user
            # copy-paste if no browser opens.
            try:
                creds = flow.run_local_server(port=0)
            except Exception as exc:
                print(
                    f"Browser launch failed ({exc}). Open the URL printed above "
                    "in your browser and paste the code back here if prompted.",
                    file=sys.stderr,
                )
                raise
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())
    return creds


# ─── Fetch ────────────────────────────────────────────────────────────────────


def fetch_events(service, days_ahead: int = 2) -> list[dict]:
    """Return list of {start, end, summary, location, description, uid, link} dicts."""
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    # Start from 6am local today so we don't miss early meetings
    local_tz = datetime.datetime.now().astimezone().tzinfo
    start_of_today_local = datetime.datetime.now(local_tz).replace(
        hour=0, minute=0, second=0, microsecond=0
    ).astimezone(datetime.timezone.utc)

    end_dt = start_of_today_local + datetime.timedelta(days=days_ahead)

    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=start_of_today_local.isoformat(),
            timeMax=end_dt.isoformat(),
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    raw_events = events_result.get("items", [])

    out = []
    for event in raw_events:
        start_raw = event.get("start", {})
        end_raw = event.get("end", {})
        start = start_raw.get("dateTime", start_raw.get("date"))
        end = end_raw.get("dateTime", end_raw.get("date"))

        # Skip all-day events from yesterday that have already ended
        if start and end:
            try:
                start_dt = datetime.datetime.fromisoformat(
                    start.replace("Z", "+00:00")
                ).astimezone(local_tz)
                end_dt_ev = datetime.datetime.fromisoformat(
                    end.replace("Z", "+00:00")
                ).astimezone(local_tz)
                now_local = datetime.datetime.now(local_tz)
                # All-day events: compare dates
                if "T" not in start:  # all-day
                    today = now_local.date()
                    event_date = datetime.datetime.fromisoformat(start).date()
                    if event_date < today:
                        continue
                else:  # timed
                    if end_dt_ev < now_local:
                        continue
            except (ValueError, TypeError):
                pass

        out.append(
            {
                "start": start,
                "end": end,
                "summary": event.get("summary", "[No Title]"),
                "location": event.get("location", ""),
                "description": event.get("description", ""),
                "uid": event.get("id", ""),
                "html_link": event.get("htmlLink", ""),
                "status": event.get("status", ""),
                "organizer": (
                    event.get("organizer", {}).get("email", "")
                    if event.get("organizer")
                    else ""
                ),
                "attendees": [
                    a.get("email", "")
                    for a in event.get("attendees", [])
                    if a.get("self") is not True
                ],
            }
        )
    return out


# ─── Render ───────────────────────────────────────────────────────────────────


def render_markdown(events: list[dict], date_str: str) -> str:
    """Render events as a markdown file."""
    local_tz = datetime.datetime.now().astimezone().tzinfo

    lines = [
        f"# 📅 {date_str} — Google Calendar",
        "",
        f"*Auto-synced from Google Calendar — last updated: {datetime.datetime.now(local_tz).strftime('%I:%M %p %Z')}*",
        "",
        "---",
        "",
    ]

    if not events:
        lines.append("*No events found for this period.*")
        lines.append("")
        return "\n".join(lines)

    today_str = datetime.date.today().isoformat()

    for i, ev in enumerate(events, 1):
        # Parse start time
        start = ev["start"]
        end = ev["end"]

        if "T" in start:
            try:
                start_dt = datetime.datetime.fromisoformat(
                    start.replace("Z", "+00:00")
                ).astimezone(local_tz)
                end_dt = datetime.datetime.fromisoformat(
                    end.replace("Z", "+00:00")
                ).astimezone(local_tz)
                time_range = f"{start_dt.strftime('%I:%M %p')} – {end_dt.strftime('%I:%M %p')} {start_dt.strftime('%Z')}"
                date_label = start_dt.strftime("%A, %B %d, %Y")
            except (ValueError, TypeError):
                time_range = "All day"
                date_label = "All day event"
        else:
            # All-day event
            try:
                ev_date = datetime.datetime.fromisoformat(start).date()
                date_label = ev_date.strftime("%A, %B %d, %Y")
            except (ValueError, TypeError):
                date_label = "All day"
            time_range = "All day"

        lines.append(f"## {i}. {ev['summary']}")
        lines.append("")
        lines.append(f"- **Time:** {time_range}")
        lines.append(f"- **Date:** {date_label}")
        lines.append(f"- **Event ID:** `{ev['uid']}`")

        if ev["status"]:
            lines.append(f"- **Status:** {ev['status']}")

        if ev["location"]:
            lines.append(f"- **Location:** {ev['location']}")

        if ev["organizer"]:
            lines.append(f"- **Organizer:** {ev['organizer']}")

        if ev["html_link"]:
            lines.append(f"- **Link:** [Open in Google Calendar]({ev['html_link']})")

        if ev["attendees"]:
            attendees_str = ", ".join(ev["attendees"][:10])
            if len(ev["attendees"]) > 10:
                attendees_str += f" +{len(ev['attendees']) - 10} more"
            lines.append(f"- **Attendees:** {attendees_str}")

        if ev["description"]:
            desc = ev["description"].strip()
            # Clean up description formatting
            desc_clean = " ".join(desc.split())
            lines.append(f"- **Description:** {desc_clean}")

        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


# ─── Main ─────────────────────────────────────────────────────────────────────


def main():
    local_tz = datetime.datetime.now().astimezone().tzinfo
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    today_display = datetime.date.today().strftime("%A, %B %d, %Y")

    VAULT_ADMIN_DIR.mkdir(parents=True, exist_ok=True)

    print(f"🔍 Fetching Google Calendar events for {today_display}…")

    creds = get_credentials()
    service = build("calendar", "v3", credentials=creds)

    events = fetch_events(service, days_ahead=2)

    # Split into today vs upcoming
    today_start = datetime.datetime.now(local_tz).replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    today_end = today_start + datetime.timedelta(days=1)

    today_events = []
    upcoming_events = []

    for ev in events:
        start_str = ev["start"]
        if "T" in start_str:
            try:
                ev_dt = datetime.datetime.fromisoformat(
                    start_str.replace("Z", "+00:00")
                ).astimezone(local_tz)
            except (ValueError, TypeError):
                upcoming_events.append(ev)
                continue
        else:
            # All-day: use the date
            try:
                ev_dt = datetime.datetime.fromisoformat(start_str).replace(
                    tzinfo=local_tz
                )
            except (ValueError, TypeError):
                upcoming_events.append(ev)
                continue

        if today_start <= ev_dt < today_end:
            today_events.append(ev)
        else:
            upcoming_events.append(ev)

    # Write today's calendar
    today_file = VAULT_ADMIN_DIR / f"{date_str}.md"
    today_content = render_markdown(today_events, date_str)
    today_file.write_text(today_content, encoding="utf-8")
    print(f"✅ Wrote today's calendar: {today_file}")

    # Write/upcoming file (next 7 days view for planning)
    upcoming_file = VAULT_ADMIN_DIR / "Upcoming.md"
    upcoming_content = render_markdown(upcoming_events, "Next 7 Days")
    # Only write if there's something or file doesn't exist
    if upcoming_events or not upcoming_file.exists():
        upcoming_file.write_text(upcoming_content, encoding="utf-8")
        print(f"✅ Wrote upcoming events: {upcoming_file}")
    elif not upcoming_events:
        print("ℹ️  No upcoming events beyond today — skipping Upcoming.md refresh")

    # Summary for stdout (cron delivery)
    print("")
    print(f"📊 Calendar sync complete — {date_str}")
    print(f"   Today's events: {len(today_events)}")
    print(f"   Upcoming events: {len(upcoming_events)}")

    if today_events:
        print("")
        print("─── Today's meetings ───")
        for ev in today_events:
            start = ev["start"]
            if "T" in start:
                try:
                    t = datetime.datetime.fromisoformat(
                        start.replace("Z", "+00:00")
                    ).astimezone(local_tz)
                    time_str = t.strftime("%I:%M %p")
                except (ValueError, TypeError):
                    time_str = "All day"
            else:
                time_str = "All day"
            print(f"   [{time_str}] {ev['summary']}")
            if ev["location"]:
                print(f"           📍 {ev['location']}")


if __name__ == "__main__":
    main()
