# Google Calendar → Obsidian Sync Setup

*Step-by-step guide to connect your Google Calendar to Paul so he can see your schedule, prep you for meetings, and be proactive.*

---

## What This Does

Once set up, a script runs twice daily (7:00 AM and 2:00 PM Mountain Time) to pull your Google Calendar events into your Obsidian vault. Paul then reads these files and can:

- See your meetings before they happen
- Prep you with the right profile, prep card, or context
- Prompt you to do your 2-min voice dump after a meeting
- Generate Weekly Briefings from your actual schedule

---

## Step 1: Create a Google Cloud Project

1. Go to [console.cloud.google.com](https://console.cloud.google.com/)
2. Click the project dropdown at the top → **New Project**
3. Name it something like **"Team Brain Calendar"** — you can leave the Organization as is
4. Click **Create**
5. Wait for it to be created, then select it from the dropdown

---

## Step 2: Enable the Google Calendar API

1. In your project, go to **APIs & Services** → **Library**
2. Search for **"Google Calendar API"**
3. Click it → **Enable**

---

## Step 3: Configure the OAuth Consent Screen

1. Go to **APIs & Services** → **OAuth consent screen**
2. Choose **External** (user type) — this is fine even for a personal Google account
3. Fill in:
   - **App name:** `Team Brain Calendar`
   - **User support email:** Your email
4. Click **Next** through the Scopes and Test Users sections (you can skip these for now — we'll add the scope when we create the credential)
5. Click **Publish** at the end (or "Save and Publish")
   - *Note: If it says "Testing" mode, that's fine too — you'll just need to add your email as a test user. But Publishing is simpler.*

---

## Step 4: Create OAuth Credentials (Desktop App)

1. Go to **APIs & Services** → **Credentials**
2. Click **Create Credentials** → **OAuth client ID**
3. Application type: **Desktop app**
4. Name: `Team Brain Calendar Sync`
5. Click **Create**
6. A JSON file downloads — this is your `credentials.json`
7. **Rename it to `credentials.json`** (if it downloaded with a long name) and place it at:

   ```
   C:\Users\sbrooksby\Downloads\Team-Brain\Admin\credentials.json
   ```

   *(Or anywhere you prefer — just tell Paul where it is.)*

---

## Step 5: First Run — OAuth Token Generation

Once `credentials.json` is in place, the sync script needs to run **once manually** to generate a `token.json` file. This is the one-time OAuth dance.

### Option A: I run it for you right now

Just tell me: *"credentials.json is in place, run the first sync"* — and I'll execute the script. It will:
1. Open a browser window asking you to sign in to Google
2. You approve access to your Calendar
3. The script saves `token.json` automatically
4. Subsequent runs use the saved token — no browser needed

### Option B: You run it yourself

```bash
cd "C:/Users/sbrooksby/Downloads/Team-Brain/Admin"
python3 -m Scripts.calendar_sync
```

Or run the script directly:
```bash
python3 "C:/Users/sbrooksby/AppData/Local/hermes/profiles/paul/scripts/calendar-sync.py"
```

The script will print a URL. Open it in your browser, sign in, approve, and copy the code back if prompted. After that, `token.json` is saved and all future runs are silent.

---

## Step 6: What the Script Produces

After a successful sync, you'll see new files in:

```
Admin/Google-Calendar/
├── 2026-09-23.md          ← Today's meetings (updated twice daily)
└── Upcoming.md            ← Next 7 days of meetings (updated twice daily)
```

**Example `2026-09-23.md`:**

```markdown
# 📅 2026-09-23 — Google Calendar

*Auto-synced from Google Calendar — last updated: 07:00 AM MDT*

---

## 1. Call Evaluation Coaching
- **Time:** 08:00 AM – 09:00 AM MDT
- **Date:** Wednesday, September 23, 2026
- **Location:** Google Meet
- **Link:** [Open in Google Calendar](...)
- **Attendees:** rafa@..., aaron@..., elena@..., samuel@...

---

## 2. 1-on-1 with Sophia
- **Time:** 02:00 PM – 02:30 PM MDT
- **Date:** Wednesday, September 23, 2026
- **Location:** Google Meet
- **Link:** [Open in Google Calendar](...)
```

---

## Step 7: Cron Jobs (Automatic Runs)

Two cron jobs are configured to run automatically:

| Job | Schedule | What it does |
|---|---|---|
| **Morning sync** | Weekdays at 7:00 AM MDT | Fetches today's events, writes `YYYY-MM-DD.md` + `Upcoming.md` |
| **Afternoon sync** | Weekdays at 2:00 PM MDT | Re-fetches in case anything changed mid-day |

Both are currently **paused** (waiting for you to complete OAuth setup first). Once you tell me the token is generated, I'll resume both.

---

## Step 8: Tell Paul It's Ready

Once `credentials.json` is in place and the first run has generated `token.json`, just tell me:

> *"Calendar credentials are set up, token is generated, resume the cron jobs."*

I'll:
1. Verify the token file exists
2. Resume both cron jobs
3. Do an immediate sync to populate today's calendar file
4. Start using the calendar data in our conversations

---

## Troubleshooting

### "credentials.json not found"
Make sure the file is named exactly `credentials.json` and is in the right place.

### "Token expired / invalid"
Delete `token.json` and run the script manually again (Option B above). It will re-do the OAuth flow.

### Browser doesn't open during OAuth
The script prints a URL. Copy-paste it into your browser manually. After approving, it should redirect and the script will pick up the token.

### "Daily Limit Exceeded"
Google Calendar API has generous quotas for personal use. If you hit a limit, wait 24 hours and it resets.

---

## Security Notes

- `credentials.json` contains your OAuth client ID and secret — treat it like a password
- `token.json` contains your access/refresh tokens — also sensitive
- Both files should **not** be shared or committed to any public repo
- The script only requests `calendar.readonly` scope — it can read your calendar but not modify it
- Everything stays on your machine — no data leaves except the API call to Google

---

*Last updated: September 23, 2026*
