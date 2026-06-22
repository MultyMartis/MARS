# Forge WordPress — Future Validator Model v1

**Document type:** Validator role and independence specification  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-03

**No validators registered as agents. No fictional runtime.**

---

## 1. Validator registry

| Validator | WV layers | Mergeable with | Independent | Human-only gates |
|-----------|-----------|----------------|-------------|------------------|
| **Architecture validator** | WV1 | — | **Yes** if implementer ≠ architect | WAD sign-off |
| **Code quality validator** | WV2 | Static analysis | Partial | Waiver on MAJOR |
| **WordPress correctness validator** | WV3, WV5 | Code quality | Partial | Functional spot-check |
| **Security validator** | WV4 | Code quality (sniffs) | **Yes** | Plugin approval |
| **Functional validator** | WV5 | WP correctness | Mergeable | Editorial walkthrough |
| **Visual parity validator** | WV6 | — | **Yes** | **Operator visual approval** |
| **Admin UX validator** | WV7 | — | **Yes** | Editor simulation |
| **Package/handoff validator** | WV9 | — | **Yes** | **WPilot handoff acceptance** |

---

## 2. Merge rules

| Combination | Allowed | Condition |
|-------------|---------|-----------|
| WV2 + WV3 | Yes | Same human **if** not sole implementer on large plugin |
| WV4 + WV2 | Partial automation | Security reviewer **must** sign WV4 independently |
| WV6 + WV2 | No merge on sign-off | Visual approval independent of PHPCS pass |
| WV7 + WV6 | Parallel | Different concerns |
| WV9 | Independent | Handoff reviewer ≠ sole packager |

---

## 3. Independence requirements

| Rule | Definition |
|------|------------|
| **R-VAL-01** | Implementer cannot be sole signatory on WV1 for same delivery |
| **R-VAL-02** | WV6 operator approval cannot be delegated to implementer agent |
| **R-VAL-03** | WV9 handoff acceptance requires human operator |
| **R-VAL-04** | Automated runner pass ≠ validator sign-off |

---

## 4. Human-only gates (non-automatable)

- WV0 operator intake confirmation  
- WV1 WAD compliance sign-off  
- WV6 PIXEL_PERFECT operator approval  
- WV7 client editor simulation  
- WV9 WPilot handoff acceptance  

---

## Related

- [FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md](FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md)
- [FORGE-WORDPRESS-HUMAN-CONTROL-MODEL-v1.md](FORGE-WORDPRESS-HUMAN-CONTROL-MODEL-v1.md)

---

*Future validator model v1.*
