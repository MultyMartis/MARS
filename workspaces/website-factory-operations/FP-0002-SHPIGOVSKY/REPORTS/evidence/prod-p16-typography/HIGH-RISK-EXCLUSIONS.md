# HIGH-RISK EXCLUSIONS — PROD-P16

Dry-run flagged **0** MANUAL_REVIEW rows among 599 proposed render-time transforms.

Policy exclusions (never auto-persisted; never typographed when technical):

- Fields matching `url|href|slug|embed|iframe|map|image|gallery|file|phone|email|tel|css|js`
- Shortcode-bearing HTML (`[name …]`)
- `<script|iframe|object|embed>`
- Semantic word-set mismatch (would stop auto apply)
- Length explosion >25%

Persisted mutations: **0** (render-time strategy). Any future stored normalization must re-run risk gate per exact object/field.
