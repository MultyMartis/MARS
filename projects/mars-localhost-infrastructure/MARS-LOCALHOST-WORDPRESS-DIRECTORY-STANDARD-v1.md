# MARS Localhost — WordPress Directory Standard v1

**Document type:** WordPress directory layout standard  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** MLI-03  
**Runtime root:** `X:\MARS-Localhost\sites\wordpress\`

---

## Purpose

Define the **WordPress-specific** directory layout on `X:\MARS-Localhost`, extending the universal [MARS-LOCALHOST-DIRECTORY-STANDARD-v1.md](MARS-LOCALHOST-DIRECTORY-STANDARD-v1.md) without coupling other platforms to WordPress conventions.

---

## Canonical path pattern

```text
X:\MARS-Localhost\sites\wordpress\{class}\{slug}\
```

| Segment | Values | Example |
|---------|--------|---------|
| **platform** | `wordpress` (fixed) | — |
| **class** | `synthetic` \| `projects` \| `sandboxes` | `synthetic` |
| **slug** | lowercase kebab-case id | `fws-0001` |

**Reference runtime (MLI-WP-SYN-001):**

```text
X:\MARS-Localhost\sites\wordpress\synthetic\fws-0001\
```

---

## Document root model

MLI uses **direct document root** at the site folder (Model B per [MARS-LOCALHOST-DOCUMENT-ROOT-DECISION-v1.md](MARS-LOCALHOST-DOCUMENT-ROOT-DECISION-v1.md)):

| Item | Path |
|------|------|
| **Physical document root** | `sites\wordpress\{class}\{slug}\` |
| **Laragon junction** | `laragon\www\{slug}` → physical root |
| **Apache DocumentRoot** | Physical root (via vhost registry) |

**Forbidden:** nested `public\` subfolder unless manifest explicitly documents subdirectory install (not default for MLI-03).

---

## Standard WordPress tree

After WP-CLI core install:

```text
{slug}\
├── index.php
├── license.txt
├── readme.html
├── wp-activate.php
├── wp-admin\
├── wp-blog-header.php
├── wp-comments-post.php
├── wp-config.php
├── wp-config-sample.php          # may remain; do not use for secrets
├── wp-content\
│   ├── index.php
│   ├── plugins\
│   ├── themes\
│   ├── uploads\                  # year/month structure after media upload
│   ├── mu-plugins\               # optional — consumer
│   └── debug.log                 # when WP_DEBUG_LOG enabled
├── wp-cron.php
├── wp-includes\
├── wp-links-opml.php
├── wp-load.php
├── wp-login.php
├── wp-mail.php
├── wp-settings.php
├── wp-signup.php
├── wp-trackback.php
├── xmlrpc.php
└── .htaccess                     # permalinks — requires mod_rewrite
```

---

## wp-content conventions

| Subfolder | Purpose | Git / brain |
|-----------|---------|-------------|
| `plugins\` | Installed plugins | Consumer source in brain; runtime copy on D: |
| `themes\` | Installed themes | Consumer source in brain; runtime copy on D: |
| `uploads\` | Media library | **Never** in Git |
| `mu-plugins\` | Must-use plugins | Optional; document in manifest if used |
| `languages\` | Translation files | Regenerated on locale install |
| `upgrade\` | Temporary upgrade scratch | Ephemeral |
| `cache\` | Plugin cache dirs | Ephemeral; exclude from backup |

**MLI-03 reference:** Forge theme/plugin **not** installed — only default bundled theme expected.

---

## Secrets and local config (outside site tree)

| Item | Location | Notes |
|------|----------|-------|
| **Runtime secrets** | `X:\AI MARS\local\mli\{slug}\runtime.env` | DB password, auth keys — **not** in site folder |
| **Optional site `.env`** | Discouraged; prefer brain-side `runtime.env` | If used, must be gitignored on D: |
| **wp-config.php** | Site root on D: | Loads secrets via guarded include only |

**Rule WP-DIR-01:** No plaintext DB passwords in `wp-config.php` body in Git-tracked templates.  
**Rule WP-DIR-02:** `wp-config.php` on D: is a runtime artefact — not copied to brain.

---

## Laragon integration paths

| Item | Path |
|------|------|
| Junction | `X:\MARS-Localhost\laragon\www\{slug}` |
| Apache vhost | `X:\MARS-Localhost\laragon\etc\apache2\sites-enabled\{slug}.test.conf` |
| Apache SSL vhost | `X:\MARS-Localhost\laragon\etc\apache2\sites-enabled\{slug}.test-ssl.conf` |
| TLS cert/key | `X:\MARS-Localhost\laragon\etc\ssl\{slug}.test.crt` / `.key` |

Domain must match [MARS-LOCALHOST-DOMAIN-STANDARD-v1.md](MARS-LOCALHOST-DOMAIN-STANDARD-v1.md): `{slug}.test`.

---

## Supporting directories (platform-level)

WordPress runtimes share MLI platform-agnostic paths:

```text
X:\MARS-Localhost\
├── databases\
│   ├── dumps\                    # mars_wp_{id}_*.sql
│   └── baselines\
├── backups\
│   └── wordpress\                # {slug}_{date}_{reason}.zip
├── storage\
│   ├── packages\                 # import ZIPs staging
│   └── fixtures\                 # synthetic XML/JSON if used
├── logs\
│   └── applications\             # optional aggregated WP logs
└── tools\
    └── wp-cli\                   # shared WP-CLI — not per site
