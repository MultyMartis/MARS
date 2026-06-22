# ORCA PPC Semantic Intelligence — Source Ledger v1

**Authority:** bibliography normalization only — not production authority.

## Verification status legend

| Status | Meaning |
|--------|---------|
| VERIFIED PRIMARY | Identified from research starter list as official/academic primary reference; title and org recoverable from research text |
| VERIFIED SECONDARY | Identified secondary reference named in research body |
| IDENTIFIED — URL UNRESOLVED | Source named in research; URL not recoverable from repository evidence |
| CITATION MARKER ONLY | Marker present in original; insufficient metadata in-repo |
| SAFE UNKNOWN | Not identifiable from available evidence |

## Source entries

### SRC-ORCA-ATTACHED-BRIEF-v0

| Field | Value |
|-------|-------|
| Original marker | `turn0file0` |
| Title | ORCA / Corvonero attached research brief (operator-supplied) |
| Organization / authors | MARS operator brief (internal) |
| Source class | researcher inference / operator input |
| Official or academic status | Internal briefing document |
| URL | SAFE UNKNOWN |
| Publication / update date | SAFE UNKNOWN |
| Supported claims | ORCA topical-vs-commercial defect; Corvonero restart constraints; gold dataset sizing guidance |
| Verification status | CITATION MARKER ONLY |
| Limitations | Not a peer-reviewed source; scope fixed to Corvonero / ORCA context |

### SRC-GOOGLE-ADS-KEYWORD-MATCHING-v0

| Field | Value |
|-------|-------|
| Original markers | `turn5view0`, `turn16view4`, `turn26view0`, `turn26view1` |
| Title | About keyword matching options (Google Ads Help) |
| Organization / authors | Google |
| Source class | platform official documentation |
| Official or academic status | Official |
| URL | IDENTIFIED — URL UNRESOLVED (not stored in canonical research bytes) |
| Publication / update date | SAFE UNKNOWN |
| Supported claims | Broad/phrase/exact semantics; Smart Bidding interaction; semantics-based matching expansion |
| Verification status | VERIFIED PRIMARY |
| Limitations | Platform behavior ≠ ORCA admission policy |

### SRC-GOOGLE-ADS-SEARCH-TECH-GUIDE-v0

| Field | Value |
|-------|-------|
| Original markers | `turn16view0`, `turn21view1` |
| Title | Unlock the Power of Search (Google Ads technical guide) |
| Organization / authors | Google |
| Source class | platform official documentation |
| Official or academic status | Official |
| URL | IDENTIFIED — URL UNRESOLVED |
| Publication / update date | SAFE UNKNOWN |
| Supported claims | Query interpretation pipeline; eligibility; ad group selection; stage separation rationale |
| Verification status | VERIFIED PRIMARY |
| Limitations | Describes auction matching, not editorial semantic-core policy |

### SRC-GOOGLE-ADS-SEARCH-TERMS-REPORT-v0

| Field | Value |
|-------|-------|
| Original marker | `turn29view0` |
| Title | About the search terms report (Google Ads Help) |
| Organization / authors | Google |
| Source class | platform official documentation |
| Official or academic status | Official |
| URL | IDENTIFIED — URL UNRESOLVED |
| Publication / update date | SAFE UNKNOWN |
| Supported claims | Post-launch search-term learning; cannot replace pre-launch core QA |
| Verification status | VERIFIED PRIMARY |
| Limitations | Post-fact optimization only |

### SRC-GOOGLE-ADS-NEGATIVE-KEYWORDS-v0

| Field | Value |
|-------|-------|
| Original marker | `turn21view0` |
| Title | About negative keywords (Google Ads Help) |
| Organization / authors | Google |
| Source class | platform official documentation |
| Official or academic status | Official |
| URL | IDENTIFIED — URL UNRESOLVED |
| Publication / update date | SAFE UNKNOWN |
| Supported claims | Negative match behavior; no close-variant matching for negatives |
| Verification status | VERIFIED PRIMARY |
| Limitations | Operator-level negative policy still required |

### SRC-GOOGLE-ADS-AD-GROUP-GUIDANCE-v0

