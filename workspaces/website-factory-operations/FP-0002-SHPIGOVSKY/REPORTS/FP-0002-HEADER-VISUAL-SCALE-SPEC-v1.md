# FP-0002 HEADER VISUAL SCALE SPEC v1

**Block ID / scope:** `FP-0002-BLK-001 + FP-0002-BLK-002` — Desktop Header (shell chrome)  
**Document type:** Visual Scale Spec (visual mass and proportion law — **not** Layout Spec, **not** Assembly Spec, **not** Pixel Audit, **not** implementation)  
**Status:** **DRAFT** — awaiting operator decision **APPROVED | REVISE**  
**Date:** 2026-06-14  
**Viewport:** Desktop **≥ 1024px** (Phase C.1 default)

**Upstream chain:**

| Layer | Document | Role |
|-------|----------|------|
| Visual SSOT | SOURCE-001 + matching PG-001…010 desktop templates | What the header **looks like** |
| Layout Spec | [FP-0002-HEADER-LAYOUT-SPEC-v2.md](FP-0002-HEADER-LAYOUT-SPEC-v2.md) | What lives **where** — rows · zones · groups · weight **tiers** |
| Assembly Spec | [FP-0002-HEADER-ASSEMBLY-SPEC-v1.md](FP-0002-HEADER-ASSEMBLY-SPEC-v1.md) | **How** groups are assembled and isolated |
| **This document** | Visual Scale Spec v1 | **How big / how loud** each group must **look** relative to others |
| HTML | *(forbidden until this layer APPROVED)* | Implementation |

**Authority applied:**

| Layer | Document | Role |
|-------|----------|------|
| A1 | [FP-0002-DESIGN-AUDIT-v1.md](FP-0002-DESIGN-AUDIT-v1.md) | Visual SSOT READ · header element inventory |
| Approval | [FP-0002-DESIGN-APPROVAL-SHEET-v1.md](FP-0002-DESIGN-APPROVAL-SHEET-v1.md) | Operator decision matrix · conflict register |
| Blocks | [FP-0002-BLOCK-INVENTORY-v1.md](../FP-0002-BLOCK-INVENTORY-v1.md) | BLK-001 / BLK-002 boundaries |
| Engineering | [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](../FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) §8.7 | Container model only — **not** visual mass SSOT |
| Factory law | [layout-spec-law-v1.md](../../../../projects/mars-website-factory/layout-spec-law-v1.md) | Pre-code gate chain |
| Shell | [canonical-clean-shell-v1.md](../../../../projects/mars-website-factory/canonical-clean-shell-v1.md) | Pre-code empty shell |
| Visual gate | [operator-visual-approval-law-v1.md](../../../../projects/mars-website-factory/operator-visual-approval-law-v1.md) | Post-build operator review |

**Failure provenance (intended):** [FP-0002-HEADER-BUILD-v1-FAILURE-AUDIT.md](FP-0002-HEADER-BUILD-v1-FAILURE-AUDIT.md) — **file not present on disk at authoring time**; §9 reconstructs HEADER BUILD v1 failure from Layout Spec v2 LR-* · Assembly Spec FT-* · [FP-0002-HEADER-MINI-AUDIT-v1.md](FP-0002-HEADER-MINI-AUDIT-v1.md) · [FP-0002-layout-spec-lesson-v1.md](../../../../projects/mars-website-factory/FP-0002-layout-spec-lesson-v1.md).

**Forbidden in this document (by charter):** HTML · SCSS · CSS · JS · DOM · px · rem · em · grid · flex · media queries · selectors · color tokens · typography tokens · component markup.

---

## 1. Purpose

### 1.1 What Visual Scale Spec is

**Visual Scale Spec** answers a question that Layout Spec and Assembly Spec **cannot** close alone:

> *Given correct zones, groups, and tier labels — **how large and how loud** must each element **look** relative to the others so the header reads like SOURCE-001, not like a structurally correct but visually flat engineering shell?*

This document binds **visual mass**, **proportional dominance**, and **compression/expansion law** — using **relationships only**, never absolute measurements.

### 1.2 What problem it closes

**Failure class addressed:** `SPEC FORMALISM WITHOUT VISUAL SCALE`

