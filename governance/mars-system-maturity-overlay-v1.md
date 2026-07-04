# MARS System Maturity Overlay v1

## Status

| Field | Value |
|---|---|
| **Status** | CURRENT SUPPLEMENT |
| **Purpose** | maturity-aware overlay for current MARS systems |
| **Relationship to master-build-map** | supplements, does not replace |
| **Relationship to programme OPERATIONAL-INDEX** | summarizes, does not replace |
| **Relationship to Web-GPT sources** | source for future sync update after operator approval |
| **Created from** | MASTER-04 MARS System Maturity and Integrity Audit |

## Non-claims

- This overlay does not prove implementation.
- This overlay does not create automatic enforcement.
- This overlay does not authorize runtime work.
- This overlay does not authorize remote operations.
- This overlay does not replace parent chats.
- This overlay does not rewrite `master-build-map.md`.

## Maturity scale L0-L8

| Level | Label | Meaning |
|---:|---|---|
| L0 | IDEA | Named concept only; no repo-native charter or SoT |
| L1 | PRIMARY_DOC | Primary documentation exists; no structured contract |
| L2 | STRUCTURED_CONTRACT | Contracts / architecture docs; not operational proof |
| L3 | TEMPLATE_OR_GATE | Templates, gates, or minimal quality surfaces |
| L4 | PILOT_PROVEN | At least one documented pilot / case with evidence |
| L5 | REPEATABLE_OPERATION | Repeatable human-operated process with SoT |
| L6 | TOOL_ASSISTED | Tool-assisted, human-invoked systems with evidence |
| L7 | ENFORCED | Automatic enforcement proven (hooks/CI/policy engine) |
| L8 | PRODUCTION_SYSTEM | Production operation proven with acceptance evidence |

**Rule:** If evidence is insufficient, use lower maturity and SAFE_UNKNOWN.

## Current maturity matrix

