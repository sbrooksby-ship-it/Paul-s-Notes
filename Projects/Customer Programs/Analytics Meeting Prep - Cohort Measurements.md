# Analytics Meeting Prep — Cohort Measurements

**Date:** October 27, 2026
**Prepared for:** Data Analytics Team Meeting
**Source:** MyVault + Team-Brain cross-referenced
**Status:** Ready for discussion

---

## Purpose

Review measurement gaps in cohort/program tracking and propose improvements for the analytics team to address.

---

## 1. VIP Cohort Simulation — Control Group Missing (Critical)

| Issue | Impact | Recommended Fix |
|---|---|---|
| **No control group** | Can't prove VIP box caused retention — only that it's consistent with it | Recruit a matched control group of similar-tenure subscribers receiving standard treatment |
| **Self-selected cohort** | Customers already among the most loyal — selection bias | Random or representative sample |
| **No baseline data** | All numbers are assumptions, not observed data | Compare to general subscriber base |

**Key reference (MyVault):** *"Ten loyal customers who were already the most loyal segment will do well. That tells us nothing about whether the attention caused it."*

**Source files:**
- `VIP Cohort Simulation - Comparison.md` (Group B vs. C results) — MyVault
- `VIP Cohort Simulation - No Control Group.md` (structural issues) — MyVault

---

## 2. Cohort Metrics — Correlation vs. Causation Required

**Source (Team-Brain — Weekly-Pulse-Check):** Sherry (Director, Division 3) owns cohort metrics. The requirement is that metrics must show **correlation AND causation**, not just correlation.

**Gap:** The VIP cohort simulation is the only cohort metrics example in the vault. It lacks a control group, so causation cannot be proven (MyVault). Team-Brain shows the ongoing expectation that Sherry's Division 3 cohort metrics must establish causation.

**Fix:** The VIP cohort simulation should be restructured with a matched control group so the causation requirement (per the Team-Brain action item) can actually be met.

---

## 3. Call Evaluation — Talk Time vs. Words Not Measured

| Issue | Impact | Recommended Fix |
|---|---|---|
| **No talk-time vs. word-count tracking** | Can't distinguish script-reading from genuine engagement | Add WPM + pause ratio to JEV data |
| **No scheduled vs. completed tracking** | No visibility on no-shows or call completion rates | Track scheduled vs. completed |
| **No time-of-day patterns** | Can't optimize call scheduling | Add temporal analysis |

**Source:** MyVault `Jev AI Automation/Analysis - Talk Time vs Words in Calls.md` (cross-referenced with Team-Brain's call eval pipeline)

---

## 4. Audit & Checklists — No Completion Metrics

| Issue | Impact | Recommended Fix |
|---|---|---|
| **No completion rates** | Can't see which checklists are hardest or who's falling behind | Track completion by agent/checklist |
| **No feedback loop** | No data on whether checklists prevent errors | Add "usefulness" ratings |

---

## 5. Broader Measurement Gaps

| Area | Missing Data |
|---|---|
| **Automation/Bots** | No bot performance metrics (accuracy, usage, errors) |
| **Database & Infrastructure** | No tracking of data freshness or sync failures |
| **Streamlit Apps** | No user adoption metrics |

---

## What's Already Good (Cohort-Specific)

| Area | Strong |
|---|---|
| **VIP Simulation (comparison)** | Quantitative ROI, referral counts, retention %, retention delta — MyVault |

---

## Recommended Next Steps

1. **Control group** — Design a matched control cohort for the VIP micro-pilot (needs 2–3 weeks to run)
2. **Call analytics** — Add talk-time + word-count fields to the JEV data schema
3. **Checklist tracking** — Add completion rate metrics to the Checklist Reporting app
4. **Admin/Synced data** — Review whether there are any sync issues or data quality problems
