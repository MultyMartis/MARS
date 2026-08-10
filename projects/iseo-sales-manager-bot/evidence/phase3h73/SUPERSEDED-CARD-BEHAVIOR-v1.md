# SUPERSEDED CARD BEHAVIOR

When operator resurfaces a lead:

1. New resurfaced card per recipient becomes authoritative
2. Older initial cards may remain as historical evidence
3. Status sync edits authoritative current cards only
4. Callback on an old card still mutates the lead once (idempotent)
5. Failure to edit a superseded historical message must NOT convert semantic ack into partial-sync warning

