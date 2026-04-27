# MARS — Integration Types v0

**Status:** documented — external system category taxonomy for integration planning. No hardcoded vendor bindings and no active connectors are defined by this file.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md).

---

## 1. Purpose

- Classify external system categories that MARS may connect to.
- Keep design vendor-neutral and avoid hard binding in core contracts.
- Support consistent risk/approval reasoning across integration planning.

---

## 2. Categories (v0)

| Category | Description |
|----------|-------------|
| **CRM** | Customer/business record systems for account, lead, or contact workflows. |
| **messaging** | Communication channels (for example: Telegram-class systems) for notifications and interactions. |
| **analytics** | Reporting/metrics systems for operational and product analysis exports. |
| **storage** | External storage targets for files, archives, or retrieval payloads. |
| **automation** | Workflow automation systems (for example: n8n-class orchestrators). |
| **APIs** | Generic third-party or partner API surfaces not covered by the categories above. |

---

## 3. Rules (normative v0)

1. **No hard binding** — categories describe classes, not specific vendor lock-in.
2. **System-agnostic design** — contracts should remain portable across providers.
3. **Category declaration required** — each planned integration should declare one primary category and optional secondary tags.

---

## 4. Relation to integration registry

This taxonomy supports [integration-registry-v0.md](integration-registry-v0.md) field consistency (`type`, risk posture, approval stance) and cross-system governance alignment.

---

## 5. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-28 | Integration Types v0 created: category taxonomy and no-hard-binding/system-agnostic rules. |

---

*End of Integration Types v0.*
