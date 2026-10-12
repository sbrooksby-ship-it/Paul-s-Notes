# Team Brain — Sync Protocol

*How Paul processes new information and updates the vault. Updated: September 23, 2026.*

---

## Default Behavior: Auto-Sync Everything

When you give Paul new information (transcript, audio recap, voice dump, conversation summary), Paul **automatically updates everything it touches** without asking:

1. **Meeting note** — created or updated in `Meetings/` or `1-on-1s/`
2. **Action Items** — any commitments extracted and added to `Master-Dashboard/Action Items.md`
3. **Profiles** — team member profiles OR people-you-make-commitments-to profiles updated
4. **Daily Log** — the day's activity noted in `Daily/YYYY-MM-DD - Day.md`
5. **Pulse** — updated if status changes significantly

You don't need to ask Paul to "also update the action items" or "also update the profile." Paul does it all as part of processing the info.

---

## What Triggers a Sync

| You give Paul… | Paul does… |
|---|---|
| A transcript (Gemini, Fireflies, Whisper text) | Creates/updates meeting note, extracts action items, updates profiles, updates daily log, updates pulse if needed |
| A voice dump (2-min audio recap) | Transcribes (if possible) or works from your recap, creates/updates note, updates everything |
| A conversation recap (like "Adrien came in, asked about recording, I said I'm working on it") | Creates/updates daily log, creates/updates person profiles if new people involved, adds commitments to Action Items |
| An audio file | Tries to transcribe (via Whisper text you paste, or Gemini API) — then processes as above |

---

## Person Profiles — Beyond the Team

Paul maintains profiles for:

- **Team members** (Michael, Sophia) — full profiles with wins, blockers, energy, working style, commitments
- **People you make commitments to** (Adrien, Brad, and anyone else you interact with where you make a promise) — lighter profiles, but tracking commitments is the key purpose

If you make a commitment to someone, that person gets a profile entry and the commitment goes in Action Items. This way you never lose track of a promise made to anyone.

---

## Recording → Transcription → Paul Workflow

**What works:**
1. Record with the HTML recorder (or phone memo, or Zoom/Meet built-in recording)
2. Transcribe with Whisper (paste me the text)
3. I process everything and auto-sync

**What doesn't work (yet):**
- I can't directly control the Whisper native app to transcribe audio you send me
- Python Whisper has DLL issues on this machine

**What's possible:**
- You paste me the Whisper transcript text → I process it
- OR you send me the audio and I transcribe via Gemini API (if you want to use that)

---

## What Paul Needs From You

- **Transcripts** — paste the text
- **Audio recaps** — record a 2-min voice dump after a meeting, transcribe with Whisper, paste the text
- **Conversation recaps** — just tell Paul what happened, like you did with Adrien today
- **Audio files** — if you want me to transcribe via Gemini API, send the file

---

*Updated September 23, 2026 — auto-sync is now the default. Profiles extend to anyone you make commitments to.*