| System | Current maturity | Evidence / SoT | What is proven | Why not higher | Owner |
|---|---:|---|---|---|---|
| MARS Core | L4 | `governance/`, `AGENTS.md`, post–Cycle 8 state | Documented governance, operational-first baseline, maturity discipline | Not L7 automatic enforcement; not full runtime product | MASTER CORE |
| Web-GPT Sources / sync packs | L4 | `web-gpt-sources/`, sync pack indexes | Imported / sync-pack documentation surface | Not live chat authority; update only after repo authority | MASTER CORE (sync after approval) |
| Agent Quality | L3 | `projects/mars-agent-quality/OPERATIONAL-INDEX.md` | Minimal task/report/failure quality surface (AQ-01) | Not automatic enforcement | MASTER CORE / AQ parent |
| Survivability / GitGuard | L6 | `projects/mars-survivability/OPERATIONAL-INDEX.md` | Human-invoked survivability / GitGuard tooling and discipline | No proven automatic enforcement (L7) | Survivability parent |
| Execution Guard / filesystem safety | L6 | `governance/mars-x-drive-root-authority-v1.md`, agent rules | X-drive authority, default-deny filesystem discipline | Not automated policy engine | MASTER CORE / Execution Guard |
| Website Factory | L5 | `projects/mars-website-factory/OPERATIONAL-INDEX.md` | Repeatable factory programme operations | Not full automation; README/index drift risk | Factory parent |
| FOUNDRY | L4 | Website Factory programme docs | Pilot / subsystem framing under Factory | Not independent production system | Factory parent |
| FP-0002 Shpigovsky | L4 | Forge WP reports / receipts (FP-0002 gates) | Documented pilot gates and admission evidence | Next gates require explicit authorization | Forge parent / operator |
| Forge WordPress / AG-WP-001 | L6 | `projects/mars-website-factory/subsystems/forge-wordpress/OPERATIONAL-INDEX.md` | Tool-assisted WP forge operations, human-invoked | Not L7 enforcement; not unattended production | Forge parent |
| WPilot | L5 | `projects/wpilot/OPERATIONAL-INDEX.md` | Repeatable WPilot programme operations | Not automatic enforcement | WPilot parent |
| OCPilot | L5 | `projects/ocpilot/OPERATIONAL-INDEX.md` | Repeatable OCPilot programme operations | Production receipts persistence not fully verified | OCPilot parent |
| Remote Operations Layer / ROL | L2 | `projects/remote-operations-layer/` (charter, starter, report gate, preflight) | Repo-native minimal charter / structured contract surface | Not runtime; not connector; not credential vault; not live production control plane; does not authorize live remote access by itself | ROL parent |
| MIG | L6 | `projects/mig/OPERATIONAL-INDEX.md` | Tool-assisted MIG operations, human-invoked | Not automatic enforcement | MIG parent |
| ORCA | L5 | `projects/orca/OPERATIONAL-INDEX.md` | Repeatable ORCA programme operations | Not production automation | ORCA parent |
| Search PPC Production | L6 | `projects/mars-search-ppc-production/README.md` | Tool-assisted Search PPC production lane | Wave 2.x acceptance not verified | Search PPC parent / operator |
| ATLAS | L4 | `projects/atlas/OPERATIONAL-INDEX.md` | Pilot / registration documentation surface | API/export not proven as runtime product | ATLAS parent |
| OPS | L4 | `projects/ops/OPERATIONAL-INDEX.md` | Pilot / programme documentation | OPS automation not proven | OPS parent |
| EAR Architecture | L3 | `shared/external-access-runtime/OPERATIONAL-INDEX.md` | Architecture / contract surface | Live connector not authorized as proven | EAR architecture owner |
| EAR Runtime | L6 | `projects/ear-runtime/OPERATIONAL-INDEX.md` | Tool-assisted EAR runtime, human-invoked | Live connector pilot needs explicit authorization | EAR runtime parent / operator |
| MARS Localhost Infrastructure / MLI | L6 | `projects/mars-localhost-infrastructure/OPERATIONAL-INDEX.md` | Tool-assisted localhost infrastructure lane | Root authority confusion risk; not full platform | MLI parent |
| MetaBOT | L3 | `projects/metabot-seo-content-agent/README.md` | Docs / agent framing | Live n8n state not verified | MetaBOT parent |
| NOVA | L2 | `projects/nova/README.md` | Structured docs / contract-level material | Not operational runtime | NOVA parent chat |
| HomeGateway | L2 | `projects/homegateway-v4-ai/OPERATIONAL-INDEX.md` | Structured docs / index | Not operational runtime | HomeGateway parent chat |
| Knowledge / Visual / Cold Brain | L2 | governance / programme references | Named knowledge layers in docs | Not proven runtime products | MASTER CORE / owners |
| mars-runtime | L6 narrow / L2 full | `mars-runtime/README.md` | Narrow tool-assisted surface may exist; full runtime is contract-level | Full multi-agent runtime not proven | MASTER CORE / runtime owner |
| tools/ | L6 | `tools/README.md` | Human-invoked operational helpers | Not tooling platform / enforcement product | MASTER CORE / tool owners |
| reports/ | L4 | `reports/` (where present) | Pilot / audit report surface | Untracked receipts may not be Git-persistent | MASTER CORE / programme owners |

## Working capabilities

| System | Proven capability | Evidence type | Repeatability |
|---|---|---|---|
| Survivability | Human-invoked GitGuard / survivability checks and discipline | OPERATIONAL-INDEX, tools, reports | Repeatable when operator invokes |
| Website Factory | Programme-level factory operations via SoT index | OPERATIONAL-INDEX, registries | Repeatable human-operated |
| Forge WordPress | Tool-assisted WP forge gates and inspections | OPERATIONAL-INDEX, receipts | Repeatable human-invoked |
| FP-0002 | Documented admission / gate evidence for Shpigovsky pilot | Gate reports, receipts | Pilot-repeatable under authorization |
| WPilot | Programme operations per WPilot SoT | OPERATIONAL-INDEX | Repeatable human-operated |
| OCPilot | Programme operations per OCPilot SoT | OPERATIONAL-INDEX | Repeatable human-operated (receipts persistence: SAFE_UNKNOWN) |
| MIG | Tool-assisted MIG lane | OPERATIONAL-INDEX, tools | Repeatable human-invoked |
| Search PPC Production | Tool-assisted Search PPC production lane | README / programme evidence | Repeatable human-invoked (Wave 2.x acceptance: SAFE_UNKNOWN) |
| EAR Runtime | Tool-assisted EAR runtime operations | OPERATIONAL-INDEX | Repeatable human-invoked (live connector: not proven) |
| MLI | Tool-assisted localhost infrastructure operations | OPERATIONAL-INDEX | Repeatable human-invoked within X: authority |
| tools/ | Lightweight human-invoked helpers | `tools/README.md`, scripts | Repeatable when invoked; not automatic |

