# Anti-Patterns and Failures — FP-0002 V9-06 Batch 01

Each item: what happened → why → how fixed → future recommendation.

---

## 1. False-positive save tests (E51-FIX01)

| | |
|--|--|
| **What happened** | Meta/`acf_save_post` simulation reported PASS; operator real Update did not keep Услуга; frontend stayed stub. |
| **Why** | Validation never exercised the real admin form field names/nonces. |
| **How fixed** | E51-FIX02: stop rewriting prepared ACF `name`/`key`; validate via authenticated form replay. |
| **Future** | Require real admin save proof for any editor switch persistence claim. |

---

## 2. Too-strict HEAD gate in monorepo micro-commit

| | |
|--|--|
| **What happened** | Tasks expected exact HEAD equality; unrelated commits landed meanwhile. |
| **Why** | Monorepo has concurrent project commits on the same branch. |
| **How fixed** | Treat required HEAD as **ancestor** check, not equality. |
| **Future** | Document ancestor-base rules in Forge Proger Git playbooks (later). |

---

## 3. Treating monorepo folders as separate repos

| | |
|--|--|
| **What happened** | Mental model of “FP-0002 repo” vs “MetaBOT repo” collided with one Git root. |
| **Why** | Paths look independent; history is shared. |
| **How fixed** | Exact path staging; push decisions consider full ahead stack. |
| **Future** | Never `git add .`; always classify ahead commits by path scope. |

---

## 4. Too much ACF visual noise from default field borders

| | |
|--|--|
| **What happened** | Thematic blocks looked like endless grey lines; hard for Olga. |
| **Why** | ACF default `border-top` between sibling fields + weak section hierarchy. |
| **How fixed** | E53 `admin-fp02-acf.css`: mute internal borders; keep `.fp02-acf-section-title` separators. |
| **Future** | Budget admin CSS as part of page-type delivery, not afterthought. |

---

## 5. Demo fallback accidentally becoming normal source

| | |
|--|--|
| **What happened** | Empty ACF still showed template demo; editors thought template was SoT. |
| **Why** | Helpful FE fallbacks left on the normal path. |
| **How fixed** | Seed into ACF; empty → hide; keep emergency helpers technical-only; rewrite admin notices. |
| **Future** | Explicit SoT statement in model docs + FE contracts. |

---

## 6. Overcomplicated editor role/layout models

| | |
|--|--|
| **What happened** | Five technical layout values confused editors; nesting mismatches. |
| **Why** | Developer template vocabulary exposed too early. |
| **How fixed** | E45 Option B: few editor roles + sync; rename `alcohol_special`. |
| **Future** | Start with editor vocabulary; map to tech values underneath. |

---

## 7. Mass changes before representative validation

| | |
|--|--|
| **What happened** | Risk of alcohol copy-paste across 26 services; other contamination. |
| **Why** | Pressure to “finish content” in one wave. |
| **How fixed** | E48 representative set, then E49 full with paste bans. |
| **Future** | Gate mass seed on representative PASS evidence. |

---

## 8. Push attempts before divergence review

| | |
|--|--|
| **What happened** | Remote tip not ancestor of HEAD (OCPilot side commits); push blocked. |
| **Why** | Concurrent remotes advanced while local stayed on dirty/mainline mixes. |
| **How fixed** | Clean worktree merge resolve; no force push; no dirty main pull. |
| **Future** | Always `git ls-remote` + ancestry gate before push. |

---

## 9. Evidence tail / postcommit loop risk

| | |
|--|--|
| **What happened** | Postcommit evidence itself becomes uncommitted work needing another commit. |
| **Why** | Closeout artifacts written after the “main” persistence commit. |
| **How fixed** | Micro-commit for evidence; accept limited tails; don’t invent endless tails. |
| **Future** | Prefer including freeze/evidence in the same allowlist wave when possible. |

---

## 10. Source/runtime CSS drift risk

| | |
|--|--|
| **What happened** | Operator runtime `v9-style.css` hash ≠ Git source; overwrite would destroy accepted polish. |
| **Why** | Live visual fixes applied in runtime without source back-port. |
| **How fixed** | Explicit preserve-drift rule; sync reports mark INTENTIONAL_DRIFT PASS. |
| **Future** | Detect drift; never “sync from source” blindly; decide per charter. |

---

## 11. Working in dirty main risk

| | |
|--|--|
| **What happened** | Thousands of foreign WIP files sit beside target changes. |
| **Why** | Multi-project workspace. |
| **How fixed** | Scope status to allowlisted paths; never reset/clean/stash whole tree. |
| **Future** | Clean worktree for risky Git ops; foreign WIP inventory before any destructive impulse. |
