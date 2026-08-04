# MODERATOR CHANGE DELIVERY BOUNDARY v1

| Event | Effect |
|-------|--------|
| New moderator after a lead | No historical backfill; future leads only |
| Moderator revoked | Future delivery stops immediately; old buttons deny at click time |
| Re-approved | Future delivery resumes if private chat still available; no bulk resend |
| Public users | Never in expansion; never lifecycle callbacks |
