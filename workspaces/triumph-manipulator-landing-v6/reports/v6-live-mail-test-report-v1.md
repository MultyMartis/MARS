# V6 live mail test report v1

**Date:** 2026-05-28  
**Workspace:** `workspaces/triumph-manipulator-landing-v6/`  
**Test type:** Human-operated production form submission on live hosting  
**Freeze context:** Full Triumph V6 Website Factory safety freeze

---

## Test configuration

| Field | Value |
|-------|--------|
| **Tested URL** | `https://manipulator-triumph.ru/konteynery.html` |
| **Tested form** | konteynery hero form (`data-form-id="konteynery-hero-quote"`) |
| **Mailer endpoint (build)** | `backend/send-lead.php` |
| **Recipient** | `client.leads@polygon-ws.ru` |

---

## Result

**PASS** — email received successfully after form submission on production hosting.

---

## Confirmed fields (operator observation in received email)

- phone
- name
- form_id
- cta_source
- landing_id
- page_type
- page URL
- IP
- User-Agent
- server date

---

## Conclusion

V6 mailer MVP is **production-working** on hosting for the konteynery hero form path tested. This satisfies the live gate for the current safety freeze checkpoint.

---

## SAFE UNKNOWN

- Other route forms (`index`, `5-tonn`, `bytovki`, modal/callback forms) still need spot testing on hosting if required by a future charter.
- Deliverability under volume, SMTP migration, and anti-spam edge cases are not validated by this single live test.
