# FP-0002 V7 Package #003 — Video Poster Map

**Date:** 2026-06-26

## Extraction method

Real frames extracted with OpenCV from frontend MP4 sources. No AI generation, no decorative processing.

## Mapping

| Video | Duration | Selected timestamp | Poster path | Preview card |
| ----- | -------: | -----------------: | ----------- | ------------ |
| `src/video/sergey-shpigovsky-interview.mp4` | 97.88 s | 48.94 s | `src/img/content/videos/sergey-shpigovsky-interview-poster.webp` | Home videos card 1 |
| `src/video/shpigovsky-center.mp4` | 92.52 s | 9.25 s | `src/img/content/videos/shpigovsky-center-poster.webp` | Home videos card 2 |

## Selection notes

- **Interview:** frame at 48.94 s — Sergey mid-speech, neutral expression, sharp focus (Laplacian 131), natural outdoor lighting.
- **Center:** frame at 9.25 s — building exterior with tree canopy, sharp (Laplacian 284), balanced brightness.

## Fancybox mapping (unchanged)

| Card | Fancybox href |
| ---- | ------------- |
| 1 | `assets/video/sergey-shpigovsky-interview.mp4` |
| 2 | `assets/video/shpigovsky-center.mp4` |

## Temporary frames

Candidate JPG frames stored under `reviews/package-003/_temp-frames/` — **not committed**.
