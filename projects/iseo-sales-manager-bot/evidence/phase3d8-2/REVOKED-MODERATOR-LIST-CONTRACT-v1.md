# REVOKED MODERATOR LIST CONTRACT v1

/moderator_pending shows two independent sections when applicable:

1. Ожидают подтверждения — new pending access requests
2. Права временно отозваны — former moderators with status=revoked

## Include

- role indicates moderator (current revoke path keeps role=moderator)
- status=revoked
- stable reactivation code exists

## Exclude

- public users
- pending users
- blocked users
- Admin
- active moderators
- malformed rows

/moderators remains active-only.
