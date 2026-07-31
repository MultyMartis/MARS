# ARCHIVE-ORDINAL-ACCEPTANCE-v1

Archive header uses actual selected count after dedupe:

`📁 Архивная карточка {i} из {N}` for i=1..N

Live:

- `/leads 3` → ordinals [1,2,3], totals all 3
- `/leads 5` → [1..5]
- `/leads 10` with 5 available → [1..5] + honest availability notice

No hardcoded index=1. No lifecycle action buttons on archive cards.
