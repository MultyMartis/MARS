# MARS Website Factory — Trust semantics v0

**Status:** **documentation only** — vocabulary for **trust signals** and placement logic aligned with blueprint **trust_strategy** and [block-registry-v0.md](block-registry-v0.md). **Not** automated trust scoring.

**Related:** [page-objective-model-v0.md](page-objective-model-v0.md), [section-payload-model-v0.md](section-payload-model-v0.md), [qa-result-payloads-v0.md](qa-result-payloads-v0.md).

---

## Mandatory ethics boundary

The factory **forbids** authoring instructions that promote:

- **Fabricated reviews** or testimonial quotes.
- **Fake metrics** (invented user counts, revenue, success rates).
- **Fake authority** (nonexistent awards, unlicensed claims, impersonation).

Violations are **SECURITY RISK** / **NEED HUMAN APPROVAL** class issues where policy applies — exact routing **TBD** per org.

---

## Trust signal categories

### social_proof

| Aspect | Content |
|--------|---------|
| **Placement logic** | After problem framing, before high-friction CTA; avoid hero-stuffing if unverifiable. |
| **Dependencies** | Real attributions, dated cases, platform widgets only when authentic. |
| **Fake trust anti-patterns** | Stock photo “clients,” generic praise blocks. |
| **SEO / commercial role** | Supports credibility; **AggregateRating** only when platform truthfully backs it. |
| **QA risks** | Unverifiable star counts; schema mismatch. |
| **Escalation triggers** | Any request to “invent” three testimonials. |

### local_trust

| Aspect | Content |
|--------|---------|
| **Placement logic** | Near geo claims, maps, hours; consistent NAP. |
| **Dependencies** | Ops-approved service area, store photos with permission. |
| **Fake trust anti-patterns** | False locations, fake “local” when national only. |
| **SEO / commercial role** | Local pack alignment; honest **LocalBusiness** fields. |
| **QA risks** | Polygon errors; holiday hours stale. |
| **Escalation triggers** | Competitor city names stuffed without service. |

### expertise_trust

| Aspect | Content |
|--------|---------|
| **Placement logic** | Methodology, team credentials, certifications — **before** aggressive pricing claims. |
| **Dependencies** | Verifiable licenses, publications, standards (ISO, etc.). |
| **Fake trust anti-patterns** | Diploma mill credentials; “certified” without issuer. |
| **SEO / commercial role** | YMYL sensitivity — higher HITL. |
| **QA risks** | Out-of-date year on “industry leader since…” |
| **Escalation triggers** | Medical/financial advice tone without professional review. |

### operational_trust

| Aspect | Content |
|--------|---------|
| **Placement logic** | Shipping, returns, SLAs, support response times — where **task_complete** UX applies. |
| **Dependencies** | Legal/ops sign-off on numbers and cut-offs. |
| **Fake trust anti-patterns** | “24/7” when not true; impossible delivery promises. |
| **SEO / commercial role** | FAQ honesty; avoid boilerplate fake FAQs. |
| **QA risks** | Mismatch between **faq** and checkout copy. |
| **Escalation triggers** | Campaign promises override ops reality. |

### B2B_trust

| Aspect | Content |
|--------|---------|
| **Placement logic** | Logos with contracts, procurement paths, security posture summaries. |
| **Dependencies** | Logo use rights; NDAs where case studies anonymized. |
| **Fake trust anti-patterns** | Fortune-500 logo wall with no relationship. |
| **SEO / commercial role** | Often secondary to sales cycle; entity pages may carry more weight. |
| **QA risks** | Case study identifies customer without release. |
| **Escalation triggers** | Unapproved customer mentions. |

### compliance_trust

| Aspect | Content |
|--------|---------|
| **Placement logic** | Privacy, terms, industry disclaimers near data collection. |
| **Dependencies** | Legal templates jurisdiction-correct. |
| **Fake trust anti-patterns** | Copy-paste policies for wrong region. |
| **SEO / commercial role** | Low direct SEO lift; high risk if wrong. |
| **QA risks** | Missing cookie consent where required (**SAFE UNKNOWN** by locale). |
| **Escalation triggers** | Regulated claims without substantiation. |

### transparency_trust

| Aspect | Content |
|--------|---------|
| **Placement logic** | Pricing methodology, limitations, “what we won’t do” sections. |
| **Dependencies** | Leadership approval for vulnerability-style honesty. |
| **Fake trust anti-patterns** | **scope_and_limits** theater with empty content. |
| **SEO / commercial role** | Supports **ai_visibility_page** and long-form help hubs. |
| **QA risks** | Contradiction with sales deck. |
| **Escalation triggers** | Marketing asks to remove all limitations text. |

### process_trust

| Aspect | Content |
|--------|---------|
| **Placement logic** | **process_steps** blocks — predictable journey reduces anxiety. |
| **Dependencies** | Actual process matches ops. |
| **Fake trust anti-patterns** | Steps 1–5 when reality is “call and we figure it out” only. |
| **SEO / commercial role** | HowTo schema only if steps on-page and accurate (**honesty**). |
| **QA risks** | Screenshots of obsolete UI in steps. |
| **Escalation triggers** | SLA in steps not met in contract. |

---

*Last updated: 2026-05-11.*
