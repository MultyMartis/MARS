# CF-011 Subdivision ARIA root cause

| Field | Value |
|---|---|
| Page | `usluga-podrazdel-v1.html` |
| Source (pre) | `service-subdivision-first-cta-v1.html` |
| Broken reference | `aria-labelledby="service-subdivision-start-heading"` |
| Missing target | `#service-subdivision-start-heading` |
| Root cause | Wrapper section declared `aria-labelledby` but no heading element carried the ID; visible title lived only in band `p.program-cta-band__title` |
| Repair | Canonical `program-cta-band.html` with `headingText` + `headingId` renders visually-hidden `h2` matching `aria-labelledby` |
| Result | REPAIRED — page-wide DOM gate PASS |
