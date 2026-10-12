# Team Brain Setup Guide

*You now have a fully structured Obsidian vault for managing your team. Here's how it all fits together.*

---

## What Was Created

```
Team-Brain/                    ← Your vault root
├── 00-Inbox/                  ← Raw unprocessed dumps
├── Team-Profiles/
│   ├── Michael.md             ← Michael's living profile
│   └── Sophia.md              ← Sophia's living profile
├── 1-on-1s/                  ← Meeting notes go here (organized by person)
├── Master-Dashboard/
│   ├── README.md             ← Your home base
│   └── Action Items.md       ← All open tasks, auto-synced by Paul
├── Recordings/
│   ├── Audio/                ← Voice memos + meeting recordings
│   └── Transcripts/          ← Gemini transcripts + Paul's transcriptions
├── Templates/
│   ├── 1-on-1-Note.md        ← Template for meeting notes
│   └── Team-Member-Profile.md ← Template for profiles
└── Resources/
    ├── Voice Dump Guide.md   ← How to do voice dumps
    └── Meet-Gemini-Integration.md ← How Gemini transcripts flow in
```

---

## Your First Steps

### 1. Open the vault in Obsidian

1. Open Obsidian
2. **File → Open folder as vault**
3. Navigate to: `C:\Users\sbrooksby\Documents\Team-Brain`
4. You'll see the full structure

### 2. Fill in the basics on each profile

Open [[Team Profiles/Michael]] and [[Team Profiles/Sophia]] and add:
- Their role
- When they started
- What you already know about their strengths and working style

This takes 5 minutes and makes the system immediately useful.

### 3. Do your first voice dump

After your next 1-on-1:
1. Open your phone's voice memo app (or Windows Voice Recorder)
2. Record 2 minutes of your raw impressions
3. Send the audio file to Paul in Hermes chat
4. Paul processes it and files everything

### 4. Ask Paul a question

Try: *"What do I know about Michael so far?"* or *"Give me a check-in question for Sophia"*

---

## Recording Options for Voice Dumps

You don't need anything fancy. Pick what you already have:

| Tool | Platform | Notes |
|---|---|---|
| **Phone voice memo** | iOS / Android | Simplest. Record → share to desktop → drag to Paul |
| **Windows Voice Recorder** | Windows | Pre-installed. Saves .m4a in `Documents/Voice Memos` |
| **OBS Studio** | Windows (free) | If you want to record full meetings too — screen + audio |
| **Audacity** | Windows (free) | Audio-only recording, more control |

**For just post-meeting dumps:** phone memo or Windows Voice Recorder is perfect. 2 minutes, done.

**For recording full meetings (alternative to Gemini):** OBS Studio records your screen + system audio + mic to a local file. Then Paul can transcribe it. Set it up if you want a backup or if Gemini isn't available for a meeting.

---

## How Paul Fits In

Paul is your librarian. You talk to Paul in Hermes chat. Paul:

- Accepts audio files (drag and drop)
- Transcribes them (using available tools)
- Structures them into your templates
- Updates team profiles
- Extracts and tracks action items
- Answers questions about your team

**Paul's system prompt** includes your exact templates so every note is consistent.

---

## Questions?

Ask Paul anything like:
- "How do I record a voice dump?"
- "Where do Gemini transcripts go?"
- "Show me what's in Michael's profile"
- "Set up OBS for meeting recording"
