# MARS — Integrations

**Status:** documentation-only (v0). This folder defines integration contracts and governance posture. No real integrations, no live endpoints, and no SDK/runtime connectors are configured in this repository.

---

## Files

| Document | Purpose |
|----------|---------|
| [integration-registry-v0.md](integration-registry-v0.md) | Central registry model for external integrations (fields, lifecycle, governance links). |
| [integration-contract-v0.md](integration-contract-v0.md) | Standard integration interface (input/output envelope, bridge/tool contract rules). |
| [data-exchange-model-v0.md](data-exchange-model-v0.md) | Exchange types and non-bypass data flow rules. |
| [webhook-model-v0.md](webhook-model-v0.md) | Inbound/outbound webhook event model and event mapping. |
| [integration-types-v0.md](integration-types-v0.md) | External system category taxonomy (system-agnostic, no hard binding). |
| [integration-security-v0.md](integration-security-v0.md) | Integration-specific risks, controls, and security governance relations. |

---

## Notes

- This folder is Stage 15 documentation scope only.
- Any future real integration work must pass risk/security/governance updates first.

---

*End of Integrations README.*