## Idea / contract-only / not-working-as-runtime areas

| Area | Current state | Risk if inflated | Required proof |
|---|---|---|---|
| ROL | L2 STRUCTURED_CONTRACT / MINIMAL_CHARTER | Unauthorized remote work without task-level approval | Operator approval + target identity + environment class + credential boundary + backup/rollback + evidence/report closeout |
| Full MARS runtime | L2 full (narrow L6 only) | False “runtime exists” claims | Scoped runtime SoT + evidence of invoked surface only |
| NOVA | L2 docs | Implementation without charter | Parent charter + operational evidence |
| HomeGateway | L2 docs | Implementation without charter | Parent charter + operational evidence |
| ATLAS API/export | Not proven as product | API/export mythology | Working export path + receipts |
| OPS automation | Not proven | Automation claims | Tool path + repeatable receipts |
| EAR live connector | Not authorized as proven | Live remote connector claims | Explicit pilot authorization + evidence |
| MetaBOT live state | Docs only for live truth | Live n8n truth drift | Verified live state evidence |
| Website Factory automation | L5 human-operated, not full automation | Automation inflation | Explicit automation evidence |
| AQ enforcement | L3 quality surface only | “Enforced quality” claims | Automatic enforcement proof (L7) |

## Integrity risks

| Risk | Severity | Affected systems | Required rule |
|---|---|---|---|
| Automatic enforcement inflation | HIGH | AQ, Survivability, tools, all L6 systems | Do not claim L7 without hooks/CI/policy proof |
| Runtime claim drift | HIGH | mars-runtime, MARS Core, EAR, Factory | Cite SoT; separate docs vs invoked tools vs runtime product |
| ROL discipline bypass | HIGH | Any remote / external operation | No remote work without ROL discipline (charter, preflight, report gate); charter alone does not authorize live access |
| Old path drift | MEDIUM | All programmes, recovery evidence | Historical C:/D:/E: paths are not current roots |
| Evidence vs Git persistence | MEDIUM | reports/, Forge receipts, OCPilot | Treat untracked evidence as non-authoritative until committed or explicitly out-of-git |
| Factory README vs OP index drift | MEDIUM | Website Factory | Prefer OPERATIONAL-INDEX as programme SoT |
| OCPilot maturity inflation | MEDIUM | OCPilot | Cap at L5 until production receipts persistence verified |
| MetaBOT live truth drift | MEDIUM | MetaBOT | Do not treat README as live n8n state |
| MLI root authority confusion | HIGH | MLI, Localhost, Storage | Only `X:\MARS-Localhost` and approved X: roots |
| Master map ambiguity | MEDIUM | All systems | Use this overlay for maturity; keep master-build-map as build-order history |

## Development order 1–3 months

| Priority | Initiative | Owner | First step |
|---:|---|---|---|
| 1 | Maturity-aware overlay for existing systems | MASTER CORE | Publish and use this overlay (MASTER-05) |
| 2 | ROL discipline adoption in remote-touching programmes | Programme parents / ROL | Apply ROL starter/preflight/report gate when remote work is chartered; adoption links deferred |
| 3 | Evidence persistence discipline | MASTER CORE coordinates | Define what must be Git-committed vs Storage-only |
| 4 | Forge WP / FP-0002 next authorized gate | Forge parent / operator | Authorize next gate only; no V9-06D.2 without approval |
| 5 | Search PPC release evidence review | Search PPC parent / operator | Verify Wave 2.x acceptance evidence |
| 6 | MLI OpenCart profile | MLI parent | Profile work under MLI SoT and X: authority |
| 7 | EAR live pilot authorization | EAR runtime parent / operator | Explicit live pilot charter before connector work |
| 8 | NOVA / HomeGateway | Parent chats | Only after charter; no implementation by default |

