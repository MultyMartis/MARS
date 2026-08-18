# LEGAL QA MATRIX — P18A

Target: reversible `#3` privacy-policy; all legal URLs on `http://shpigovsky.beget.tech` (no follow to legacy apex).

| Case | Setup | Banner | Result |
|------|-------|--------|--------|
| 1 | Production ready + Demo OFF + Blocker OFF (all 4 pages, saved `0`) | absent | PASS |
| 2 | Demo ON (`legal_demo_marker=1` on #3) | present | PASS |
| 3 | Demo OFF again (`0` restored) | absent | PASS |
| 4 | Blocker ON + Demo OFF | absent | PASS |
| 5 | Preview | same helper: current ID, then parent if revision/autosave lacks key | documented; published URL is CASE 1 |

QA rows restored: all four pages `legal_demo_marker=0`, `legal_production_blocker=0`, `legal_status=production_ready`.

**DEMO MARKER OFF = NO DEMO BANNER**

Machine: `DEPLOY-QA.json`, `LEGAL-META-AFTER-QA.txt`.
