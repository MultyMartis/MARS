# QA Lead Cleanup — P18D-FU01

## Exact QA object

Captured in `08-post-removal-form-qa.json`:

- lead id: `7`
- `form_context = p18d-fu01-qa`
- `is_qa = 1`
- `utm_source = p18d-fu01-qa`
- delivery status before cleanup: `MAIL_ACCEPTED`

## Cleanup rule applied

Deletion allowed because the row was explicitly identifiable as QA by:

- exact known ID from FU01 evidence; and
- `is_qa = 1`; and
- FU01 marker values.

## Cleanup result

Recorded in `09-qa-cleanup.json`:

- requested: `7`
- deleted: `7`
- skipped: none

## Safety note

No uncertain rows were deleted.  
No real leads were touched.  
There were no pre-existing QA rows remaining after FU01 cleanup.
