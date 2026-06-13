# Website Factory — Legal Pack v1 FREEZE

**Версия:** v1  
**Дата freeze:** 2026-05-30  
**Статус:** **FROZEN**  
**Operator:** APPROVED BY OPERATOR  
**Область freeze:** `workspaces/website-factory-reference-v1/legal/` + `legal-entity/`  
**Validated pilot:** Triumph Manipulator Landing V6 — Legal Pilot Phase 2

**Не является:** юридической экспертизой, runtime, CI-валидатором, автоматической генерацией.

---

## Purpose

Legal Pack v1 — канонический **documentation + human-operated workflow** слой Website Factory для Core Legal Pack (L1–L4): шаблоны, правила подстановки, discovery юрлица, контракт генерации и production rules (Footer Rule, Consent Rule, placeholder gate).

**Layout principle (v1 freeze):** legal pages **inherit project content layout and typography** — см. [LEGAL-IMPLEMENTATION-RULES.md](LEGAL-IMPLEMENTATION-RULES.md) §9 Legal Content Layout Rule; layout checks — [LEGAL-GENERATION-CONTRACT-v1.md](LEGAL-GENERATION-CONTRACT-v1.md) Phase 3.

Freeze фиксирует **завершённый** baseline после успешного Triumph Legal Pilot Phase 2 и финального consistency/URL audit.

---

## Scope

| In scope (frozen) | Out of scope |
|-------------------|--------------|
| Core Legal Pack L1–L4 templates | Extension Packs (ECOMMERCE, SAAS, MARKETPLACE, Corporate Custom) |
| Legal Pack Architecture v1 | SITE-TYPE-BLUEPRINTS-v1 |
| Legal Entity Discovery System v1 | SITE-TYPE-SEO-MAPPING-v2 |
| Legal Input Sheet + Generation Contract + Workflow | Design System Mapping |
| Production rules (footer, consent, URLs) | Automatic HTML pipeline / CI validator |
| Triumph V6 pilot as reference implementation | Licensed legal review |

**Pilot workspace:** `workspaces/triumph-manipulator-landing-v6/`

---

## Included components

| Component | Location | Freeze status |
|-----------|----------|---------------|
| **Legal Templates** (L1–L4) | `legal/*-template.md` | **FROZEN** |
| **Legal Architecture** | [LEGAL-PACK-ARCHITECTURE-v1.md](LEGAL-PACK-ARCHITECTURE-v1.md) | **FROZEN** |
| **Legal Entity Discovery** | [legal-entity/LEGAL-ENTITY-DISCOVERY-RULES-v1.md](../legal-entity/LEGAL-ENTITY-DISCOVERY-RULES-v1.md) | **FROZEN** |
| **Legal Entity Card** | [legal-entity/LEGAL-ENTITY-CARD-v1.md](../legal-entity/LEGAL-ENTITY-CARD-v1.md) (+ template, workflow, validation) | **FROZEN** |
| **Legal Input Sheet** | [LEGAL-INPUT-SHEET-v1.md](LEGAL-INPUT-SHEET-v1.md) (+ template, instructions) | **FROZEN** |
| **Legal Generation Contract** | [LEGAL-GENERATION-CONTRACT-v1.md](LEGAL-GENERATION-CONTRACT-v1.md) | **FROZEN** |
| **Legal Workflow** | [LEGAL-GENERATION-WORKFLOW-v1.md](LEGAL-GENERATION-WORKFLOW-v1.md) | **FROZEN** |

**Supporting frozen artifacts:**

- [LEGAL-IMPLEMENTATION-RULES.md](LEGAL-IMPLEMENTATION-RULES.md) — Footer Rule, Consent Rule
- [LEGAL-VARIABLE-REGISTRY.md](LEGAL-VARIABLE-REGISTRY.md)
- [SITE-TYPE-LEGAL-MAPPING-v2.md](SITE-TYPE-LEGAL-MAPPING-v2.md)
- [LEGAL-TEMPLATE-HARDENING-v1.1.md](LEGAL-TEMPLATE-HARDENING-v1.1.md)

---

## Validated pilot — Triumph Manipulator V6

**Phase 2 outcome:** legal pages generated in pilot workspace.

