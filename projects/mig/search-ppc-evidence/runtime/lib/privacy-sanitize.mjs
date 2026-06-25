import fs from 'node:fs';

const PII_PATTERNS = [
  { id: 'LOGIN_FIELD_VALUE', pattern: /"login"\s*:\s*"[^"]+"/gi },
  { id: 'LOGGED_IN_FLAG', pattern: /"isLoggedIn"\s*:\s*true/gi },
  { id: 'YANDEXUID_VALUE', pattern: /yandexuid[=:]["']?[a-z0-9]+/gi },
  { id: 'UID_FIELD_VALUE', pattern: /"uid"\s*:\s*"\d+"/gi },
  { id: 'EMAIL_VALUE', pattern: /[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}/gi },
  { id: 'SESSION_TOKEN_VALUE', pattern: /Session_id=[^;\s]+|secure_token[=:][^;\s"']+/gi },
];

export function scanHtmlForSessionIdentifiers(html) {
  const findings = [];
  for (const { id, pattern } of PII_PATTERNS) {
    const matches = html.match(pattern) || [];
    if (matches.length) {
      findings.push({ id, count: matches.length, sanitized: true });
    }
  }
  return {
    contains_session_identifiers: findings.length > 0,
    finding_types: findings.map((f) => f.id),
    findings,
    raw_values_withheld: true,
  };
}

export function assertRepoSafeText(text, label = 'output') {
  const scan = scanHtmlForSessionIdentifiers(text);
  if (scan.contains_session_identifiers) {
    const blocked = scan.finding_types.join(', ');
    throw new Error(`PRIVACY SANITIZATION FAILED for ${label}: ${blocked}`);
  }
  return scan;
}

export function privacySanitizationSummary(htmlPath) {
  if (!htmlPath || !fs.existsSync(htmlPath)) {
    return { html_present: false, contains_session_identifiers: false, raw_html_outside_git: true };
  }
  const html = fs.readFileSync(htmlPath, 'utf8');
  const scan = scanHtmlForSessionIdentifiers(html);
  return {
    html_present: true,
    html_path_class: 'EXTERNAL_EVIDENCE_ONLY',
    raw_html_committed_to_git: false,
    ...scan,
  };
}
