# P0-I Operator Review Source Parity v1

**Pilot run:** `p0-i-real-slice-v1`  
**Runtime checkpoint:** `1fcf3d2`  
**Status:** PASS

## Reconciliation

| Source | Count | Expected | Match |
|--------|------:|---------:|:-----:|
| Frozen input | 200 | 200 | ✓ |
| Selection manifest | 200 | 200 | ✓ |
| Semantic records | 200 | 200 | ✓ |
| Unique query IDs | 200 | 200 | ✓ |
| ACCEPT | 77 | 77 | ✓ |
| REJECT | 53 | 53 | ✓ |
| ABSTAIN | 70 | 70 | ✓ |
| Legacy commercial → REJECT | 39 | 39 | ✓ |
| Legacy commercial → ABSTAIN | 69 | 69 | ✓ |
| Legacy/new same | 92 | 92 | ✓ |
| Operator decisions populated | 0 | 0 | ✓ |

## Boundary checks

- P0-D: **ON HOLD**
- Corvonero: **FROZEN**
- Pilot package: **uncommitted**
- Runtime checkpoint `1fcf3d2`: **present in history**


