# REPORT — Corvonero RSY import candidate v0.2

## Verdict

CORVONERO RSY IMPORT CANDIDATE:
PASS

## Environment

Drive:
X:

Volume:
AI WS

Repository:
X:\AI MARS

Branch:
mars/canonical-post-recovery

## Operator decisions applied

Structure:
one-campaign fallback

Campaign:
CORVONERO-RSY

Budget:
50 000 ₽

Strategy:
payment for leads/conversions

Goals:
form + calls / operator-confirmed

## Package

Storage:
X:\AI MARS STORAGE\exports\corvonero\CORVONERO-RSY-IMPORT-CANDIDATE-v0.2-2026-08-19

Repo refs:
projects/mars-search-ppc-production/pilots/corvonero/rsy/import-candidate/

Report:
projects/mars-search-ppc-production/reports/REPORT-corvonero-rsy-import-candidate-v0.2.md

## Candidate structure

Campaigns:
1

Groups:
10

Directions included:
5/5

LOCAL represented:
YES

REMOTE represented:
YES

Weak/non-converting directions included:
YES

## Created

Campaign/group candidates:
CREATED

Ad candidates:
CREATED

URL/UTM candidates:
CREATED

Targeting candidates:
CREATED

Image requirements:
CREATED WITHOUT PROMPTS

Exclusions:
CREATED

Operator review checklist:
CREATED

Not-upload-ready guard:
CREATED

## Readiness

Import candidate:
READY_FOR_OPERATOR_REVIEW / NOT_READY

Upload-ready:
NO

Launch approved:
NO

## Not created / not modified

Direct upload file:
NOT CREATED

Final Direct ads:
NOT FINAL

Image prompts:
NOT CREATED

Images:
NOT CREATED

Direct:
NOT MODIFIED

Commander:
NOT MODIFIED

Search campaign package:
UNCHANGED

RSY previous refs:
UNCHANGED

## Validation

Main XLSX sheets:
16/16

Budget recorded:
YES

Strategy intent recorded:
YES

Goals operator-confirmed:
YES

Exact goal IDs:
CHECK_REQUIRED

Exact geo:
CHECK_REQUIRED

No image prompt syntax:
YES

No upload-ready claim:
YES

Git checkpoint:
NOT PERFORMED

Foreign WIP:
PRESERVED

## Remaining blockers before upload-ready

- Exact Direct campaign type (CHECK_REQUIRED).
- Exact Direct strategy field names for payment for leads/conversions (CHECK_REQUIRED).
- Whether Direct import format supports these settings (CHECK_REQUIRED). Exact RSY/ЕПК Commander/import template not verified; optional Direct-like XLSX was therefore not created.
- Exact Metrica/Direct goal names and IDs for form and calls (CHECK_REQUIRED).
- Exact LOCAL geography approval and import mapping.
- Exact REMOTE geography and Novosibirsk exclusion approval.
- Mapping of 50 000 ₽ to daily/weekly/monthly/account field.
- Operator review of all 10 groups, ad candidates, UTM, exclusions.
- Images: not created; prompts not created; manual upload later.
- Landing/legal live-check before launch.
- Approval of import package generation v1.
- Approval of Direct import.
- Approval of launch.

## Required final line

CORVONERO RSY IMPORT CANDIDATE:
PASS — ONE-CAMPAIGN RSY IMPORT CANDIDATE CREATED FOR OPERATOR REVIEW WITH 50 000 ₽ BUDGET AND LEAD-PAYMENT STRATEGY; NOT UPLOAD-READY; NO IMAGE PROMPTS OR DIRECT MODIFICATIONS

## Execution safety

- cwd: X:\AI MARS
- scope lock honored: yes
- allowed roots: X:\AI MARS (repo refs/report); X:\AI MARS STORAGE (package)
- destructive ops: none
- protected zone touch: none (programme docs under projects/mars-search-ppc-production only)
- Direct/Commander: not opened
- stage/commit/push: not performed
