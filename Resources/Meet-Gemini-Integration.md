# Google Meet + Gemini Integration

*Your Google Meet recordings are transcribed by Gemini. Here's how they flow into your Team Brain.*

---

## Current Setup

- **Meetings:** Google Meet (recording enabled)
- **Transcription:** Gemini auto-transcribes each meeting
- **Output:** Transcript files saved by Gemini

---

## Getting Transcripts Into the Vault

### Option A — Drag and Drop (Simple)

1. Find the Gemini transcript (.txt, .md, or .docx)
2. Drag it into `Recordings/Transcripts/` in Obsidian, OR into a Hermes chat with Paul
3. Tell Paul: *"Incorporate the Gemini transcript from [meeting]"*
4. Paul reads it, extracts what matters, and updates the relevant team profile + creates a 1-on-1 note if appropriate

### Option B — Folder Watch (Automated)

If Gemini saves transcripts to a consistent folder, Paul can watch that folder and auto-process new ones. Tell Paul where Gemini saves them and we'll set this up.

---

## What Paul Extracts from a Gemini Transcript

From a full meeting transcript, Paul pulls:

- **Key decisions made**
- **Action items** (who said they'd do what)
- **Blockers mentioned**
- **Wins or progress noted**
- **Sentiment / energy signals** (if discernible from tone/word choice)
- **Follow-up topics** that didn't get resolved

These get folded into the team member's profile and the 1-on-1 note for that meeting.

---

## Voice Dump vs. Gemini Transcript

| | **Your Voice Dump** | **Gemini Transcript** |
|---|---|---|
| **What it is** | Your post-meeting impressions | The full meeting record |
| **Best for** | Your reads, promises, vibes | What was actually said, decisions |
| **When** | Within 2 min of meeting ending | After Gemini finishes transcribing |
| **Paul does** | Structures + profiles + tasks | Extracts + cross-references + flags |

**Best practice:** Use both. The voice dump captures what only you know. The transcript captures what everyone said. Paul merges them.
