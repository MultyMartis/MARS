# Example routes (Phase 1A conceptual map)

These routes are implemented in `app/routes.php` for the source skeleton.

| Method | Path | Handler | Notes |
|--------|------|---------|-------|
| GET | `/` | DashboardController::index | Status cards stub |
| GET | `/login` | AuthController::showLogin | Login form stub |
| POST | `/login` | AuthController::attemptLogin | Returns “Auth persistence not implemented in Phase 1A” |
| GET | `/logout` | AuthController::logout | Clears placeholder session keys only |
| GET | `/health` | HealthController::index | PHP/extension checks; no DB |
| * | (unmatched) | HealthController::notFound | 404 page |

Also available as a direct public entrypoint: `public/health.php` (same health view via bootstrap).

No regex routing. No client report routes yet. No DB.
