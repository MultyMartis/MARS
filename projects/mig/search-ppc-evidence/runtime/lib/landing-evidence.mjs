import { nowIso, extractDomain } from './utils.mjs';

export function captureLandingEvidence({ destinationUrl, pageData, evidenceLinks }) {
  if (!destinationUrl) {
    return { ok: false, state: 'PAGE LOAD FAILURE', observed: {}, inferred: {} };
  }

  const observed = {
    final_url: pageData?.final_url || destinationUrl,
    domain: extractDomain(destinationUrl),
    page_title: pageData?.page_title || null,
    h1: pageData?.h1 || null,
    offer_text: pageData?.offer || null,
    cta: pageData?.cta || null,
    phone_present: !!pageData?.phone,
    form_present: !!pageData?.form,
    trust_markers: pageData?.trust_markers || [],
    pricing_claims: pageData?.pricing_claims || [],
    geography_claims: pageData?.geography_claims || [],
    capture_timestamp: nowIso(),
    screenshot_ref: evidenceLinks?.screenshot || null,
    html_ref: evidenceLinks?.html || null,
    redirect_chain: pageData?.redirect_chain || [],
  };

  return {
    ok: true,
    state: observed.page_title ? 'PARTIAL' : 'PARTIAL',
    observed,
    extracted_text: pageData?.extracted_text || {},
    analyst_inference: {},
    note: 'Landing evidence separates observed facts from analyst inference',
  };
}
