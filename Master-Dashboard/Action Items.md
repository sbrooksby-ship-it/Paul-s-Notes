# Action Items

*Everything you owe your team AND people you make commitments to — extracted automatically from your voice dumps, transcripts, and conversation recaps by Paul. Auto-synced on every update.*

**Last synced:** October 8, 2026

---

## 🔴 Due Soon / Overdue

*All clear as of today (Wed 9/30). Previously overdue items resolved last week — see Recently Done below.*

---

## 🟡 This Week (Mon 10/12 – Sun 10/18)

*Active tasks with deadlines this week.*

- [ ] **Follow up with team members on cohort reports — Sherry's cohort (Division 3)** — Seven is responsible for following up with team members' reports. Must ensure metrics have correlation AND causation, not just correlation.

- [ ] **add jev to grade AI for sales call**

- [ ] **Hear back from Sherry — she'll follow up with me** — Sherry said she'll follow up with Seven on cohort metrics. Track this.
- [ ] **Adjust compliance AI tool to see if agents are leading them** — Review whether the compliance AI tool is properly guiding agents, or if agents are leading/redirecting the AI's responses.

- [ ] **Build checklist examiner bot** — A bot that examines checklists when agents add them, summarizes the outs (what was missed/disapproved), and emails the summary to whoever needs it (Rafa, Jared, Aaron — whoever I need to send it to). Self-managed — I handle all Streamlit + automation work alone.

