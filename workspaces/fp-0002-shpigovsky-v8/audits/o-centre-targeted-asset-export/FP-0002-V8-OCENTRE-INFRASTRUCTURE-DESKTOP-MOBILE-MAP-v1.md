# FP-0002 V8 O-Centre Infrastructure Desktop/Mobile Map v1

| Asset candidate | Desktop node | Mobile node | Same ref | Same crop | Same role | Decision |
|---|---|---|---:|---:|---:|---|
| OC-INF-01 | `1:2451` | `1:5710` | 1 | 1 | 1 | ONE_SHARED_FILE |
| OC-INF-02 | `1:2452` | `1:5721` | 1 | 1 | 1 | ONE_SHARED_FILE |
| OC-INF-03 | `1:2453` | — | 0 | 1 | 1 | DESKTOP_ONLY |
| OC-INF-04 | `1:2458` | `1:5738` | 1 | 1 | 1 | ONE_SHARED_FILE |
| OC-INF-05 | `1:2459` | `1:5749` | 1 | 1 | 1 | ONE_SHARED_FILE |
| OC-INF-06 | `1:2460` | — | 0 | 1 | 1 | DESKTOP_ONLY |
| OC-INF-07 | `1:2465` | `1:5766` | 1 | 1 | 1 | ONE_SHARED_FILE |
| OC-INF-08 | `1:2466` | — | 0 | 1 | 1 | DESKTOP_ONLY |
| OC-INF-09 | `1:2467` | — | 0 | 1 | 1 | DESKTOP_ONLY |
| OC-INF-10 | `1:2472` | `1:5794` | 1 | 1 | 1 | ONE_SHARED_FILE |
| OC-INF-11 | `1:2473` | `1:5805` | 1 | 1 | 1 | ONE_SHARED_FILE |
| OC-INF-12 | `1:2474` | — | 0 | 1 | 1 | DESKTOP_ONLY |
| OC-INF-13 | `1:2496` | `1:5838` | 1 | 1 | 1 | ONE_SHARED_FILE |
| OC-INF-14 | `1:2499` | `1:5839` | 1 | 1 | 1 | ONE_SHARED_FILE |
| OC-INF-15 | `1:2500` | `1:5841` | 1 | 1 | 1 | ONE_SHARED_FILE |
| OC-INF-16 | `1:2501` | `1:5842` | 1 | 1 | 1 | ONE_SHARED_FILE |
| OC-INF-17 | `1:2507` | `1:5846` | 1 | 1 | 1 | ONE_SHARED_FILE |
| OC-INF-18 | `1:2508` | `1:5847` | 1 | 1 | 1 | ONE_SHARED_FILE |
| OC-INF-19 | — | `1:5720`, `1:5748` | 0 | 1 | 1 | MOBILE_ONLY |
| OC-INF-20 | — | `1:5777` | 0 | 1 | 1 | MOBILE_ONLY |

## Result

All production assets use **ONE_SHARED_FILE** when bitmap hash matches across breakpoints.
No separate mobile canonical files created (CSS crop only).