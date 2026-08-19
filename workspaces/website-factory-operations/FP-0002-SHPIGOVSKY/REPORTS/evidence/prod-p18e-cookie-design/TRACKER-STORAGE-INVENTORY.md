# Tracker / Storage Inventory — FP-0002 PROD-P18E

**Wave:** design/specification only  
**Verification date:** 2026-08-19  
**Verification mode:** read-only production intake + source/runtime inspection  
**Public origin:** `https://shpigovsky.ru/`

## Scope note

This inventory covers the **actually observed** public site surfaces and the current source/runtime contract visible from:

- live HTML on `https://shpigovsky.ru/`;
- current theme/plugin source in `WORDPRESS/`;
- current legal pages;
- prior production evidence from P18A/P18D.

No imaginary vendors are included.  
Anonymous WordPress Admin/session cookies are listed separately as **admin-only / not public-visitor scope**.

## Current production summary

**ACTUAL COOKIE / STORAGE / TRACKER INVENTORY COMPLETED**

Observed public tracker/storage reality on 2026-08-19:

1. Yandex Metrika counter `98284776` is loaded directly on the public site.
2. The site frontend stores UTM values in `sessionStorage` key `fp02_utm`.
3. Lead forms include hidden reCAPTCHA fields and frontend loader code, but the current localized config leaves `siteConfigEndpoint=''`, so no active public reCAPTCHA vendor load was confirmed from the inspected homepage HTML.
4. Contacts can render Yandex Constructor map script or a map iframe depending on admin data.
5. No live GA/GTM snippet, Google Fonts, Cookiebot, OneTrust, Facebook Pixel, VK Pixel, calltracking, social widget embeds, or video platform embeds were confirmed on the inspected homepage HTML.

## Inventory table

| Technology | Owner / provider | Script / storage / resource | First-party or third-party | Purpose | When it loads today | External transmission | Necessary? | Consent category | Block before consent feasible? | Current legal disclosure status |
|---|---|---|---|---|---|---|---|---|---|---|
| Yandex Metrika | Yandex | Inline snippet in `wp_footer`; loads `https://mc.yandex.ru/metrika/tag.js`; noscript image `https://mc.yandex.ru/watch/98284776` | Third-party service with first-party storage on site domain | Analytics, behavior measurement, goals, webvisor currently enabled in snippet | Immediately on page load, before any visitor choice | Yes, to Yandex | No | Analytics | Yes, by deferring snippet execution and suppressing noscript path when analytics is not allowed | Partially disclosed; privacy/cookie pages mention analytics, but current cookie policy is still generic/demo and does not reflect actual consent gating |
| Yandex Metrika cookies | Yandex | Documented cookie family such as `_ym_uid`, `_ym_d`, `_ym_isad`, `_ym_visorc_*`, `ymex` | First-party cookies created by third-party analytics code | User/session identification and analytics support | After Metrika initializes | Yes | No | Analytics | Yes, if Metrika does not initialize | Not listed factually by name in current live policy |
| Yandex Metrika localStorage / sessionStorage | Yandex | Documented localStorage keys such as `_ym_uid`, `_ym_retryReqs`, `_ym_lastHit`, `_ym_lsid`; sessionStorage keys like `_ym_debugger_state` | First-party browser storage created by third-party analytics code | Analytics support, request retry, identifiers | After Metrika initializes | Yes | No | Analytics | Yes, if Metrika does not initialize | Not listed factually by key in current live policy |
| FP-0002 UTM storage | FP-0002 first-party theme JS | `sessionStorage['fp02_utm']` | First-party | Persist UTM parameters across page views and forms | On frontend JS execution when UTM params are present | No direct external transmission by itself; values later submitted with lead form if visitor submits | Not strictly necessary for basic site rendering; useful for attribution | Recommended under Necessary for current v1 only if the operator wants attribution preserved without extra choice friction; otherwise can be grouped under Analytics in a later stricter model | Yes, technically feasible, but not required for the minimum P18E objective because it is first-party ephemeral storage and not an analytics vendor by itself | Not specifically disclosed today |
| Lead form nonce / hidden operational fields | WordPress / FP-0002 | Hidden form fields, no cookie observed from public GET | First-party | CSRF protection, request integrity, form context | On form render | No by itself | Yes for requested form submission | Necessary | Not applicable | Covered indirectly by form/legal docs, not by cookie policy |
| Form personal-data consent checkbox | FP-0002 | Required checkbox `name="consent"` in public forms | First-party UI state only until submit | Separate consent for submitted personal data | On form render | Submitted only if visitor sends form | Yes for form processing | Outside cookie categories; separate legal basis flow | Not a cookie control | Already present and must remain separate from analytics consent |
| Potential Google reCAPTCHA integration path | Google, if enabled later | Hidden field `g-recaptcha-response`; loader code exists in `v9-shell.js`, but active site key fetch was not confirmed from inspected homepage HTML | Third-party when enabled | Anti-spam | Conditional; not confirmed active in current live homepage | Would transmit to Google if enabled | Usually necessary only for protected form submission, not for page view | `LEGAL REVIEW / OPERATOR DECISION REQUIRED` if enabled later; not part of the current minimum justified categories because live activation not confirmed | Yes, if later implemented through gated lazy loading on form intent | Not confirmed as live today |
| Yandex map embed / constructor | Yandex | Sanitized constructor script or Yandex map iframe on contacts locations | Third-party | Map display | Page-specific; only when contacts block includes map data | Yes | No for baseline site access; yes for map display if visitor explicitly uses that page feature | Not included in v1 categories because current mission explicitly limits the model to Necessary + Analytics unless actual justified extra categories are needed; current recommendation is keep maps out of P18E-v1 scope and review if live map embed becomes material | Technically yes, but not part of current minimum consent model | Current cookie/privacy docs do not accurately describe this as a distinct embedded provider flow |
| WordPress anonymous frontend cookies | WordPress core / hosting / security stack | None confirmed on anonymous homepage response headers (`curl -I` showed no `Set-Cookie`) | First-party | Core technical operation | Not observed on anonymous GET | Not observed | Not applicable based on current anonymous verification | Necessary only if later observed for a real public function | Not applicable | Not specifically listed |

