# Forge WordPress — Validation Runner Architecture v1

**Document type:** Runner design specification  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-03

**Honesty:** Runner **interface and mapping** only — not full implementation.

---

## 1. WV runner map

| WV | Runner class | Automated | Validator | Human |
|----|--------------|----------:|----------:|------:|
| **WV0** | `wv0-manifest-lint` | **Yes** | Completeness checklist | Operator intake |
| **WV1** | `wv1-architecture-compliance` | Partial | Forge Architect | WAD sign-off |
| **WV2** | `wv2-phpcs` | **Yes** | WordPress Validator | Waiver on MAJOR |
| **WV3** | `wv3-wp-correctness` | Partial | WordPress Validator | Spot-check |
| **WV4** | `wv4-security-scan` | Partial | Security Reviewer | Plugin approval |
| **WV5** | `wv5-playwright-smoke` | **Yes** | WordPress Validator | Editorial walkthrough |
| **WV6** | `wv6-visual-diff` | **Yes** | Visual Parity Validator | **Operator visual approval** |
| **WV7** | `wv7-admin-ux-review` | No | Admin UX Specialist | Editor simulation |
| **WV8** | `wv8-a11y-perf` | Partial | WordPress Validator | Hosting waiver |
| **WV9** | `wv9-package-lint` | **Yes** | WPilot Handoff Reviewer | **BLOCKING handoff** |

---

## 2. Runner interface (specification)

```text
runner_id: string          # e.g. wv2-phpcs
wv_layer: WV0–WV9
inputs: RunnerInput[]      # paths, manifest refs, env profile
outputs: RunnerOutput[]    # report path, exit code, artifacts
exit_codes:
  0 = pass
  1 = fail (blocking)
  2 = warn (non-blocking per profile)
  3 = skip (missing prerequisite)
  4 = error (runner failure)
report_format: markdown + json summary
evidence_storage: REPORTS/ + STORAGE bulk
blocking: boolean per project profile
manual_override: operator sign-off with reason (logged)
```

---

## 3. Layer runners

### WV0 — Manifest and input checker

| Attribute | Value |
|-----------|-------|
| **Runner** | `wv0-manifest-lint` |
| **Inputs** | Handoff manifest, FRONTEND-HANDOFF, passport |
| **Checks** | Schema, required fields, SHA, production_mode |
| **Blocking** | Missing handoff |

### WV1 — Architecture compliance

| Attribute | Value |
|-----------|-------|
| **Runner** | `wv1-architecture-compliance` |
| **Automated** | File presence (theme/plugin split, ACF JSON) |
| **Human** | WAD vs implementation |

### WV2 — PHPCS / lint

| Attribute | Value |
|-----------|-------|
| **Runner** | `wv2-phpcs` |
| **Tool** | PHPCS + WPCS project ruleset |
| **Blocking** | Critical security sniffs |

### WV3 — WordPress correctness

| Attribute | Value |
|-----------|-------|
| **Runner** | `wv3-wp-correctness` |
| **Checks** | Template hierarchy, enqueue, ACF sync (`acf-json` diff) |
| **Optional** | PHPUnit hooks |

### WV4 — Security

| Attribute | Value |
|-----------|-------|
| **Runner** | `wv4-security-scan` |
| **Checks** | FW-S-07 minimum set; secret scan; dependency audit |
| **Human** | Plugin register security |

### WV5 — Functional

| Attribute | Value |
|-----------|-------|
| **Runner** | `wv5-playwright-smoke` |
| **Paths** | Nav, forms, CPT archives |

### WV6 — Visual

| Attribute | Value |
|-----------|-------|
| **Runner** | `wv6-visual-diff` |
| **Human** | **Mandatory** for PIXEL_PERFECT |

### WV7 — Admin UX

| Attribute | Value |
|-----------|-------|
| **Runner** | `wv7-admin-ux-review` |
| **Automated** | — |
| **Human** | Editable regions map compliance |

### WV8 — A11y / perf

| Attribute | Value |
|-----------|-------|
| **Runner** | `wv8-a11y-perf` |
| **Tools** | axe-playwright, Lighthouse CLI |

### WV9 — Package / handoff

| Attribute | Value |
|-----------|-------|
| **Runner** | `wv9-package-lint` |
| **Checks** | RELEASE-MANIFEST, ZIP integrity, no secrets, WV report bundle |

---

## 4. Evidence and blocking

| Rule | Definition |
|------|------------|
| **Evidence** | JSON summary in `REPORTS/`; bulky artifacts in STORAGE |
| **Blocking** | Exit code 1 stops release pipeline |
| **Override** | Operator + validator written waiver — not silent |
| **Sign-off** | WV6, WV9 require human evidence artifact |

---

## 5. Implementation priority (FW-05)

1. `wv0-manifest-lint`
2. `wv2-phpcs`
3. `wv6-visual-diff`
4. `wv5-playwright-smoke`
5. `wv9-package-lint`

---

## Related

- [FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md](FORGE-WORDPRESS-VALIDATION-ARCHITECTURE-v1.md)
- [standards/FORGE-WORDPRESS-VALIDATION-STANDARD-v1.md](standards/FORGE-WORDPRESS-VALIDATION-STANDARD-v1.md)

---

*Runner architecture v1 — specification only.*
