import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import {
  AD_URL_QUERY_FORBIDDEN,
  TRACKING_POLICY_GLOBAL,
  cleanAdUrl,
  isGlobalTrackingPolicy,
  resolveAdLandingUrl,
  validateCleanAdUrl,
} from '../src/url-policy.mjs';

describe('url-policy', () => {
  const globalConfig = {
    tracking_policy: TRACKING_POLICY_GLOBAL,
    ad_url_query_parameters: AD_URL_QUERY_FORBIDDEN,
  };

  it('detects global tracking transport policy', () => {
    assert.equal(isGlobalTrackingPolicy(globalConfig), true);
    assert.equal(isGlobalTrackingPolicy({}), false);
  });

  it('accepts clean landing URL', () => {
    const url = 'https://lk.corvonero.ru/programmist-1s/';
    assert.equal(validateCleanAdUrl(url).length, 0);
    assert.equal(cleanAdUrl(url), url);
  });

  it('rejects UTM in ad URL', () => {
    const url =
      'https://lk.corvonero.ru/programmist-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=corv_programmist_1s&utm_content=ca-01-direct-service-order';
    const violations = validateCleanAdUrl(url);
    assert.ok(violations.some((v) => v.code === 'URL_QUERY_FORBIDDEN'));
    assert.ok(violations.some((v) => v.code === 'UTM_IN_AD_URL'));
  });

  it('rejects arbitrary query string', () => {
    const url = 'https://lk.corvonero.ru/programmist-1s/?foo=bar';
    assert.ok(validateCleanAdUrl(url).some((v) => v.code === 'URL_QUERY_FORBIDDEN'));
  });

  it('rejects fragment in ad URL', () => {
    const url = 'https://lk.corvonero.ru/programmist-1s/#section';
    assert.ok(validateCleanAdUrl(url).some((v) => v.code === 'URL_FRAGMENT_FORBIDDEN'));
  });

  it('rejects {keyword} macro in ad URL', () => {
    const url = 'https://lk.corvonero.ru/programmist-1s/{keyword}';
    assert.ok(validateCleanAdUrl(url).some((v) => v.code === 'KEYWORD_MACRO_IN_URL'));
  });

  it('resolveAdLandingUrl strips UTM under global policy', () => {
    const dirty =
      'https://lk.corvonero.ru/programmist-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=corv_programmist_1s&utm_content=ca-01-direct-service-order';
    assert.equal(
      resolveAdLandingUrl(dirty, globalConfig, {
        campaignSlug: 'corv_programmist_1s',
        groupSlug: 'ca-01-direct-service-order',
      }),
      'https://lk.corvonero.ru/programmist-1s/'
    );
  });
});
