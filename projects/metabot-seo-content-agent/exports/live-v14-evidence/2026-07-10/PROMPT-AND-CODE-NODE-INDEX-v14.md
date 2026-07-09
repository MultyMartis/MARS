# PROMPT-AND-CODE-NODE-INDEX-v14

| workflow | node name | node type | content type | purpose | approximate size | secret scan result | quality relevance | migration relevance | notes |
|----------|-----------|-----------|--------------|---------|------------------|--------------------|-------------------|---------------------|-------|
| SEO Content Agent Beta.v14 - Intake | Build User Lock Key | n8n-nodes-base.code | code | lock/state | 606 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Intake | Send Busy Message | n8n-nodes-base.telegram | prompt | telegram IO | 150 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Intake | Check Active Lock | n8n-nodes-base.code | code | lock/state | 1190 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Intake | Send Task Accepted | n8n-nodes-base.telegram | prompt | telegram IO | 496 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Intake | Debug Lock State | n8n-nodes-base.code | code | lock/state | 224 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Intake | Detect Local Command | n8n-nodes-base.code | code | code transform | 2966 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Intake | Send Local Intake Message | n8n-nodes-base.telegram | prompt | telegram IO | 26 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Intake | Send NOT-FOUND Message | n8n-nodes-base.telegram | prompt | telegram IO | 158 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Intake | Build Worker Payload | n8n-nodes-base.code | code | code transform | 1637 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Format Local Response | n8n-nodes-base.code | code | code transform | 2088 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Send Telegram Local | n8n-nodes-base.telegram | prompt | telegram IO | 97 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Format Single Mode Message | n8n-nodes-base.code | code | code transform | 9725 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Send Telegram Single | n8n-nodes-base.telegram | prompt | telegram IO | 97 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Run Extract Outline | n8n-nodes-base.code | code | code transform | 1462 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Run Extract Text | n8n-nodes-base.code | code | code transform | 1441 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Run Extract SEO QA | n8n-nodes-base.code | code | quality layer | 4161 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Format Run Pipeline | n8n-nodes-base.code | code | code transform | 11755 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Send Telegram Run | n8n-nodes-base.telegram | prompt | telegram IO | 31 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Prepare Memory Row Local | n8n-nodes-base.code | code | code transform | 514 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Prepare Memory Row Single | n8n-nodes-base.code | code | code transform | 791 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Prepare Memory Row Run | n8n-nodes-base.code | code | code transform | 791 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Route Command | n8n-nodes-base.code | code | routing | 4363 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Run Extract Factcheck | n8n-nodes-base.code | code | quality layer | 1579 chars | CLEAN_AFTER_SANITIZE | high | high | |
| SEO Content Agent Beta.v14 - Worker | Format Memory Get | n8n-nodes-base.code | code | code transform | 1540 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Send Telegram Memory Get | n8n-nodes-base.telegram | prompt | telegram IO | 97 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Prepare Memory Reuse | n8n-nodes-base.code | code | code transform | 2637 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Compute Content Score | n8n-nodes-base.code | code | code transform | 6276 chars | CLEAN_AFTER_SANITIZE | high | medium | |
| SEO Content Agent Beta.v14 - Worker | Auto Fix Text | n8n-nodes-base.code | code | code transform | 224 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Auto Polish Text | n8n-nodes-base.code | code | code transform | 3452 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Extract Auto Polish Text | n8n-nodes-base.code | code | code transform | 1103 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Ensure FAQ Text | n8n-nodes-base.code | code | code transform | 221 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Commercial Layer Text | n8n-nodes-base.code | code | code transform | 227 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Final Text Cleanup | n8n-nodes-base.code | code | code transform | 1971 chars | CLEAN_AFTER_SANITIZE | high | medium | |
| SEO Content Agent Beta.v14 - Worker | Store Worker Meta | n8n-nodes-base.code | code | code transform | 748 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Status Outline | n8n-nodes-base.telegram | prompt | telegram IO | 51 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Status Strategy | n8n-nodes-base.telegram | prompt | telegram IO | 58 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Status Text | n8n-nodes-base.telegram | prompt | telegram IO | 50 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Status SEO QA | n8n-nodes-base.telegram | prompt | telegram IO | 60 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Status Factcheck | n8n-nodes-base.telegram | prompt | telegram IO | 77 chars | CLEAN_AFTER_SANITIZE | high | medium | |
| SEO Content Agent Beta.v14 - Worker | Status Final | n8n-nodes-base.telegram | prompt | telegram IO | 61 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Build Outline Payload | n8n-nodes-base.code | code | code transform | 3637 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Find Memory Reuse Row | n8n-nodes-base.code | code | code transform | 552 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Build Factcheck Payload | n8n-nodes-base.code | code | quality layer | 2764 chars | CLEAN_AFTER_SANITIZE | high | high | |
| SEO Content Agent Beta.v14 - Worker | Postcheck Strict Claims | n8n-nodes-base.code | code | code transform | 3364 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Build SEOQA Payload | n8n-nodes-base.code | code | quality layer | 3628 chars | CLEAN_AFTER_SANITIZE | high | high | |
| SEO Content Agent Beta.v14 - Worker | Extract SEO Strategy | n8n-nodes-base.code | code | code transform | 1226 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Build Text Payload | n8n-nodes-base.code | code | code transform | 4611 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Build SEO Strategy Payload | n8n-nodes-base.code | code | code transform | 1527 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Build Single Payload | n8n-nodes-base.code | code | code transform | 6555 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Parse Mode | n8n-nodes-base.code | code | code transform | 405 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Status Complete | n8n-nodes-base.telegram | prompt | telegram IO | 60 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Take First Item | n8n-nodes-base.code | code | code transform | 18 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Restore Format Run Items | n8n-nodes-base.code | code | code transform | 150 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Restore Postcheck Data | n8n-nodes-base.code | code | code transform | 382 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Restore Route Data | n8n-nodes-base.code | code | routing | 88 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Restore Outline Data | n8n-nodes-base.code | code | code transform | 146 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Restore SEO Strategy Data | n8n-nodes-base.code | code | code transform | 149 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Restore Content Score Data | n8n-nodes-base.code | code | code transform | 733 chars | CLEAN_AFTER_SANITIZE | high | medium | |
| SEO Content Agent Beta.v14 - Worker | Hard Final Cleanup | n8n-nodes-base.code | code | code transform | 250 chars | CLEAN_AFTER_SANITIZE | high | medium | |
| SEO Content Agent Beta.v14 - Worker | Restore Lock Context | n8n-nodes-base.code | code | lock/state | 304 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Find Memory Get Row | n8n-nodes-base.code | code | code transform | 506 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Restore Format Run Items After Lock | n8n-nodes-base.code | code | lock/state | 150 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Build Text Repair Payload | n8n-nodes-base.code | code | code transform | 2819 chars | CLEAN_AFTER_SANITIZE | high | high | |
| SEO Content Agent Beta.v14 - Worker | Extract Text Repair | n8n-nodes-base.code | code | code transform | 1049 chars | CLEAN_AFTER_SANITIZE | high | medium | |
| SEO Content Agent Beta.v14 - Worker | Normalize Run Output | n8n-nodes-base.code | code | code transform | 4918 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Status Single | n8n-nodes-base.telegram | prompt | telegram IO | 611 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Take First Single Item | n8n-nodes-base.code | code | code transform | 18 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Status Single Complete | n8n-nodes-base.telegram | prompt | telegram IO | 60 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Restore Format Single Items After Lock | n8n-nodes-base.code | code | lock/state | 137 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Restore Route Data Single | n8n-nodes-base.code | code | routing | 88 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Worker | Build Single Text Repair Payload | n8n-nodes-base.code | code | code transform | 2502 chars | CLEAN_AFTER_SANITIZE | high | medium | |
| SEO Content Agent Beta.v14 - Worker | Extract Single Text Repair | n8n-nodes-base.code | code | code transform | 2798 chars | CLEAN_AFTER_SANITIZE | high | medium | |
| SEO Content Agent Beta.v14 - Worker | Strict Cleanup | n8n-nodes-base.code | code | code transform | 3314 chars | CLEAN_AFTER_SANITIZE | high | medium | |
| SEO Content Agent Beta.v14 - Worker | Table Sanity Check | n8n-nodes-base.code | code | code transform | 2610 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Worker | Strict Risk Scanner | n8n-nodes-base.code | code | code transform | 4003 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Admin | Build Admin Response | n8n-nodes-base.code | code | admin/recovery | 7292 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Admin | Send Admin Telegram | n8n-nodes-base.telegram | prompt | admin/recovery | 26 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Admin | Prepare Cancelled Locks | n8n-nodes-base.code | code | lock/state | 273 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Admin | Send Stop All Flow Success | n8n-nodes-base.telegram | prompt | admin/recovery | 59 chars | CLEAN_AFTER_SANITIZE | medium | medium | |
| SEO Content Agent Beta.v14 - Admin | Format Locks Response | n8n-nodes-base.code | code | lock/state | 1019 chars | CLEAN_AFTER_SANITIZE | medium | high | |
| SEO Content Agent Beta.v14 - Admin | Format Health Response | n8n-nodes-base.code | code | code transform | 1644 chars | CLEAN_AFTER_SANITIZE | medium | high | |
