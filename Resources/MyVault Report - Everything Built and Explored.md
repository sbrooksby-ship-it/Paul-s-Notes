# MyVault Report — Everything Built & Explored

**Source vault:** `\\dc.bon.local\Users\sbrooksby\Documents\Zoom\MyVault` (142 markdown files, ~985KB)
**Report compiled:** October 1, 2026
**Scope:** Aug 26 → Oct 1, 2026

---

## The One-Paragraph Version

You are not "exploring AI." You are running a production call-quality automation platform that you built yourself, on a Google Workspace + Supabase + Python stack, that scrapes every Five9 call transcript, grades it against a 36-point rubric with a Gemini model, and feeds coaching feedback back to team leads — and you are three weeks into migrating that from spreadsheets to a self-hosted Postgres graph database so the whole thing becomes auditable, evidence-linked, and legally defensible. The Catalog Project proposal you wrote for Adrien this afternoon is the endpoint of that arc: turning the grading layer into a claims-verification engine.

---

## Part 1 — What's Actually Live

### Quality Assist Bots — the core system

**Project:** `C:\Users\sbrooksby\projects\quality-assist-bots\`
**Console app:** `appv2.py`
**Status: LIVE in production**

The pipeline:

| Stage | Component | Detail |
|---|---|---|
| Scrape | Five9 + Playwright | GitHub Actions, hourly. Dropped files (Sales 10:45pm) |
| Queue | `call_kanban_queue.backlog` | Cards wait here; backlog grows safely |
| Grade | `kanban_worker.py --daemon` | 120s loop. **Flash, 36-pt strict rubric**, slim JSON |
| Store | `call_scores` / `coaching_feedback` | → done. **429s return cards to backlog, never error** |
| Adverse | Workspace Gem → Sheet → `pull_adverse_sheet.py` | → `adverse_events`. Review tab only |
| Join | 7-digit `call_key` | → `graded_with_adverse` view |
| Wiki/RAG | 183 pages + 4 adverse hubs | `match_wiki_pages` RPC; vector + 1-hop links + drill-down |
| Checklist | `checklist_bot.py` | Parses ops PDFs → `checklist_validations`; verifies #1 TIP tabs, #9 Discount Tracker, #19/#20 tickets |

**Live Streamlit apps:**
- `division5calltool.streamlit.app` — spreadsheet route
- `div5callsupabase.streamlit.app` — Postgres route
- `d5checklistreports.streamlit.app` — checklist reporting
- `div5tickets.streamlit.app` — Asana ticket desk (full source in the vault)

**The 36-point rubric:** `BG1-2, ARC1-4, OE1-3, PE1-5, QC1-8, CL1-4, CC1-5, COMP1-5` — defined in `gs private for data transfer.md` with `CRITERIA_KEYWORDS` regex fallbacks.

**Cost discipline:** ~$161 → **~$60/mo** after slimming JSON (~$30 batched). Gemini Flash at 10k calls = $56.25/mo. Supabase Pro $25. **Hard rule in the log: "Never downgrade grader (Lite rejected)."**

---

### Support rules you wrote down as "hard-won — do not regress"

These are worth as much as the code. They're the institutional memory of what went wrong:

- **Call team is 3rd party.** BON checklists cover internal staff only; transcripts/scores are out of scope for them.
- **Checklist "reviewer" = the EXAMINER** (e.g. Sandy conducts), never the subject. **Bot surfaces exception lists; human disposes.**
- **Adverse registry = 3rd-party population.** BON-staff completeness needs BON-attributed sources (Issue Authority).
- **Onboarding Tracker ≠ TIP population** — false-positive lesson, recorded on the validation row.
- **Individual In/Out circles are not machine-readable from PDF text** — verdicts ride doc totals.

---

### Findings you actually surfaced

| Finding | Numbers | Root cause you identified |
|---|---|---|
| Adverse-event handling | **35% → 13% flagged** (improved) | — |
| Complaints | **29% → 47%** (worsened) | **Ticket-filing skipped on F&V fill complaints** — an identification problem, not a detection one. Training Received all FALSE. |
| Discount Tracker | 556/984 handled, **527 dateless**, 23 stale | — |
| TIP tabs | Layouts differ per tab | Header-driven parsing required |

That complaint finding is the sharpest piece of analysis in the whole vault. The system improved on one axis while silently degrading on another, and you traced it to a specific skipped step rather than accepting the aggregate number.

---

## Part 2 — The Migration In Flight

### The strategic arc

```
Aug 26  Supabase chosen over BigQuery/Firebase
   ↓    (BigQuery abandoned — "no card on file")
Aug 27  Apps built — call eval console, checklist tracker, adverse chain
   ↓
Sep 3   Vector RAG / LLM Wiki / Graph RAG architecture decided
   ↓
