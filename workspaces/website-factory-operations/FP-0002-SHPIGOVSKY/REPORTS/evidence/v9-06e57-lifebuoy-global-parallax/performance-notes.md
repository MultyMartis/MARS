# Performance notes

- Scroll listener: passive
- Updates via requestAnimationFrame coalesce
- Transform-only animation (translate3d + scale); no layout thrash intended
- Single global instance (validated count=1)
- Synthetic 21-step scroll loop elapsed ~348ms (validation harness)
- No console/page errors during validation matrix
- No duplicated animation roots
