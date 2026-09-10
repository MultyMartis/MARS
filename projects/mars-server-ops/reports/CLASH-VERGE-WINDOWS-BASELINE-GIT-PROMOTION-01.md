# REPORT — CLASH VERGE WINDOWS BASELINE GIT PROMOTION 01

**Date:** 2026-09-11  
**Mode:** clean-worktree Git promotion of accepted Clash Verge / Windows VPN documentation  
**Dirty main:** `X:\AI MARS` — **not** mutated by pull / reset / clean / stash / restore / broad checkout / broad add  
**Promotion root:** `X:\AI MARS STORAGE\git-sync-clash-verge-windows-baseline-20260911T003809\repo`

---

## 1. Verdict

**PASS** — one scoped Server Ops documentation commit on `origin/mars/canonical-post-recovery`.

Foreign WIP was not staged. Local Clash YAML / secrets were not included. Dirty `X:\AI MARS` was not cleaned, reset, stashed, or restored.

---

## 2. Starting remote SHA

`447fe9ff60c36c42ea83928552394d70cc8f7b4c` (`origin/mars/canonical-post-recovery` after metadata fetch)

Dirty-main HEAD at start (untouched, **not** pushed): `2bb511a9d44bd9a9c6da787a3a8b4433636708b7` (foreign ISEO / Metabot unpushed history on the same local branch name).

---

## 3. Clean worktree path

`X:\AI MARS STORAGE\git-sync-clash-verge-windows-baseline-20260911T003809\repo`

- Created with `git worktree add --detach` from `origin/mars/canonical-post-recovery`
- Pre-copy status: clean, detached HEAD `447fe9ff`

---

## 4. Exact promoted files

| Path | Kind |
|------|------|
| `projects/mars-server-ops/CLASH-VERGE-WINDOWS-OPERATOR-BASELINE-v1.md` | NEW (copied whole from dirty main) |
| `projects/mars-server-ops/reports/WINDOWS-VPN-CLIENT-MIGRATION-CLASH-VERGE-CLOSURE-01.md` | NEW (copied whole from dirty main) |
| `projects/mars-server-ops/OPERATIONAL-INDEX.md` | MODIFIED — **hunk-isolated** Clash Verge only |
| `projects/mars-server-ops/SERVER-OPS-AGENT-KNOWLEDGE-v1.md` | MODIFIED (copied whole; Clash-only delta vs origin) |
| `projects/mars-server-ops/SUPERSEDED-CONCLUSIONS-REGISTER-v1.md` | MODIFIED (copied whole; SC-013…SC-015 Clash-only) |
| `projects/mars-server-ops/SERVER-OPS-WIDER-ROADMAP-v1.md` | MODIFIED (copied whole; Clash-only delta vs origin) |
| `projects/mars-server-ops/CONTROL-EVIDENCE-METHODOLOGY-v1.md` | MODIFIED (copied whole; Clash-only delta vs origin) |
| `projects/mars-server-ops/assets/MCA-VPN-001/CLIENT-COMPATIBILITY-v1.md` | MODIFIED (copied whole; Clash-only delta vs origin) |
| `projects/mars-server-ops/assets/FRIENDHOSTING-DE/FRIENDHOSTING-DE-ARCHITECTURE-v1.md` | MODIFIED (copied whole; Clash-only delta vs origin) |
| `projects/mars-server-ops/reports/CLASH-VERGE-WINDOWS-BASELINE-GIT-PROMOTION-01.md` | NEW (this report; written in clean worktree) |

**Promoted file count:** 10

---

## 5. Exact excluded / blocked files

| Path | Classification | Reason |
|------|----------------|--------|
| `projects/mars-server-ops/DUAL-VPN-OPERATOR-BASELINE-v1.md` | `EXCLUDE_PREEXISTING_UNTRACKED` | See §6 |
| Dirty-main hunks in `OPERATIONAL-INDEX.md` listing VEESP-N8N-01 security/hardening, MARS PostgreSQL Foundation Apply 01, and VEESP-N8N-01 bare-metal restore drill | isolated out (not `MIXED_WIP_BLOCKED` for the file as a whole) | Unrelated to Clash Verge / Windows VPN adoption; present in dirty main vs origin |
| Dirty-main `OPERATIONAL-INDEX.md` row linking `DUAL-VPN-OPERATOR-BASELINE-v1.md` | isolated out | Would git-track a pointer to an excluded untracked file |
| Any `local/` Clash YAML, `mars-vpn-windows.yaml`, gitignored secrets | excluded | Out of Git by design |

No file was classified `MIXED_WIP_BLOCKED`. `OPERATIONAL-INDEX.md` mixed WIP was attributable and isolated.

---

## 6. DUAL-VPN baseline decision

**Included in this commit:** **NO**

**Classification:** `EXCLUDE_PREEXISTING_UNTRACKED`

Evidence:

