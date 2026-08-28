# CARD-RENDERER-INVENTORY-v1

| Entry point | Node/path | Status source | Renderer (pre-patch) | Keyboard | Problem |
|---|---|---|---|---|---|
| Realtime notify | OPS → Admin ingest | lifecycle | Format / notify path | pending actions | Reference UX |
| `sm:q:` queue_open | Handle Callback Action | token → CLEAN | compact card | partial | No full actions; `answer_text: Лид` |
| Reminder exact lead | same as sm:q: | same | same | same | Reduced card |
| `/leads N` | Recent Leads | manager_status | always archive header | none on pending | Mislabeled archival |
| `sm:f:` full card | Handle Callback Action | lifecycle | buildFinalCard | lifecycle-based | OK |
| Processed/Spam terminal | HCA applied paths | new_status | terminal edit | terminal | OK |
| Reopen/resurface | HCA reopen | lifecycle transition | existing contract | reopen controls | unchanged |

**Post-patch static checks (patch-deploy.json):** queue_open uses buildFinalCard; no literal Лид; Recent Leads pending header + keyboard.