## MASTER CORE ownership

| Area | MASTER CORE role | Parent / external owner |
|---|---|---|
| Core truth / maturity labels | Maintain overlay and anti-drift labels | MASTER CORE |
| Web-GPT source pack implications | Authorize repo-first updates; trigger sync after approval | MASTER CORE + sync operator |
| AQ / task-report quality | Keep AQ as quality surface, not enforcement product | AQ parent |
| Survivability / GitGuard | Coordinate discipline; do not claim L7 | Survivability parent |
| Website Factory | Summarize maturity; do not replace OP index | Factory parent |
| Forge WP / FP-0002 | Gate authorization awareness only | Forge parent / operator |
| WPilot / OCPilot | Maturity labels; no parent replacement | WPilot / OCPilot parents |
| ROL | Maintain maturity label; require ROL discipline for remote work; charter does not authorize live access | ROL parent |
| MIG / ORCA / Search PPC | Maturity labels; route work to parents | Programme parents / operators |
| ATLAS / OPS | Maturity labels; no API/automation inflation | ATLAS / OPS parents |
| EAR / MLI | Maturity labels; authority and live-pilot gates | EAR / MLI parents |
| MetaBOT | Docs vs live-state separation | MetaBOT parent |
| NOVA / HomeGateway | Block implementation without charter | Parent chats |

## Do-not-touch zones

- ROL runtime, connector, or credential-vault implementation
- Remote work without ROL discipline and operator approval
- Full MARS runtime
- Storage (`X:\AI MARS STORAGE\`) mutation without explicit task scope
- Localhost (`X:\MARS-Localhost\`) mutation without explicit task scope
- `master-build-map.md` direct rewrite
- Web-GPT sources before repo authority update
- NOVA / HomeGateway implementation
- EAR live connector
- FP-0002 V9-06D.2 without authorization
- Foreign WIP (dirty/untracked tree outside explicit task scope)

## Web-GPT source update implications

| Source / chat | Update only after | Trigger |
|---|---|---|
| `web-gpt-sources/mars-current-x-drive-2026-06/` | Repo authority / overlay accepted | Operator approval for sync pack refresh |
| `WEB-GPT-SOURCE-PACK-INDEX.md` | Repo authority update | Index regeneration after accepted repo truth |
| `WEB-GPT-CHAT-SYNC-PACK.md` | Repo authority update | Sync pack refresh authorization |
| MASTER CORE chat sync | This overlay + related governance accepted | Explicit MASTER CORE sync request |
| Factory / Forge / FP chats | Programme SoT and gate status accepted in repo | Parent-chat sync after repo update |
| ROL chat | Repo-native ROL charter accepted in repo | Sync after post-charter alignment if needed |
| External Web-GPT project chats | Relevant programme SoT accepted in repo | Per-project operator approval |

## SAFE UNKNOWN

- Programme-level ROL adoption links (WPilot / OCPilot / MetaBOT / EAR) not verified in this overlay wave.
- Live remote verification is not proven by ROL charter alone.
- Untracked reports/receipts may or may not be intended for Git.
- MetaBOT live n8n state not verified.
- Search PPC Wave 2.x acceptance not verified.
- OCPilot production receipts persistence not fully verified.
- External Web-GPT chat sync state not verified.
- Automatic hooks/CI enforcement outside repo not verified.

## Usage rule

- Before claiming a system is implemented, cite its SoT and evidence.
- Before raising maturity, require report/receipt/tool/proof.
- Before updating Web-GPT sources, update repo authority first.
- Before touching parent-owned systems, route to parent chat.
- Before remote work, require ROL discipline (charter, preflight, report gate) plus operator approval; charter alone does not authorize live access.
- Before destructive work, require Survivability/Execution Guard charter.
