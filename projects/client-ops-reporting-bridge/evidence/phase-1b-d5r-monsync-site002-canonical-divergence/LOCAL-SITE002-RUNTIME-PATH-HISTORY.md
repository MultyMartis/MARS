# LOCAL-SITE002-RUNTIME-PATH-HISTORY

## Monitor

| Commit | Subject | Blob note |
|--------|---------|-----------|
| `55214648` | ocpilot: monitor SITE-002 post-1C catalog growth | early monitor line |
| `647bbbbe` | ocpilot: harden SITE-002 post-1C monitor artifacts | local committed monitor still `f2273b18` at HEAD |
| (no local baseline-1737 port before MONSYNC) | — | origin `af5f3fca` not ancestor of local HEAD |

Local HEAD monitor blob before MONSYNC: `f2273b18e0fb1002250c728cc497415a6da22ed9` (regressive vs 1737).

## Runner + harness

| Commit | Subject | Paths |
|--------|---------|-------|
| `874feb43` | prepare SITE-002 post-1C monitor scheduler | runner lineage |
| `9c5d9510` | fix SITE-002 post-1C monitor runner quoting | runner |
| `647bbbbe` | harden SITE-002 post-1C monitor artifacts | runner lineage |
| `9a48e93b` | **fix(site-002): preserve monitor artifact classification in runner summary** | runner `a96b7aef` + harness `a125ce31` |

## Ancestry required by MONSYNC

`9a48e93b` **is** ancestor of local HEAD `a6802b1a` (verified).