| Field | Value |
|-------|-------|
| Original marker | `turn28view0` |
| Title | Ad group / keyword thematic grouping guidance (Google Ads Help — inferred from research) |
| Organization / authors | Google |
| Source class | platform official documentation |
| Official or academic status | Official (inferred) |
| URL | IDENTIFIED — URL UNRESOLVED |
| Publication / update date | SAFE UNKNOWN |
| Supported claims | Theme-based ad groups; task-based clustering alignment |
| Verification status | IDENTIFIED — URL UNRESOLVED |
| Limitations | Exact help page URL not in canonical source |

### SRC-YANDEX-DIRECT-KEYWORDS-v0

| Field | Value |
|-------|-------|
| Original markers | `turn6view3`, `turn6view1` |
| Title | Keywords (Yandex Direct Help) |
| Organization / authors | Yandex |
| Source class | platform official documentation |
| Official or academic status | Official |
| URL | IDENTIFIED — URL UNRESOLVED |
| Publication / update date | SAFE UNKNOWN |
| Supported claims | Word-by-word and semantic matching; stop words; search query report |
| Verification status | VERIFIED PRIMARY |
| Limitations | Russian morphology and operators need separate operator tests |

### SRC-YANDEX-DIRECT-OPERATORS-v0

| Field | Value |
|-------|-------|
| Original marker | `turn8view0` |
| Title | Symbols and operators (Yandex Direct Help) |
| Organization / authors | Yandex |
| Source class | platform official documentation |
| Official or academic status | Official |
| URL | IDENTIFIED — URL UNRESOLVED |
| Publication / update date | SAFE UNKNOWN |
| Supported claims | `" "`, `!`, `+`, `[]` semantics; operator-aware normalization requirement |
| Verification status | VERIFIED PRIMARY |
| Limitations | Parser tests required for ORCA normalization layer |

### SRC-YANDEX-DIRECT-NEGATIVE-KEYWORDS-v0

| Field | Value |
|-------|-------|
| Original markers | `turn9view0`, `turn9view2` |
| Title | Negative keywords (Yandex Direct Help) |
| Organization / authors | Yandex |
| Source class | platform official documentation |
| Official or academic status | Official |
| URL | IDENTIFIED — URL UNRESOLVED |
| Publication / update date | SAFE UNKNOWN |
| Supported claims | Multi-level negatives; operator support; overlap rules; network caution |
| Verification status | VERIFIED PRIMARY |
| Limitations | Collision QA required before apply |

### SRC-YANDEX-DIRECT-AUTOTARGETING-v0

| Field | Value |
|-------|-------|
| Original markers | `turn9view3`, `turn9view4`, `turn9view5` |
| Title | Autotargeting (Yandex Direct Help) |
| Organization / authors | Yandex |
| Source class | platform official documentation |
| Official or academic status | Official |
| URL | IDENTIFIED — URL UNRESOLVED |
| Publication / update date | SAFE UNKNOWN |
| Supported claims | Non-keyword matching; ad/landing-driven expansion; dirty-core amplification risk |
| Verification status | VERIFIED PRIMARY |
| Limitations | Autotargeting policy separate from manual core admission |

### SRC-ORCAS-I-PAPER-v0

| Field | Value |
|-------|-------|
| Original markers | `turn23academia0` |
| Title | ORCAS-I: Queries Annotated with Intent using Weak Supervision |
| Organization / authors | Academic authors (SAFE UNKNOWN — full author list not in canonical bytes) |
| Source class | academic paper |
| Official or academic status | Academic |
| URL | IDENTIFIED — URL UNRESOLVED |
| Publication / update date | SAFE UNKNOWN |
| Supported claims | Intent taxonomy; abstain class; weak supervision on web queries |
| Verification status | VERIFIED SECONDARY |
| Limitations | Web intent taxonomy ≠ B2B service hire without adaptation |

### SRC-SNORKEL-PAPER-v0

| Field | Value |
|-------|-------|
| Original markers | `turn23academia1`, `turn23academia2` |
| Title | Snorkel: Rapid Training Data Creation with Weak Supervision |
| Organization / authors | Snorkel / academic (SAFE UNKNOWN detail) |
| Source class | academic paper |
| Official or academic status | Academic / engineering publication |
| URL | IDENTIFIED — URL UNRESOLVED |
| Publication / update date | SAFE UNKNOWN |
| Supported claims | Labeling functions; weak supervision bootstrap |
| Verification status | VERIFIED SECONDARY |
| Limitations | Noisy labels require human adjudication |

