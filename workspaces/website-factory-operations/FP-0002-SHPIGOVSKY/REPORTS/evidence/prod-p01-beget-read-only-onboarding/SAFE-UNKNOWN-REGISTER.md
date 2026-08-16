# SAFE UNKNOWN REGISTER — PROD-P01

- Beget docroot path
- Beget account / panel IDs
- Backup ID / path / timestamp (operator-confirmed existence only)
- Production DB name / host / prefix (local history: mars_wp_fp0002 / fp02_ — production verification SAFE UNKNOWN)
- WordPress core exact version (generator meta empty/absent in public HTML)
- Exact production WPilot plugin Version / RELEASE_LABEL (ping does not expose)
- Whether migrated WPilot token matches local token file (must not probe with secrets)
- SMTP / mail delivery
- OPcache / WAF / ModSecurity details beyond public nginx+PHP headers
- Cache layer beyond public Cache-Control absence
- HTTPS certificate (HTTPS endpoint timed out / unavailable in this wave)
- Logs location
- Whether old hosting shpigovsky.ru content differs (out of scope)