| Symptom | Meaning |
|---------|---------|
| Agent places Logo in ZONE E and labels it **PRIMARY** | Zone and tier are **formally correct** |
| Built logo reads as **small mark + caption text** | **Visual mass** is **not bound** — PRIMARY became a label, not a proportion rule |
| Agent places phones in ZONE D and labels them **SECONDARY** | Placement correct |
| Built phones read as **fine-print meta** | SECONDARY was interpreted as “style everything in Row 1 weakly” |
| Agent places CTA in ZONE G | Zone correct |
| Built CTA reads as **sixth nav link** or **generic engineering button** | ZONE G is not dominance — conversion object must **occupy** the right anchor at **action scale** |

Layout Spec v2 §6 Visual Weight Model defines **tiers** (PRIMARY · SECONDARY · UTILITY · SUPPORTING).  
Assembly Spec v1 defines **order and isolation**.  
Neither defines **relative visual mass ratios** agents must preserve at implementation.

### 1.3 What Visual Scale Spec is not

| Artifact | Why it does not substitute |
|----------|----------------------------|
| **Layout Spec v2** | Zones · tiers · alignment — not proportional mass law |
| **Assembly Spec v1** | Assembly order · merge bans — not “how big” |
| **Design Audit / Mini-Audit** | Element inventory — not scale relationships |
| **Production Standards v3** | Engineering tokens — can **flatten** visual hierarchy if applied as mass substitute (CF-010) |
| **Pixel Audit / Numeric Design Rules** | Absolute numbers — out of scope for this layer; downstream of scale law |
| **Operator Visual Review** | Post-build gate — too late for prevention |

### 1.4 Mandatory path (updated)

```text
Visual SSOT
    ↓
Layout Spec (composition decomposition)
    ↓
Assembly Spec (assembly order · isolation)
    ↓
Visual Scale Spec (visual mass · proportion law)   ← THIS DOCUMENT
    ↓
Operator APPROVED (all upstream + this layer)
    ↓
HTML
    ↓
QA → Operator Visual Review
```

**Rule:** HTML/CSS for header scope remains **FORBIDDEN** until Layout Spec v2 **APPROVED**, Assembly Spec v1 **APPROVED**, **and** this Visual Scale Spec v1 **APPROVED**.

---

## 2. Authority Chain

Strict authority for desktop header ≥1024px:

```text
Visual SSOT (SOURCE-001 + matching PG-001…010 templates)
        ↓
Layout Spec — FP-0002-HEADER-LAYOUT-SPEC-v2.md
        ↓
Assembly Spec — FP-0002-HEADER-ASSEMBLY-SPEC-v1.md
        ↓
Visual Scale Spec — FP-0002-HEADER-VISUAL-SCALE-SPEC-v1.md (this document)
        ↓
HTML (shell header markup — FORBIDDEN until Visual Scale Spec APPROVED)
        ↓
QA (technical build · structure checks)
        ↓
Operator Visual Review (live page — separate gate)
```

| Stage | Gate question | Who decides |
|-------|---------------|-------------|
| Visual SSOT | Is there an approved visual source? | Operator / A1 audit |
| Layout Spec | Is composition decomposition correct? | Operator **APPROVED \| REVISE** |
| Assembly Spec | Is assembly order and isolation sufficient? | Operator **APPROVED \| REVISE** |
| **Visual Scale Spec** | Are visual mass relationships bound? | Operator **APPROVED \| REVISE** |
| HTML | May markup be written? | **Only after all three specs APPROVED** |
| Operator Review | Does built page match SSOT mass and composition? | Operator **ACCEPT \| REVISE** |

**Downstream rule:** Production Standards v3, starter patterns, and engineering placeholders **must not** override Visual SSOT **mass intent** when they would compress Logo, Phones, CTA, or Nav below the relationships in §4–§7.

**Tier vs scale rule:** Layout Spec **tier labels** (PRIMARY, SECONDARY, etc.) are **necessary but not sufficient**. Visual Scale Spec **binds** what those tiers **must look like** in relative terms.

---

## 3. Visual Weight Hierarchy

**Scale vocabulary for this document:**

| Level | Meaning in header context |
|-------|---------------------------|
| **Dominant** | Largest intentional visual mass in its scope — eye lands here first within band or stack |
| **Strong** | Clearly present — must not be mistaken for meta, utility, or nav footnote |
| **Medium** | Readable and intentional — supports stronger elements; never competes with Dominant/Strong anchors |
| **Weak** | Context/meta — visible but must not pull attention before Strong/Dominant elements |

### 3.1 Element register

