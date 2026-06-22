# MARS Localhost MLI-03 — WordPress Runtime Profile Input v1

**Document type:** Stage input (not executed)  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** MLI-03 — **NEXT**

---

## Prerequisites (MLI-02 complete)

- Shared toolchain hardened
- Hosts management documented
- HTTPS baseline tested
- PHPCS/WPCS/PHPCompatibility available
- Playwright smoke fixture proven
- WP-CLI baseline ready
- **No WordPress site yet**

---

## MLI-03 scope

1. WordPress runtime provisioning (synthetic)
2. Runtime manifest per site
3. DB/user creation (local least-privilege)
4. Local domain + hosts
5. HTTPS optional trust step
6. WordPress core download/install via WP-CLI
7. Theme/plugin installation (synthetic)
8. Synthetic data only
9. Forge WordPress consumer handoff pointers
10. Backup/reset procedure
11. Browser validation (Playwright)
12. **No production** access

---

## Forge handoff

- Enable FW-05R live synthetic validation after MLI-03 evidence
- FP-0002 remains **out of scope** until explicit charter

---

## Related

- [MARS-LOCALHOST-WPCLI-STANDARD-v1.md](../MARS-LOCALHOST-WPCLI-STANDARD-v1.md)
- [MARS-LOCALHOST-MYSQL-LOCAL-CREDENTIALS-POLICY-v1.md](../MARS-LOCALHOST-MYSQL-LOCAL-CREDENTIALS-POLICY-v1.md)

---

*MLI-03 input v1 — prepared at MLI-02 closeout.*
