# Mark OS Demo — Meeting Log (Oct 5)

**When:** Monday, October 5, 2026 (watched; meeting was too long to watch live — transcript reviewed from recording)
**Presenter:** Marius Ciocirlan (Mark OS — 2-yr startup, Bessemer Ventures; clients include VW, Centauri, King of England, White Claw)
**On our side:** James Ford (lead), Ben Bybee, Brett Andersen (compliance), Spencer McMullin (marketing), Dakota Cox (design), Shannon Gardner (first time seeing it)
**Your note:** Mark O said **we need to provide the claims to him** (the claim sheet / approved claims).

---

## What Mark OS IS (so you can talk about it)

**Not a content generator. Not another AI writer.** Mark OS is an AI review layer embedded into the tools you already use — Premiere (video), Photoshop (images), Asana (briefs/approvals) — plus its own dashboard. It reviews content **before it goes out**, scanning for regulatory issues, brand safety, brand elements, and performance best practices. The goal: catch problems in round 1, not round 3, reducing review cycles.

Core mechanism: decomposes images/video into scenes/frames/copy; each rule runs an agentic workflow with benchmarks and consistency checks; results are deterministic (not random AI guesses), with consistency scores (e.g., 100% fail/pass reliability).

---

## Key sections covered (with timestamps, so you can reference specific moments)

| Time  | Topic                                                              | Key point                                                                                                                                                                                                                                                                              |
| ----- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 00:09 | Intro / ethos                                                      | "Content hits the mark every time" — brand safe, compliant, high-performing at scale                                                                                                                                                                                                   |
| 00:12 | How it works                                                       | Reviews images/audio/video; embedded in production tools; gives bird's-eye view of what's live                                                                                                                                                                                         |
| 00:14 | Pre-loaded rules                                                   | Laws/regulations, platform best practices (Meta/YouTube/TikTok), regional/cultural understanding, trademarks, copyrights                                                                                                                                                               |
| 00:15 | **YOUR CLAIMS → THEIR SYSTEM** (⚠️ **the commitment you flagged**) | "You give us a **claim list** — what claims you can/cannot make — and we train on it." The rebuilt pipeline (call flow + sheets → Supabase) feeds this. Mark OS uses the claim sheet as source material when reviewing briefs. **This is why you need to provide the claims to Mark.** |
| 00:16 | Self-updating standards                                            | They track updates; notify you of rule changes; allow back-audits of historical content against new rules                                                                                                                                                                              |
| 00:19 | Their audit of our live content                                    | Only 8% of our creative followed 4/6 Meta best practices; Nature's Bounty at 80%; industry average 40–50%. Cost of non-compliance: 37–42% higher delivery cost on Meta                                                                                                                 |
| 00:21 | Dashboard / brand health scores                                    | Adherence metrics per brand; highlights high-risk content                                                                                                                                                                                                                              |
| 00:27 | Pre-check flow (video demo)                                        | Upload → review <30 sec → red/yellow/green; flags off-label use (e.g., "Sprayd only approved for ornamental plants and lawns" vs. vegetable plant depiction)                                                                                                                           |
| 00:29 | **BRIEF REVIEW (Asana extension)** — this is where claims matter   | Scans brief text for claim violations; pulls from **our claim sheet** and shows approved alternatives; flags issues like "this claim is US-only but brief covers US + UK"                                                                                                              |
| 00:30 | Influencer check (Kate Sigman example)                             | Scans people in creative against contracts and brand-fit; flagged Kate for controversial behavior (Grand Canyon incident) incompatible with Slothful's nature/environment brand                                                                                                        |
| 00:32 | Premiere plugin — live production check                            | Checks within video timeline; flags logo clear space, text legibility, audio sync issues, copyrighted music, color-gradient banding                                                                                                                                                    |
| 00:35 | Image rights / facial recognition                                  | Identifies people in video (e.g., Case Dudley); checks contract expiration; flags expired image rights                                                                                                                                                                                 |
| 00:39 | Review workflow / approval stages                                  | Multi-stage approvals (brand → legal → etc.); comments feed back into system; approval/rejection trains future reviews                                                                                                                                                                 |
| 00:43 | Attention detection                                                | Predictive analysis of where viewer attention lands; useful for ensuring disclaimers/calls-to-action are in high-attention zones                                                                                                                                                       |
| 00:45 | Packaging checks                                                   | Catches incorrect volume conversions; compares against master artwork; detects changes (e.g., scaled-down strawberry illustration)                                                                                                                                                     |
| 00:47 | Rule training (effortless tone example)                            | Human annotates → AI learns → consistency tracked; they manage the process; 30-min weekly check-in with you                                                                                                                                                                            |
| 00:50 | Our audit results (deep dive reference)                            | Only 8% following rules; competitors far ahead                                                                                                                                                                                                                                         |
| 00:53 | Sandbox / onboarding (Ben's question)                              | Sandbox available; 30-day hands-on test. Phase 1 = 2 weeks (standard rules); Phase 2 = 2–6 weeks (custom claims, contracts, image rights, brand policy). Without custom training: overly cautious (many false positives)                                                               |
| 01:03 | Google doc / brand policy integration (Dakota's question)          | **Can integrate with live Google doc** (James asked if brand policy updates sync automatically). They recommend Mark OS as system of record, but can set up link-checking                                                                                                              |

---

## Key people/roles in meeting
- **James Ford** — our lead; led Q&A; asked about Google doc sync; negotiating scope/volume/pricing
- **Ben Bybee** — wants hands-on sandbox; asks about onboarding timeline; cautious about FDA compliance
- **Brett Andersen / Sherry** — compliance; Brett confirms the tool fits marketing/creative workflow but that compliance team benefits from pre-filtered content
- **Spencer McMullin** — marketing; sees value in tracking live content and best-practices score
- **Dakota Cox** — design; excited by Premiere/Photoshop integration; asks about live Google doc updates
- **Shannon Gardner** — first exposure; confirmed alignment with expectations

---

## Your open commitment (⚠️ flagged)

> **We need to provide the claims to Mark.**

The rebuilt pipeline (redid call flow + rebuilt sheets feeding call evals into Supabase) produces the evidence. That feeds the claim sheet Mark OS uses during review. Action item added to daily note.

---

## What to say in future conversations about this meeting

- **What Mark OS is:** AI review layer embedded in production/design/approval tools; not a generator. Checks brand, legal, and performance before content goes live.
- **Why it's relevant to us:** Our audit showed only 8% of live creative met Meta best practices (vs. 40–50% industry average); non-compliance costs 37–42% more in delivery.
- **What we need from them:** A claim sheet (the rebuilt Supabase pipeline feeds this); brand policies; contracts/image rights; 30-day sandbox; then 2–6 week custom training.
- **The contract:** Annual; pricing based on volume/brands/products/scope.
- **Your role:** Provide claims + coordinate onboarding; rebuilt pipeline is the source.
