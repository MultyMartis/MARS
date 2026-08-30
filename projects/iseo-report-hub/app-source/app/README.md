# app/ — application code (Phase 1A)

Minimal plain-PHP application layer (no Composer, no framework):

| Area | Role |
|------|------|
| `bootstrap.php` | Paths, session, config load, service wiring |
| `routes.php` | Conceptual GET/POST routes for Phase 1A |
| `Controllers/` | Dashboard, Auth stub, Health, BaseController |
| `Views/` | Layout, pages, partials (no template engine) |
| `Services/` | ConfigService, AuthService, CsrfService |
| `Support/` | helpers, Router, View, Response |
| `Models/` | Placeholder only — no ORM / no DB models yet |

**Boundaries:** no database connection; auth persistence not implemented; optional `.env.local` parser exists but file is not required and must not be created in Phase 1A.