| Element | Zone | Layout tier (v2) | **Visual weight (this spec)** | Mass statement |
|---------|------|------------------|-------------------------------|----------------|
| **Logo mark** (graphic) | E | PRIMARY | **Dominant** | The mark is the **visual anchor** of the brand object — must read as institution identity, not favicon or bullet |
| **Brand text** (title + subtitle stack) | E | PRIMARY | **Strong** | Multi-line institutional title — **stronger than any single nav link**; subordinate to mark within Logo Group |
| **Primary Nav** (five links, equal to each other) | F | PRIMARY | **Strong** | Horizontal IA spine — each link **medium-strong within group**; group as whole **Strong** |
| **CTA** «Заказать звонок» | G | PRIMARY | **Dominant** | Isolated **action object** — must **dominate** nav link text and **balance** logo mass on the right |
| **Phones** (two-number cluster) | D | SECONDARY | **Strong** | Contact climax of Row 1 — **must look callable**; strongest mass in top strip |
| **Utility Links** («Генотипирование» · «Специалисты») | C | SECONDARY (weak) | **Medium** | Secondary shortcuts — above meta, **below** phones and **far below** nav |
| **Region** («Москва,» · «Московская область») | A | UTILITY | **Weak** | Locale context — never nav-sized |
| **Hours** (schedule string) | B | SUPPORTING | **Weak** | Lowest intentional mass in header — meta footnote within strip |

### 3.2 Within-group nuance

| Group | Internal hierarchy |
|-------|-------------------|
| **Logo Group** | Mark **Dominant** > brand text **Strong** > optional tagline (SU-03) **Medium–Strong** if present |
| **Primary Nav Group** | All five links **equal mass** — no item louder than another |
| **Phone Group** | Both numbers **equal mass** — one cluster, not primary/secondary phone |
| **Utility Links Group** | Both links **equal mass** — paired, weaker than phones |

### 3.3 Cross-band summary

```text
DOMINANT:   Logo mark · CTA button
STRONG:     Brand text · Primary Nav (group) · Phone cluster
MEDIUM:     Utility Links pair
WEAK:       Region labels · Hours string
```

---

## 4. Relative Scale Model

**Rule:** All statements below are **proportional relationships**, not measurements. Agent must preserve **direction and approximate ratio intent** at implementation.

### 4.1 Cross-stack (full header)

```text
MAIN ROW band visual mass  >>  TOP ROW band visual mass     (approx. 2×–2.5× band dominance)

Within MAIN ROW:
  Logo mark visual mass       ≈  CTA visual mass             (left/right anchor balance)
  CTA visual mass             >  any single nav link           (clear action lift)
  CTA visual mass             >  Phone cluster               (conversion row beats contact strip)
  Logo Group (mark + text)    >  Phone cluster               (identity stage beats top strip)
  Primary Nav (group)         >  Utility Links (group)       (site menu beats top shortcuts)
  Primary Nav link mass       <  Logo mark mass              (nav supports brand, not overshadows)
  Primary Nav link mass       <  CTA mass                    (button is not a link sibling)

Within TOP ROW:
  Phone cluster mass          >  Utility Links mass          (contact beats shortcuts)
  Utility Links mass          >  Region mass                 (links beat locale labels)
  Utility Links mass          >  Hours mass                  (links beat schedule meta)
  Region mass                 ≈  Hours mass                  (both Weak — neither competes with phones)
  Phone cluster mass          >> Hours mass                  (phones must not read as footnote)

Cross-row contact column:
  Phone cluster (Row 1)       <  CTA (Row 2)                 (right column: action row wins)
  Phone cluster (Row 1)       >  Hours + Region (Row 1)        (phones are strip climax)
```

### 4.2 Logo — why **big**, not merely PRIMARY

| Formal spec alone | Visual Scale binding |
|-------------------|---------------------|
| «Logo Group = PRIMARY, ZONE E left» | Logo mark must occupy a **brand-object footprint** — visual mass **comparable to CTA** as the left counterweight |
| Agent can satisfy PRIMARY with **small square + text caption** | **Forbidden** — PRIMARY without scale = favicon header |
| SOURCE-001 intent | Mark + stacked title reads as **one institution block** — the **largest single object** in MAIN ROW besides CTA |

**Relationship chain for logo:**

```text
Logo mark  >  brand text line mass  >  any nav link  >  utility link  >  hours/region
Logo mark  ≈  CTA control mass     (anchor balance across MAIN ROW)
```

### 4.3 Phones — why **important**, not merely SECONDARY

