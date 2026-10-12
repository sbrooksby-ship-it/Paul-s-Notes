# Proposal: Catalog Project & Enterprise Verification Engine

**Prepared by:** Seven Brooksby
**For:** Adrien — VP, Division 5
**Date:** September 30, 2026
**Status:** Drafted Sep 30 — pending send to Adrien (he requested it by EOD today)

---

## 1. Executive Summary & Strategic Intent

This proposal outlines the implementation plan for the Catalog Project, establishing a centralized **Enterprise Verification and Evidence Engine**. The primary objective is to make all product claims fully verifiable through an accurate, organized, independently credible, and structured evidence base.

By combining structured data storage with an advanced retrieval architecture — integrating **Vector RAG**, an **LLM Wiki**, and **Graph RAG** — this infrastructure ensures that every promotional claim, product specification, and customer interaction is strictly grounded in verified scientific literature and legal standards. Furthermore, this system serves as the foundational catalog layer for an autonomous, self-improving AI ecosystem.

---

## 2. Core Architectural Triad: Vector RAG, LLM Wiki & Graph RAG

The catalog architecture relies on three complementary retrieval and reasoning technologies to maintain scientific and legal integrity:

**Vector RAG (Semantic Search):** Converts scientific literature, clinical trials, and ingredient research into dense vector embeddings for fast semantic lookup and similarity matching across vast reference materials.

**LLM Wiki (Structured Living Knowledge Base):** Serves as the centralized, human- and machine-readable repository for living catalog context, ingredient specifications, standard operating procedures (SOPs), brand policies, and compliance guidelines. The LLM Wiki keeps guidelines structured, easily navigable, and dynamically accessible to AI agents.

**Graph RAG (Deep Scientific Traceability):** Explicitly maps multi-hop relationships across catalog entities, connecting products, ingredients, clinical studies, and legal claims into a connected knowledge graph.

---

## 3. Core Database Schema & Automated Guardrails

To establish absolute compliance, the core database implements two interconnected tables:

### A. The Scientific Studies Catalog (`scientific_studies`)

Acts as the central evidence repository linked directly to vector embeddings.

**Schema Columns:** `study_id`, `methodology`, `limitations`, `permitted_conclusions` (strict text), `product_relevance` (e.g., Fruits, Veggies, Spice), and `current_usage_status` (Active, Under Review, Archived).

**Automated Guardrail:** Content generation and validation bots query this table prior to drafting or verifying copy. If a study's limitations specify that clinical trials were conducted exclusively on athletes, the system automatically flags any draft marketing copy claiming benefits for the general elderly population.

### B. The Legal & Scientific Claims Matrix (`approved_claims_matrix`)

Connects directly to `scientific_studies` via a foreign key relationship to act as an absolute legal safeguard.

**Schema Columns:** `claim_id`, `exact_approved_wording`, `linked_study_id`, `context_limitations`, and `approval_status` (Approved, Pending Legal, Rejected).

**Automated Enforcement:** Automated review systems use this matrix as their grading rubric across all generated communications and transcript volumes. If an unapproved statement is detected (e.g., an unauthorized medical claim), the system recognizes the violation, logs a compliance failure, and cites the exact approved wording from the matrix.

---

## 4. Deep Scientific Traceability via Graph RAG

By deploying Graph RAG on top of the central database, the catalog moves beyond basic relational links into explicit multi-hop entity mapping:

$$\text{Product A} \longrightarrow \text{Ingredient B} \longrightarrow \text{Clinical Study C} \longrightarrow \text{Marketing Claim D}$$

**Multi-Hop Traversal:** The system explicitly understands the direct lineage connecting a finished SKU to its composite ingredients, the underlying clinical trials supporting those ingredients, and the legal marketing statements authorized by those trials.

**Automated Invalidation & Dosage Safeguards:** If an ingredient's dosage or formulation changes in the product catalog, Graph RAG automatically traverses downstream graph edges. It instantly flags and invalidates all marketing claims, customer support talking points, and web copy that are no longer scientifically grounded by the updated dosage.

---

## 5. R&D "What-If" Analysis Engine

The Graph RAG knowledge graph and LLM Wiki enable interactive scenario planning for R&D and product strategy teams.

