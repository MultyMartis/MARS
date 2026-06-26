# FP-0002 — Services V2 Program Component Reuse Decision v1

| Check | Verdict |
| ----- | ------- |
| Home Program inspected | yes — `home-rehabilitation-program.html` |
| Content reuse | partial — same 4 direction titles; Services lead/intro/item bodies differ |
| DOM reuse | **no** — Home vertical row cards; Services 2×2 image-top cards |
| CSS pattern reuse | yes — head link, lead border, CTA dark band, button/modal hooks |
| Services-specific structure required | **yes** |
| New partial | `services-program-v2.html` + `services-program-v2-item.html` |
| Over-abstraction avoided | yes — only used parameters |
| **Verdict** | **SERVICES_SPECIFIC_PARTIAL** |