- [x] **🔴 Ask Brad: can our app be used by other teams/departments? (Samuel's question)** — Oct 7. Samuel raised the question that our app may be usable beyond our own group — Seven needs to **ask Brad when he's back in town next Monday (Oct 12).** Brad was off all week Oct 5–9. **This is a scope/permission question, not a build question** — worth asking before anyone builds on the assumption it's shareable. Samuel's own words: Dept 15 "can help with any training that you need."

- [ ] **Watch whether Care automation waits for Dept 14 mock training** — Sales pilots this week, Care likely next week. Dept 14 planning a mock training with a test, possibly this week. Worth asking whether Care goes live in parallel with the mock or waits for the result.

---

## 🟢 Upcoming (Next Week+)

*- [ ] **Michael side project — checklist automation** — Michael gathers "true sources" for checklist items; AI (JEV/Solar) marks pass/fail. Won't count toward his call eval stats. 2-hr Friday block (10/16, 2-4 PM). Needs: criteria doc, intake process.
  - [ ] File the "side projects don't count toward stats" agreement in Michael's profile.
  - [ ] Set up intake process for Michael (vault folder vs. shared doc).
  - [ ] Finalize "What Makes a Source 'True'" criteria doc.
  - [ ] Schedule weekly 2-hr block for Michael on Friday.

*- [ ] **JEV AI — parameters & alerts (due Friday 10/30)** — Set up JEV parameters for auditors to remove/flag data from the front end. Create easier visibility for JEV flags. Set up alert for "no customer interaction." Ensure the alert accounts for flagged data removal.
  - [ ] Auditor data removal parameters for JEV
  - [ ] Simpler JEV flags visibility
  - [ ] Alert for "no customer interaction"

*- [ ] **A.I.M Executive Report — quarterly report** — First draft due first week of January. File a quarterly A.I.M report with:
  - Key findings & observations (past 3 months)
  - Findings from Call Listen-Ins
  - Findings from Dept. 15 meetings & working with AIM team members
  - What BoN has done to support AIM and improve performance
  - Trainings held or provided
  - Recommendations from Division 5
  - Overall quality score and any trends

*- [ ] **Next Michael check-in** — ~October 5, 2026 (Monday of next week). Recrrent invite still needs to be created.

*- [ ] **Next Sophia check-in** — ~October 6, 2026 (Tuesday of next week). Recurring invite still needs to be created.

---

## ✅ Recently Done

**Oct 7 (Wed):**
- [x] **Call Review Coaching — first week under the 80/20 format, rollout live** — attended with Samuel, Sophia, Jared, Aaron, Elena, Rafa. 2 lowest points only (ARC-4 + PE-2), 4 calls capped by Sophia. Meeting note: `Meetings/2026-10/2026-10-07 - Call Review Coaching - ARC-4 and PE-2.md`.
- [x] **ARC-4 compliance conversation with Sheila** — held before the meeting; **Samuel confirmed clean, no follow-up needed.** Closed the high-priority item blocking Rafa. (Gathering-data follow-up still unconfirmed.)
- [x] **Advanced Playbook approved** — Seven's TLs reviewed and approved it; IAA = Dept 15 signed off. Whitney's approval granted Oct 6.
- [x] **Team lead attendance DECIDED — one TL at a time, rotating weekly** — settles the open question from Sep 30.
- [x] **Meeting moved 8:00 AM → 9:00 AM starting next week** — Elena raised it (too early for Amsterdam); Samuel owns updating the recurring invite.
- [x] **Care automation flagged AT RISK** — 3 of 4 care agents quit last week + 1 on sick leave; training on standby, no one to train. Sales pilots this week; Care needs a staffing check before go-live.
- [x] **No exemplar call exists in the company** — Sophia: "we don't have close to 100%, but I can get you as close to it as possible." Sophia sending best available examples this week.
- [x] **Phantom agent "Kyle" found in the Customer Sales heat map** — scored all 1s, no agent named Kyle exists. Suspected a customer name misparsed as an agent name. Fix the parser, not the data.
- [x] **Amon has resigned** — surfaced via Jared relaying Rafa (Oct 6). Previously under Michael's agents; team still needs verification.
- [x] **Discovered ARC-4 and PE-2 are the same coaching point** — discovery questions → acknowledgements → feeling seen and heard → more ARC-4. Fix one and the other moves.

**Oct 6 (Tue):**
- [x] **Playbook approval granted** — final approval to give the Advanced Playbook to agents.
- [x] **Compliance Training (Div 5), 1–2 PM** — attended.

**Oct 5 (Mon):**
- [x] **Dept 13 Weekly Sync** — Aaron, Sophia, Seven (Michael out — medical procedure; Brad off all week). Key outcomes: (1) **Seven's call-eval sharing proposal APPROVED — team leads can now share call evals with their team members.** This is the fix for the Oct 2 rollout confusion; root cause was that TLs/agents didn't know what they were scored on and Brad pushed back on direct sharing. (2) Sales calls pilot the automation this week, Care likely next week. (3) Aaron updated inactive checklists to the new pillar format — **Brad approved Friday.** Issue authorities sent to Lindsay; Taylor, Albert, Jen, Alicia, Rafa pending. (4) Aaron now emails checklists for feedback instead of scheduling meetings — meetings are review/approval only. (5) This week's checklist focus: 16A (Data & Intelligence), starting with director Sam. (6) Agent guide submitted, awaiting Dept 14 sign-off. Meeting note: `Meetings/2026-10/2026-10-05 - Department 13 Weekly Sync.md`.

**Oct 2 (Fri):**
- [x] **🔴 Fixed all 4 broken cron jobs** — all failing on the model change (3 unpinned drift-skips + 1 HTTP 404 on Solar Pro 4 free tier ending). Pinned every job to `stealth/space-bunny-alpha` via `hermes cron edit`. **Calendar sync had been silently broken since the model switch.**
- [x] **Brad approved the call rollout** — the 3-week phased automation plan is greenlit (Sales first, monitoring week, then Care at full scale). Gating approval for 100% call grading coverage.
- [x] **Call playbook — matrix portion sent to Whitney (Dept 14 trainer) for approval** — Brad's feedback was to keep just the matrix portion.
- [x] **Impromptu call with Michael Barreto** — he flagged that Tamara was unaware the checklist/call eval were live. Rollout communication gap identified. Meeting note: `Meetings/2026-10/2026-10-02 - Michael Barreto - Checklist Rollout Confusion.md`.

**Oct 1 (Thu):**
- [x] **Send proposal to Adrien (VP Division 5)** — sent. `Projects/Catalog-Project-Enterprise-Verification-Engine-Proposal.md`
- [x] **Q3 commission recommendations** — completed.

**Sep 30 (Wed):**
- [x] **Call Review Coaching — NEW MEETING FORMAT + 80/20 rule** — Samuel restructured the meeting: open with previous week's action steps, AI eval data picks the lowest points, set specific plans, Gorgias open during review. **3 focus points:** ARC4 (authentic personal experience / success story), discovery questions / personal education, COM3 (offering the survey). Team average 57.67% (103.8/180), goal 80% (144/180). Tone improved significantly; message still transactional. Meeting note: `Meetings/2026-09/2026-09-30 - Call Review Coaching - New Format ARC-4 and PE-2.md`.
- [x] **Jared proposed combining Div 4/5 meetings + including team leads** — Samuel, Aaron, Sophia all supported. **Elena's approval needed.**
- [x] **Met with Adrien (VP Division 5)** — went over the product catalog and explained the GraphRAG approach.
- [x] **Call eval report for team leads — Aaron — COMPLETED** — Aaron out sick; report pulled with actual call scores alongside outs per Jared's request. Ready to send when Aaron returns.
- [x] **Playwright call upload method — COMPLETED** — Aaron out sick; automated call upload flow finished.
- [x] **Sales coaching session (9 AM) cancelled** — Sophia declined both sessions; team carrying sales.

**Sep 29 (Tue):**
- [x] **Gaia AI demo** — Cody Cloward demoed Gorgias's new Gaia AI assistant. Team decided to use freely during early access. Meeting note: `Meetings/2026-09/2026-09-29 - Gorgias Gaia AI Demo.md`.
- [x] **Met with Cody Cloward (Director of Communications)** — everyone having databases, MCP server (build it or StarkSys does it). Jared likes the MCP server idea.
- [x] **Met with Sherry (Division 3 Director)** — cohort metrics. Seven responsible for following up on team member reports. Metrics must have correlation AND causation.
- [x] **Jared wants call scores in the report with the outs** — noted: include actual scores alongside outs.
- [x] **Follow up with Michael on non-checklist call eval storage** — he stores them separately; once reflected they move to the team system.
- [x] **Follow up with Whitney on test results** — idioms features tested Sep 25; got the results.
- [x] **Brad's meeting structure questions — ANSWERED** — care checklists vs. sales meetings, and how to distribute checklist due dates.
- [x] **Monitor hours (Michael)** — kept under 42 hrs/week per Brad's directive. Tracked and reported.
- [x] **Get Brad's board into a Google Doc** — built and shared.

**Sep 25 (Fri):**
- [x] **Call eval agent list — Sophia** — RECEIVED. 14 agents: Danilyn Suaybaguio, Mariz Talavera, Raul Canales Gallegos, Thelma Alondra Monsivais Hernandez, Miguel Angel Huerta Alvarez, Jhonathan Gadiuel Gonzalez Lemos, Adriel Hezraí Gámez García, Amon Feitosa, Carlos Fernandes, Tyrone Merejildo, Marcos Vazquez, Rose Ferdinand, Karl Nikko de Leon, Michael Nkanta.
- [x] **Agent list — Michael** — RECEIVED. 10 agents: Roman Jair Nuñez Perales, Jesus Abelandonio Martinez Guzman, Patrick Sam-MBOMA, Imelda Cardona Casillas, Michel Alejandro Sandoval Ochoa, Denia Naomi Cazares Salazar, Miguel Angel Rodriguez Salazar, Nestor Alfredo Govea Gonzalez, Francisco Miguel Bautista Madrigal, Sergio Garibay Gallegos. TLs excluded: Tamara Garrocho, Jose Moreno.
- [x] **Reach out to Rafa** — DONE (replied Sep 25): examiner continues meeting with TLs, he's invited to those meetings, summary of the outs + focus areas still helpful.
- [x] **Reach out to Jared** — DONE (replied Sep 25): examiner continues with team leads, still invited as optional, summary of the outs + focus areas still helpful.
- [x] **Upload "As a Man Thinketh" workbook** — uploaded.
- [x] **Cedric replied to Streamlit question** — after ~1 month: "We deployed streamlit and PostgreSQL we just need to understand how you will access streamlit." Answered with corporate VPN + GitHub Git pull.
- [x] **First 1-on-1s** — Michael (Sep 21), Sophia (Sep 22).

**Sep 24 (Thu):**
- [x] **Streamlit app — fix** — was deleting/overwriting raw data each day (data loss). Fixed by switching to append-only.
- [x] **Fix missing Supabase -> Streamlit data flow** — resolved the connection so Streamlit can read/write to Supabase properly.
- [x] **Start Paperclip integration** — beginning to get Paperclip involved in the workflow.
- [x] **End-game AI vision for ecosystem** — four-pillar autonomous architecture documented. Cross-vault: `obsidian://open?vault=MyVault&file=Main Notes/Ai Vision for D5.md`

---

## Open action items by person:

- [[Team Profiles/Michael]] → Hours monitoring (ongoing), bi-weekly calendar invite pending
- [[Team Profiles/Sophia]] → Bi-weekly calendar invite pending, database solution affects her workflow, Talk to Lance (meeting structure — who is Lance?)
- [[Team Profiles/Adrien]] → Commitments (1 outstanding — recording of last meeting)
- [[Team Profiles/Brad]] → Commitments (1 outstanding — recording of last meeting, if it involved Brad) + Brad meeting structure questions + 2027 budget + take practice exam to test exam difficulty
- [[Team Profiles/Cedric]] → Commitments (1 outstanding — Streamlit database answer pending response)
- [[Team Profiles/Whitney]] → Commitments (1 outstanding — test results pending — follow up this week)
- [[Team Profiles/Sheila]] → Commitments (1 outstanding — schedule meeting this week to follow up on gathering data)
- [[Team Profiles/Cody Cloward]] → Commitments (1 outstanding — meet to discuss MCP server / everyone having databases)
- [[Team Profiles/Jared]] → Commitments (1 outstanding — calls scores in report with outs per his request; also: share 3 focus points/rubric with team leads; Jared will remind TLs + Luis about survey)
- [[Team Profiles/Sherry]] → Commitments (1 outstanding — follow up with team members on cohort reports, ensure correlation AND causation)
- [[Team Profiles/Elena]] → Approval needed for: (1) combining Div 4/5 meetings, (2) including team leads in meetings; Seven to run unified-meeting + team-leads-included proposal past her
- [[Team Profiles/Samuel Ribeiro]] → Commitments (3 outstanding — email action plans to group; share Call Evaluation Guide/rubric with Jared; confirm team leads have OTA access for Health Coach course)

*Want Paul to remind you about overdue items? Ask: "What am I behind on?"*