**Complex Formulation Queries:** Product development teams can execute direct queries against the graph and LLM Wiki prior to manufacturing or reformulating products.

**Example Scenario:** R&D asks the system — *"If we formulate a new product combining Ingredient X and Ingredient Y, what existing approved claims from our matrix can we immediately use?"*

**Outcome:** The graph traverses pre-indexed clinical studies for both ingredients, cross-references permitted conclusions against the LLM Wiki brand guidelines, and returns an immediate list of pre-approved claims from the matrix — saving weeks of legal review.

---

## 6. Strict Logic Tree: Catalog and Brand Policy to Matrix Statements

To derive matrix statements deterministically, a strict logic tree pipeline connects raw catalog specifications and corporate brand policies stored in the LLM Wiki directly to claims generation:

```
[ Catalog Specification ] + [ Brand Policy / LLM Wiki ]
             │
             ▼
┌─────────────────────────────────────────┐
│ 1. Ingredient & Dosage Match            │
│    Cross-reference scientific_studies   │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│ 2. Limitation & Scope Filter            │
│    Evaluate study boundaries            │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│ 3. Brand Governance & Prohibitions      │
│    Enforce LLM Wiki policy rules        │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│ 4. Deterministic Matrix Output          │
│    exact_approved_wording + status      │
└────────────────────┬────────────────────┘
```

1. **Ingredient & Dosage Match:** Map catalog item ingredients to primary entries in `scientific_studies`.
2. **Limitation & Scope Filter:** Evaluate trial methodologies, permitted conclusions, and demographic restrictions.
3. **Brand Governance Check:** Apply strict compliance rules from the LLM Wiki (e.g., prohibiting ungrounded health claims or review manipulation).
4. **Deterministic Matrix Output:** Generate the `exact_approved_wording`, set contextual constraints, and assign `approval_status` (Approved, Pending Legal, Rejected).

---

## 7. Long-Term AI Vision: Autonomous, Self-Improving Catalog Ecosystem

This catalog infrastructure connects directly into a four-pillar autonomous AI architecture:

- **Central Orchestration (The Director):** Evaluates catalog-related user requests and dispatches task-specific bots.
- **Delegated Task Bots (The Workforce):** Fleet of specialized micro-agents (Routing, Validation, QA Checklist) executing automated operational checks against the database and LLM Wiki.
- **The Backend Platform (The Memory):** Centralized database and LLM Wiki housing the Knowledge Base (SOPs, policies, study catalogs) and relational data tracking live queue statuses.
- **Workflow & Human Oversight (The Safeguard):** Output is delivered to human experts for validation (Agree / Disagree).

**Continuous Improvement Feedback Loop:** When a human expert disagrees with an automated classification or claim mapping, the failure is logged and the LLM Wiki and logic rules are automatically updated. The ultimate vision is a catalog ecosystem that **never makes the same mistake twice**.

---

## 8. Key Deliverables & Implementation Milestones

**Core Program Deliverables**

- **Priority Evidence Catalog & Claims Matrix:** Complete evidence inventory and legal guardrail linking approved statements to evidence.
- **Public Research Pages:** Public assets featuring citations, authors, disclosures, limitations, and plain-language summaries.
- **Knowledge Base & LLM Wiki Integration:** Authoritative product knowledge base for customers, staff, search, and AI systems.
- **Corrective Trigger:** Unsupported or ambiguously supported public claims are escalated immediately. Any evidence work failing to state its scientific limitations is classified as not publication-ready.

---

## 🔗 Connection to Existing Vault Work

- **End-game AI vision** — This proposal is the catalog layer of the four-pillar autonomous architecture documented in MyVault: `obsidian://open?vault=MyVault&file=Main Notes/Ai Vision for D5.md`
- **Streamlit + Supabase stack** — self-managed; the database schema above builds directly on the Supabase instance Cedric approved (Sep 28) and the existing Streamlit front end.
- **Call evaluation work** — the `approved_claims_matrix` grading rubric extends to the call eval review process currently running in the Wednesday coaching meetings.
- **Checklist examiner bot** — the Validation micro-agent in Section 7 is essentially the automated version of this task.

---

*Last updated: September 30, 2026 by Seven Brooksby*