Sep 11  Catalog Project tables designed
Sep 16  Quality Assist Bots build log starts
Sep 25  AI Vision (4-pillar ecosystem) + Automate Exams designed
Sep 29  MCP gateway + 3-week All Calls Rollout planned
Sep 30  Call-eval presentation proposal + Catalog Project formalized for Adrien
```

### Supabase (Aug 26) — the platform decision

Researched BigQuery → blocked (no card). Firebase → rejected ("too simple"). **Supabase adopted.**

- $25/mo base + $10/project; 8GB DB; 250GB egress; auto REST + GraphQL; RLS
- **Embeddings are free** via local `sentence-transformers` — a 2,500-word transcript costs **<$0.0003** to embed → **3,000–4,000 transcripts per $1.00**
- Blended total **~$27–28/mo**
- Note: *"Easy integration into Coolify if Cedric goes that way"* — the seeds of the Supabase approval that took a month

### Vector RAG / LLM Wiki / Graph RAG (Sep 3) — why you chose graph

Your argument for rejecting pure vector search in three places:

1. **Clinical claims** — vector search may return a study with similar vocabulary but a *different product line*. Graph RAG follows explicit UUID links in `page_links`, so only the verified study is cited.
2. **QA scores** — vector search can't compute exact scores for `BG 1`, `ARC 1`, `PE 1`. Structured columns can.
3. **Adverse events** — "cannot rely on an engine guessing what *sounds* like a medical complaint." Deterministic `call_id → adverse_event_node → timestamp & quote` = 100% auditable.

**Rubric Knowledge Graph:** instead of one giant Gemini prompt, criteria codes (`BG 1`, `PE 1`) become parent nodes with children for passing/failing conditions, required key phrases, and objection-handling rules.

```
[ Call Segment ] → [ Matches Code: PE 1 ] → [ Fetches Subgraph: Rules & Phrases ]
```

**Your metaphor:** vector RAG = scanning a pile of loose pages. Graph RAG + Wiki = table of contents with explicit page numbers.

### Catalog Project (Sep 11 → Sep 30) — the endpoint

Two tables:

**`scientific_studies`** — `study_id`, `methodology`, `limitations`, `permitted_conclusions`, `product_relevance` (Fruits/Veggies/Spice), `current_usage_status` (Active/Under Review/Archived)

**`approved_claims_matrix`** — `claim_id`, `exact_approved_wording`, `linked_study_id` (FK), `context_limitations`, `approval_status` (Approved/Pending Legal/Rejected)

The guardrail logic: if a study's `limitations` says the trial was **athletes-only**, the bot automatically flags any draft copy claiming the benefit for the **general elderly population**.

Graph traversal: `Product → Ingredient → Clinical Study → Marketing Claim`. **Dosage change → automatic downstream invalidation** of every claim, talking point, and web copy no longer grounded.

### AI Vision for D5 (Sep 24) — the four pillars

1. **Central Orchestration (The Director)** — evaluates intent, dispatches specialized bots
2. **Delegated Task Bots (The Workforce)** — Routing, Validation, Digital Avatars, QA Checklist
3. **The Backend Platform (The Memory)** — Knowledge Base + relational live state
4. **Workflow & Human Oversight (The Safeguard)** — human decides **Agree / Disagree**

**The core mechanic:** disagreement → Continuous Improvement Route → failure logged, knowledge base auto-updated. *"A system that never makes the same mistake twice."*

### All Calls Rollout (Sep 29) — 100% grading

| Week | Action | Why |
|---|---|---|
| 1 | Auto-pull **Sales** calls in 1–2hr batches | Steady trickle prevents crashes and daily data limits |
| 2 | **Care stays manual** — monitor Sales strictly | Buffer to fix hidden bugs, timeouts, verify Supabase flags missed files |
| 3 | Auto-pull **Care** at full scale | 100% coverage, zero downtime |

### MCP Gateway (Sep 29) — the convergence point

One FastMCP Python file fronts everything: custom SQL tools for Supabase + Neon, `create_proxy()` + `mcp.mount()` for Gorgias and Notion with `namespace=` to prevent collisions. Secrets stay host-side in env vars; clients get **one URL**. Deploy GitHub → Railway/Render. Clients: Claude Desktop, Cursor, n8n.

Goal: *"Did Michel make an approved product claim on call 121210, and which study supports it?"* — answered by cross-referencing Supabase scorecards, Neon logs, Notion wikis, and Gorgias tickets in one hop.

### Proposal for Presenting the Call Eval (Sep 30) — newest note

Two-tier knowledge framework:
- **Tier 1 — TLs get the full Call Evaluation Guideline** with granular 1–5 progressions for targeted coaching
- **Tier 2 — Agents get "Mastering the Balance of Nature Customer Journey"** — principles, not a scorecard

Anchor on VFP. Structure by the **7-phase call flow** (Research → Contact → Interview → Qualify → Educate → Agreement → Close) instead of rubric categories.

---

## Part 3 — Blocked, Staged, and Unbuilt

### ⛔ Blocked

**Compliance Gem — inconsistent.** *"It isn't consistent with its results at all, need to improve consistency before going out."* Target 70%. Prescribed a 2-pass fix: Phase 1 full inventory, Phase 2 audit against FDA 21 CFR §101.3 / FD&C §403(s), FTC Act Sec 5, ROSCA 15 USC §8403 + 16 CFR 425. The 60K test CSV is unusable as-is.

This is the one item with a hard "don't ship" signal.

### 🔨 Unbuilt per plan

Exam Bot · Gorgias source · Clinical Wiki curation · IA/PolicyTech/CRM credentials · Tab 2 `[ERROR-TRACKED]` flag fix · 5-digit key matcher · Test-row filter

### ⏸ Staged

Scraper bridge (needs repo commit + 2 secrets + manual run; 20/day free quota) · `appv2.py` push to GitHub · nightly adverse pull schedule · file-watcher test

### 🧱 Infrastructure gotchas recorded

- **Office DNS hijacks `db.*` hostnames** → Supabase DDL must go via **pooler**, IP resolved via 8.8.8.8
- **Firewall constraint:** private IP `172.16.17.58` must be whitelisted; Streamlit must live *inside* the firewall; **Apps Script "push" fails behind the firewall — must invert to "pull"**
- Google auth fallback chain: service account (shared sheets) → user OAuth (`google_oauth_login.py`)
- 7-digit `call_key` join misses short IDs and Test rows (known gaps)
- `DATABASE_URL` in `.env`, git-ignored

---

## Part 4 — ⚠️ Four Things You Should Fix

These are real and worth acting on before this vault or that code goes anywhere.

### 1. Live Gemini API key in plaintext 🔴
`Parts/coaching feedback data transfer gs.md` line 60 contains a hardcoded API key. **Revoke it in Google AI Studio, then remove the literal from this file.** This note broke the "No secrets in this note" rule.

### 2. Ticket App code is corrupted — don't treat it as source

`Main Notes/Streamlit Div 5 Ticket App.md` contains a full 562-line app, but an Obsidian wikilink find/replace ("index", "streamlit") ran over the code block. Result: `[[index]]=1` and `[[Streamlit|streamlit]]` appear **inside the source**, breaking every affected call. Fine as documentation, broken as code.

### 3. Default credentials in the Ticket App 🔴

Same file — auth falls back to `admin`/`admin` if `st.secrets` are unset:

```python
hmac.compare_digest(username, st.secrets.get("AUTH_USERNAME", "admin"))
```

Silent fallback to a known-weak credential. If secrets ever fail to load, the app opens.

### 4. Hardcoded admin allowlist

`Parts/code for checklist tracker.md` — `admin_emails` list starting with `sbrooksby@bonadmin.com`, gate at line 61. Should be env/config.

---

## Part 5 — The Warehouse

`gemma-wiki/` — a local Gemma 4 plugin indexes 53 notes into cards, all running on your GPU, no API calls. Useful: it's a second reading of your own work. Two housekeeping items:

- **23 tags have been sitting in the Pending list since Sep 8** — the log warned that near-duplicate tags keep coining until you run "Tidy the wiki"
- The `Vector Rag, Wiki LLM, Graph Rag.md` note contains **two generations of the same explanation** appended rather than reconciled — the later section corrects the earlier framing (*"What you described as GraphRAG is actually standard Vector RAG"*). Worth consolidating so you don't re-read the wrong version later.

---

## Part 6 — The Pattern

Five themes, in order of maturity:

| Theme | Maturity |
|---|---|
| **Call eval automation** | **Developed & live** — Scripts, Streamlit apps, GitHub Actions, real data |
| **Supabase / graph migration** | **Active direction** — docs complete, code mid-migration |
| **Google Apps Script glue** | **Built, likely stale** — ~8 files, most repetitive |
| **Hermes multi-agent architecture** | **Vision** — diagrams and prose, no code yet |
| **Compliance / regulatory** | **Blocked on consistency** |

**What ties it together:** every design decision you made argues for **auditability over convenience**. Fuzzy vector search → rejected for graph traversal. Automated grading → always paired with "bot surfaces exception lists, human disposes." 429s → return to backlog, never error. Blackout conditions → documented as "hard-won, do not regress." That's a consistent instinct, and it's why the Catalog Project proposal to Adrien is credible rather than aspirational.

**The gap:** the compliance layer is the one piece where the auditability instinct hasn't yet paid off — the Gem is inconsistent, so the thing that would make the whole system legally defensible is the thing that isn't reliable yet.

---

## Appendix — File Map

| Path | Contents |
|---|---|
| `Main Notes/` (16) | Project notes — Quality Assist Bots build log is the operational source of truth |
| `Parts/` (42) | Excalidraw architecture canvases, code dumps, requirements, examples |
| `gemma-wiki/cards/` (53) | Auto-generated local-LLM summaries of your notes |
| `gemma-wiki/log.md` | Every plugin operation, dated — shows ingest history Aug→Sep |
| `Tags/` (15) | Tag vocabulary; 0-byte stubs for unused tags |
| `Parts/Tasks active things/Dept 13 Tasks.md` | Placeholder — contains one line: "mini hat" |

---

*Compiled by Paul from 142 files across MyVault. Findings on the API key, corrupted code, default credentials, and admin allowlist were verified directly against the files, not taken from a summary.*
