# Triumph Manipulator — Legal Gap Report v1

**Версия:** v1  
**Дата:** 2026-05-30  
**Статус:** pilot preparation only — **NO page generation**, **NO Triumph workspace edits**  
**Site type:** `LANDING`  
**Pilot plan:** [TRIUMPH-LEGAL-PILOT-PLAN-v1.md](TRIUMPH-LEGAL-PILOT-PLAN-v1.md)  
**Templates:** Core Legal Pack L1–L4 (post [LEGAL-TEMPLATE-HARDENING-v1.1.md](../LEGAL-TEMPLATE-HARDENING-v1.1.md))

---

## 1. Triumph input audit

### 1.1. Sources reviewed

| Source | Role |
|--------|------|
| `workspaces/triumph-manipulator-landing-v6/` | **Primary candidate** — production candidate state, built contacts, footers, forms |
| `projects/triumph-manipulator-landing/` | Governance, V6 structure map, production candidate docs |
| `workspaces/triumph-manipulator-landing/` | Legacy workspace — **not** primary for V6 pilot |

**Operator confirmation:** production deploy target = v6 — **assumed from** `V6-PRODUCTION-CANDIDATE-STATE.md`; formal Legal Input Sheet — **not on file**.

### 1.2. Contact and identity data

| Field | Value found | Evidence | Confidence |
|-------|-------------|----------|------------|
| **Domain** | `manipulator-triumph.ru` | `canonical` in `src/pages/*.html`; deploy reports | **High** |
| **Email** | `info@manipulator-triumph.ru` | Footer, `backend/config.php` | **High** |
| **Phone** | `+7 (918) 991-2-991` / `tel:+79189912991` | Header, footer, forms | **High** |
| **Legal entity (display)** | ООО «ТРИУМФ» | `landing-footer.html` copyright | **Medium** — needs operator confirm for `{{company_name}}` |
| **ИНН** | `5009114932` | Footer | **High** |
| **ОГРН** | `1185027010321` | Footer | **High** |
| **Юридический адрес** | Not in footer/legal partials | — | **Missing** in audit sources |
| **Город (marketing)** | Краснодар | Page titles/descriptions | N/A for legal vars unless operator adds `{{address}}` |

### 1.3. Legacy / drift signals (must not appear in generated legal output)

| Signal | Location | Risk |
|--------|----------|------|
| `gruzotaxi_triumph` (Telegram) | Multiple PPC partials | Brand legacy — **not** legal template leak if unchanged |
| `opergt@gktriumph.ru` | `backend/config.php` BCC | Email drift — review at deploy, **outside** legal page body |
| `gruzotaxi-triumph.ru`, `info@gktriumph.ru` | Documented as removed from templates | **Must not** reappear in generated L1–L4 |

### 1.4. Footer links (current state)

**Partials:** `v5-page01/landing-footer.html`, `legal/landing-footer-legal.html`

| Required (canon) | URL | Footer text | Current v6 |
|------------------|-----|-------------|------------|
| L1 | `/privacy-policy/` | Политика конфиденциальности | ✓ match |
| L3 | `/user-agreement/` | Пользовательское соглашение | ✓ match |
| L2 | `/consent-personal-data/` | Согласие на обработку персональных данных | ✓ match |
| L4 | `/cookie-files-policy/` | Политика Cookie-файлов | **DRIFT** → `/cookies/` + «Cookie файлы» |

### 1.5. Legal navigation (legal shell)

**Partial:** `legal/legal-nav.html`

| Link | Current | Canon |
|------|---------|-------|
| L4 | `/cookies/` + «Cookies» | `/cookie-files-policy/` + «Политика Cookie-файлов» |
| L2 short label | «Согласие на обработку данных» | Footer/H1: полное название |

### 1.6. Legal pages (HTML)

| Page | `src/pages/` entry | Status |
|------|-------------------|--------|
| `/privacy-policy/` | **Absent** | Not built in V6 route set |
| `/consent-personal-data/` | **Absent** | Not built |
| `/user-agreement/` | **Absent** | Not built |
| `/cookie-files-policy/` | **Absent** | Not built |
| `/cookies/` (legacy) | **Absent** | Referenced in footer only |

**Shell exists:** `legal/legal-header.html`, `legal-document.html`, `legal-nav.html`, `landing-footer-legal.html` — **preparation partials only**.

`projects/triumph-manipulator-landing/V6-ACTIVE-STRUCTURE-MAP.md`: footer links to legal URLs; **no legal page HTML in build**.

### 1.7. Consent text (forms)

**Status:** **PASS** — canonical Consent Rule HTML on sampled forms (hero, FAQ, CTA).

```html
Я&nbsp;даю согласие на&nbsp;обработку персональных данных в&nbsp;соответствии с&nbsp;<a href="/consent-personal-data/" target="_blank">Согласием на&nbsp;обработку персональных данных</a> и&nbsp;соглашаюсь с&nbsp;<a href="/privacy-policy/" target="_blank">Политикой конфиденциальности</a>.
```