| Check | Result |
|-------|--------|
| L1 `/privacy-policy/` — page + H1 «Политика конфиденциальности» | **PASS** |
| L2 `/consent-personal-data/` — page + H1 «Согласие на обработку персональных данных» | **PASS** |
| L3 `/user-agreement/` — page + H1 «Пользовательское соглашение» | **PASS** |
| L4 `/cookie-files-policy/` — page + H1 «Политика Cookie-файлов» | **PASS** |
| Footer links (`landing-footer.html`, `landing-footer-legal.html`) — text = H1 | **PASS** |
| Legal nav (`legal-nav.html`) — text = H1 | **PASS** (fixed at freeze: L2 short label) |
| Consent Rule (form partials) | **PASS** |
| Forbidden placeholders in legal content | **PASS** (zero `{{...}}` in legal partials) |
| Legacy `/cookies/` in V6 workspace | **PASS** (none remaining) |

**Pilot artifacts (V6):**

- `src/pages/privacy-policy/index.html`
- `src/pages/consent-personal-data/index.html`
- `src/pages/user-agreement/index.html`
- `src/pages/cookie-files-policy/index.html`
- `src/partials/sections/legal/content/*.html`
- Shell: `legal-document.html`, `legal-nav.html`, `legal-header.html`, `landing-footer-legal.html`

**Pre-freeze fix applied:** `legal-nav.html` L2 label «Согласие на обработку данных» → «Согласие на обработку персональных данных».

---

## Known limitations

| Limitation | Notes |
|------------|-------|
| **No automated CI validator** | [LEGAL-GENERATION-CONTRACT-v1.md](LEGAL-GENERATION-CONTRACT-v1.md) Phase 3 — human-operated grep only |
| **No OCR pipeline** | Legal Entity Discovery — manual extraction per [LEGAL-ENTITY-EXTRACTION-GUIDE-v1.md](../legal-entity/LEGAL-ENTITY-EXTRACTION-GUIDE-v1.md) |
| **No legal review by licensed lawyer** | Templates are operational baseline, not legal advice |
| **Human-operated workflow** | Copy from templates → substitute variables → manual audit; no autonomous generation |
| **Extension packs not frozen** | ECOMMERCE, SAAS, MARKETPLACE, Corporate Custom — see Future Extensions |
| **Footer copyright drift (Triumph)** | Main footer uses `ООО «ТРИУМФ»`; legal footer uses `© 2026 Триумф` — operator alignment optional |
| **Form validation copy** | Error text «Подтвердите согласие на обработку данных» — UX message, not nav link; outside Footer Rule scope |

---

## Future extensions (NOT part of freeze v1)

These extension packs are **documented in architecture** but **explicitly excluded** from Legal Pack v1 freeze:

| Extension | Scope (planned) | Status |
|-----------|-----------------|--------|
| **ECOMMERCE Extension** | Offer, payment, delivery, returns legal docs | **NOT FROZEN** |
| **SAAS Extension** | Subscription, SLA, account terms | **NOT FROZEN** |
| **MARKETPLACE Extension** | Seller/buyer, commission, dispute terms | **NOT FROZEN** |
| **Corporate Custom Extension** | Bespoke corporate legal pages beyond Core L1–L4 | **NOT FROZEN** |

Reference: [LEGAL-PACK-ARCHITECTURE-v1.md](LEGAL-PACK-ARCHITECTURE-v1.md) — Extension Packs section.

---

## Canonical URLs (frozen)

| Doc | URL | Link text (= H1) |
|-----|-----|------------------|
| L1 Privacy Policy | `/privacy-policy/` | Политика конфиденциальности |
| L2 Personal Data Consent | `/consent-personal-data/` | Согласие на обработку персональных данных |
| L3 User Agreement | `/user-agreement/` | Пользовательское соглашение |
| L4 Cookie Policy | `/cookie-files-policy/` | Политика Cookie-файлов |

**Forbidden legacy paths:** `/cookies/`, `/privacy/`, `/terms/` — must not appear in production footers or legal nav.

---

## Freeze verdict

**Website Factory Legal Pack v1: FROZEN**

Change control after freeze: modifications require explicit operator charter; new work defaults to **next approved workstream** — SITE-TYPE-BLUEPRINTS-v1.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Formal `TRIUMPH-LEGAL-INPUT-v1.md` artifact in V6 workspace | **UNKNOWN** — pilot pages exist; signed Input Sheet path not verified in repo at freeze |
| Licensed legal review for Triumph production deploy | **UNKNOWN** |
| Production deploy authorization for Triumph legal pages | **UNKNOWN** — pending operator |
| Cookie banner requirement on Triumph | **UNKNOWN** |
| Live analytics/recaptcha inventory for L4 factual accuracy | **UNKNOWN** |

---

*Freeze document version: v1. Canonical location: `workspaces/website-factory-reference-v1/legal/`.*
