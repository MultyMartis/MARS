# FP-0002 Service Subdivision — GROUP 3 Comparison Before v1

| Region | Runtime before | Design | Text | Structure | Count | Order | Action |
|--------|----------------|--------|------|-----------|------:|-------|--------|
| Rehabilitation heading/lead | Present, matching copy | Same | MATCH | MATCH | 1 | OK | KEEP |
| Numbered stages | 4 steps, matching titles/bodies | 4 steps | MATCH | MATCH | 4 | OK | KEEP |
| Guest-visit CTA | **Absent** | Dark band after stage 04 | MISSING | MISSING | 0 vs 1 | Wrong | **ADD** |
| Support block | Present, 4 items | Same | MATCH | MATCH | 4 | OK | KEEP |
| Section order | stages → support | stages → CTA → support | — | WRONG | — | Wrong | **REORDER via insert** |
| Transition | stages → team-stats | support → corridor | — | N/A | — | — | NO CHANGE (team out of scope) |

Primary delta: missing embedded guest-visit CTA between stages and support.
