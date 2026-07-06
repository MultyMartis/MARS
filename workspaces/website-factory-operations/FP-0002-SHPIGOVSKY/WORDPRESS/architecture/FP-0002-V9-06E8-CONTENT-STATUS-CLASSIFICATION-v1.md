# FP-0002 V9-06E8 Content Status Classification v1

See `validation/v9-06e8-static-v9-content-main-layout-authority-repair/content-status-classification.json`.

| Route | Before | After |
|-------|--------|-------|
| `/uslugi/` | CONTENT_AND_LAYOUT_DRIFT | EXACT_V9_CONTENT_AND_LAYOUT |
| `/kontakty/` | LAYOUT_DRIFT | EXACT_V9_CONTENT_AND_LAYOUT |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | CONTENT_AND_LAYOUT_DRIFT | EXACT_V9_LAYOUT (+ fixture demo program) |
| `/uslugi/psihicheskoe-zdorovie/` | UNKNOWN | TEMPLATE_MATCH_DEMO_CONTENT |
| `/uslugi/rasstroystva-pischevogo-povedeniya/` | UNKNOWN | TEMPLATE_MATCH_DEMO_CONTENT |