| Formal spec alone | Visual Scale binding |
|-------------------|---------------------|
| «Phone Group = SECONDARY, ZONE D» | SECONDARY means **subordinate to MAIN ROW band**, **not** “render weakly like all Row 1 text” |
| Agent can satisfy SECONDARY by **uniform tiny top bar** | **Forbidden** — phones are **Strong** within header; **strongest in Row 1** |
| SOURCE-001 intent | Two numbers **close the top strip** as **contact objects** — reader must perceive **call now** without hunting |

**Relationship chain for phones:**

```text
Phones  >  Utility Links  >  Region ≈ Hours
Phones  <  Logo mark / CTA / MAIN ROW band overall
Phones  >>  Hours          (must not collapse to schedule footnote styling)
```

### 4.4 CTA — why **dominate**, not merely ZONE G

| Formal spec alone | Visual Scale binding |
|-------------------|---------------------|
| «CTA Group = PRIMARY, ZONE G right» | ZONE G is **placement** — not permission to match nav link size |
| Agent can satisfy ZONE G with **text link** or **small pill** | **Forbidden** — CTA is **Dominant action mass** at right edge |
| SOURCE-001 intent | «Заказать звонок» is **conversion punctuation** — visually **separated** and **heavier** than nav |

**Relationship chain for CTA:**

```text
CTA  >  any nav link
CTA  ≈  Logo mark           (paired anchors)
CTA  >  Phone cluster
CTA  ≠  nav list item       (must not share link-scale mass)
```

### 4.5 Complete relative model (reference strip)

```text
BAND:     MAIN ROW  >>>  TOP ROW  (≈2×–2.5×)

DOMINANCE LADDER (high → low):
  Logo mark ≈ CTA
  Brand text · Nav group · Phones
  Utility Links
  Region · Hours
```

---

## 5. Row Dominance Model

### 5.1 Which row is stronger

**Row 2 (MAIN ROW / BLK-002)** is the **dominant visual band** of the entire header stack.  
**Row 1 (TOP ROW / BLK-001)** is the **supporting contact strip**.

### 5.2 Approximate visual ratio

| Dimension | Relationship | Intent |
|-----------|--------------|--------|
| **Band envelope (height + type scale + object size)** | Row 2 ≈ **2×–2.5×** Row 1 | MAIN ROW must read as **main stage**; TOP ROW as **strip above stage** |
| **Typographic loudness** | Row 2 >> Row 1 | Nav and brand text **clearly larger** than top-bar meta |
| **Object scale** | Row 2 >> Row 1 | Logo mark and CTA **clearly larger** than phones; phones **clearly larger** than hours |
| **Attention capture** | Row 2 first, Row 1 second | Eye path: **brand + nav + CTA**, then **phones**, then meta |

### 5.3 Forbidden row relationships

| Forbidden | Why |
|-----------|-----|
| Row 1 ≈ Row 2 band mass | Inverts header — contact strip competes with identity row (Layout Spec LR-011) |
| Row 1 > Row 2 | TOP ROW must never overpower MAIN ROW |
| Equal typographic scale across rows | Collapses dual-row intent into single-density chrome |

### 5.4 Row coupling (right column)

Phone cluster (Row 1, right) and CTA (Row 2, right) form a **contact/conversion column intent**:

```text
CTA mass (Row 2)  >  Phone mass (Row 1)   — same horizontal anchor, different band
```

Both align to container right edge per Layout Spec §7.3 — scale spec adds: **CTA must visually outweigh phones** even when vertically aligned.

---

## 6. Group Dominance Matrix

**Reading:** Cell = **row group vs column group**.  
**A > B** = A must look visually stronger than B.  
**A ≈ B** = co-primary balance (still distinct roles).  
**A ≠ B** = must **not** look the same mass (forbidden parity).

|  | Logo | Brand text | Nav | CTA | Phones | Utility | Region | Hours |
|--|:----:|:----------:|:---:|:---:|:------:|:-------:|:------:|:-----:|
| **Logo mark** | — | **>** | **>** | **≈** | **>>** | **>>** | **>>** | **>>** |
| **Brand text** | **<** | — | **>** | **<** | **>>** | **>>** | **>>** | **>>** |
| **Nav (group)** | **<** | **<** | — | **<** | **>>** | **>>** | **>>** | **>>** |
| **CTA** | **≈** | **>** | **>** | — | **>>** | **>>** | **>>** | **>>** |
| **Phones** | **<<** | **<<** | **<<** | **<<** | — | **>** | **>** | **>>** |
| **Utility Links** | **<<** | **<<** | **<<** | **<<** | **<** | — | **>** | **>** |
| **Region** | **<<** | **<<** | **<<** | **<<** | **<** | **<** | — | **≈** |
| **Hours** | **<<** | **<<** | **<<** | **<<** | **<<** | **<** | **≈** | — |

