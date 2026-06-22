# FWS-0001 — Theme Architecture v1

```
fws-synthetic/
├── style.css
├── functions.php
├── header.php / footer.php
├── front-page.php, archive-service.php, single-service.php, page-contacts.php
├── inc/ (setup, assets, template-tags, options)
├── template-parts/
└── assets/css, assets/js
```

Bootstrap via `functions.php`; no business logic in theme beyond presentation helpers.
