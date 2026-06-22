# Operator-Assisted Live SERP Capture Contract v1 (Wave 2.2)

**Mode:** `OPERATOR-ASSISTED LIVE SERP CAPTURE` (Mode B)  
**Authority:** Technical test evidence only — not production market evidence

## Purpose

Governed degraded fallback when automated Paid SERP acquisition is blocked by CAPTCHA, browser reputation, interactive confirmation, or other external limitation.

The operator captures **bounded raw evidence** only. MIG remains responsible for validation, parsing, registry, and lifecycle registration.

## Operator actions (minimal)

1. Open Yandex in a normal interactive browser (not automation profile).
2. Verify the intended region (e.g. Москва).
3. Run the supplied query during the approved business-hours window.
4. Save raw page evidence using the provided capture method (DevTools snippet or prepared bundle folder).
5. Do **not** classify results, type advertiser fields, or rewrite observations.

## Forbidden operator actions

- Manually typing advertiser rows into the evidence registry
- Editing HTML or screenshot after capture
- Bypassing CAPTCHA
- Using client or Corvonero production queries
- Claiming production authority

## Required capture bundle

| Field | Required |
|-------|----------|
| `project_id` | Yes |
| `session_id` | Yes |
| `query_id` | Yes — must belong to approved technical query set |
| `query` | Yes — exact query text |
| `captured_at` | Yes — ISO timestamp |
| `timezone` | Yes |
| `region` | Yes |
| `device_browser` | Yes |
| Full-page screenshot | Yes where possible |
| HTML / DOM snapshot | Yes, or `html_limitation` recorded |
| `page_url` | Yes |
| Operator attestation | Yes |
| Checksums | Yes — screenshot, HTML, manifest |

## Validation gate

Invalid bundles must block with:

```text
BLOCKED — ASSISTED LIVE CAPTURE BUNDLE INVALID
```

## Import command

```bash
node projects/mig/search-ppc-evidence/runtime/cli/mig-evidence.mjs paid-serp:import-assisted \
  --manifest <project-ppc-state-manifest.json> \
  --bundle <capture-bundle-directory>
```

## Authority

```text
TECHNICAL TEST EVIDENCE ≠ PRODUCTION MARKET EVIDENCE
```

Registered assisted evidence validates acquisition mechanism and parser behavior only.
