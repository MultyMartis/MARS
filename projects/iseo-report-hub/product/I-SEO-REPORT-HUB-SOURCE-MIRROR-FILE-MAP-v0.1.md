# I-SEO Report Hub — Source Mirror File Map v0.1

**Status:** PLANNING MAP ONLY — NO FILES COPIED  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Authority:** Operator Model A source mirror + deploy/sync charter 01  
**Related:** [I-SEO-REPORT-HUB-MODEL-A-SOURCE-MIRROR-CHARTER-v0.1.md](I-SEO-REPORT-HUB-MODEL-A-SOURCE-MIRROR-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-DEPLOY-SYNC-POLICY-v0.1.md](I-SEO-REPORT-HUB-DEPLOY-SYNC-POLICY-v0.1.md)

---

## 1. Status

Planning map only. **No** files copied. **No** `app-source/` created in this wave.

Runtime inspection (read-only, 2026-07-24) confirmed Phase 0 paths listed below **exist** under:

`X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`

Planned mirror root (not created):

`X:\AI MARS\projects\iseo-report-hub\app-source\`

---

## 2. Include Map

| Runtime source path | Planned app-source path | Include reason |
|---------------------|-------------------------|----------------|
| `README.md` | `app-source/README.md` | Runtime identity + Phase 0 status docs |
| `.env.example` | `app-source/.env.example` | Placeholder env contract; no secrets |
| `.gitignore` | `app-source/.gitignore` | Keeps secrets/generated paths out of future commits |
| `public/index.php` | `app-source/public/index.php` | Phase 0 index page |
| `public/health.php` | `app-source/public/health.php` | Health/extension sanity page |
| `public/assets/css/app.css` | `app-source/public/assets/css/app.css` | Minimal static asset |
| `public/assets/js/app.js` | `app-source/public/assets/js/app.js` | Minimal static asset |
| `app/README.md` | `app-source/app/README.md` | App layer placeholder docs |
| `app/Controllers/.keep` | `app-source/app/Controllers/.keep` | Directory placeholder |
| `app/Models/.keep` | `app-source/app/Models/.keep` | Directory placeholder |
| `app/Views/.keep` | `app-source/app/Views/.keep` | Directory placeholder |
| `app/Services/.keep` | `app-source/app/Services/.keep` | Directory placeholder |
| `app/Support/.keep` | `app-source/app/Support/.keep` | Directory placeholder |
| `config/README.md` | `app-source/config/README.md` | Config layer docs |
| `config/app.example.php` | `app-source/config/app.example.php` | App config example (placeholders) |
| `config/database.example.php` | `app-source/config/database.example.php` | DB config example (placeholders) |
| `storage/README.md` | `app-source/storage/README.md` | Storage policy docs |
| `storage/.gitignore` | `app-source/storage/.gitignore` | Ignore generated storage contents |
| `storage/logs/.keep` | `app-source/storage/logs/.keep` | Empty logs dir marker |
| `storage/uploads/.keep` | `app-source/storage/uploads/.keep` | Empty uploads dir marker |
| `storage/cache/.keep` | `app-source/storage/cache/.keep` | Empty cache dir marker |
| `database/README.md` | `app-source/database/README.md` | Database docs placeholder |
| `database/schema-draft-not-migration.md` | `app-source/database/schema-draft-not-migration.md` | Non-executable schema draft |
| `database/seeds/README.md` | `app-source/database/seeds/README.md` | Seeds placeholder docs |
| `docs/README.md` | `app-source/docs/README.md` | Runtime-local docs entry |
| `docs/SOURCE-RUNTIME-POLICY.md` | `app-source/docs/SOURCE-RUNTIME-POLICY.md` | Runtime copy of source/runtime policy reminder (**present** on runtime) |

Relative paths above are under the runtime root and planned `app-source/` root respectively.

---

## 3. Exclude Map

| Path / pattern | Reason |
|----------------|--------|
| `.env` | Live secrets / local credentials — never version |
| `.env.local` | Local override secrets — never version |
| `storage/logs/*` except `.keep` | Generated logs — runtime-only |
| `storage/uploads/*` except `.keep` | Uploaded evidence/files — runtime-only / may be private |
| `storage/cache/*` except `.keep` | Generated cache — runtime-only |
| `vendor/` | Dependency tree not approved for Phase 0; Composer not installed |
| `node_modules/` | Frontend package tree not approved; npm not used in Phase 0 |
| SQL dumps (`*.sql` dumps with data, exports) | May contain private client/business data |
| Private reports / unsanitized metrics exports | Security and corpus policy |
| Production credentials (any file) | Secrets policy |
| OS/editor temp files (`.DS_Store`, `Thumbs.db`, `*.log`, editor swap) | Noise; not product source |
| Nested `.git/` under runtime | Forbidden; runtime is not a separate repo |
| Laragon / hosts / vhost configs outside project tree | Infrastructure — not app source |

---

## 4. Validation Required Before Mirror

Before creating `app-source/` and copying:

1. **No secrets** — confirm absence of `.env`, `.env.local`, real passwords, tokens, production URLs with credentials.
2. **No nested `.git`** — confirm runtime is not a separate Git repository.
3. **No generated files** — logs/uploads/cache contain only `.keep` (or are empty aside from markers).
4. **No runtime-only local files** outside the include map unless a supplemental charter adds them.
5. **Path allowlist** — copy only paths in §2 (or an explicitly updated map version).
6. **Drive / volume / branch preflight** — Active Brain writes only under approved MARS roots on `X:` / `AI WS`.

---

## 5. SAFE UNKNOWN

- Whether additional Phase 0 files appear on runtime between this map and the mirror creation wave.
- Whether `docs/SOURCE-RUNTIME-POLICY.md` content should later be replaced by a thin pointer to Active Brain policy (content identity not re-audited line-by-line in this wave beyond presence).
- Whether future phases add folders (`migrations/`, `tests/`, etc.) — would require map revision before mirror expansion.
