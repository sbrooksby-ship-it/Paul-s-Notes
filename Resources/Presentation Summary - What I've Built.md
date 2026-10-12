# What I've Built & Explored — Presentation Summary

*Prepared Oct 1, 2026 · Source: 142 files in MyVault (Aug 26 → Oct 1, 2026)*

---

## The Headline

**I built a production call-quality automation platform — and I'm now rebuilding it on a graph database so every AI judgment it makes is traceable to evidence.**

The system scrapes every Five9 call transcript, grades it against a 36-point rubric with an AI model, and feeds coaching feedback to team leads. Right now it runs on spreadsheets. I've spent the last three weeks migrating it to Postgres so that the grading layer doubles as a claims-verification engine.

---

## 1. What Runs Today

| | |
|---|---|
| **Pipeline** | Five9 → Playwright scraper (hourly) → grading daemon (120s loop) → Supabase → Streamlit |
| **Grading** | AI, 36-point rubric, scored + coaching feedback written per call |
| **Scale** | 4 live Streamlit apps · 183-page RAG wiki · checklist bot parsing ops PDFs |
| **Cost** | **$161/mo → ~$60/mo** after optimizing payloads |

**Reliability decisions I made deliberately:**
- Rate-limit errors return calls to the queue — never drop a call
- Backlog grows safely when quota is hit
- Bots surface exception lists; **humans always dispose**
- Every infrastructure gotcha documented as "hard-won — do not regress"

---

## 2. One Finding That Changed the Data

My automated adverse-event detection **improved** — flagged rate dropped 35% → 13%.

But complaints **worsened** — 29% → 47%.

Instead of reporting the win, I traced it: **call-center ticket filing is being skipped on product-fill complaints.** So it's an *identification* problem, not a detection problem. The system sees the complaint; nobody files the ticket. Training-completed flag is FALSE across the board.

That single trace is why I trust the rest of the numbers.

---

## 3. Why I Moved Off Spreadsheets

Vector search is fuzzy. For compliance work, fuzzy is a liability. I rejected it in three specific places:

| Need | Why vector search fails | What I built instead |
|---|---|---|
| **Product claims** | May return a study with similar vocabulary but a *different product* | Graph traversal — only the linked, verified study is ever cited |
| **QA scoring** | Can't compute exact scores for rubric codes like ARC-1, PE-1 | Structured columns — direct database queries |
| **Adverse events** | Can't rely on a model guessing what *sounds* like a medical complaint | Deterministic path: call → event → timestamp → quote. **100% auditable** |

**Graph RAG over Vector RAG** — in a 1,000-page book, vector search finds the chapter about the train robbery. Graph RAG explains *why the business failed* by connecting a contract on page 200 to a character on page 12.

---

## 4. The Catalog Project — Turning Grading Into Verification

Two tables in Postgres:

**`scientific_studies`** — methodology, limitations, permitted conclusions, product relevance, status
**`approved_claims_matrix`** — exact approved wording, linked study, context limitations, approval status

**The guardrail:** if a study's limitations say the trial was conducted **only on athletes**, the system automatically flags any draft copy claiming the benefit for the **general elderly population.**

**The chain:** Product → Ingredient → Clinical Study → Marketing Claim
**The safeguard:** if a dosage changes, the graph auto-invalidates every downstream claim, talking point, and web page no longer supported by the evidence.

**The value:** R&D can ask *"if we combine Ingredient X and Y, which approved claims can we use immediately?"* — and get an answer in minutes instead of weeks of legal review.

---

## 5. Where It's Headed

- **100% call grading coverage** — phased automation, Sales first, Care after a monitoring week
- **One AI gateway** — single URL fronts all data sources (call scores, tickets, wikis, chat). Team members never touch a database password; rate limiting and audit logging happen centrally
- **Automated exam generation** — build tests from existing SOPs, with rubrics, graded by the same AI engine that grades calls
- **Self-improving system** — when a human disagrees with an AI output, the failure is logged and the rules update. **A system that never makes the same mistake twice.**

---

## The Through-Line

Every design choice I made argues the same way: **auditability over convenience.**

Automated grading is always paired with "bot surfaces exceptions, human decides." Fuzzy matching is replaced with deterministic links. Compliance rules are enforced by database constraints, not by hoping the prompt worked.

That's why I think the verification engine is worth building — not because AI can grade calls, but because it can do so in a way a regulator, a legal team, or an executive can trace back to the evidence.

---

## Honest Gaps

- **Compliance checking isn't reliable yet.** The AI is inconsistent against its own results — target is 70% consistency, not there. I have a two-pass fix designed but not deployed.
- **Some pieces are designed, not built:** exam bot, the unified AI gateway, clinical wiki curation.
- **Data joins have known holes:** short call IDs and test rows don't match yet.
