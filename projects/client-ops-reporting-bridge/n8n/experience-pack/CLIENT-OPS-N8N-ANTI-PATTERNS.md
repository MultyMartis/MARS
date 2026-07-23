# Client Ops n8n Anti-Patterns

**Status:** SKELETON — TO BE COMPLETED AFTER FIRST SANDBOX APPLY

## Forbidden

- Manual n8n UI assembly of Client Ops Bridge.
- Embedding secrets, chat IDs, credential IDs, or webhook IDs in Git JSON.
- Claiming durable dedupe while sandbox mode is deferred.
- Adding Telegram to the first create.
- Using workflow staticData as sole production dedupe authority without evidence.
- Inventing node typeVersions without live/reference evidence.
- Using GET-only exporter client for POST/PUT/PATCH/DELETE.
- Auto-activating after create.
- Echoing auth mismatch details or raw bodies in HTTP responses.
- Recomputing SITE-002 classification inside n8n from raw artifacts.
