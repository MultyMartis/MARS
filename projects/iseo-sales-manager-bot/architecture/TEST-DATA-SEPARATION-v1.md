# TEST DATA SEPARATION v1

- Real leads → `LEADS` + production `LEAD_EVENTS`
- Fixtures → `TEST_LEADS` + `TEST_LEAD_EVENTS` only
- Fixtures never enter production stats, `/leads`, pending, reminders, or reporting workbook
- Optional admin `/cleanup_tests`: preview + confirmation token; test tabs only
- After acceptance, archive/delete test rows without touching production
