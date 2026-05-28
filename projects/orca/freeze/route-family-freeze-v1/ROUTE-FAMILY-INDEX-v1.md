# Route Family Index v1

**Freeze:** ORCA Route Family Freeze v1 · 2026-05-28  
**Project:** `triumph-manipulator-krasnodar`  
**Registry:** `projects/orca/projects/triumph-manipulator-krasnodar/landing-route-registry.json`

**Legend — Website Factory rollout:** `built` · `scaffold` · `pack-only`  
**Legend — mobile QA:** `partial` · `pending` · `unknown`  
**Legend — calibration:** `stabilized` · `pack-frozen` · `open-items`

---

## Index table

| Route | Semantic class | Tone | Trust mode | CTA style | Logistics behavior | Differentiation focus | Factory rollout | Mobile QA | Calibration |
|-------|----------------|------|------------|-----------|-------------------|----------------------|-----------------|-----------|-------------|
| **zakaz** `/` | master | Hot operational; capability-first filter | `operational_proof` (+ social in trust section) | Form-primary (`cta_priority: form`); call tension documented | General dispatch; multi-scenario cargo cards | Master hot ≠ generic fleet; one-machine; qualification in hero | **built** (V6 `index.html`) | **partial** (device QA open) | **open-items** (D2 H1 multi-ad; handoff MD missing) |
| **5-tonn** | capability | Capability-first; reduced aggression vs zakaz | `hybrid_proof` / operational | Form + call balanced | Standard KMU 5/3/14; capability specs in hero | Machine capability route; no fake hero price; denied fleet | **scaffold** (V6 partials) | **pending** | **stabilized** (`5-tonn-stabilized-v1`) |
| **bytovki** | use-case · logistics | Calm coordination; logistics scenario | `operational_proof` | Call + form (`call_plus_form`) | Load → route → placement/install | Separate logistics scenario ≠ «ещё один манипулятор» | **scaffold** | **pending** | **pack-frozen** (stabilized v1 baseline per batch notes) |
| **stroymaterialy** | use-case | Delivery-to-site; structured commercial | Operational (pack copy) | Form-primary «Рассчитать доставку» + call secondary | Site delivery; unload-by-crane framing | Stroymaterialy on object; not master hot | **scaffold** | **pending** | **pack-frozen** |
| **yurlic** | b2b | B2B coordination; object/supply framing | Documents + operational (B2B proof) | Form «Получить расчёт»; object/scheduling CTAs | Org supply to site; payment/docs in pack | Юрлица payment story; not consumer-only | **scaffold** | **pending** | **pack-frozen** |
| **vezdehod** | capability (6×6) | Terrain / access-first | Operational + access proof | Standard calc form + call | 6×6 lock; difficult access qualification | Different machine story (6×6) — anti copy-paste 5т | **scaffold** | **pending** | **pack-frozen** |
| **oborudovanie** | use-case | Careful handling; low drama | Careful handling (batch: safe load/unload) | Consultation + calc | Equipment load/unload discipline | Fragility / handling constraints | **scaffold** | **pending** | **pack-frozen** (+ logistics batch lock) |
| **konteynery** | use-case | Industrial coordination | Coordination + industrial capability (batch) | Calc + call; container-specific forms | Container load/place feasibility | Industrial use-case; anti generic cargo | **scaffold** | **pending** | **pack-frozen** (+ logistics batch lock) |
| **armatura** | use-case | Construction supply; long-load aware | Mass + site delivery | Calc to site | Armatura to construction object | Long-load / typography risk flagged for Factory | **scaffold** | **pending** | **pack-frozen** |
| **kirpich-bloki** | use-case | Masonry materials delivery | Site delivery operational | Calc + call | Brick/blocks to site | Distinct from stroymaterialy hero overlap — pack H1 locked | **scaffold** | **pending** | **pack-frozen** |
| **fbs-zhbi** | use-case · heavy logistics | Construction heavy units | Construction logistics (batch) | Capacity confirmation + calc | FBS/ZHB mass-zone-site gate | Heavy structural FAQ UNKNOWNs; slug `/perevozka-fbs-zhbi/` | **scaffold** | **pending** | **pack-frozen** (+ logistics batch lock) |
| **kray** | geo | Intercity / regional route framing | Geo + operational route proof | «Рассчитать выезд»; route fields | Intercity addresses; route comment | Geo framing without overclaim — operator area lock | **scaffold** | **pending** | **pack-frozen** |

---

## Pack profile map

| Route | Pack path | Profile | `allowed_for_factory` (pack STATUS) | `approved_for_factory` (human gate) |
|-------|-----------|---------|-------------------------------------|-------------------------------------|
| zakaz | `triumph-manipulyator-zakaz-pack-v1/` | A (full) | — | **false** |
| 5-tonn | `triumph-manipulyator-5-tonn-pack-v1/` | A (full) | — | pending sign-off |
| bytovki | `triumph-bytovki-pack-v1/` | A (full) | — | pending sign-off |
| stroymaterialy | `triumph-stroymaterialy-pack-v1/` | B (flat) | yes | pending |
| yurlic | `triumph-yurlic-pack-v1/` | B | yes | pending |
| vezdehod | `triumph-vezdehod-pack-v1/` | B | yes | pending |
| oborudovanie | `triumph-oborudovanie-pack-v1/` | B | yes | pending |
| konteynery | `triumph-konteynery-pack-v1/` | B | yes | pending |
| armatura | `triumph-armatura-pack-v1/` | B | yes | pending |
| kirpich-bloki | `triumph-kirpich-bloki-pack-v1/` | B | yes | pending |
| fbs-zhbi | `triumph-fbs-zhbi-pack-v1/` | B | yes | pending |
| kray | `triumph-kray-pack-v1/` | B | yes | pending |

---

## PPC group mapping (frozen)

| Group | Route slug | Blueprint |
|-------|------------|-----------|
| 01 | 5-tonn | `05-capability-5-ton.md` |
| 02 | bytovki | `02-use-case-bytovka.md` |
| 03 | stroymaterialy | `03-use-case-stroymaterialy.md` |
| 04 | yurlic | `06-b2b-yurlica.md` |
| 05 | vezdehod | `07-capability-6x6-vezdekhod.md` |
| 06 | oborudovanie | `04-use-case-oborudovanie.md` |
| 07 | konteynery | `10-use-case-konteynery.md` |
| 08 | armatura | `11-use-case-armatura.md` |
| 09 | kirpich-bloki | `12-use-case-kirpich-bloki.md` |
| 10 | fbs-zhbi | `09-use-case-fbs-zhb.md` |
| 11 | kray | `08-intercity-krai.md` |
| 12 | zakaz | `01-master-hot-general.md` |

**Instance reference:** `projects/orca/ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json`

---

## Update protocol

После Factory pilot на маршруте — обновить строку в этой таблице и в [remaining-routes-status-matrix-v1.md](../../coordination/remaining-routes-status-matrix-v1.md). Freeze v1 **не** автоматически пересматривается.