```

---

## Class-specific layout notes

### synthetic

| Attribute | Rule |
|-----------|------|
| **Example** | `synthetic\fws-0001` |
| **Data** | Generated users/posts only |
| **Retention** | Resettable after archived evidence |
| **Manifest** | Required before sustained use |

### projects

| Attribute | Rule |
|-----------|------|
| **Example** | `projects\shpigovsky` (future FP-0002) |
| **Data** | Client exports only with charter |
| **Backup** | Required before destructive change |
| **Manifest** | Link to FP-ID / project passport |

### sandboxes

| Attribute | Rule |
|-----------|------|
| **Example** | `sandboxes\acf-test` |
| **Lifetime** | Short; delete on experiment end |
| **Manifest** | Recommended |

---

## Slug and ID mapping

| Consumer ID | Folder slug | Runtime ID pattern |
|-------------|-------------|-------------------|
| FWS-0001 | `fws-0001` | `MLI-WP-SYN-001` |
| FP-0002 (future) | `shpigovsky` or `fp-0002` | `MLI-WP-PRJ-{nnn}` |
| Ad-hoc sandbox | `{descriptive-slug}` | `MLI-WP-SBX-{nnn}` |

Slug in folder path **must** match canonical domain slug (`fws-0001.test` → folder `fws-0001`).

---

## Forbidden placements

| Forbidden | Correct location |
|-----------|------------------|
| WordPress core in `X:\AI MARS` | `X:\MARS-Localhost\sites\wordpress\...` |
| Uploads in Git | D: site `wp-content\uploads\` |
| MySQL data files in site folder | Laragon MySQL datadir |
| Duplicate core trees under `laragon\www\` without junction | Physical root in `sites\` only |
| Production domain as folder name | Use MLI slug only |

---

## Creation checklist

- [ ] Choose class: `synthetic` | `projects` | `sandboxes`
- [ ] Create `sites\wordpress\{class}\{slug}\`
- [ ] Register [WordPress runtime registry](registries/MARS-LOCALHOST-WORDPRESS-RUNTIME-REGISTRY-v1.md) row
- [ ] Register [vhost registry](registries/MARS-LOCALHOST-VHOST-REGISTRY-v1.md) row
- [ ] Create brain [manifest](manifests/) before DB population
- [ ] Configure junction + Apache vhost
- [ ] Add hosts entry via `tools\hosts\add-mli-host`
- [ ] Create `X:\AI MARS\local\mli\{slug}\runtime.env` (outside Git)
- [ ] WP-CLI core install into physical root

---

## Related

- [MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md](MARS-LOCALHOST-WORDPRESS-RUNTIME-PROFILE-v1.md)
- [MARS-LOCALHOST-LARAGON-VHOST-MODEL-v1.md](MARS-LOCALHOST-LARAGON-VHOST-MODEL-v1.md)
- [MARS-LOCALHOST-SITE-CLASSIFICATION-STANDARD-v1.md](MARS-LOCALHOST-SITE-CLASSIFICATION-STANDARD-v1.md)

---

*WordPress directory standard v1 — MLI-03.*
