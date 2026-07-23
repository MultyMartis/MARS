# ISEO-SU HYBRID DISCOVERY QUESTIONNAIRE v1

**Audience:** Operator (Andrey)  
**Programme:** ISEO-SU-SITE-OPS  
**Phase:** 2 — Non-secret evidence intake  
**Status:** READY FOR OPERATOR COMPLETION (start with Wave A topics)  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`  

Instructions:

- Answer factually. Use **unknown** when unsure.  
- Do **not** provide passwords, tokens, cookies, keys, DSNs, or `wp-config` values.  
- Prefer short answers. Attach sanitized evidence only after reading the redaction guide.  
- Wave A answers are requested first; deeper items can wait until Wave A review.

Related: [ISEO-SU-NON-SECRET-EVIDENCE-REQUEST-v1.md](ISEO-SU-NON-SECRET-EVIDENCE-REQUEST-v1.md)

---

## Hosting

1. What is the hosting provider name?  
2. What control panel (if any) do you use?  
3. Is there a separate staging/dev host? If yes, what is the public hostname (no secrets)?  

## Docroot

4. What is the site document root path shape (redact account segment if needed)?  
5. Is the public site root the same folder as WordPress, or a parent/sibling layout?  

## Static files

6. Which main sections are static HTML files?  
7. Where do static assets (css/js/images) usually live (folder names only)?  

## WordPress path

8. Does WordPress admin exist for this site?  
9. What is the WordPress directory name/path relative to docroot (if known)?  

## Routing

10. How do requests choose static pages vs WordPress (rewrite, subdirectory, unknown)?  
11. Are there special entry files (e.g. `index.html` vs `index.php`) you know of by name?  

## Header / footer

12. Who owns the site header and footer — static includes, WordPress theme, both, or unknown?  
13. If shared, how are they included (filename/theme part names if known)?  

## Theme

14. What is the active theme name?  
15. Is there a child theme? Name?  

## Plugins

16. List active plugins you know (names only).  
17. Any security, cache, SEO, form, or ACF-related plugins you recall?  

## ACF

18. Is Advanced Custom Fields (or ACF Pro) active?  
19. Which entities/pages use ACF fields (plain language)?  

## Blog

20. What is the public blog URL/path?  
21. Is the blog the only WordPress content surface, or are there more WP pages/CPTs?  

## Tariffs

22. Where do tariff cards appear (URL/path)?  
23. Are tariff cards static markup, WP/ACF, or unknown?  

## Calculator

24. What is the SEO calculator public URL/path?  
25. What does it do in one sentence?  
26. Known source folder/file names?  

## Web commercial proposal (web-KP)

27. What is the web-KP public URL/path?  
28. What does it do in one sentence?  
29. Known source folder/file names?  
30. Any external integrations (CRM, mail, PDF, payment) by product name only?  

## Forms

31. Which pages have lead forms?  
32. Where do submissions go (email / CRM / WP / unknown) — no credentials?  

## Mail

33. How is mail sent in plain language (hosting mail, SMTP plugin, external ESP, unknown)?  
34. Who notices if forms stop delivering?  

## Build tools

35. Is there a frontend build step (npm, gulp, webpack, none, unknown)?  
36. Who usually rebuilds/publishes assets?  

## Git / source

37. Does current source exist in Git? Remote name or “local only” / “none” / “unknown”?  
38. Is production ever edited directly without Git?  

## Backups

39. What backup method exists today (hosting backup, manual archive, none, unknown)?  
40. Who can restore, and roughly what retention exists?  

## Manual drift

41. Which production files/areas were changed manually and must be preserved?  
42. Any “never overwrite” paths or tools?  

## Staging

43. Can changes be tested off production? If not, what is the riskiest area to touch live?  

## Critical routes

44. List business-critical pages/tools that must not be touched without explicit approval.  

## Forbidden areas

45. List areas agents/operators must not modify until a later charter (e.g. billing, mail, auth).  

## Access existence (yes/no only — no secrets)

46. Does FTP or SFTP access exist?  
47. Does anyone besides you currently have panel/WP/file access (roles/names only)?  

---

## Answer log (operator fill-in)

| Q# | Answer | Date | Classification hint |
|----|--------|------|---------------------|
| | | | OPERATOR CONTEXT / CONFIRMED BY OPERATOR / SAFE UNKNOWN |

*(Leave blank until answers arrive. Do not paste secrets here.)*

---

*Hybrid discovery questionnaire v1 · 2026-07-22 · no credential questions.*
