# Check-In Questions Engine

*Interactive system for generating context-aware check-in questions. Ask @paul things like "give me a check-in question for Michael today" and this engine powers the response.*

---

## How It Works

When you ask for check-in questions, I pull from multiple sources in order of specificity:

1. **Last meeting's follow-up questions** — questions that were specifically suggested for next time (highest priority)
2. **Aging promises / action items** — things that have been open too long
3. **Open blockers** — things that need follow-up
4. **The person's meeting framework** — questions that work well for them specifically
5. **Energy trend** — if energy is declining, tailor questions to check in on wellbeing
6. **General manager questions** — fallback if nothing else applies

The more meetings you've had, the more specific and useful the questions get.

---

## Question Sources (Priority Order)

### 1. Last Meeting's Follow-Up Questions

Each 1-on-1 note includes a "Follow-Up Questions for Next Time" section. These are the highest-value questions because they're directly connected to what came up last time.

**Example (Michael, from Sep 21 meeting):**
- "Did you get a chance to send that agent list over?"
- "How are you tracking on hours this week?"
- "Anything you've been wanting to get involved in outside your core role?"

### 2. Aging Promises / Action Items

Anything open more than 7 days gets flagged. Questions surface naturally:
- "I'm still waiting on X — any update?"
- "We agreed to Y last week — how's that going?"

### 3. Open Blockers

Anything in the person's "Blockers (Active)" section or "Things to Ask About" in their prep card.

### 4. Person-Specific Framework

Each person has a "Meeting Framework" note with questions that work well for them specifically. For Michael, these include:
- Success/metrics framing (he responds well to it)
- Direct probe for blockers (he doesn't volunteer them)
- Project interest (he's a "yes person" — check capacity)

### 5. Energy Trend

If energy has been declining, questions shift from "what are you working on?" to "how are you doing?" — more about wellbeing than output.

### 6. General Manager Questions (Fallback)

Questions that work for anyone:
- "What's a win this week?"
- "Anything frustrating you?"
- "How can I help?"
- "What's the biggest thing on your plate right now?"

---

## How to Ask

| You say | I do |
|---|---|
| "Give me a check-in question for Michael today" | Pull from sources 1-6, give 2-3 context-aware questions with reasoning |
| "What should I ask Sophia this week?" | Same, tailored to Sophia's profile status |
| "I'm meeting with Michael in 10 minutes — what do I ask?" | Urgent mode — pull the top 3 must-ask questions |
| "What are good questions for a first meeting with a new direct report?" | General framework you can apply to Sophia |
| "Give me questions for both Michael and Sophia" | Side-by-side, each tailored |

---

## Example Response (Michael)

> **You asked:** "Give me a check-in question for Michael today"
>
> **Here's what I'd suggest:**
>
> **Must-ask (follow-up from last meeting):**
> *"Did you get a chance to pull together that agent list? Want to make sure I have the latest."*
> → This has been outstanding since Sep 21. It's the #1 aging item.
>
> **Probe for blockers (he doesn't volunteer them):**
> *"Anything frustrating this week — processes, tools, anything at all? Even small stuff."*
> → He hasn't reported any blockers yet but that may be because he doesn't naturally flag them. One more direct probe this week.
>
> **Development / rapport:**
> *"You mentioned being interested in projects outside your core role — anything you've been wanting to kick off?"*
> → He's a "yes person" and available for projects. Worth circling back.

---

## Building the Question Bank

Over time, as you have more meetings, the question bank for each person grows. These come from:

- **Your voice dumps** — when you say "I should ask her about X next time," that becomes a suggested question
- **Their responses** — questions that get good responses get added to their framework
- **Recurring themes** — if X keeps coming up, the question bank reflects that

The goal: after 6 months, you have a rich set of questions that actually work for each person — not generic manager questions, but questions tuned to how Michael and Sophia think and communicate.

---

## Integration with Meeting Prep Cards

Each person's "Meeting Prep Card" includes a "Questions to Ask This Meeting" section that's generated from this engine. Before each meeting:

1. Open the prep card
2. Scroll to "Questions to Ask This Meeting"
3. Those questions are already pulled from the engine — specific to where things stand right now
4. Bring 2-3 of them into the meeting

You don't need to ask @paul for questions every time — the prep card has them. But if you want fresh ones or a different angle, asking @paul works too.

---

*This engine powers every check-in question @paul generates. The quality improves with every meeting.*
