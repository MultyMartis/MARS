# SITE-002 — CORPORATE INTRO IMAGE PROMPT PACK v1

**Program:** SITE-002 (BZPM / ЗПМ)  
**Task ID:** SITE-002 — Corporate Intro Image Prompt Pack  
**Mode:** Documentation only — **no** image generation · **no** FTP · **no** deploy · **no** site changes  
**Branch:** `mars/canonical-post-recovery`  
**Date:** 2026-06-29  

---

## 1. Purpose

Этот документ — **единый prompt-pack** для будущей HITL-генерации шести вводных (intro) изображений корпоративных страниц SITE-002.

Cursor **не** генерирует изображения, **не** загружает assets и **не** меняет Twig/CSS/PHP. Задача ограничена подготовкой:

- общего визуального стиля;
- шести page-specific промптов;
- глобального negative prompt;
- реестра будущих файлов;
- процесса operator HITL.

После утверждения стиля по первому кадру (About) оператор генерирует оставшиеся пять изображений во внешнем генераторе (ChatGPT Images, Midjourney, DALL·E и т.п.). Отдельная Cursor-задача подключит готовые файлы в intro-блоки.

**Scope страниц:** About · Delivery · Payment · Warranty · Dealers · Custom Manufacturing (M9.13–M9.18).

---

## 2. Visual authority

### Primary authority — Home page

| Source | Role |
|--------|------|
| **Live Home** | https://zpm.new-site.space/ — главный визуальный эталон |
| `SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01` | CTA band, commercial trust rhythm |
| `SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01` | CSS spacing, card weight, section rhythm |
| `SITE-002-STABLE-LIVE-LOCAL-FONTS-01` | Inter typography stack |