### 6.1 Forbidden parity pairs

These groups **must not look the same visual mass**:

| Pair | Why parity fails |
|------|------------------|
| **Logo mark ≈ nav link** | Brand anchor collapses to menu noise |
| **Logo mark ≈ hours** | Institution identity demoted to meta |
| **CTA ≈ nav link** | Conversion control lost (CR-02 · CR-07) |
| **CTA ≈ utility link** | Callback demoted to top-bar shortcut |
| **Phones ≈ hours** | Contact path hidden (LR-001 · LR-005) |
| **Phones ≈ region** | Phones read as locale footnote |
| **Nav ≈ utility links** | Primary IA confused with secondary shortcuts (CR-04) |
| **Utility links ≈ hours** | Secondary links must stay **Medium**, hours **Weak** |
| **Row 1 band ≈ Row 2 band** | Dual-row hierarchy destroyed (LR-011) |

### 6.2 Permitted near-balance pairs

| Pair | Rule |
|------|------|
| **Logo mark ≈ CTA** | Left/right anchor balance — **different roles**, similar **object mass** |
| **Region ≈ Hours** | Both Weak meta — neither may approach Phone or Nav mass |
| **Nav links (within group)** | Equal mass across five items |

---

## 7. Visual Compression Rules

**Compression** = reducing visual mass below bound relationships to fit layout, starter habits, or engineering tokens.

### 7.1 Must not compress (hard floor)

| Element | Compression forbidden | Minimum relative intent |
|---------|----------------------|-------------------------|
| **Logo mark** | Shrinking to icon/favicon/placeholder square | Must remain **Dominant** — **≈ CTA** anchor mass |
| **Brand text stack** | Collapsing to single small caption line | Must remain **Strong** — **> any nav link** |
| **CTA** | Shrinking to nav-link scale or text-only link | Must remain **Dominant** — **> nav links** |
| **Primary Nav (group)** | Collapsing to icon menu or microtext | Must remain **Strong** group — readable IA spine |
| **Phones** | Shrinking to hours/region meta scale | Must remain **Strong** in Row 1 — **>> hours** |

### 7.2 Compression triggers to reject

| Trigger | Typical agent behavior | Verdict |
|---------|------------------------|---------|
| Uniform Row 1 styling | All top-bar text same small size | **FAIL** — violates Phone **Strong** floor |
| Starter placeholder logo | Empty box at minimum size | **FAIL** — violates Logo **Dominant** floor |
| Production Standards pill defaults (CF-010) | CTA styled as small generic button | **FAIL** if mass drops below **Dominant** intent |
| Space pressure at 1024 | Shrink logo/phones first | **Forbidden** — compress **Weak/Medium** first (§8) |
| «SECONDARY means small» | Phones at caption scale | **FAIL** — tier misread; see §4.3 |

### 7.3 What may absorb compression (see §8)

Region · Hours · Utility Links · inter-zone whitespace · nav letter-spacing (within Strong floor) — **never** Logo · CTA · Phones · Nav readability.

---

## 8. Visual Expansion Rules

### 8.1 May expand (flexible mass)

| Element | Expansion rule |
|---------|----------------|
| **Inter-zone whitespace** | May grow/shrink within row to preserve group isolation |
| **Hours string** | May wrap/truncate only if **Weak** mass preserved and phones untouched |
| **Region labels** | May wrap if **Weak** mass preserved |
| **Utility Links gap** | Whitespace before Phone cluster may flex |
| **Nav inter-link spacing** | May flex if five links remain **Strong** and CTA isolation preserved |

### 8.2 May shrink (first sacrifice order)

When horizontal pressure increases (narrow desktop, long copy), reduce in this order **before** touching §7.1 floors:

```text
1. Whitespace gaps (zones B/C, nav gaps)
2. Hours presentation length (not phone mass)
3. Region presentation (not phone mass)
4. Utility Links spacing (not link readability)
5. Brand text line breaks (mark mass unchanged)
6. Nav spacing (not nav mass floor)
—— STOP — do not proceed below —
7. Logo mark · CTA · Phones · Nav mass floors (FORBIDDEN)
```

### 8.3 Must not expand into dominance

