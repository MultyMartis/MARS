# FP-0002 Service Subdivision — GROUP 4 Empty Space Root Cause v1

| Empty zone | Selector/component | Cause | Correction | Result |
|---|---|---|---|---|
| Large gap before team | `.service-subdivision-team-stats-v1__photo` min-height 280px + missing corridor load geometry | placeholder min-height + wrong DOM order | removed min-height; corridor first with fixed 388px height | FIXED |
| Floating stats cards | home stats in wrong section | Home pattern imported; not in PNG | removed home stats; replaced with approach cards | FIXED |
| Corridor collapsed area | corridor last + broken composition | wrong order | moved corridor first | FIXED |

Summary: empty media wrappers=0, zero-height required media=0, artificial min-heights=0.
