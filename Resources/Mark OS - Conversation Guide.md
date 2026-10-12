# Mark OS — Summary for Conversation

*Built Oct 5 from full transcript review. You did NOT attend live — transcript too long. This is the "what to say" version.*

## The 30-second pitch (say this in any meeting)

> "Mark OS is an AI review layer, not a content generator. It embeds in Premiere, Photoshop, and Asana and checks content before it goes live — brand, legal, performance. Our audit showed only 8% of our live creative hits Meta best practices (industry avg 40–50%). Non-compliance costs 37–42% more in delivery. They train on our claim sheet and brand policies; 2-week sandbox, then 2–6 week custom onboarding. Annual contract, volume-based pricing. We need to provide them our claims — that's coming from our rebuilt Supabase pipeline."

## The one line you must say to James / team

> **"We rebuilt the pipeline feeding call evals into Supabase — that produces the claim sheet Mark OS needs. I need to hand that off. The claims commitment is on us."**

---

## The 5 things you must know cold

1. **It's NOT generative AI.** It does not write content. It reviews it — decomposing images/video into frames/scenes/copy, running agentic rules, giving deterministic (not random) results with consistency scores.
2. **It lives where you work.** Premiere plugin, Photoshop, Asana extension, web dashboard. No context-switching.
3. **Our audit was bad.** 8% following rules; Nature's Bounty at 80%. The cost of not following best practices is concrete (Meta delivery cost +37–42%).
4. **The claim sheet is OUR responsibility.** They train the system on our approved claims, ingredients, contracts, image rights. Without that, their reviews will be overly cautious (many false positives). This is the dependency you flagged today.
5. **Sandbox available.** 30-day hands-on test possible. No full integration in sandbox — just web platform review. Custom training (phase 2) takes 2–6 weeks after claim/data collection.

---

## Key quotes/names to drop naturally

- **Marius Ciocirlan** — founder/presenter; mentioned Bessemer Ventures, clients (VW, Centauri, White Claw, King of England)
- **James Ford** — our lead; asked about Google doc sync and pricing/volume
- **Ben Bybee** — wants sandbox access; cautious on FDA compliance
- **Brett / Sherry** — compliance; confirmed value in pre-filtering before it reaches them
- **Spencer** — marketing; cares about tracking live content + best-practices score
- **Dakota** — design; cares about Premiere/Photoshop integration; asked about live Google doc updates
- **Shannon** — first exposure; confirmed expectations
- **"We give you a claim list"** (00:15) — the dependency line
- **"Only 8% of your creative followed 4/6 Meta rules"** (00:49) — the audit result
- **"Overly cautious without custom training"** (00:54) — sandbox warning

---

## What Mark OS actually checks (example categories)

- **Compliance:** off-label use claims, FDA/FTC rules, regional claim differences (US vs. UK)
- **Brand:** logo presence, colors, tone of voice (e.g., "effortless tone"), brand values alignment (e.g., influencer history check — Kate Sigman flagged for Grand Canyon incident against Slothful's nature brand)
- **Performance:** Meta/YouTube/TikTok best practices, attention zones (disclaimers in high-attention areas)
- **Production:** text legibility, logo clear space, audio sync (mouth vs. sound), copyrighted music, color gradient banding, packaging accuracy, master artwork comparison, image-rights expiration

---

## Your rebuilt pipeline → their claim sheet (dependency chain)

```
Call flow rebuilt → Sheets rebuilt → Supabase feed updated
            ↓
    [Produces claim evidence / approved claims matrix]
            ↓
    [Handed to Mark OS as claim list + scientific evidence]
            ↓
    [Used during brief/content review; feeds agentic rules]
```

**This is the open item.** Without it, Mark OS runs overly cautious (many false positives, long onboarding correction cycle). With it, onboarding is faster and more accurate.

---

*Meeting log: `Meetings/2026-10/2026-10-05 - Mark OS Demo.md` (full transcript, timestamps). This file is the conversation-ready version.*