| Element | Forbidden expansion |
|---------|---------------------|
| **Hours / Region** | Must not grow to **Medium** or **Strong** — stays **Weak** |
| **Utility Links** | Must not grow to **Nav parity** — stays **Medium** |
| **Phones** | Must not grow to **Logo/CTA parity** or move to Row 2 mass |
| **Nav** | Must not grow past **Strong** into **Dominant** — CTA and Logo own Dominant tier |
| **Row 1 band** | Must not expand vertically to match Row 2 envelope |

### 8.4 Background vs content mass

Full-bleed header background may span viewport width — **background expansion does not substitute** for Logo · CTA · Phone **content mass**.

---

## 9. Failure Examples — HEADER BUILD v1

**Evidence note:** [FP-0002-HEADER-BUILD-v1-FAILURE-AUDIT.md](FP-0002-HEADER-BUILD-v1-FAILURE-AUDIT.md) is **referenced by task charter but not found on disk**. Analysis below is reconstructed from corroborating artefacts. Treat detailed build-by-build diffs as **SAFE UNKNOWN** until failure audit is filed.

### 9.1 Failure class manifestation

| Class | Observed pattern (HEADER BUILD v1 era) |
|-------|----------------------------------------|
| **SPEC FORMALISM WITHOUT VISUAL SCALE** | Structure partially present (dual-row intent, labels, zones) but **visual mass collapsed** — header read as **engineering chrome**, not SOURCE-001 institution header |

### 9.2 Documented failure modes mapped to scale gaps

| ID | What went wrong | Formal spec said | Scale gap | Trap ref |
|----|-----------------|------------------|-----------|----------|
| **VS-F01** | Logo rendered as **placeholder / small mark + generic text** | Logo PRIMARY, ZONE E | PRIMARY did not bind **Dominant ≈ CTA** mass | LR-004 · FT-04 |
| **VS-F02** | Phones rendered as **smallest top-bar text** | Phone SECONDARY, ZONE D | SECONDARY misread as “weak strip text” not **Strong >> hours** | LR-001 · FT-05 |
| **VS-F03** | CTA as **generic engineering pill** or **nav-like link** | CTA PRIMARY, ZONE G | ZONE G did not bind **Dominant > nav**; Production Standards radius (CF-010) altered **object mass feel** | LR-002 · FT-06 |
| **VS-F04** | **Equal-density Row 1 and Row 2** | MAIN ROW must dominate | Row ratio **≈2×–2.5×** not bound | LR-011 |
| **VS-F05** | **SaaS-style** centered logo or single-row feel | Left anchor · dual-row | Mass layout followed starter, not SSOT anchors | LR-006 · FT-02 |
| **VS-F06** | Hours/region **same visual weight as phones** | Hours SUPPORTING · Phones SECONDARY | Forbidden parity (§6.1) | LR-005 |
| **VS-F07** | Utility links **nav-scale** | Utility SECONDARY weak | Medium vs Strong boundary missing | CR-04 · FT-04 |
| **VS-F08** | Implementation used **engineering min-height placeholders** without SSOT mass check | Mini-audit §8 — heights UNKNOWN | Absolute placeholders substituted for **relative law** | SU-01 |

### 9.3 Root cause chain (systemic)

```text
Visual SSOT
    ↓
Layout Spec v2 (tiers + zones)     — present / drafted
    ↓
Assembly Spec v1                   — present / drafted
    ↓
Visual Scale Spec                  — MISSING at BUILD v1
    ↓
Agent applied tiers as labels + engineering tokens as mass
    ↓
SPEC FORMALISM WITHOUT VISUAL SCALE
```

### 9.4 Why Layout + Assembly alone did not prevent BUILD v1

| Layer provided | What agent still guessed |
|----------------|-------------------------|
| PRIMARY / SECONDARY tiers | Absolute **size** and **loudness** |
| Zone placement | **Object scale** within zone |
| Assembly isolation | **Relative mass** between isolated groups |
| Production Standards v3 | **Button/logo/phone scale** — engineering defaults **≠** visual mass SSOT |

---

## 10. Visual Scale Acceptance

Header is **visually scale–accepted** (ready for Operator Visual Review on mass grounds) **only when all** checks pass:

### 10.1 Band checks

| # | Check | Pass criterion |
|---|-------|----------------|
| VS-A01 | Row dominance | Row 2 reads **clearly dominant** over Row 1 (~**2×–2.5×** band intent) |
| VS-A02 | No row parity | Row 1 does **not** match Row 2 typographic/object density |

### 10.2 Anchor checks