Home задаёт **premium industrial B2B** тон: чистые поверхности, нержавеющая сталь, спокойная палитра (`--main-light-color` #F7F8FD, `--main-dark-color`, акценты без перенасыщения), мягкий естественный свет, без «рекламного HDR».

### Corporate visual language (current TEST)

| Checkpoint | Relevance |
|------------|-----------|
| `SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02` | About hero уже использует photoreal factory photo (`about-page-img.jpg`) — **style reference**, не duplicate scene |
| `SITE-002-STABLE-LIVE-UNIVERSAL-CORPORATE-CTA-01` | Единый corp CTA; intro images must not compete with cert podium / form card |
| M9.14–M9.18 corp pages | Lead через `.zpm-corp-page-lead`; будущий intro visual — **~1/3 desktop column** рядом с текстовым lead |

### Style lineage (images)

Prior About polish (`SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1`) заменил sterile 3D render на **photoreal stainless-steel factory production**. Новые intro images должны **продолжить эту линию**, не возвращаться к CGI kitchen / isometric stock.

### Explicit non-authority

PLP, PDP, каталог, filter density, generic stock «chef kitchen» renders.

---

## 3. Global image style

Единый стиль для **всех 6** intro images:

| Parameter | Specification |
|-----------|---------------|
| **Genre** | Photorealistic premium industrial photography |
| **Subject domain** | Clean food-service equipment factory; stainless steel neutral equipment manufacturing |
| **Environment** | Modern, orderly production / warehouse / engineering workspace — **not** dirty workshop |
| **Metal** | Brushed / satin stainless steel surfaces; realistic reflections |
| **Color grade** | Calm blue-gray tone; neutral whites; restrained saturation |
| **Lighting** | Soft natural daylight; large-window factory light or diffused overhead; **no** dramatic spotlights |
| **Depth** | Shallow depth of field; subject sharp; background gently blurred |
| **Mood** | Corporate realism; trustworthy B2B manufacturer; quiet premium factory atmosphere |
| **People** | Optional; professional attire; natural poses; faces partially visible or mid-distance OK |
| **Composition** | Horizontal 16:9; main subject in **right two-thirds** or centered with clean left margin for future text overlay |
| **Forbidden look** | Obvious AI artifacts · visible text · logo · watermark · exaggerated HDR · CGI/3D render · plastic stock photo · fantasy factory · clutter · unsafe equipment |

**Cross-page consistency rule:** Same color grade, lens character (~35–50mm equivalent), and lighting temperature across all six files. Operator compares each new image side-by-side with approved `about-intro.jpg` before batch approval.

---

## 4. Technical target

| Parameter | Recommendation |
|-----------|----------------|
| **Aspect ratio** | **16:9** (landscape) |
| **Master resolution** | **1600×900** minimum; prefer **1920×1080** or **2048×1152** for generation headroom |
| **Final web export** | JPG quality 82–88 **or** WebP quality 80–85 after operator crop review |
| **Future deploy path** | `assets/img/corporate/` on TEST FTP |
| **Repo staging (optional)** | `projects/ocpilot/sites/site-002/reports/corporate-intro-images-work/assets/img/corporate/` |
| **Layout role** | Desktop intro block visual — **~1/3 width** column beside lead copy (2/3 text) |
| **Crop safe zone** | Keep critical subject and faces inside central **70%** frame; avoid edge-critical details in outer 15% left/right (text may sit left) |
| **Mobile** | Full-width stack below H1/lead; subject remains readable at ~390px width |
| **Alt text** | Prepared at connect phase — not in image file |

**Filename convention:** `{page-slug}-intro.jpg` (lowercase kebab-case).

---

## 5. Global negative prompt

Reusable negative prompt — append to **every** page generation:

```text
no text, no watermark, no logo, no brand marks, no distorted hands, no extra fingers, no cartoon, no illustration, no isometric, no 3d render, no CGI look, no plastic stock photo, no oversaturated colors, no dramatic HDR, no fantasy factory, no dirty workshop, no unsafe equipment, no clutter, no unreadable signs, no low resolution, no blur, no deformed machinery
```

**Russian operator note:** если генератор поддерживает отдельное поле «Negative prompt», вставлять блок выше целиком. Если только один prompt — добавить в конец positive prompt фразу: `Avoid: [negative list].`

---

## 6. Page prompts

Each prompt = **Global style prefix** + **page scene** + **Global negative** (or negative field).

### Global style prefix (prepend to every page prompt)

```text
Photorealistic premium industrial photograph, clean food-service equipment manufacturing facility, stainless steel surfaces, calm blue-gray color grade, soft natural daylight, shallow depth of field, corporate B2B realism, 16:9 horizontal composition, high detail, no visible text or logos,
```

---

### About

| Field | Value |
|-------|--------|
| **Filename** | `about-intro.jpg` |
| **Future path** | `assets/img/corporate/about-intro.jpg` |
| **Page URL** | `/about` |

**Scene:** modern clean production workshop, stainless steel food-service equipment manufacturing, professional industrial environment, quiet premium factory atmosphere.

**Full prompt:**

```text
Photorealistic premium industrial photograph, clean food-service equipment manufacturing facility, stainless steel surfaces, calm blue-gray color grade, soft natural daylight, shallow depth of field, corporate B2B realism, 16:9 horizontal composition, high detail, no visible text or logos, modern clean production workshop with stainless steel neutral food-service equipment being assembled or inspected, professional workers in clean work attire optional at mid distance, orderly factory floor, quiet premium manufacturing atmosphere, wide factory windows with soft daylight, brushed stainless steel tables and racks in foreground, background gently blurred
```

**Negative:** use §5 global negative prompt.

**Style gate:** generate **this image first**; operator approves before remaining five.

---

### Delivery

| Field | Value |
|-------|--------|
| **Filename** | `delivery-intro.jpg` |
| **Future path** | `assets/img/corporate/delivery-intro.jpg` |
| **Page URL** | `/delivery` |

**Scene:** equipment prepared for shipment, pallet, protective packaging, straps, warehouse dispatch area, forklift only secondary, no truck hero.

**Full prompt:**

```text
Photorealistic premium industrial photograph, clean food-service equipment manufacturing facility, stainless steel surfaces, calm blue-gray color grade, soft natural daylight, shallow depth of field, corporate B2B realism, 16:9 horizontal composition, high detail, no visible text or logos, warehouse dispatch area with stainless steel food-service equipment prepared for shipment on wooden pallet, shrink wrap and protective packaging, securing straps visible, clean organized loading zone, forklift present only in soft background not as hero subject, no truck cab or trailer dominating frame, calm logistics atmosphere
```

**Negative:** use §5 global negative prompt.

---

### Payment

| Field | Value |
|-------|--------|
| **Filename** | `payment-intro.jpg` |
| **Future path** | `assets/img/corporate/payment-intro.jpg` |
| **Page URL** | `/payment-methods` |

**Scene:** factory manager / sales engineer reviewing documents, quote, contract, order specification, professional B2B order agreement, not accounting, not cash.

**Full prompt:**

```text
Photorealistic premium industrial photograph, clean food-service equipment manufacturing facility, stainless steel surfaces, calm blue-gray color grade, soft natural daylight, shallow depth of field, corporate B2B realism, 16:9 horizontal composition, high detail, no visible text or logos, factory manager or sales engineer at clean desk reviewing printed order documents and specification sheets, B2B commercial quote and contract papers with illegible generic text blocks only, modern office adjacent to production, professional business attire, calm trustworthy atmosphere, no cash money no coins no bank cards no accounting calculator hero, stainless steel equipment sample visible softly in background
```

**Negative:** use §5 global negative prompt.

---

### Warranty

| Field | Value |
|-------|--------|
| **Filename** | `warranty-intro.jpg` |
| **Future path** | `assets/img/corporate/warranty-intro.jpg` |
| **Page URL** | `/guarantee` |

**Scene:** service engineer inspecting stainless steel equipment, diagnostics, tools, quality check, calm professional service environment.

**Full prompt:**

```text
Photorealistic premium industrial photograph, clean food-service equipment manufacturing facility, stainless steel surfaces, calm blue-gray color grade, soft natural daylight, shallow depth of field, corporate B2B realism, 16:9 horizontal composition, high detail, no visible text or logos, service engineer inspecting stainless steel food-service equipment on workbench, quality check with professional hand tools and measurement gauge, diagnostics and careful examination, clean service bay or QC station, calm professional after-sales service environment, no dramatic repair chaos no spilled fluids no broken equipment
```

**Negative:** use §5 global negative prompt.

---

### Dealers

| Field | Value |
|-------|--------|
| **Filename** | `dealers-intro.jpg` |
| **Future path** | `assets/img/corporate/dealers-intro.jpg` |
| **Page URL** | `/dealers` |

**Scene:** manufacturer partnership meeting, representatives discussing cooperation, product samples or catalog materials, long-term B2B partnership, no handshake close-up.

**Full prompt:**

```text
Photorealistic premium industrial photograph, clean food-service equipment manufacturing facility, stainless steel surfaces, calm blue-gray color grade, soft natural daylight, shallow depth of field, corporate B2B realism, 16:9 horizontal composition, high detail, no visible text or logos, manufacturer partnership meeting in bright conference room or showroom, two or three business representatives discussing cooperation over table with stainless steel equipment product samples and closed catalog binders, long-term B2B partnership atmosphere, professional attire, natural conversational distance, no handshake close-up no stock cliché handshake, factory visible through glass partition optional
```

**Negative:** use §5 global negative prompt.

---

### Custom Manufacturing

| Field | Value |
|-------|--------|
| **Filename** | `custom-intro.jpg` |
| **Future path** | `assets/img/corporate/custom-intro.jpg` |
| **Page URL** | `/custom-equipment` |

**Scene:** engineering office, CAD model on screen, technical drawings, custom stainless steel equipment design, product development, modern engineer workspace.

**Full prompt:**

```text
Photorealistic premium industrial photograph, clean food-service equipment manufacturing facility, stainless steel surfaces, calm blue-gray color grade, soft natural daylight, shallow depth of field, corporate B2B realism, 16:9 horizontal composition, high detail, no visible text or logos, modern engineer workspace with large monitor showing CAD 3D model of custom stainless steel food-service equipment, technical drawings and blueprints on desk, product development and custom design process, engineer at workstation in clean office, soft daylight from window, physical stainless steel prototype component on desk optional, no futuristic sci-fi UI no holograms
```

**Negative:** use §5 global negative prompt.

**Note:** CAD on screen is acceptable as **photographed screen content** in a real office — overall image must remain photoreal, not CGI hero render.

---

## 7. Prompt template

Reusable template for operator variations or regeneration:

```text
[GLOBAL_STYLE]
[PAGE_SCENE]
[PAGE_MOOD]
[PAGE_OBJECTS]
Composition: 16:9 horizontal, subject in right two-thirds or center with clean left margin, shallow depth of field, calm blue-gray grade, soft natural light.
Avoid: [PAGE_FORBIDDEN]
[GLOBAL_NEGATIVE]
```

### Variable reference

| Variable | Content |
|----------|---------|
| `[GLOBAL_STYLE]` | §6 global style prefix (single paragraph) |
| `[PAGE_SCENE]` | Primary location and activity (one sentence) |
| `[PAGE_MOOD]` | Emotional tone: quiet premium / trustworthy B2B / calm professional |
| `[PAGE_OBJECTS]` | 3–5 concrete props (pallet, CAD monitor, QC tools, etc.) |
| `[PAGE_FORBIDDEN]` | Page-specific exclusions (e.g. Delivery: no truck hero; Payment: no cash) |
| `[GLOBAL_NEGATIVE]` | §5 full negative prompt block |

### Example (Delivery) filled template

```text
[GLOBAL_STYLE] Photorealistic premium industrial photograph, clean food-service equipment manufacturing facility, stainless steel surfaces, calm blue-gray color grade, soft natural daylight, shallow depth of field, corporate B2B realism, 16:9 horizontal composition, high detail, no visible text or logos,

[PAGE_SCENE] Warehouse dispatch area with equipment prepared for outbound shipment.

[PAGE_MOOD] Calm organized logistics; trustworthy manufacturer fulfillment.

[PAGE_OBJECTS] Wooden pallet, shrink-wrapped stainless steel equipment, securing straps, clean loading zone, forklift far background.

Composition: 16:9 horizontal, subject in right two-thirds or center with clean left margin, shallow depth of field, calm blue-gray grade, soft natural light.

Avoid: truck cab as hero, readable shipping labels, clutter, dirty floor.

[GLOBAL_NEGATIVE] no text, no watermark, no logo, no brand marks, no distorted hands, no extra fingers, no cartoon, no illustration, no isometric, no 3d render, no CGI look, no plastic stock photo, no oversaturated colors, no dramatic HDR, no fantasy factory, no dirty workshop, no unsafe equipment, no clutter, no unreadable signs, no low resolution, no blur, no deformed machinery
```

---

## 8. Future asset registry

| Page | Filename | Future path | Purpose | Status |
|------|----------|-------------|---------|--------|
| About | `about-intro.jpg` | `assets/img/corporate/about-intro.jpg` | Intro visual — manufacturing trust anchor | **TO_GENERATE** |
| Delivery | `delivery-intro.jpg` | `assets/img/corporate/delivery-intro.jpg` | Intro visual — dispatch / shipment readiness | **TO_GENERATE** |
| Payment | `payment-intro.jpg` | `assets/img/corporate/payment-intro.jpg` | Intro visual — B2B order documentation flow | **TO_GENERATE** |
| Warranty | `warranty-intro.jpg` | `assets/img/corporate/warranty-intro.jpg` | Intro visual — service / QC / guarantee support | **TO_GENERATE** |
| Dealers | `dealers-intro.jpg` | `assets/img/corporate/dealers-intro.jpg` | Intro visual — partnership / channel cooperation | **TO_GENERATE** |
| Custom Manufacturing | `custom-intro.jpg` | `assets/img/corporate/custom-intro.jpg` | Intro visual — engineering / custom design | **TO_GENERATE** |

**Total:** 6 files · 0 generated at pack creation time.

---

## 9. HITL process

| Step | Actor | Action |
|------|-------|--------|
| **1** | Operator | Generate **`about-intro.jpg`** only using §6 About prompt + §5 negative |
| **2** | Operator | Compare against Home + existing `about-page-img.jpg` tone; approve or regenerate |
| **3** | Operator | Lock approved style notes (color grade, lighting, lens feel) — optional screenshot reference in `corporate-intro-images-work/` |
| **4** | Operator | Generate remaining **5** images using same generator settings and §6 prompts |
| **5** | Operator | Batch review — side-by-side grid; reject outliers; regenerate single pages if needed |
| **6** | Operator | Export masters; optional WebP; store under `assets/img/corporate/` on TEST when ready |
| **7** | Cursor (future task) | Connect approved images into corporate intro blocks (Twig/CSS) — **separate charter** |

**Approval criteria:**

- Photoreal, not CGI
- Consistent blue-gray grade across set
- No text/logo/watermark
- Subject readable at ~530px width (1/3 of ~1600 container)
- Scene matches page meaning without literal clichés (no cash, no handshake hero, no truck hero)

---

## 10. Safety

| Rule | Status |
|------|--------|
| This prompt pack **does not authorize** site modification | **ACTIVE** |
| No FTP deploy from this task | **CONFIRMED** |
| No TEST/production code changes | **CONFIRMED** |
| No image binary files in repo from this task | **CONFIRMED** |
| Image connect requires **separate** implementation task + operator HITL | **REQUIRED** |

---

## Authority chain (reference)

- `SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01`
- `SITE-002-STABLE-LIVE-LOCAL-FONTS-01`
- `SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02`
- `SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01`
- `SITE-002-STABLE-LIVE-UNIVERSAL-CORPORATE-CTA-01`

---

*Document version: v1 · Created: 2026-06-29 · Classification: prompt-pack / pre-generation artifact only*