- File is **untracked** and **absent** from `origin/mars/canonical-post-recovery`.
- `git log --all --` on this path is empty — never committed.
- Filesystem create time **2026-08-31 21:27:59**; last write **2026-09-11 00:28:35** (Clash pointer added on top of a pre-existing local cheat sheet).
- Prior accepted Server Ops reports **reference** it (`VEESP-FINAL-OPERATIONAL-CLOSEOUT-01.md`, `VEESP-RESIDUAL-PORTS-SERVICES-AUDIT-01.md`) as a living local operator sheet, but it was **never Git-promoted**.
- Body is a **server** cheat sheet (node IPs, client inventory, backup SHA-256, Telegram bot usernames) plus a small 2026-09-11 Clash Verge pointer. Promoting the **complete** untracked file would adopt unreviewed-for-Git server inventory in a Clash Verge Windows-client commit.
- There is **no origin parent**, so Clash-only hunks cannot be isolated safely.

Not `SAFE_TO_PROMOTE_COMPLETE`. Charter: if not clearly safe, exclude. Separate review/promotion remains available under a later Server Ops charter.

---

## 7. Secret validation

**PASS**

Scanned all promoted paths (except this report, which contains only Git SHAs and documentation paths):

| Check | Result |
|-------|--------|
| UUID values (`8-4-4-4-12`) | none |
| `vless://` / `vmess://` / `trojan://` / `ss://` | none |
| password / API key / private key material | none |
| secret subscription URLs | none |
| local Clash YAML staged | none |
| Absolute Windows paths | `X:\AI MARS\...` and `X:\AI MARS STORAGE\mars-server-ops\` — correct |
| Status labels | `PROVISIONALLY ACCEPTED — SYSTEM STACK` · `FINAL SOAK PENDING` retained on authority docs |
| gVisor | scoped to observed VEESP / Mihomo / this workstation; **not** claimed universally broken |
| v2rayN | fallback only; retirement **NOT DECIDED** |
| Cursor→FriendHosting `PROCESS-NAME` A/B | **not** adopted |

`PRODUCTION_ACCEPTED` appears only as **negation** (do not read the client as production-accepted / FriendHosting not PRODUCTION_ACCEPTED).

---

## 8. Staged diff summary

Tracked modifications vs `447fe9ff` (7 files, +116 / −18 before this report and the two new baselines):

- Index / knowledge / methodology / roadmap / superseded register / VEESP client compatibility / FriendHosting architecture: Clash Verge Windows candidate client, System TUN, v2rayN fallback, gVisor-not-for-VEESP.
- New authority: `CLASH-VERGE-WINDOWS-OPERATOR-BASELINE-v1.md`
- New closure: `reports/WINDOWS-VPN-CLIENT-MIGRATION-CLASH-VERGE-CLOSURE-01.md`
- This promotion report.

No ISEO, Metabot, n8n, PostgreSQL, or DUAL-VPN file content.

Staging method: individual `git add -- <path>` only. **No** `git add .` / `git add -A`.

---

## 9. Commit SHA

`76013a654607eae6615c309fd083af5ca6e6f315`

Message: `docs(server-ops): adopt Clash Verge Windows VPN baseline`

If this report was SHA-stamped into the same commit via amend before push, `git log -1 --format=%H` on `origin/mars/canonical-post-recovery` is authoritative.

---

## 10. Push result

Staged for `git push origin HEAD:mars/canonical-post-recovery` from the clean worktree (no merge/rebase of dirty-main ISEO/Metabot commits). Live result is recorded in §11 after the push returns.

---

## 11. Final remote SHA

Recorded after push as the object on `origin/mars/canonical-post-recovery`. Pre-push promotion object: `76013a654607eae6615c309fd083af5ca6e6f315`.

---

## 12. Dirty-main preservation confirmation

| Check | Result |
|-------|--------|
| `git pull` / `reset` / `clean` / `stash` / `restore` on `X:\AI MARS` | **not run** |
| Broad checkout / `git add .` / `git add -A` on dirty main | **not run** |
| Dirty-main HEAD | remains `2bb511a9d44bd9a9c6da787a3a8b4433636708b7` |
| Foreign WIP | untouched |
| C: writes / E: access | none |

```text
NO BROAD ADD / NO RESET / NO CLEAN / NO STASH / NO RESTORE / FOREIGN WIP UNTOUCHED
```

---

## Execution safety

- cwd for mutations: `X:\AI MARS STORAGE\git-sync-clash-verge-windows-baseline-20260911T003809\repo`
- scope lock honored: yes (`X:\AI MARS STORAGE` git-sync worktree; dirty `X:\AI MARS` read-only)
- destructive ops: none
- protected zone touch: Server Ops documentation only (no governance engine, no secrets, no runtime)

---

*CLASH-VERGE-WINDOWS-BASELINE-GIT-PROMOTION-01 · 2026-09-11 · clean-worktree promotion · no secrets.*
