# Password configured-state preservation

**Required:** `RECIPIENT EDITING CANNOT ERASE SMTP SECRET`

| Checkpoint | Password configured |
|------------|---------------------|
| Intake before code change | YES |
| After deploy, before QA saves | YES |
| After adding temporary recipient | YES |
| After removing temporary recipient | YES |
| Final | YES |

- `smtp_password` HTML value remains empty
- QA posts used blank password and did not set `smtp_password_clear`
- `fp02_mailbox_auth` secret never printed (length-only at intake: 22)
- Secret not present in Admin HTML, Dashboard HTML, Activity Log titles, this evidence, or Git source

Non-secret SMTP fingerprint unchanged across recipient saves: host `smtp.beget.com`, port `465`, encryption `none`, auth `1`, username `noreply@shpigovsky.ru`, from `noreply@shpigovsky.ru`, from name `Шпиговский дом`, Metrika goal empty, retention `0`, verified `0`, delivery_active `0`.
