# Direct Commander Export Workflow v0

## Goal

Prepare a structured export package for human review and manual use in Direct Commander style import workflows.

## Steps

1. Confirm that campaign structure and ad copy are human-approved for export preparation.
2. Map campaign, ad group, keyword, negative, and ad fields to export tables.
3. Mark missing required fields as SAFE UNKNOWN.
4. Check naming consistency and duplicate rows.
5. Prepare manual import notes and platform assumptions.

## Inputs

- Campaign structure contract.
- Draft ad copy.
- Keyword and negative keyword tables.
- Platform field requirements.
- Human export preferences.

## Outputs

- Export package contract.
- Export-ready draft tables.
- Manual import checklist.
- Format risk notes.

## Human Checkpoints

- Confirm export format and target platform.
- Review all required fields.
- Approve tracking parameters and URLs.
- Perform the actual import manually.

## Failure Risks

- Platform column requirements differ from the assumed template.
- Missing URL, tracking, or region fields block import.
- Incorrect names create account clutter.
- Human review is skipped before import.

## REPORT Expectations

The report must include included tables, missing fields, format assumptions, SAFE UNKNOWN items, and whether the package is ready for human import review.

This workflow does not connect to, upload to, or modify Yandex.Direct or Google Ads.
