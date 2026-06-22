const RELATION_TYPES = ['known_same_domain', 'probable_relation', 'separate_entity', 'unresolved'];

export function buildAdvertiserRegistry(observations) {
  const advertisers = new Map();
  const domains = new Map();

  for (const obs of observations) {
    for (const ad of obs.ads || []) {
      const domain = ad.domain;
      if (!domain) continue;

      if (!domains.has(domain)) {
        domains.set(domain, {
          domain,
          advertiser_ids: [],
          first_observed: ad.observed_timestamp,
          last_observed: ad.observed_timestamp,
          observation_count: 0,
          regions: new Set(),
          devices: new Set(),
        });
      }
      const d = domains.get(domain);
      d.observation_count += 1;
      d.regions.add(ad.region);
      d.devices.add(ad.device);
      if (ad.observed_timestamp < d.first_observed) d.first_observed = ad.observed_timestamp;
      if (ad.observed_timestamp > d.last_observed) d.last_observed = ad.observed_timestamp;

      const displayKey = (ad.advertiser_display_name || domain).toLowerCase();
      if (!advertisers.has(displayKey)) {
        advertisers.set(displayKey, {
          advertiser_id: `adv-${advertisers.size + 1}`,
          display_name: ad.advertiser_display_name || domain,
          primary_domain: domain,
          relation_to_domain: 'known_same_domain',
          merge_policy: 'domain_primary_not_display_name',
          observation_count: 0,
          query_coverage: new Set(),
        });
      }
      const a = advertisers.get(displayKey);
      a.observation_count += 1;
      a.query_coverage.add(ad.query);
      if (a.primary_domain !== domain) a.relation_to_domain = 'probable_relation';
    }
  }

  return {
    advertisers: [...advertisers.values()].map((a) => ({
      ...a,
      query_coverage: [...a.query_coverage],
    })),
    domains: [...domains.values()].map((d) => ({
      ...d,
      regions: [...d.regions],
      devices: [...d.devices],
    })),
    relation_types: RELATION_TYPES,
  };
}

export function assessAdvertiserMerge(nameA, nameB, domainA, domainB) {
  if (domainA && domainB && domainA === domainB) return 'known_same_domain';
  if (nameA && nameB && nameA.toLowerCase() === nameB.toLowerCase() && domainA !== domainB) return 'unresolved';
  return 'separate_entity';
}
