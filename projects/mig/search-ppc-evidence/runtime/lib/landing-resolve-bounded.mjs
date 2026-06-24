import { nowIso, extractDomain } from './utils.mjs';

const DEFAULT_TIMEOUT_MS = 12000;
const MAX_REDIRECTS = 5;

export async function resolveLandingBounded(destinationUrl, { timeoutMs = DEFAULT_TIMEOUT_MS } = {}) {
  if (!destinationUrl) {
    return {
      ok: false,
      state: 'LANDING RESOLUTION NOT AVAILABLE',
      displayed_url: null,
      final_url: null,
      redirect_chain: [],
      http_status: null,
      title: null,
      h1: null,
      primary_cta: null,
      resolved_at: nowIso(),
      limitation: 'NO_DESTINATION_URL',
    };
  }

  const redirect_chain = [destinationUrl];
  let current = destinationUrl;
  let response;
  try {
    for (let i = 0; i < MAX_REDIRECTS; i += 1) {
      response = await fetch(current, {
        method: 'GET',
        redirect: 'manual',
        headers: {
          'User-Agent': 'MARS-MIG-LandingResolver/1.0 (bounded-technical-test)',
          Accept: 'text/html,application/xhtml+xml',
        },
        signal: AbortSignal.timeout(timeoutMs),
      });
      if (response.status >= 300 && response.status < 400) {
        const loc = response.headers.get('location');
        if (!loc) break;
        current = new URL(loc, current).href;
        redirect_chain.push(current);
        continue;
      }
      break;
    }
  } catch (e) {
    return {
      ok: false,
      state: 'LANDING RESOLUTION NOT AVAILABLE',
      displayed_url: destinationUrl,
      final_url: redirect_chain[redirect_chain.length - 1],
      redirect_chain,
      http_status: null,
      title: null,
      h1: null,
      primary_cta: null,
      resolved_at: nowIso(),
      limitation: `FETCH_ERROR: ${e.name}`,
    };
  }

  const http_status = response?.status ?? null;
  let body = '';
  if (response && http_status && http_status < 400) {
    body = await response.text();
  }

  const title = body.match(/<title[^>]*>([^<]{1,300})<\/title>/i)?.[1]?.trim() || null;
  const h1 = body.match(/<h1[^>]*>([\s\S]{1,400}?)<\/h1>/i)?.[1]?.replace(/<[^>]+>/g, '').trim() || null;
  const primary_cta =
    body.match(/<a[^>]*class="[^"]*(?:btn|button|cta)[^"]*"[^>]*>([^<]{2,120})</i)?.[1]?.trim() ||
    body.match(/<button[^>]*>([^<]{2,120})</i)?.[1]?.trim() ||
    null;

  return {
    ok: http_status !== null && http_status < 400,
    state: http_status !== null && http_status < 400 ? 'RESOLVED' : 'LANDING RESOLUTION NOT AVAILABLE',
    displayed_url: destinationUrl,
    final_url: redirect_chain[redirect_chain.length - 1],
    redirect_chain,
    http_status,
    title,
    h1,
    primary_cta,
    domain: extractDomain(redirect_chain[redirect_chain.length - 1]),
    resolved_at: nowIso(),
    limitation: http_status && http_status >= 400 ? `HTTP_${http_status}` : null,
  };
}