| # | Check | Pass criterion |
|---|-------|----------------|
| VS-A03 | Logo mass | Mark reads **Dominant** — **not** favicon/placeholder |
| VS-A04 | CTA mass | Button reads **Dominant** — **>** any nav link; **≈** logo mark counterweight |
| VS-A05 | Anchor balance | Left Logo Group and right CTA **balance** MAIN ROW as paired anchors |

### 10.3 Contact checks

| # | Check | Pass criterion |
|---|-------|----------------|
| VS-A06 | Phone mass | Phones **Strong** — **>>** hours/region; **callable** at glance |
| VS-A07 | Phone ceiling | Phones **<** MAIN ROW Dominant anchors (not louder than logo/CTA) |

### 10.4 IA checks

| # | Check | Pass criterion |
|---|-------|----------------|
| VS-A08 | Nav mass | Nav group **Strong** — **<** logo mark and CTA; **>** utility links |
| VS-A09 | Utility mass | Utility links **Medium** — **≠** nav parity |
| VS-A10 | Meta mass | Region + hours **Weak** — do not compete with phones or MAIN ROW |

### 10.5 Forbidden parity scan

| # | Check | Pass criterion |
|---|-------|----------------|
| VS-A11 | Parity scan | No forbidden pairs from §6.1 appear **same mass** at arm's-length viewing |
| VS-A12 | CTA isolation | CTA **≠** sixth nav link by mass or styling tier |

### 10.6 Process checks

| # | Check | Pass criterion |
|---|-------|----------------|
| VS-A13 | Spec citation | Implementation REPORT cites this document **APPROVED** |
| VS-A14 | No token override | Production Standards did not compress §7.1 floors without operator decision |

**Verdict semantics:**

| Result | Meaning |
|--------|---------|
| **VISUAL SCALE ACCEPTED** | VS-A01…VS-A14 **PASS** — proceed to Operator Visual Review for full SSOT compare |
| **VISUAL SCALE REVISE** | Any **FAIL** — fix mass relationships; **do not** patch with layout-only tweaks |

---

## 11. SAFE UNKNOWN

Agent **must not invent** scale facts to fill gaps. Record only; defer to operator or downstream pixel pass.

| ID | Topic | Impact on scale spec |
|----|-------|----------------------|
| **VSU-01** | Exact band height ratio Row 2:Row 1 | §5.2 uses **≈2×–2.5× intent** from Layout Spec cross-row rule — not measured from live PDF this session |
| **VSU-02** | Logo mark **left of** vs **above** text (SU-09) | Internal Logo Group axis — does not change Dominant/Strong split |
| **VSU-03** | «Лечение и профилактика» placement (SU-03) | If inside Logo Group — **Medium–Strong**; if absent — no scale change |
| **VSU-04** | Logo graphic asset (SU-04) | Asset gap — **Dominant mass floor still binding** (placeholder forbidden as mass substitute) |
| **VSU-05** | Phone pair inline vs stacked (SU-07) | Cluster mass unchanged — layout micro only |
| **VSU-06** | CTA fill/outline variant (SU-18 · CF-008) | Affects **perceived** mass — operator decision before treating as bound |
| **VSU-07** | CTA corner radius (CF-010) | Engineering 30 vs PDF ~6 — alters **object character**; scale acceptance may fail VS-A04 until resolved |
| **VSU-08** | Sticky/shrink on scroll (SU-02) | Behavior — scale law applies to default desktop static state |
| **VSU-09** | PDF files not on disk for operator re-open (SU-15) | Operator visual compare should use archived PDFs |
| **VSU-10** | **FP-0002-HEADER-BUILD-v1-FAILURE-AUDIT.md missing** | §9 reconstructed from peer docs — detailed build screenshots/diffs **UNKNOWN** |
| **VSU-11** | Font family weight steps (Inter weights) | Relative hierarchy binding stands; exact weight numbers deferred |
| **VSU-12** | 1024–1199 narrowing behavior (SU-16) | Sacrifice order §8.2 applies — exact wrap strategy open |

---

## 12. Operator Decisions

Decisions that affect **visual scale acceptance** but are **not closed** in this spec:

