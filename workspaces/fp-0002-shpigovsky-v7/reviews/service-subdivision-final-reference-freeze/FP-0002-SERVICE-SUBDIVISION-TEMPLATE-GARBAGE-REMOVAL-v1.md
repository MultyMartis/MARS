# FP-0002 SERVICE SUBDIVISION — TEMPLATE GARBAGE REMOVAL v1

- Visible fragment: `else { }` near Program heading link
- Source file: `src/partials/sections/services-program-v2.html`
- Root cause: `gulp-file-include` does not process `} else {` branches; literal `else {` leaked into compiled HTML when `usePlayLinkIcon === 'true'`
- Source correction: split into two `@@if` blocks (`=== 'true'` and `!== 'true'`) for head and foot link icons
- Subdivision compiled `else {` count: **0**
- Services V2 compiled `else {` count: **0**
- Home compiled `else {` count: **0**
- CSS/JS hiding used: **no**
- Verdict: **PASS**
