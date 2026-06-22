# Forge WordPress — Future Skill Model v1

**Document type:** Future reusable skill specification  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-03

**No skills created. No agent registration.**

---

## 1. Skill catalog

| Skill ID | Purpose | Inputs | Outputs | Standards | Allowed tools | Human gate | Future owner | Priority |
|----------|---------|--------|---------|-----------|---------------|------------|--------------|----------|
| FW-SK-01 | Frontend package inspection | Handoff manifest, FRONTEND path | WV0 checklist | FW-C-01 | Git, npm, inspect ops | Operator intake | Implementer | **P1** |
| FW-SK-02 | Block-to-WP mapping | Section list, template map | BLOCK-TO-WP-MAPPING | FW-S-03, Gulp model | Read FS | Architect approval | Theme Specialist | **P1** |
| FW-SK-03 | Content modeling | Brief, IA | CONTENT-MODEL, CPT map | FW-S-01 | — | G4 sign-off | Content Modeler | **P1** |
| FW-SK-04 | WAD preparation | Mode, maps | WAD document | FW-01 modes | — | G3 | Forge Architect | **P1** |
| FW-SK-05 | Theme architecture | WAD, handoff | Theme scaffold plan | FW-S-03 | PHPCS read | Architect | Theme Specialist | **P1** |
| FW-SK-06 | ACF architecture | Content model | ACF-SCHEMA, JSON | FW-S-02 | inspect_acf | Content Modeler | Content Modeler | **P2** |
| FW-SK-07 | CPT/taxonomy design | IA | CPT-TAXONOMY-MAP | FW-S-01 | — | G4 | Content Modeler | **P2** |
| FW-SK-08 | Admin UX | Editable regions | ADMIN-UX-MAP | FW-S-05 | — | G4 | Admin UX Specialist | **P2** |
| FW-SK-09 | Plugin governance | Plugin list | PLUGIN-REGISTER | FW-S-06 | WP-CLI read | Operator | Forge Architect | **P2** |
| FW-SK-10 | PHP/WP coding | WAD, templates | Theme/plugin code | FW-S-07 | PHPCS, WP-CLI | Code review | Theme Specialist | **P1** |
| FW-SK-11 | Security review | Code, register | WV4 report | FW-S-07 | wv4-security-scan | Security reviewer | Validator | **P1** |
| FW-SK-12 | Visual validation | Baselines, WP URL | VISUAL-QA-REPORT | WV6 | Playwright | **Operator approval** | Visual Validator | **P1** |
| FW-SK-13 | Packaging | Built artifacts | RELEASE-MANIFEST | FW-T-12 | zip, wv9 | G9 | Forge Architect | **P1** |
| FW-SK-14 | WPilot handoff | RC package | WPILOT-HANDOFF | FW-C-03 | prepare_wpilot_handoff | **G10 BLOCKING** | Handoff Reviewer | **P1** |

---

## 2. Minimum skill set for first pilot

1. FW-SK-01 Frontend package inspection  
2. FW-SK-02 Block-to-WP mapping  
3. FW-SK-04 WAD preparation  
4. FW-SK-05 Theme architecture  
5. FW-SK-10 PHP/WP coding  
6. FW-SK-12 Visual validation  
7. FW-SK-13 Packaging  
8. FW-SK-14 WPilot handoff  

Optional for pilot if no custom logic: FW-SK-06, FW-SK-07.

---

## 3. Registration boundary

Skills may become Cursor skills or agent tool cards in **FW-05+** — **not** in FW-03. `AG-WP-001` registration remains **FW-05 charter**.

---

## Related

- [FORGE-WORDPRESS-ROLE-AND-AGENT-MODEL-v1.md](FORGE-WORDPRESS-ROLE-AND-AGENT-MODEL-v1.md)
- [FORGE-WORDPRESS-FUTURE-VALIDATOR-MODEL-v1.md](FORGE-WORDPRESS-FUTURE-VALIDATOR-MODEL-v1.md)

---

*Future skill model v1 — design only.*
