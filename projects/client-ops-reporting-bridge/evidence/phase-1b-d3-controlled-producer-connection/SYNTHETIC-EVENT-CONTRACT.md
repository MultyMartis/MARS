# SYNTHETIC-EVENT-CONTRACT

- site_id: `SITE-002`
- domain: `bzpm.ru`
- event_type: `site.post_1c_monitor`
- status: `OK`
- producer marker: `mars-client-ops-producer-live-d3`
- fixture: `fixtures/fixture-d3-synthetic-producer`
- unique synthetic metrics (not production monitor output)
- event_id via canonical UUID v5 producer identity
- FIRST_SEEN and exact replay share the same persisted envelope / event_id
- explicit sandbox / control-test wording in action text