## Admin-only / not public-visitor scope

These should **not** be treated as public cookie-banner scope for anonymous visitors:

| Technology | Notes |
|---|---|
| `wordpress_logged_in_*`, `wordpress_sec_*`, `wp-settings-*`, `wp-settings-time-*`, `wordpress_test_cookie` | Admin/auth/session cookies for WordPress backend use |
| Activity Log data | Admin/system evidence surface, not public visitor storage |
| SMTP/mail settings | Backend operational settings, not public browser storage |

## Public HTML and source evidence highlights

- Live homepage raw HTML includes direct Metrika bootstrap and noscript watch image for counter `98284776`.
- Theme source `inc/seo-integrations.php` outputs the Metrika snippet directly in `wp_footer`.
- The same source currently enables `webvisor:true`.
- Lead form frontend code in `v9-shell.js` stores UTM values in `sessionStorage['fp02_utm']`.
- Form success can call `window.ym(counter, 'reachGoal', goal)` only after backend-accepted JSON.
- Contacts template can render Yandex map embeds/scripts from sanitized admin data.

## Classification decisions for P18E v1

### Necessary

- form security/integrity fields and server-side processing required for a requested submission;
- consent-state persistence itself once P18E is implemented;
- any truly required WordPress/security/session mechanism if later observed for anonymous frontend operation.

### Analytics

- Yandex Metrika counter load;
- Yandex Metrika cookies;
- Yandex Metrika browser storage;
- Metrika goal firing after backend-confirmed form success.

### Deferred / outside current minimal v1 category set

- map embeds;
- any future reCAPTCHA activation;
- any future GTM/GA/custom injected trackers discovered by a fresh implementation-wave intake.

If those become materially active and consent-sensitive, P18E versioning must support category review or a justified future category expansion.

## Current legal disclosure gaps

1. `cookie-files-policy` still contains a demo placeholder for connected analytics systems.
2. The page still says no separate banner/panel is implemented, which is true today but becomes false after P18E implementation.
3. Current documents do not factually enumerate the live Metrika provider, counter gating behavior, or the first-party consent record that P18E plans to introduce.
4. Current documents do not describe browser storage keys in a factual inventory style.

## Inventory conclusion

The smallest justified P18E-v1 consent model remains:

- `Necessary`
- `Analytics`

because the only clearly confirmed non-essential runtime tracker is **Yandex Metrika**.
