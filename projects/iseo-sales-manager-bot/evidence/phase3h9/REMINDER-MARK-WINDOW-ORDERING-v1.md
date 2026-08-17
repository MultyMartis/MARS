# REMINDER MARK-WINDOW ORDERING v1

Classifier output: `reminder_mark_window_complete=false`.

Mark Window Complete still attempted **evaluation observability writes** (last_evaluation / last_decision=ERROR), not `pending_reminder_last_window`. Those writes also failed with invalid_grant.

Invariant held: business date **not** marked complete before (or without) successful send. 10:15 was not suppressed by last_window.
