# FP-0002 V9-04 ACF Field Architecture v1

**Date:** 2026-07-02

**ACF Pro:** deferred — see Open Decisions. Architecture supports Free; repeaters may require Pro or code registration.

## Field groups

| Group ID | Machine name | Location | Purpose |
|----------|--------------|----------|---------|
| FG-SITE-OPTIONS | group_site_options | Options | phones, email, address, socials |
| FG-HOME | group_home_page | front-page | hero, grids, FAQ, CTA |
| FG-SERVICES-HUB | group_services_hub | services hub template | category sections |
| FG-SERVICE-SUBDIVISION | group_service_subdivision | subdivision template | stages, approach |
| FG-SERVICE-LEAF | group_service_leaf | leaf template | signs, program |
| FG-SERVICE-LEAF-ALCOHOL | group_service_leaf_alcohol | alcohol page | extends leaf |
| FG-O-CENTRE | group_o_centre | o-centre template | infrastructure G0-G5 |
| FG-CONTACTS | group_contacts | contacts template | map, methods |
| FG-REVIEWS | group_reviews_page | reviews template | reviews repeater |
| FG-BLOG-POST | group_blog_post | post | sources, related |
| FG-LEGAL | group_legal_meta | legal template | effective date, version |
| FG-MODAL | group_modal_form | options | default labels, consent URLs |
| FG-PLACEHOLDER | group_placeholder_notice | placeholder template | notice text |

## Naming convention

`fp02_` prefix for fields; keys stable in `acf-json/`. No giant flexible content layout.

See `manifests/FP-0002-V9-FORGE-FIELDS-v1.json` for machine IDs.
