import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, '..');
const srcPath = path.join(root, 'ORCA-PPC-SEMANTIC-CORE-WORLD-PRACTICE-RESEARCH-v1.md');
const outPath = path.join(root, 'intake', 'ORCA-PPC-SEMANTIC-CORE-WORLD-PRACTICE-RESEARCH-NORMALIZED-v1.md');

const src = fs.readFileSync(srcPath, 'utf8');

const markerMap = {
  turn0file0: 'SRC-ORCA-ATTACHED-BRIEF-v0',
  turn5view0: 'SRC-GOOGLE-ADS-KEYWORD-MATCHING-v0',
  turn16view0: 'SRC-GOOGLE-ADS-SEARCH-TECH-GUIDE-v0',
  turn16view4: 'SRC-GOOGLE-ADS-KEYWORD-MATCHING-v0',
  turn21view0: 'SRC-GOOGLE-ADS-NEGATIVE-KEYWORDS-v0',
  turn21view1: 'SRC-GOOGLE-ADS-SEARCH-TECH-GUIDE-v0',
  turn29view0: 'SRC-GOOGLE-ADS-SEARCH-TERMS-REPORT-v0',
  turn28view0: 'SRC-GOOGLE-ADS-AD-GROUP-GUIDANCE-v0',
  turn26view0: 'SRC-GOOGLE-ADS-KEYWORD-MATCHING-v0',
  turn26view1: 'SRC-GOOGLE-ADS-KEYWORD-MATCHING-v0',
  turn6view3: 'SRC-YANDEX-DIRECT-KEYWORDS-v0',
  turn6view1: 'SRC-YANDEX-DIRECT-SEARCH-QUERIES-v0',
  turn8view0: 'SRC-YANDEX-DIRECT-OPERATORS-v0',
  turn9view0: 'SRC-YANDEX-DIRECT-NEGATIVE-KEYWORDS-v0',
  turn9view2: 'SRC-YANDEX-DIRECT-NEGATIVE-KEYWORDS-v0',
  turn9view3: 'SRC-YANDEX-DIRECT-AUTOTARGETING-v0',
  turn9view4: 'SRC-YANDEX-DIRECT-AUTOTARGETING-v0',
  turn9view5: 'SRC-YANDEX-DIRECT-AUTOTARGETING-v0',
  turn23academia0: 'SRC-ORCAS-I-PAPER-v0',
  turn23academia1: 'SRC-SNORKEL-PAPER-v0',
  turn23academia2: 'SRC-SNORKEL-PAPER-v0',
  turn18academia0: 'SRC-ACTIVE-LEARNING-SURVEY-v0',
  turn20academia1: 'SRC-ACTIVE-LEARNING-SURVEY-v0',
  turn24academia2: 'SRC-COST-SENSITIVE-REJECTION-v0',
  turn24academia3: 'SRC-COST-SENSITIVE-REJECTION-v0',
  turn25academia0: 'SRC-COST-SENSITIVE-REJECTION-v0',
  turn34academia0: 'SRC-SEARCH4CODE-PAPER-v0',
  turn34academia1: 'SRC-PRODUCT-INSIGHTS-BING-v0',
  turn19academia0: 'SRC-SEARCH4CODE-PAPER-v0',
  turn19academia2: 'SRC-PRODUCT-INSIGHTS-BING-v0',
  turn35academia1: 'SRC-SPONSORED-SEARCH-CATEGORY-SIM-v0',
  turn35academia2: 'SRC-SPONSORED-SEARCH-CATEGORY-SIM-v0',
  turn3academia0: 'SRC-SPONSORED-SEARCH-CATEGORY-SIM-v0',
};

function slugify(title) {
  return title
    .toLowerCase()
    .replace(/[^\w\u0400-\u04FF]+/g, '-')
    .replace(/^-|-$/g, '');
}

let body = src;
body = body.replace(/^## (.+)$/gm, (m, title) => `## ${title} {#sec-${slugify(title)}}`);
body = body.replace(/^### (.+)$/gm, (m, title) => `### ${title} {#sec-${slugify(title)}}`);
body = body.replace(/\uE200filecite\uE202turn0file0\uE201/g, '[SRC-ORCA-ATTACHED-BRIEF-v0]');
body = body.replace(/\uE200cite\uE202([^\uE201]+)\uE201/g, (_, inner) => {
  const ids = [...inner.matchAll(/turn[a-z0-9]+/g)].map((x) => markerMap[x[0]] || `UNRESOLVED:${x[0]}`);
  return `[${[...new Set(ids)].join('; ')}]`;
});

const header = `# ORCA PPC Semantic Core — World Practice Research (Normalized Companion v1)

> **Normalization status:** companion to canonical source — original bytes preserved separately.
> **Authority class:** ANALYTICAL SOURCE — SELECTIVE PROMOTION REQUIRED
> **Canonical source:** \`../ORCA-PPC-SEMANTIC-CORE-WORLD-PRACTICE-RESEARCH-v1.md\`
> **SHA-256 (canonical):** \`984192DAFC79AA9E7071C5F915CD30A630924C5EEBAE22BFD6C26CCD43CE5ACD\`

## Normalization notes

- Stable section anchors added as \`{#sec-...}\` suffixes on headings.
- Internal citation markers replaced with stable source IDs where mapping is supported by the research starter source list.
- Unmapped markers retained as \`UNRESOLVED:<marker>\` inside bracket groups.
- Sections labeled as ORCA recommendations in the original remain recommendations — not documented ORCA facts.
- This file is **not** a phrase decision registry and **not** production authority.

## Bibliography mapping (marker → source ID)

| Original marker | Stable source ID |
|-----------------|------------------|
| turn0file0 | SRC-ORCA-ATTACHED-BRIEF-v0 |
| turn5view0 | SRC-GOOGLE-ADS-KEYWORD-MATCHING-v0 |
| turn16view0 | SRC-GOOGLE-ADS-SEARCH-TECH-GUIDE-v0 |
| turn21view0 | SRC-GOOGLE-ADS-NEGATIVE-KEYWORDS-v0 |
| turn29view0 | SRC-GOOGLE-ADS-SEARCH-TERMS-REPORT-v0 |
| turn6view3 | SRC-YANDEX-DIRECT-KEYWORDS-v0 |
| turn8view0 | SRC-YANDEX-DIRECT-OPERATORS-v0 |
| turn9view0 | SRC-YANDEX-DIRECT-NEGATIVE-KEYWORDS-v0 |
| turn9view3 | SRC-YANDEX-DIRECT-AUTOTARGETING-v0 |
| turn23academia0 | SRC-ORCAS-I-PAPER-v0 |
| turn23academia1 | SRC-SNORKEL-PAPER-v0 |
| turn18academia0 | SRC-ACTIVE-LEARNING-SURVEY-v0 |
| turn24academia2 | SRC-COST-SENSITIVE-REJECTION-v0 |
| turn34academia0 | SRC-SEARCH4CODE-PAPER-v0 |
| turn34academia1 | SRC-PRODUCT-INSIGHTS-BING-v0 |

---

## Original research body (normalized citations)

`;

fs.writeFileSync(outPath, header + body, 'utf8');
console.log('written', outPath);