### SRC-ACTIVE-LEARNING-SURVEY-v0

| Field | Value |
|-------|-------|
| Original markers | `turn18academia0`, `turn20academia1` |
| Title | A Survey of Active Learning for Text Classification using Deep Neural Networks |
| Organization / authors | Academic survey (SAFE UNKNOWN detail) |
| Source class | academic paper |
| Official or academic status | Academic |
| URL | IDENTIFIED — URL UNRESOLVED |
| Publication / update date | SAFE UNKNOWN |
| Supported claims | Hard-case annotation; reviewer queue design |
| Verification status | VERIFIED SECONDARY |
| Limitations | Survey ≠ ORCA implementation |

### SRC-COST-SENSITIVE-REJECTION-v0

| Field | Value |
|-------|-------|
| Original markers | `turn24academia2`, `turn24academia3`, `turn25academia0` |
| Title | Classification with Rejection Based on Cost-sensitive Classification |
| Organization / authors | Academic (SAFE UNKNOWN detail) |
| Source class | academic paper |
| Official or academic status | Academic |
| URL | IDENTIFIED — URL UNRESOLVED |
| Publication / update date | SAFE UNKNOWN |
| Supported claims | Abstention; cost-sensitive admission; calibration |
| Verification status | VERIFIED SECONDARY |
| Limitations | Thresholds require operator decision (D3) |

### SRC-SEARCH4CODE-PAPER-v0

| Field | Value |
|-------|-------|
| Original markers | `turn34academia0`, `turn19academia0` |
| Title | Search4Code (query intent disambiguation research — per research naming) |
| Organization / authors | Academic (SAFE UNKNOWN detail) |
| Source class | academic paper |
| Official or academic status | Academic |
| URL | IDENTIFIED — URL UNRESOLVED |
| Publication / update date | SAFE UNKNOWN |
| Supported claims | Same lexical topic, different user tasks |
| Verification status | IDENTIFIED — URL UNRESOLVED |
| Limitations | Domain differs from B2B services |

### SRC-PRODUCT-INSIGHTS-BING-v0

| Field | Value |
|-------|-------|
| Original markers | `turn34academia1`, `turn19academia2` |
| Title | Product Insights (Bing query taxonomy research — per research naming) |
| Organization / authors | Microsoft / Bing research (inferred from research text) |
| Source class | academic paper |
| Official or academic status | Academic / industry research |
| URL | IDENTIFIED — URL UNRESOLVED |
| Publication / update date | SAFE UNKNOWN |
| Supported claims | Product-related queries are subset of web search; separate taxonomy needed |
| Verification status | IDENTIFIED — URL UNRESOLVED |
| Limitations | English-centric evidence; Russian transfer unproven |

### SRC-SPONSORED-SEARCH-CATEGORY-SIM-v0

| Field | Value |
|-------|-------|
| Original markers | `turn35academia1`, `turn35academia2`, `turn3academia0` |
| Title | Sponsored search category similarity / semantic expansion research (unnamed in starter list) |
| Organization / authors | SAFE UNKNOWN |
| Source class | academic paper |
| Official or academic status | Academic (inferred) |
| URL | CITATION MARKER ONLY |
| Publication / update date | SAFE UNKNOWN |
| Supported claims | Semantic expansion needs downstream relevance control |
| Verification status | CITATION MARKER ONLY |
| Limitations | Full bibliographic record not in canonical source |

### SRC-ORCA-RECOMMENDATION-COLLECTION-v0

| Field | Value |
|-------|-------|
| Original marker | N/A (synthetic ledger entry) |
| Title | ORCA target architecture recommendations within research report |
| Organization / authors | Research author / ORCA-oriented synthesis |
| Source class | ORCA recommendation |
| Official or academic status | Not official |
| URL | N/A |
| Publication / update date | 2026-06 (package receipt) |
| Supported claims | Hierarchical gates; hybrid stack; threshold table; failure-mode catalogue |
| Verification status | researcher inference |
| Limitations | Requires selective promotion (D1); not implemented |

## Marker index

See `bibliography/orca-ppc-semantic-intelligence-source-ledger-v1.json` for machine-readable marker → source_id mapping.