| ID | Topic | Why operator needed | Scale impact |
|----|-------|---------------------|--------------|
| **VODR-01** | Visual Scale Spec v1 **APPROVED \| REVISE** | Gate for this document | Unlocks HTML mass law |
| **VODR-02** | Layout Spec v2 **APPROVED** (upstream) | Required before HTML | Composition prerequisite |
| **VODR-03** | Assembly Spec v1 **APPROVED** (upstream) | Required before HTML | Isolation prerequisite |
| **VODR-04** | CTA / accent Visual SSOT vs Production Standards (CF-008, CF-010 · ODR-04) | CTA **object character** | VS-A04 may fail if generic pill applied |
| **VODR-05** | «Лечение и профилактика» placement (SU-03 · ODR-03) | Logo Group internal mass | Optional tagline tier |
| **VODR-06** | Logo asset delivery (SU-04 · ODR-05) | Cannot verify mark silhouette | Dominant **floor** still binding |
| **VODR-07** | File **FP-0002-HEADER-BUILD-v1-FAILURE-AUDIT.md** | Referenced but missing | Confirm §9 failure inventory or amend |

```text
OPERATOR DECISION — FP-0002-HEADER-VISUAL-SCALE-SPEC-v1:

[ ] APPROVED
[ ] REVISE
```

**Unlock sequence for HEADER BUILD v2:**

```text
1. Operator APPROVED — FP-0002-HEADER-LAYOUT-SPEC-v2.md
2. Operator APPROVED — FP-0002-HEADER-ASSEMBLY-SPEC-v1.md
3. Operator APPROVED — FP-0002-HEADER-VISUAL-SCALE-SPEC-v1.md (this document)
4. THEN — Header HTML/CSS permitted (cite all three REFs + this scale REF)
5. THEN — Build → VS-A01…A14 self-check → Operator Visual Review
```

---

## 13. Failure Class — New or Existing?

### 13.1 Question

Create new failure class **VISUAL SCALE NOT BOUND**, or keep **SPEC FORMALISM WITHOUT VISUAL SCALE**?

### 13.2 Verdict

| Artifact | Decision | Rationale |
|----------|----------|-----------|
| **Failure class (observable outcome)** | **KEEP `SPEC FORMALISM WITHOUT VISUAL SCALE`** | Describes what operator sees: specs followed **formally** (zones, tiers, assembly order) but header **visually wrong** because **mass relationships** were unbound |
| **Failure cause (missing gate)** | **REGISTER `VISUAL SCALE NOT BOUND`** | Describes **why** — Visual Scale Spec layer skipped or not APPROVED before HTML — analogous to **LAYOUT SPEC SKIPPED** under **VISUAL INTERPRETATION WITHOUT LAYOUT SPEC** |
| **Replace class with cause name?** | **NO** | **VISUAL SCALE NOT BOUND** is **not** a substitute class — it is the **upstream capture-point gap** this document closes |

### 13.3 Taxonomy placement (recommended)

```text
FAILURE CLASS:     SPEC FORMALISM WITHOUT VISUAL SCALE
FAILURE CAUSE:     VISUAL SCALE NOT BOUND
CAPTURE POINT:     Visual Scale Spec Gate — before Header HTML (after Layout + Assembly APPROVED)
EXPECTED ARTIFACT: FP-0002-HEADER-VISUAL-SCALE-SPEC-v1.md — operator APPROVED
```

### 13.4 Relationship to prior failure classes

| Prior class | Relationship |
|-------------|--------------|
| **VISUAL INTERPRETATION WITHOUT LAYOUT SPEC** | Upstream — composition fantasy **before** zones exist |
| **SPEC FORMALISM WITHOUT VISUAL SCALE** | **This layer** — composition may be correct; **mass** is flat/wrong |
| **PRE-LAYOUT-SPEC STARTER RESIDUE** | Parallel risk — starter mass habits **compound** scale failure |

**Promotion note:** Adding **VISUAL SCALE NOT BOUND** to [frontend-failure-attribution-model-v1.md](../../../../projects/mars-website-factory/frontend-failure-attribution-model-v1.md) is **recommended** but **out of scope** for this filing — operator charter required.

---

## Document control

| Field | Value |
|-------|-------|
| Version | **v1** |
| Status | **DRAFT** |
| Upstream | Layout Spec v2 · Assembly Spec v1 |
| Downstream | HEADER BUILD v2 (when gates pass) |
| Commit / push | Not performed |
| Workspace touched | **NO** — documentation only |

---

**Operator gate request:**

Visual Scale Spec v1 готов как обязательный слой **массы и пропорций** между Assembly Spec и HTML для desktop header (BLK-001 + BLK-002, ≥1024px).  
Проверьте относительную модель (§4), матрицу доминирования (§6) и правила сжатия/расширения (§7–§8) против Visual SSOT (SOURCE-001).  
Требуется решение: **APPROVED** или **REVISE**.  
HTML/CSS/JS **запрещены** до APPROVED на Layout Spec v2 **и** Assembly Spec v1 **и** на этом документе.