**Consent drift:** none detected in form markup.

### 1.8. Placeholder availability (for generation)

| Variable | Triumph source | Ready? |
|----------|----------------|--------|
| `{{company_name}}` | ООО «ТРИУМФ» (footer) | **Pending operator confirm** |
| `{{domain}}` | `manipulator-triumph.ru` | ✓ |
| `{{email}}` | `info@manipulator-triumph.ru` | ✓ |
| `{{privacy_policy_url}}` | `https://manipulator-triumph.ru/privacy-policy/` | ✓ (derived) |
| `{{consent_personal_data_url}}` | `https://manipulator-triumph.ru/consent-personal-data/` | ✓ (derived) |
| `{{phone}}` | Available | Optional — not in Core template bodies |
| `{{address}}` | Not found | **Missing** if operator requires in legal body |
| `{{inn}}` / `{{ogrn}}` | In footer | Optional — not in Core template bodies |

---

## 2. Current state vs target state

| Dimension | Current state | Target state (pilot) |
|-----------|---------------|----------------------|
| Legal pages L1–L4 | Not in build | 4 HTML pages from hardened Core templates |
| Footer L4 link | `/cookies/`, «Cookie файлы» | `/cookie-files-policy/`, «Политика Cookie-файлов» |
| Legal nav | Legacy `/cookies/` | Canon URLs + H1-aligned labels |
| Consent on forms | Canonical | Unchanged |
| Template placeholders | N/A (no pages) | Zero `{{...}}` in production HTML |
| `{{company_name}}` | Inconsistent branding («Триумф» vs ООО «ТРИУМФ») | Single operator-approved string in all L1–L4 |
| LEGAL-GENERATION-CONTRACT Phase 3 | Not run | PASS before deploy |

---

## 3. Gap analysis

### 3.1. Missing data

1. **Formal Legal Input Sheet** — not committed; operator sign-off on variable set.
2. **`{{company_name}}` exact string** — footer uses ООО «ТРИУМФ»; legal footer variant uses «Триумф» without ООО in copyright line.
3. **`{{address}}`** — юридический адрес не найден в audited sources (optional unless operator mandates).

### 3.2. Footer drift

- L4 URL: `/cookies/` → must become `/cookie-files-policy/`
- L4 link text: «Cookie файлы» → «Политика Cookie-файлов»
- Affects: `landing-footer.html`, `landing-footer-legal.html` (+ scan all footer variants at execution)

### 3.3. URL drift

- Legal nav active route key `cookies` → should align with `cookie-files-policy` page slug
- No live legal pages — links currently **404** in production build

### 3.4. Consent drift

- **None** in form consent markup.

### 3.5. Placeholder / template gaps

- Core templates ready post v1.1.
- Triumph still needs **substitution pass** + **page creation** in `src/pages/` (future execution).
- Analytics/cookie inventory for Triumph (Метрика, reCAPTCHA) — **SAFE UNKNOWN** for L4 factual accuracy.

---

## 4. Pilot readiness

### Verdict: **NOT READY** (for legal page generation execution)

**Rationale:** Core templates hardened and contact variables largely known, but **human gates** and **workspace gaps** block generation per [LEGAL-GENERATION-CONTRACT-v1.md](../LEGAL-GENERATION-CONTRACT-v1.md).

### Exactly what is missing before generation

| # | Item | Owner |
|---|------|-------|
| 1 | Operator-signed **Legal Input Sheet** with confirmed `{{company_name}}` | Human |
| 2 | Operator confirmation: **v6** = production legal target workspace | Human |
| 3 | Decision on **`{{address}}`** (include in legal pages or omit) | Human |
| 4 | Tag/cookie inventory sign-off (if legal text must name active trackers) | Human / SAFE UNKNOWN |
| 5 | Execution tasks (not prep): create 4 pages, substitute variables, fix footer/nav drift | Future pilot phase |

**Ready subcomponents (prep complete):**

- Template hardening v1.1 ✓
- Domain, email, phone, INN, OGRN ✓
- Consent Rule on forms ✓
- Legal shell partials exist ✓

---

## 5. Recommended execution order (when approved)

1. Record Legal Input Sheet in pilot folder or operator channel.
2. Generate `privacy-policy`, `consent-personal-data`, `user-agreement`, `cookie-files-policy` pages in v6.
3. Fix footer + `legal-nav.html` L4 drift.
4. Run LEGAL-GENERATION-CONTRACT Phase 3 scan (placeholders, URLs, H1=footer, consent).
5. Operator production sign-off.

---

## 6. SAFE UNKNOWN

- Licensed legal review for Triumph — **not scheduled**.
- Whether `opergt@gktriumph.ru` remains in production mailer BCC — **not verified** on live host.
- PHP vs static-only legal page convention in v6 — **UNKNOWN**.
- Cookie banner presence/requirement on Triumph — **UNKNOWN**.

---

*Gap report version: v1. Location: `workspaces/website-factory-reference-v1/legal/pilots/`.*
