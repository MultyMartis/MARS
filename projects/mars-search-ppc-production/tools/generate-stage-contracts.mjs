#!/usr/bin/env node
/**
 * generate-stage-contracts.mjs
 * Writes SPPC stage contract markdown files and stages/README.md index.
 * Run: node tools/generate-stage-contracts.mjs
 */

import { mkdir, writeFile } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');
const STAGES_DIR = join(ROOT, 'stages');

/** @typedef {object} StageDef */

/** @type {StageDef[]} */
const STAGES = [
  {
    id: 'SPPC-01',
    num: '01',
    slug: 'business-intake',
    name: 'Business Intake and Operator Authority',
    purpose:
      'Establish operator authority, commercial scope, risk posture, and project charter before any semantic or campaign work begins. ATLAS owns the intake record and binds who may advance the lifecycle.',
    owning: 'ATLAS',
    participating: ['Operator', 'MIG (read-only context)', 'ORCA (read-only context)'],
    requiredInputs: [
      'Operator identity and authority declaration',
      'Client or brand identifier and commercial objective',
      'Geography, language, and platform targets (e.g. Yandex Direct Search)',
      'Budget envelope and timeline constraints',
      'Known constraints: legal, compliance, brand voice, prohibited claims',
      'Pointer to prior campaigns or SAFE UNKNOWN declaration',
    ],
    optionalInputs: [
      'Historical performance exports',
      'Existing site or landing inventory',
      'Competitor shortlist from operator',
      'CRM or lead-routing notes',
    ],
    sourceOfTruth: [
      'ATLAS intake record is SoT for operator authority and scope boundaries.',
      'No downstream system may override intake scope without a documented ATLAS reopen.',
      'Commercial claims not captured in intake are SAFE UNKNOWN until explicitly added.',
    ],
    processing: [
      'Validate operator authority and signing role.',
      'Capture commercial objective, KPI intent, and failure tolerance.',
      'Record geography, platform, and budget envelope.',
      'Declare prohibited topics, claims, and out-of-scope services.',
      'Issue intake completion token for SPPC-02.',
    ],
    requiredOutputs: [
      'ATLAS business intake record (versioned markdown or JSON)',
      'Operator authority statement with effective date',
      'Scope boundary manifest (in-scope / out-of-scope / SAFE UNKNOWN)',
      'Risk and compliance notes',
    ],
    prohibitedOutputs: [
      'Keyword lists or semantic classifications',
      'Campaign structure or ad copy',
      'Pilot corpus substitutions framed as production intake',
      'Implicit launch authorization',
    ],
    validation: [
      'All required intake fields populated or explicitly marked SAFE UNKNOWN.',
      'Operator role and approval chain documented.',
      'No downstream artifact references without intake version binding.',
    ],
    blocking: [
      'Missing operator authority declaration',
      'Undefined geography or platform target',
      'Conflicting scope statements without resolution',
      'Intake record not versioned or not written to project path',
    ],
    completionStatus: 'COMPLETE when intake record is approved and version-stamped; status token `intake_approved`.',
    evidence: [
      'Committed intake file under project intake path',
      'REPORT or audit line referencing intake version ID',
      'Operator sign-off timestamp',
    ],
    nextStages: ['SPPC-02'],
    rollback:
      'Reopen intake invalidates all downstream stage tokens. Operator must re-approve scope changes; MIG/ORCA artifacts remain read-only until new intake version is bound.',
    role: 'Operator (primary); ATLAS maintainer (documentation)',
    operatorApproval: 'yes',
    charterNotes: null,
  },
  {
    id: 'SPPC-02',
    num: '02',
    slug: 'source-registration',
    name: 'Source Registration',
    purpose:
      'Register and fingerprint every external data source MIG will consume: Wordstat exports, site crawls, SERP providers, competitor feeds, and operator-supplied files. No ingestion without registered provenance.',
    owning: 'MIG',
    participating: ['ATLAS (scope binding)', 'Operator'],
    requiredInputs: [
      'SPPC-01 intake_approved token',
      'Source file manifests with checksums',
      'Acquisition timestamps and method (export, API, crawl)',
      'Geography and language metadata per source',
    ],
    optionalInputs: [
      'Provider credentials reference (not secrets in repo)',
      'Prior MIG research pack pointers',
      'Throttling or rate-limit notes',
    ],
    sourceOfTruth: [
      'MIG source registry is SoT for what was ingested and when.',
      'Unregistered files must not enter semantic or campaign pipelines.',
      'Checksum mismatch triggers re-registration, not silent overwrite.',
    ],
    processing: [
      'Register each source with ID, type, geography, and acquisition time.',
      'Compute and store checksums for all registered blobs.',
      'Bind sources to intake version from SPPC-01.',
      'Emit source registration manifest for SPPC-03.',
    ],
    requiredOutputs: [
      'MIG source registration manifest (JSON)',
      'Per-source metadata records with checksums',
      'Source-to-intake version binding record',
    ],
    prohibitedOutputs: [
      'Semantic classifications',
      'Normalized keyword registry',
      'Campaign or ad artifacts',
    ],
    validation: [
      'Every file slated for corpus intake appears in registry.',
      'Checksums reproducible on re-read.',
      'Geography and language align with intake scope.',
    ],
    blocking: [
      'SPPC-01 not complete',
      'Unregistered source referenced in downstream job',
      'Checksum failure without operator resolution',
    ],
    completionStatus: 'COMPLETE when manifest is committed and `sources_registered` token issued.',
    evidence: [
      'Committed source registration manifest',
      'Checksum audit log or inline hashes',
      'REPORT line listing source count and types',
    ],
    nextStages: ['SPPC-03'],
    rollback:
      'Adding or replacing sources reopens SPPC-02 and downstream semantic stages. Prior corpus artifacts marked stale until re-intake.',
    role: 'MIG operator / research lead',
    operatorApproval: 'no',
    charterNotes: null,
  },
  {
    id: 'SPPC-03',
    num: '03',
    slug: 'full-semantic-corpus-intake',
    name: 'Full Semantic Corpus Intake',
    purpose:
      'Ingest the complete semantic demand corpus for the scoped geography and language. Production lifecycle requires full corpus intake — no pilot row-cap substitution.',
    owning: 'MIG / ORCA (joint)',
    participating: ['MIG (ingestion)', 'ORCA (corpus binding)', 'Operator (scope witness)'],
    requiredInputs: [
      'SPPC-02 sources_registered token',
      'Full Wordstat or equivalent demand export for scoped market',
      'Registered source manifest with valid checksums',
      'Intake geography and language binding',
    ],
    optionalInputs: [
      'Supplementary long-tail exports',
      'Seasonal adjustment notes from operator',
      'Legacy corpus for diff-only analysis (not substitution)',
    ],
    sourceOfTruth: [
      'Committed full corpus artifact is SoT for raw demand rows entering normalization.',
      'Row count and checksum must match registered sources — no partial silent drops.',
      '200-row pilot slices are explicitly prohibited as production corpus substitutes.',
    ],
    processing: [
      'Ingest 100% of registered demand rows for scoped market.',
      'Reject or quarantine rows outside geography/language scope.',
      'Record corpus statistics: row count, unique queries, date range.',
      'Bind corpus to source registry and intake version.',
      'Emit corpus intake receipt for SPPC-04.',
    ],
    requiredOutputs: [
      'Full semantic corpus artifact (JSON or canonical table)',
      'Corpus intake receipt with row count, checksum, and scope binding',
      'Quarantine log for out-of-scope rows',
    ],
    prohibitedOutputs: [
      '200-row or other pilot-substitution corpora labeled as production',
      'Normalized or classified keyword registry',
      'Campaign-ready keyword lists',
      'Silent truncation without operator waiver on record',
    ],
    validation: [
      'Row count matches sum of registered source rows minus documented quarantine.',
      'No pilot slice filename or metadata present.',
      'Corpus checksum stable across re-ingest of same sources.',
      'Geography and language filters documented.',
    ],
    blocking: [
      'SPPC-02 incomplete',
      'Corpus row count below registered source total without waiver',
      'Pilot slice detected in production path',
      'Checksum mismatch',
    ],
    completionStatus: 'COMPLETE when full corpus committed and `corpus_intake_complete` token issued.',
    evidence: [
      'Committed corpus artifact path and size',
      'Intake receipt with explicit full-corpus row count',
      'REPORT confirming no pilot substitution',
    ],
    nextStages: ['SPPC-04'],
    rollback:
      'Corpus replacement reopens SPPC-03 through all semantic stages. Operator must acknowledge row-count delta.',
    role: 'MIG ingestion lead with ORCA corpus binding witness',
    operatorApproval: 'yes — witness sign-off that full corpus, not pilot, was ingested',
    charterNotes:
      '**Charter rule:** Full corpus only. The 200-row P0-I pilot pattern is integration evidence, not a production intake substitute. Any waiver for partial corpus requires explicit operator charter amendment.',
  },
  {
    id: 'SPPC-04',
    num: '04',
    slug: 'normalization-and-canonical-registry',
    name: 'Normalization and Canonical Registry',
    purpose:
      'Normalize raw corpus rows into a canonical keyword registry with stable IDs, deduplicated surface forms, and traceable lineage to source rows.',
    owning: 'ORCA',
    participating: ['MIG (source lineage)', 'Operator (anomaly review)'],
    requiredInputs: [
      'SPPC-03 corpus_intake_complete token',
      'Full semantic corpus artifact',
      'Normalization ruleset version',
    ],
    optionalInputs: [
      'Legacy registry for merge-only comparison',
      'Operator synonym overrides',
    ],
    sourceOfTruth: [
      'ORCA canonical keyword registry is SoT for normalized demand entities.',
      'Every registry row must trace to one or more corpus source rows.',
      'Normalization ruleset version is frozen per registry generation.',
    ],
    processing: [
      'Apply normalization: casing, whitespace, punctuation, locale rules.',
      'Deduplicate surface forms; assign stable canonical IDs.',
      'Preserve lineage pointers to corpus and source registry.',
      'Flag anomalies (encoding, empty, ultra-short) to quarantine.',
      'Emit registry manifest for SPPC-05.',
    ],
    requiredOutputs: [
      'Canonical keyword registry (JSON)',
      'Normalization report: dedupe stats, quarantine count',
      'Ruleset version binding record',
    ],
    prohibitedOutputs: [
      'Commercial intent decisions (ACCEPT/REJECT)',
      'Campaign structure',
      'Tier assignments',
    ],
    validation: [
      'Registry row count ≤ corpus unique forms; lineage complete.',
      'No orphan registry rows without corpus pointer.',
      'Ruleset version documented.',
    ],
    blocking: [
      'SPPC-03 incomplete',
      'Lineage gaps above threshold',
      'Ruleset version missing',
    ],
    completionStatus: 'COMPLETE when registry committed and `registry_normalized` token issued.',
    evidence: [
      'Committed registry artifact',
      'Normalization report with counts',
      'Lineage spot-check sample',
    ],
    nextStages: ['SPPC-05'],
    rollback:
      'Ruleset change or corpus reopen forces registry regeneration; downstream admission invalidated.',
    role: 'ORCA semantic pipeline operator',
    operatorApproval: 'no',
    charterNotes: null,
  },
  {
    id: 'SPPC-05',
    num: '05',
    slug: 'commercial-intent-admission',
    name: 'Commercial Intent Admission',
    purpose:
      'Decide commercial fitness of each normalized keyword using ORCA Semantic Intelligence with mandatory ACCEPT, REJECT, or ABSTAIN outcomes. Regex or rule-only shortcuts are not final authority.',
    owning: 'ORCA Semantic Intelligence',
    participating: ['Operator (ABSTAIN resolution)', 'MIG (context)', 'Validators'],
    requiredInputs: [
      'SPPC-04 registry_normalized token',
      'Canonical keyword registry',
      'Admission policy pack version',
      'Business intake scope boundaries from SPPC-01',
    ],
    optionalInputs: [
      'Legacy commercial labels for disagreement audit',
      'Protected class definitions',
      'Operator pre-notes on edge cases',
    ],
    sourceOfTruth: [
      'Admission decision per keyword is SoT in registry extension — one of ACCEPT, REJECT, ABSTAIN only.',
      'Semantic Intelligence model/policy pack is authoritative; regex filters may pre-sort but never finalize.',
      'ABSTAIN rows require escalation ladder resolution before export paths.',
    ],
    processing: [
      'Run Semantic Intelligence admission scorer per registry row.',
      'Assign ACCEPT, REJECT, or ABSTAIN with confidence and rationale code.',
      'Route ABSTAIN to escalation ladder: auto-retry → operator queue → policy amendment.',
      'Block ACCEPT for rows failing protected-class or scope gates.',
      'Emit admission ledger for SPPC-06.',
    ],
    requiredOutputs: [
      'Admission ledger with ACCEPT / REJECT / ABSTAIN per keyword ID',
      'Escalation queue for ABSTAIN rows',
      'Policy pack version and model run metadata',
      'Disagreement audit vs legacy labels (if provided)',
    ],
    prohibitedOutputs: [
      'Binary pass/fail without ABSTAIN path',
      'Regex-only final decisions',
      'Silent promotion of ABSTAIN to ACCEPT',
      'Campaign keywords without admission status',
    ],
    validation: [
      '100% registry rows have exactly one of ACCEPT, REJECT, ABSTAIN.',
      'No ACCEPT without scope and protected-class check.',
      'Escalation ladder documented for every ABSTAIN.',
      'Policy pack version matches committed artifact.',
    ],
    blocking: [
      'SPPC-04 incomplete',
      'Any row missing admission decision',
      'ABSTAIN backlog above operator SLA without waiver',
      'Regex marked as sole authority in processing log',
    ],
    completionStatus:
      'COMPLETE when admission ledger committed, ABSTAIN queue routed, and `admission_complete` token issued.',
    evidence: [
      'Admission ledger artifact',
      'Escalation queue export',
      'REPORT with ACCEPT/REJECT/ABSTAIN distribution',
    ],
    nextStages: ['SPPC-06'],
    rollback:
      'Policy pack or intake scope change reopens admission; prior ACCEPT rows re-scored.',
    role: 'ORCA Semantic Intelligence operator; Operator for ABSTAIN resolution',
    operatorApproval: 'yes — required when ABSTAIN escalation reaches human queue',
    charterNotes:
      '**Charter rule:** ACCEPT / REJECT / ABSTAIN only. Escalation ladder: (1) auto-retry with alternate context, (2) operator review queue, (3) policy amendment charter. Regex and heuristics may assist routing but are **not** final admission authority.',
  },
  {
    id: 'SPPC-06',
    num: '06',
    slug: 'demand-priority-segmentation-t1-t5',
    name: 'Demand Priority Segmentation T1–T5',
    purpose:
      'Assign demand priority tiers T1 through T5 to ACCEPT-admitted keywords to drive budget, bid, and production sequencing without conflating tier with campaign structure.',
    owning: 'ORCA',
    participating: ['ORCA Semantic Intelligence', 'Operator (tier dispute resolution)'],
    requiredInputs: [
      'SPPC-05 admission_complete token',
      'Admission ledger (ACCEPT rows only)',
      'Tiering rubric version',
      'Business intake KPI and budget signals',
    ],
    optionalInputs: [
      'Historical conversion proxies',
      'Seasonal weighting notes',
    ],
    sourceOfTruth: [
      'Tier field on ACCEPT rows is SoT for demand priority.',
      'Each ACCEPT row carries exactly one tier T1–T5.',
      'REJECT and ABSTAIN rows carry no tier.',
    ],
    processing: [
      'Score ACCEPT rows against tiering rubric.',
      'Assign T1 (highest priority) through T5 (lowest priority).',
      'Document tie-break rules and manual overrides.',
      'Emit tier distribution report for SPPC-07.',
    ],
    requiredOutputs: [
      'Tier-augmented registry subset for ACCEPT rows',
      'Tier definitions binding document (embedded in contract)',
      'Distribution report: counts per tier',
    ],
    prohibitedOutputs: [
      'Campaign or ad group assignments',
      'Bid values',
      'Keywords without tier on ACCEPT rows',
    ],
    validation: [
      'Every ACCEPT row has exactly one tier T1–T5.',
      'Tier definitions match rubric version.',
      'No REJECT/ABSTAIN rows tiered.',
    ],
    blocking: [
      'SPPC-05 incomplete',
      'ACCEPT row missing tier',
      'Rubric version mismatch',
    ],
    completionStatus: 'COMPLETE when tier assignments committed and `tiers_assigned` token issued.',
    evidence: [
      'Tier-augmented artifact',
      'Distribution report',
      'Override log if any manual tier changes',
    ],
    nextStages: ['SPPC-07'],
    rollback: 'Rubric or admission reopen invalidates tiers; re-segment from SPPC-05 or SPPC-06 as scoped.',
    role: 'ORCA demand analyst',
    operatorApproval: 'no — yes only on documented tier dispute overrides',
    charterNotes: `**Charter rule — tier definitions:**
| Tier | Definition | Typical use |
|------|------------|-------------|
| **T1** | Core money intent — highest commercial fit, direct service match, operator-mandated must-win queries | Priority budget, first production wave, tight QA |
| **T2** | Strong commercial intent — clear buyer signal, minor ambiguity | Full production, standard bids |
| **T3** | Moderate intent — commercial but broader or comparative | Production with efficiency guardrails |
| **T4** | Exploratory intent — plausible demand, weaker conversion signal | Limited groups, test budgets |
| **T5** | Long-tail / reservoir — admitted but deprioritized; may be paused pre-launch | Hold or minimal presence unless strategy elevates |`,
  },
  {
    id: 'SPPC-07',
    num: '07',
    slug: 'service-and-meaning-ownership',
    name: 'Service and Meaning Ownership',
    purpose:
      'Bind each ACCEPT keyword to an owned service line, landing meaning, and offer surface so downstream clustering and ads do not invent product semantics.',
    owning: 'ORCA',
    participating: ['ATLAS (scope)', 'Operator (ownership disputes)', 'Website Factory (landing inventory)'],
    requiredInputs: [
      'SPPC-06 tiers_assigned token',
      'Tier-augmented ACCEPT registry',
      'Service catalog from intake',
      'Landing / offer inventory or SAFE UNKNOWN manifest',
    ],
    optionalInputs: [
      'Site intelligence pack',
      'Cross-sell rules',
    ],
    sourceOfTruth: [
      'Service ownership field per keyword is SoT for meaning routing.',
      'Unowned ACCEPT keywords block clustering and campaign production.',
      'Landing URL assignments are provisional until SPPC-17 alignment.',
    ],
    processing: [
      'Map each ACCEPT keyword to exactly one primary service owner.',
      'Attach meaning tags: intent class, offer type, geo modifier handling.',
      'Flag conflicts: keyword maps to multiple services or none.',
      'Emit ownership manifest for SPPC-08.',
    ],
    requiredOutputs: [
      'Service ownership manifest keyed by keyword ID',
      'Conflict report with resolution status',
      'Provisional landing pointers where known',
    ],
    prohibitedOutputs: [
      'Final ad copy',
      'Cluster IDs without ownership',
      'Invented services not in catalog',
    ],
    validation: [
      '100% ACCEPT rows have primary service owner or documented conflict in queue.',
      'No keyword with two primary owners without split rule.',
      'Service catalog version bound.',
    ],
    blocking: [
      'SPPC-06 incomplete',
      'Unresolved ownership conflicts above threshold',
      'Service catalog missing',
    ],
    completionStatus: 'COMPLETE when ownership manifest committed and `ownership_bound` token issued.',
    evidence: [
      'Ownership manifest artifact',
      'Conflict resolution log',
      'Service catalog version reference',
    ],
    nextStages: ['SPPC-08', 'SPPC-09'],
    rollback: 'Service catalog or intake change reopens ownership; clusters and negatives invalidated.',
    role: 'ORCA meaning architect; Operator for conflict resolution',
    operatorApproval: 'yes — when ownership conflicts reach human queue',
    charterNotes: null,
  },
  {
    id: 'SPPC-08',
    num: '08',
    slug: 'semantic-clustering',
    name: 'Semantic Clustering',
    purpose:
      'Group owned ACCEPT keywords into semantic clusters that will inform ad groups and message themes without collapsing distinct commercial meanings.',
    owning: 'ORCA',
    participating: ['ORCA Semantic Intelligence', 'Operator (cluster merges/splits)'],
    requiredInputs: [
      'SPPC-07 ownership_bound token',
      'Ownership manifest',
      'Clustering policy version',
    ],
    optionalInputs: [
      'Operator theme preferences',
      'Negative seed hints (non-binding)',
    ],
    sourceOfTruth: [
      'Cluster assignment per keyword is SoT for ad group candidacy.',
      'Clusters are scoped within service owner — no cross-service clusters without charter.',
      'Cluster IDs are stable for a given clustering policy version.',
    ],
    processing: [
      'Cluster keywords within each service owner partition.',
      'Enforce minimum and maximum cluster size policy.',
      'Label clusters with theme summary and representative queries.',
      'Flag singleton and mega-clusters for operator review.',
      'Emit cluster map for SPPC-14+.',
    ],
    requiredOutputs: [
      'Semantic cluster map (keyword ID → cluster ID)',
      'Cluster metadata: theme, service owner, tier histogram',
      'Review queue for edge clusters',
    ],
    prohibitedOutputs: [
      'Campaign or ad group IDs',
      'Final negatives list',
      'Ad headlines',
    ],
    validation: [
      'Every owned ACCEPT keyword in exactly one cluster per service partition.',
      'Cluster policy version documented.',
      'No cross-service cluster without waiver.',
    ],
    blocking: [
      'SPPC-07 incomplete',
      'Unclustered owned keywords',
      'Policy version missing',
    ],
    completionStatus: 'COMPLETE when cluster map committed and `clusters_locked` token issued.',
    evidence: [
      'Cluster map artifact',
      'Cluster statistics report',
      'Edge cluster review outcomes',
    ],
    nextStages: ['SPPC-09', 'SPPC-12'],
    rollback: 'Ownership or clustering policy change reopens SPPC-08; campaign architecture must wait.',
    role: 'ORCA clustering operator',
    operatorApproval: 'no — yes only for edge cluster merge/split decisions',
    charterNotes: null,
  },
  {
    id: 'SPPC-09',
    num: '09',
    slug: 'negative-keyword-intelligence',
    name: 'Negative Keyword Intelligence',
    purpose:
      'Produce negative keyword intelligence after admission and ownership are complete. Cross-route negative conflicts block Commander export until resolved.',
    owning: 'ORCA',
    participating: ['MIG (SERP context)', 'Validators', 'Operator (conflict resolution)'],
    requiredInputs: [
      'SPPC-05 admission_complete token',
      'SPPC-07 ownership_bound token',
      'SPPC-08 clusters_locked token (recommended)',
      'Cross-negative rules pack version',
      'REJECT keyword set from admission',
    ],
    optionalInputs: [
      'Competitor brand lists',
      'Operator negative seeds',
      'SPPC-10 SERP intelligence (when available)',
    ],
    sourceOfTruth: [
      'Negative matrix is SoT for what must not co-serve across routes.',
      'Negatives must not be finalized before admission and ownership — no pre-admission negative authority.',
      'Unresolved cross-route conflicts are hard blockers for SPPC-20 export.',
    ],
    processing: [
      'Generate campaign-level, group-level, and cross-route negatives from REJECT rows and rules.',
      'Build cross-negative conflict matrix across service owners and clusters.',
      'Flag conflicts where a positive in route A is negated incorrectly in route B.',
      'Require operator resolution for unresolved conflicts.',
      'Emit negative intelligence pack for SPPC-15 and SPPC-19.',
    ],
    requiredOutputs: [
      'Negative keyword intelligence pack',
      'Cross-negative conflict matrix with resolution status',
      'Rules pack version binding',
    ],
    prohibitedOutputs: [
      'Negatives computed before SPPC-05 admission',
      'Export-ready XLSX',
      'Silent suppression of conflict rows',
    ],
    validation: [
      'Admission and ownership tokens present in processing log.',
      'Conflict matrix built; zero unresolved conflicts for export path.',
      'Every negative traces to rule ID or REJECT admission row.',
    ],
    blocking: [
      'SPPC-05 or SPPC-07 incomplete',
      'Unresolved cross-negative conflicts',
      'Negatives generated on pre-admission snapshot',
    ],
    completionStatus:
      'COMPLETE when negative pack committed, conflicts resolved or waived, and `negatives_ready` token issued.',
    evidence: [
      'Negative intelligence pack artifact',
      'Conflict matrix with resolution audit',
      'REPORT confirming post-admission/ownership ordering',
    ],
    nextStages: ['SPPC-15', 'SPPC-19', 'SPPC-20'],
    rollback: 'Admission, ownership, or cluster change forces negative regeneration; export blocked until re-validated.',
    role: 'ORCA negative intelligence operator',
    operatorApproval: 'yes — required for conflict resolution and waivers',
    charterNotes:
      '**Charter rule:** Negative intelligence runs **after** commercial intent admission (SPPC-05) and service/meaning ownership (SPPC-07). Unresolved cross-route negative **conflicts block Commander export** (SPPC-20).',
  },
  {
    id: 'SPPC-10',
    num: '10',
    slug: 'daytime-paid-serp-intelligence',
    name: 'Daytime Paid SERP Intelligence',
    purpose:
      'Collect paid SERP snapshots during business hours via MIG PAID SERP BUSINESS HOURS mode to inform strategy, competitor cues, and ad format expectations. Degraded mode applies when collection is incomplete.',
    owning: 'MIG (mode: PAID SERP BUSINESS HOURS)',
    participating: ['ORCA (consumption)', 'Operator (degraded mode acceptance)'],
    requiredInputs: [
      'SPPC-02 sources_registered token',
      'Target query sample from ACCEPT registry or strategist slice',
      'Business hours window definition (timezone, weekdays)',
      'SERP provider configuration reference',
    ],
    optionalInputs: [
      'SPPC-08 cluster representatives',
      'Competitor domain watchlist',
    ],
    sourceOfTruth: [
      'Committed SERP snapshot pack is SoT for daytime paid landscape at capture time.',
      'Snapshots are time-stamped; stale SERP does not override fresh intake.',
      'Degraded mode flag is SoT when business-hours collection incomplete.',
    ],
    processing: [
      'Schedule captures within defined business hours window only.',
      'Record ad presence, formats, domains, and approximate positions.',
      'Tag queries missing SERP data or captured outside window.',
      'If coverage below threshold, emit degraded_mode manifest.',
      'Deliver SERP pack to SPPC-11 and SPPC-12 consumers.',
    ],
    requiredOutputs: [
      'Daytime paid SERP snapshot pack',
      'Coverage report: queries captured vs planned',
      'degraded_mode flag (true/false) with reason codes',
    ],
    prohibitedOutputs: [
      'Campaign structure decisions',
      'Final bid recommendations',
      'SERP data presented as 24/7 representative without disclaimer',
    ],
    validation: [
      'Capture timestamps fall within business hours window or flagged exception.',
      'Coverage metrics computed and attached.',
      'Degraded mode explicitly set when coverage incomplete.',
    ],
    blocking: [
      'SPPC-02 incomplete',
      'Zero captures without degraded mode declaration',
      'Business hours window undefined',
    ],
    completionStatus:
      'COMPLETE when SERP pack committed and `serp_intelligence_ready` or `serp_degraded_mode` token issued.',
    evidence: [
      'SERP snapshot pack path',
      'Coverage and hours compliance report',
      'Degraded mode operator acknowledgment if applicable',
    ],
    nextStages: ['SPPC-11', 'SPPC-12'],
    rollback: 'Re-capture opens SPPC-10 only; analytical pack consumers must refresh bindings.',
    role: 'MIG SERP operator',
    operatorApproval: 'yes — when degraded_mode requires strategic acceptance',
    charterNotes:
      '**Charter rule:** Paid SERP collection runs in **business hours mode** only. If captures are missing or below coverage threshold, system enters **degraded mode** — downstream stages may proceed only with operator acknowledgment and degraded_mode flag on SPPC-12 pack.',
  },
  {
    id: 'SPPC-11',
    num: '11',
    slug: 'competitor-advertising-audit',
    name: 'Competitor Advertising Audit',
    purpose:
      'Audit competitor advertising presence, messaging patterns, and offer positioning using MIG research outputs to inform strategy without copying non-compliant claims.',
    owning: 'MIG',
    participating: ['ORCA (strategy consumption)', 'Operator (compliance review)'],
    requiredInputs: [
      'SPPC-02 sources_registered token',
      'Competitor domain / advertiser list',
      'SPPC-10 SERP pack (when available)',
      'Intake compliance boundaries',
    ],
    optionalInputs: [
      'Historical competitor exports',
      'Operator anecdotal notes',
    ],
    sourceOfTruth: [
      'Competitor audit artifact is SoT for observed competitor ads at audit time.',
      'Audit is observational — not authorization to copy claims.',
      'Compliance filter from intake overrides attractive competitor copy.',
    ],
    processing: [
      'Identify competitor ads for scoped queries and domains.',
      'Extract themes, offers, CTAs, and landing patterns (observational).',
      'Flag compliance risks vs intake prohibited claims.',
      'Summarize whitespace and saturation signals.',
      'Emit audit pack for SPPC-12.',
    ],
    requiredOutputs: [
      'Competitor advertising audit document',
      'Domain-level summary tables',
      'Compliance risk flags',
    ],
    prohibitedOutputs: [
      'Plagiarized ad copy ready for paste',
      'Unauthorized trademark use recommendations',
      'Campaign export artifacts',
    ],
    validation: [
      'Competitor list matches intake scope.',
      'Compliance flags present for risky patterns.',
      'Audit date stamped.',
    ],
    blocking: [
      'SPPC-02 incomplete',
      'Empty competitor list without SAFE UNKNOWN waiver',
    ],
    completionStatus: 'COMPLETE when audit committed and `competitor_audit_ready` token issued.',
    evidence: [
      'Audit artifact path',
      'Competitor list version',
      'Compliance review note',
    ],
    nextStages: ['SPPC-12'],
    rollback: 'Competitor list change reopens audit; SPPC-12 pack section must refresh.',
    role: 'MIG competitive research lead',
    operatorApproval: 'no',
    charterNotes: null,
  },
  {
    id: 'SPPC-12',
    num: '12',
    slug: 'dated-analytical-pack',
    name: 'Dated Analytical Pack',
    purpose:
      'Assemble a single dated cross-system analytical pack that binds semantic, SERP, competitor, and tier signals for strategy — the mandatory input to AI PPC Strategist.',
    owning: 'Cross-system (ORCA lead assembly)',
    participating: ['MIG', 'ORCA', 'ORCA Semantic Intelligence', 'Operator (pack approval)'],
    requiredInputs: [
      'SPPC-06 tiers_assigned token',
      'SPPC-08 clusters_locked token',
      'SPPC-09 negatives_ready token (or in-progress with flag)',
      'SPPC-10 serp_intelligence_ready or serp_degraded_mode token',
      'SPPC-11 competitor_audit_ready token',
    ],
    optionalInputs: [
      'Budget scenarios from operator',
      'Historical performance SAFE UNKNOWN declarations',
    ],
    sourceOfTruth: [
      'Dated analytical pack with embedded as-of date is SoT for strategy session inputs.',
      'Pack sections are authoritative only at pack version — not live registry edits.',
      'degraded_mode from SPPC-10 must appear in pack metadata when active.',
    ],
    processing: [
      'Assemble required sections into versioned pack.',
      'Stamp as-of date and source artifact versions.',
      'Compute executive summary metrics.',
      'Flag stale or missing sections.',
      'Emit pack for SPPC-13.',
    ],
    requiredOutputs: [
      'Dated analytical pack document (markdown + machine-readable index)',
      'Pack manifest listing section sources and versions',
      'Executive summary metrics sheet',
    ],
    prohibitedOutputs: [
      'Campaign architecture decisions',
      'Commander export files',
      'Strategy without dated pack reference',
    ],
    validation: [
      'All required sections present or explicitly marked MISSING with waiver.',
      'As-of date and pack version unique.',
      'Source artifact versions match committed paths.',
    ],
    blocking: [
      'SPPC-06 or SPPC-08 incomplete',
      'SPPC-10 token missing entirely',
      'Pack assembled without date stamp',
    ],
    completionStatus: 'COMPLETE when pack committed and `analytical_pack_dated` token issued.',
    evidence: [
      'Committed pack path',
      'Manifest with section checklist',
      'Operator approval on degraded sections if applicable',
    ],
    nextStages: ['SPPC-13'],
    rollback: 'Any source stage reopen forces new pack version; strategist must re-bind.',
    role: 'ORCA assembly lead; Operator pack sign-off',
    operatorApproval: 'yes — pack completeness and degraded SERP acknowledgment',
    charterNotes: `**Charter rule — required pack sections:**
1. **Pack metadata** — as-of date, version, intake binding, degraded_mode flags
2. **Demand summary** — corpus scale, admission distribution, tier histogram
3. **Service ownership map** — counts and conflicts resolved
4. **Semantic clusters** — cluster catalog with tier and service binding
5. **Negative intelligence summary** — conflict status, unresolved blockers
6. **Daytime paid SERP** — coverage, business hours compliance, degraded notes
7. **Competitor audit** — domain summaries and compliance flags
8. **Executive metrics** — T1–T5 counts, ACCEPT rate, ABSTAIN backlog, key risks
9. **Strategy input index** — pointers for SPPC-13 gates`,
  },
  {
    id: 'SPPC-13',
    num: '13',
    slug: 'ai-ppc-strategist',
    name: 'AI PPC Strategist',
    purpose:
      'Produce a human-reviewed PPC strategy from the dated analytical pack. Strategy gates must pass before campaign production; jumping directly to Commander export is forbidden.',
    owning: 'AI PPC Strategist',
    participating: ['Operator', 'ORCA', 'Campaign Production (read-only)'],
    requiredInputs: [
      'SPPC-12 analytical_pack_dated token',
      'Dated analytical pack artifact',
      'Intake budget and KPI constraints',
    ],
    optionalInputs: [
      'Operator strategic priorities',
      'Brand positioning notes',
    ],
    sourceOfTruth: [
      'Approved strategy document is SoT for campaign architecture intent.',
      'Strategy version binds to analytical pack version — no orphan strategies.',
      'Forbidden: Commander export or XLSX generation before strategy gates pass.',
    ],
    processing: [
      'Ingest dated analytical pack sections.',
      'Propose campaign topology, budget split, tier emphasis, and risk posture.',
      'Run strategy gates: pack freshness, admission completeness, negative conflict status, degraded SERP acknowledgment.',
      'Submit strategy for operator review.',
      'On approval, emit strategy authorization for SPPC-14.',
    ],
    requiredOutputs: [
      'PPC strategy document with version ID',
      'Strategy gate checklist (pass/fail per gate)',
      'Budget and tier emphasis recommendations',
      'Explicit non-goals and hold lists',
    ],
    prohibitedOutputs: [
      'Commander XLSX or export bundles',
      'Keyword-level final bids without architecture stage',
      'Strategy referencing undated or pilot corpus',
      'Bypass of SPPC-14–19 production stages',
    ],
    validation: [
      'All strategy gates documented PASS or waived with operator sign-off.',
      'Pack version ID matches SPPC-12 manifest.',
      'No export artifacts in strategist output directory.',
    ],
    blocking: [
      'SPPC-12 incomplete',
      'Any mandatory strategy gate FAIL without waiver',
      'Attempt to jump to SPPC-20',
      'Unresolved negative conflicts (from pack)',
    ],
    completionStatus: 'COMPLETE when strategy approved and `strategy_authorized` token issued.',
    evidence: [
      'Strategy document path',
      'Gate checklist artifact',
      'Operator approval timestamp',
    ],
    nextStages: ['SPPC-14'],
    rollback: 'Pack refresh or intake change invalidates strategy; production stages halt.',
    role: 'AI PPC Strategist operator; Operator approver',
    operatorApproval: 'yes',
    charterNotes:
      '**Charter rule:** Strategy gates must pass before campaign production. **Forbidden:** direct jumps from strategist output to Commander export (SPPC-20). Production path is SPPC-14 → … → SPPC-19 → SPPC-20.',
  },
  {
    id: 'SPPC-14',
    num: '14',
    slug: 'campaign-architecture',
    name: 'Campaign Architecture',
    purpose:
      'Translate authorized strategy into campaign topology: campaigns, directions, and group shells aligned to clusters and service owners.',
    owning: 'Campaign Production',
    participating: ['ORCA (cluster binding)', 'QA (structure review)'],
    requiredInputs: [
      'SPPC-13 strategy_authorized token',
      'Approved strategy document',
      'SPPC-08 cluster map',
      'SPPC-07 ownership manifest',
    ],
    optionalInputs: [
      'Platform-specific naming conventions',
      'Historical campaign naming',
    ],
    sourceOfTruth: [
      'Campaign architecture artifact is SoT for structural IDs.',
      'Architecture must trace to strategy version and cluster map version.',
      'No keyword or ad content at this stage — structure only.',
    ],
    processing: [
      'Define campaigns aligned to strategy budget split.',
      'Map clusters to ad group shells within service partitions.',
      'Assign directional labels and platform metadata.',
      'Validate structure against strategy non-goals.',
      'Emit architecture manifest for SPPC-15.',
    ],
    requiredOutputs: [
      'Campaign architecture manifest (campaign / direction / group shells)',
      'Cluster-to-group mapping table',
      'Architecture validation report',
    ],
    prohibitedOutputs: [
      'Populated keyword rows',
      'Ad copy',
      'Bids or budgets as final values',
      'XLSX export',
    ],
    validation: [
      'Every in-scope cluster maps to exactly one group shell or documented split.',
      'Strategy version bound.',
      'No orphan group shells.',
    ],
    blocking: [
      'SPPC-13 incomplete',
      'Cluster map version mismatch',
      'Strategy non-goals violated',
    ],
    completionStatus: 'COMPLETE when architecture committed and `architecture_locked` token issued.',
    evidence: [
      'Architecture manifest path',
      'Mapping validation report',
    ],
    nextStages: ['SPPC-15'],
    rollback: 'Strategy or cluster change reopens architecture; downstream distribution cleared.',
    role: 'Campaign Production architect',
    operatorApproval: 'no',
    charterNotes: null,
  },
  {
    id: 'SPPC-15',
    num: '15',
    slug: 'keyword-and-negative-distribution',
    name: 'Keyword and Negative Distribution',
    purpose:
      'Distribute ACCEPT keywords and negative intelligence into architecture group shells with match types and cross-route negatives attached.',
    owning: 'Campaign Production',
    participating: ['ORCA', 'Validators'],
    requiredInputs: [
      'SPPC-14 architecture_locked token',
      'SPPC-09 negatives_ready token',
      'Architecture manifest',
      'Tier-augmented ACCEPT registry',
      'Negative intelligence pack',
    ],
    optionalInputs: [
      'Match type policy overrides',
      'Operator hold list from strategy',
    ],
    sourceOfTruth: [
      'Distribution ledger is SoT for which keyword lives in which group with which match type.',
      'Negatives must match SPPC-09 pack version or newer resolved version.',
      'No keyword distribution without architecture binding.',
    ],
    processing: [
      'Place ACCEPT keywords into group shells per cluster map.',
      'Apply match type policy by tier and strategy.',
      'Attach group and campaign negatives from intelligence pack.',
      'Validate no positive/negative self-conflicts at group level.',
      'Emit distribution ledger for SPPC-16.',
    ],
    requiredOutputs: [
      'Keyword distribution ledger',
      'Negative attachment manifest',
      'Distribution validation report',
    ],
    prohibitedOutputs: [
      'Ad copy',
      'Final bid values',
      'Export XLSX',
      'Keywords in groups without architecture ID',
    ],
    validation: [
      'No ACCEPT keyword unassigned unless on strategy hold list.',
      'Negative pack version ≥ SPPC-09 committed version.',
      'No unresolved cross-route conflicts.',
    ],
    blocking: [
      'SPPC-14 or SPPC-09 incomplete',
      'Cross-negative conflicts unresolved',
      'Architecture token missing',
    ],
    completionStatus: 'COMPLETE when ledger committed and `distribution_complete` token issued.',
    evidence: [
      'Distribution ledger path',
      'Validation report',
      'Negative version binding',
    ],
    nextStages: ['SPPC-16', 'SPPC-19'],
    rollback: 'Architecture, negatives, or admission reopen forces redistribution.',
    role: 'Campaign Production keyword lead',
    operatorApproval: 'no',
    charterNotes: null,
  },
  {
    id: 'SPPC-16',
    num: '16',
    slug: 'ad-production',
    name: 'Ad Production',
    purpose:
      'Produce compliant ad copy variants per group shell following strategy tone, intake compliance, and platform format limits.',
    owning: 'Campaign Production',
    participating: ['QA (copy compliance)', 'Operator (brand voice)'],
    requiredInputs: [
      'SPPC-15 distribution_complete token',
      'Distribution ledger',
      'Intake compliance and brand rules',
      'Strategy tone and offer guidance',
    ],
    optionalInputs: [
      'Approved copy templates',
      'A/B variant count policy',
    ],
    sourceOfTruth: [
      'Ad copy artifact is SoT for headlines, descriptions, and display paths.',
      'Copy must reference group IDs from distribution ledger.',
      'Compliance rules from intake override creative preference.',
    ],
    processing: [
      'Draft ads per group with required format fields.',
      'Run compliance lint against intake prohibitions.',
      'Ensure uniqueness constraints per platform rules.',
      'Attach final URLs as provisional pending SPPC-17.',
      'Emit ad copy pack for SPPC-17 and SPPC-19.',
    ],
    requiredOutputs: [
      'Ad copy pack keyed by group ID',
      'Compliance lint report',
      'Provisional URL map',
    ],
    prohibitedOutputs: [
      'Non-compliant claims from competitor audit',
      'Export XLSX',
      'Ads without group binding',
    ],
    validation: [
      'Every active group has ≥1 compliant ad variant.',
      'Compliance lint PASS or waived with operator sign-off.',
      'Character limits satisfied per platform spec.',
    ],
    blocking: [
      'SPPC-15 incomplete',
      'Compliance lint FAIL without waiver',
      'Missing ads for in-scope groups',
    ],
    completionStatus: 'COMPLETE when ad pack committed and `ads_produced` token issued.',
    evidence: [
      'Ad copy pack path',
      'Compliance lint artifact',
    ],
    nextStages: ['SPPC-17', 'SPPC-19'],
    rollback: 'Distribution or compliance rule change reopens ad production for affected groups.',
    role: 'Campaign Production copy lead',
    operatorApproval: 'no — yes for compliance waivers only',
    charterNotes: null,
  },
  {
    id: 'SPPC-17',
    num: '17',
    slug: 'landing-and-offer-alignment',
    name: 'Landing and Offer Alignment',
    purpose:
      'Align final URLs, offers, and landing messaging with ads and service ownership so click paths deliver coherent commercial promises.',
    owning: 'QA / Campaign Production',
    participating: ['Website Factory', 'Operator', 'ORCA (ownership)'],
    requiredInputs: [
      'SPPC-16 ads_produced token',
      'Ad copy pack with provisional URLs',
      'SPPC-07 ownership manifest',
      'Landing inventory or published site map',
    ],
    optionalInputs: [
      'UTM policy',
      'Offer variant tests',
    ],
    sourceOfTruth: [
      'URL alignment manifest is SoT for final landing URLs per group/ad.',
      'Offer claims on landing must match ad promises within intake tolerance.',
      'Misaligned groups block QA and export.',
    ],
    processing: [
      'Resolve provisional URLs to production or staging finals.',
      'Verify offer parity: service, geo, price signals vs ads.',
      'Apply UTM and tracking parameters per policy.',
      'Flag broken links, mismatched offers, or missing landings.',
      'Emit alignment manifest for SPPC-19.',
    ],
    requiredOutputs: [
      'Landing and offer alignment manifest',
      'URL verification report',
      'Mismatch resolution log',
    ],
    prohibitedOutputs: [
      'Export XLSX',
      'Silent use of homepage fallback without flag',
      'New offer claims not in intake',
    ],
    validation: [
      'All active ads have verified final URL.',
      'No unresolved offer mismatches.',
      'Tracking parameters policy-compliant.',
    ],
    blocking: [
      'SPPC-16 incomplete',
      'Broken URLs without waiver',
      'Offer mismatch above threshold',
    ],
    completionStatus: 'COMPLETE when alignment manifest committed and `landing_aligned` token issued.',
    evidence: [
      'Alignment manifest path',
      'URL verification report',
      'Mismatch resolutions',
    ],
    nextStages: ['SPPC-18', 'SPPC-19'],
    rollback: 'Site publish or offer change reopens alignment for affected groups.',
    role: 'QA landing lead',
    operatorApproval: 'yes — for offer mismatch waivers',
    charterNotes: null,
  },
  {
    id: 'SPPC-18',
    num: '18',
    slug: 'bidding-and-budget-strategy',
    name: 'Bidding and Budget Strategy',
    purpose:
      'Define bidding approach and budget allocation per campaign with explicit manual vs automated branch selection and tier-weighted emphasis.',
    owning: 'Campaign Production',
    participating: ['Operator', 'AI PPC Strategist (budget alignment)'],
    requiredInputs: [
      'SPPC-13 strategy_authorized token',
      'SPPC-14 architecture_locked token',
      'SPPC-06 tier assignments',
      'Intake budget envelope',
    ],
    optionalInputs: [
      'Platform automated bidding eligibility',
      'Historical CPC SAFE UNKNOWN notes',
    ],
    sourceOfTruth: [
      'Bidding strategy artifact is SoT for bid mode and budget splits.',
      'Branch selection (manual vs automated) must be explicit per campaign.',
      'Placeholder bids in export are not final — operator calibrates in platform unless automated branch authorized.',
    ],
    processing: [
      'Allocate budget across campaigns per strategy.',
      'Select manual or automated bidding branch per campaign with rationale.',
      'Apply tier weights to initial bid guidance.',
      'Document calibration expectations for manual branch.',
      'Emit bidding manifest for SPPC-19 and SPPC-20.',
    ],
    requiredOutputs: [
      'Bidding and budget strategy manifest',
      'Manual vs automated branch declaration per campaign',
      'Initial bid guidance table (placeholders allowed for manual)',
    ],
    prohibitedOutputs: [
      'Silent default to automated without declaration',
      'Budget exceeding intake envelope without waiver',
      'Final live bids presented as committed without operator calibration note',
    ],
    validation: [
      'Every campaign has branch selection and budget line.',
      'Total budget ≤ intake envelope or waiver on record.',
      'Tier weights documented.',
    ],
    blocking: [
      'SPPC-13 or SPPC-14 incomplete',
      'Missing branch selection',
      'Budget overrun without waiver',
    ],
    completionStatus: 'COMPLETE when bidding manifest committed and `bidding_strategy_locked` token issued.',
    evidence: [
      'Bidding manifest path',
      'Branch selection audit',
      'Budget sum reconciliation',
    ],
    nextStages: ['SPPC-19', 'SPPC-20'],
    rollback: 'Strategy or budget envelope change reopens bidding; export waits for re-lock.',
    role: 'Campaign Production budget lead; Operator for envelope waivers',
    operatorApproval: 'yes — automated branch and budget envelope exceptions',
    charterNotes:
      '**Charter rule:** Explicit **manual vs automated** branch per campaign. Manual branch expects operator calibration post-import; automated branch requires platform eligibility and operator authorization.',
  },
  {
    id: 'SPPC-19',
    num: '19',
    slug: 'campaign-qa',
    name: 'Campaign QA',
    purpose:
      'Run validators across architecture, keywords, negatives, ads, landing alignment, and bidding before any Commander export. QA failure blocks SPPC-20.',
    owning: 'QA / Validators',
    participating: ['Campaign Production', 'ORCA', 'Operator'],
    requiredInputs: [
      'SPPC-15 distribution_complete token',
      'SPPC-16 ads_produced token',
      'SPPC-17 landing_aligned token',
      'SPPC-18 bidding_strategy_locked token',
      'SPPC-09 negatives_ready token',
      'Validator ruleset version',
    ],
    optionalInputs: [
      'Spot-check query list from operator',
      'Prior QA failure remediations',
    ],
    sourceOfTruth: [
      'QA report with pass/fail per rule is SoT for export eligibility.',
      'Validators assist humans — failures require remediation or operator waiver.',
      'No export when mandatory rules fail.',
    ],
    processing: [
      'Run structural validation against architecture manifest.',
      'Validate keyword/negative consistency and cross-route matrix.',
      'Lint ads for compliance and format.',
      'Verify URL alignment and tracking.',
      'Check bidding manifest completeness.',
      'Emit QA report with export_ready boolean.',
    ],
    requiredOutputs: [
      'Campaign QA report (rule-level pass/fail)',
      'export_ready flag',
      'Remediation ticket list for failures',
    ],
    prohibitedOutputs: [
      'Commander XLSX (reserved for SPPC-20)',
      'Launch authorization',
      'QA pass without evidence logs',
    ],
    validation: [
      'All mandatory validator rules executed.',
      'export_ready true only when zero mandatory failures or waivers documented.',
      'Artifact versions match production ledger.',
    ],
    blocking: [
      'Any upstream production token missing',
      'Mandatory QA rule FAIL',
      'Unresolved negative conflicts',
      'export_ready false',
    ],
    completionStatus: 'COMPLETE when QA report committed with export_ready true and `qa_passed` token issued.',
    evidence: [
      'QA report path',
      'Validator ruleset version',
      'Waiver log if applicable',
    ],
    nextStages: ['SPPC-20'],
    rollback: 'Any production artifact change reopens QA; export_ready revoked.',
    role: 'QA validator operator',
    operatorApproval: 'yes — for mandatory rule waivers',
    charterNotes: null,
  },
  {
    id: 'SPPC-20',
    num: '20',
    slug: 'commander-export',
    name: 'Commander Export',
    purpose:
      'Generate Yandex Direct Commander transport XLSX from validated production artifacts. Export is transport-only — no semantic or strategic decisions at this stage.',
    owning: 'Commander Export',
    participating: ['Campaign Production (source artifacts)', 'Validators (pre-export gate)'],
    requiredInputs: [
      'SPPC-19 qa_passed token with export_ready true',
      'Architecture, distribution, ad, alignment, and bidding manifests',
      'Commander template version',
      'Exporter tool version',
    ],
    optionalInputs: [
      'Operator spot-check sample size',
    ],
    sourceOfTruth: [
      'Production JSON/manifests remain SoT for meaning; XLSX is disposable transport snapshot.',
      'Exporter maps fields — it does not invent keywords, negatives, or copy.',
      'Template version and exporter version must be recorded on every export.',
    ],
    processing: [
      'Verify SPPC-19 export_ready and SPPC-09 conflict-free status.',
      'Run exporter CLI against bound artifact bundle.',
      'Run transport validation (duplicates, sheet split, hygiene).',
      'Stamp export manifest with versions and checksum.',
      'Hand off XLSX to SPPC-21 — no launch.',
    ],
    requiredOutputs: [
      'Commander XLSX transport file',
      'Export manifest: template version, exporter version, checksum',
      'Transport validation log',
    ],
    prohibitedOutputs: [
      'Semantic reclassification or tier changes',
      'New keywords or ads not in production manifests',
      'Launch or budget activation',
      'Export without qa_passed token',
      'Strategic decisions embedded in exporter run',
    ],
    validation: [
      'qa_passed and export_ready true.',
      'Transport validation PASS.',
      'Checksum recorded; row counts reconcile with manifests.',
      'Export log explicitly marks transport-only role.',
    ],
    blocking: [
      'SPPC-19 incomplete or export_ready false',
      'SPPC-09 unresolved conflicts',
      'Transport validation FAIL',
      'Attempt to export from undated strategy or pilot corpus',
    ],
    completionStatus: 'COMPLETE when XLSX and export manifest committed and `export_transport_ready` token issued.',
    evidence: [
      'XLSX path (gitignored acceptable) + export manifest in repo',
      'Transport validation log',
      'Exporter and template version IDs',
    ],
    nextStages: ['SPPC-21'],
    rollback: 'Any production artifact change invalidates export; regenerate from SPPC-19.',
    role: 'Commander Export operator',
    operatorApproval: 'no',
    charterNotes:
      '**Charter rule:** Commander Export is **transport only**. It maps validated manifests to XLSX — no admission decisions, no strategy changes, no negative invention. Meaning SoT remains ORCA production artifacts.',
  },
  {
    id: 'SPPC-21',
    num: '21',
    slug: 'dry-run-and-operator-approval',
    name: 'Dry Run and Operator Approval',
    purpose:
      'Operator reviews campaign readiness at the correct abstraction — campaigns, groups, strategy risks, and QA summary — not line-by-line approval of every keyword.',
    owning: 'Operator',
    participating: ['QA', 'Campaign Production', 'Commander Export'],
    requiredInputs: [
      'SPPC-20 export_transport_ready token',
      'Commander XLSX and export manifest',
      'SPPC-19 QA report',
      'SPPC-13 strategy document',
      'Dry-run checklist',
    ],
    optionalInputs: [
      'Spot-check keyword samples',
      'Simulated import preview screenshots',
    ],
    sourceOfTruth: [
      'Operator approval record is SoT for authorization to import.',
      'Approval binds to export manifest checksum — different XLSX requires re-approval.',
      'Approval granularity: campaign/group/strategy level — not per-keyword unless escalated.',
    ],
    processing: [
      'Import dry-run or sandbox preview where platform allows.',
      'Review QA summary, tier emphasis, budget split, and negative conflict status.',
      'Spot-check representative groups — not full keyword enumeration.',
      'Record approve / hold / reject with rationale.',
      'On approve, emit import_authorized token for SPPC-22.',
    ],
    requiredOutputs: [
      'Operator approval record with checksum binding',
      'Dry-run checklist completed',
      'Hold or reject tickets if not approved',
    ],
    prohibitedOutputs: [
      'Per-keyword mandatory sign-off grid as default gate',
      'Launch without explicit import_authorized',
      'Approval of different checksum than export manifest',
    ],
    validation: [
      'Approval record references export manifest checksum.',
      'Dry-run checklist complete.',
      'Strategy and QA artifacts version-bound.',
    ],
    blocking: [
      'SPPC-20 incomplete',
      'Checksum mismatch vs approval record',
      'QA export_ready false',
      'Operator reject without remediation plan',
    ],
    completionStatus: 'COMPLETE when operator approves and `import_authorized` token issued.',
    evidence: [
      'Signed approval record',
      'Dry-run checklist artifact',
      'Checksum match audit',
    ],
    nextStages: ['SPPC-22'],
    rollback: 'New export or production change revokes import_authorized; return to SPPC-19 or SPPC-20.',
    role: 'Operator (account owner)',
    operatorApproval: 'yes',
    charterNotes:
      '**Charter rule:** Operator approval at the **right abstraction** — campaigns, budget, risk summary, QA pass, representative spot checks. **Not** mandatory approval of every individual keyword.',
  },
  {
    id: 'SPPC-22',
    num: '22',
    slug: 'import-and-launch',
    name: 'Import and Launch',
    purpose:
      'Human operator imports Commander XLSX into Yandex Direct and activates campaigns per bidding branch — platform actions are never agent-automated.',
    owning: 'Operator / Platform',
    participating: ['Commander Export (support)', 'QA (post-import smoke)'],
    requiredInputs: [
      'SPPC-21 import_authorized token',
      'Commander XLSX matching approved checksum',
      'Platform account access (out of repo)',
      'Bidding branch manifest from SPPC-18',
    ],
    optionalInputs: [
      'Import session notes',
      'Calibration bid sheet for manual branch',
    ],
    sourceOfTruth: [
      'Platform campaign IDs after import are SoT for live state — recorded in launch log.',
      'Repo artifacts remain pre-launch SoT for intended structure until import confirms.',
      'Launch timestamps and operator identity required in launch log.',
    ],
    processing: [
      'Import XLSX via Commander with checksum verification.',
      'Calibrate bids if manual branch selected.',
      'Verify negatives live in platform.',
      'Activate campaigns per strategy schedule.',
      'Run post-import smoke checks.',
      'Record platform IDs and launch status.',
    ],
    requiredOutputs: [
      'Launch log with platform campaign IDs',
      'Post-import smoke report',
      'Import session record with operator identity',
    ],
    prohibitedOutputs: [
      'Agent-automated platform API launch without operator',
      'Import of non-approved checksum',
      'Silent partial launch without log',
    ],
    validation: [
      'import_authorized token present.',
      'Checksum matches SPPC-21 approval.',
      'Smoke checks PASS or waived.',
      'Manual branch calibration documented if applicable.',
    ],
    blocking: [
      'SPPC-21 incomplete',
      'Checksum mismatch',
      'Smoke FAIL on critical rules',
    ],
    completionStatus: 'COMPLETE when campaigns live (or staged per strategy) and `launch_recorded` token issued.',
    evidence: [
      'Launch log path',
      'Smoke report',
      'Screenshots or platform export reference (out of repo acceptable)',
    ],
    nextStages: ['SPPC-23'],
    rollback: 'Pause or rollback in platform is operator action; repo launch log updated with status change — does not auto-regenerate export.',
    role: 'Operator platform lead',
    operatorApproval: 'yes',
    charterNotes: null,
  },
  {
    id: 'SPPC-23',
    num: '23',
    slug: 'post-launch-learning',
    name: 'Post-Launch Learning',
    purpose:
      'Capture performance signals, search term insights, and semantic feedback loops after launch to inform future cycles without mutating frozen launch artifacts.',
    owning: 'Post-Launch Learning',
    participating: ['MIG', 'ORCA', 'Operator', 'AI PPC Strategist'],
    requiredInputs: [
      'SPPC-22 launch_recorded token',
      'Launch log with platform IDs',
      'Performance export schedule',
      'Intake KPI definitions',
    ],
    optionalInputs: [
      'Search terms reports',
      'Conversion data SAFE UNKNOWN handling',
      'Operator qualitative notes',
    ],
    sourceOfTruth: [
      'Post-launch learning pack is SoT for observations after launch — separate version line from pre-launch production artifacts.',
      'Learning outputs do not retroactively edit SPPC-03–20 committed artifacts.',
      'New cycle requires charter for reopen from appropriate stage.',
    ],
    processing: [
      'Collect scheduled performance and search term exports.',
      'Identify tier performance drift, negative gaps, and new query candidates.',
      'Propose learnings and reopen recommendations — not silent mutation.',
      'Feed insights to future SPPC-12 pack or operator review.',
      'Emit learning pack with dated observations.',
    ],
    requiredOutputs: [
      'Post-launch learning pack (dated)',
      'Reopen recommendations with target stage pointers',
      'KPI tracking sheet vs intake targets',
    ],
    prohibitedOutputs: [
      'Retroactive edit of launch export manifests',
      'Automatic keyword admission without new SPPC-05 cycle',
      'Autonomous budget changes in platform',
    ],
    validation: [
      'Launch log bound.',
      'Learning pack dated and versioned.',
      'Reopen recommendations cite target SPPC stage — no vague "fix in export".',
    ],
    blocking: [
      'SPPC-22 incomplete',
      'Learning pack without date',
    ],
    completionStatus: 'ONGOING — initial pack due per schedule; `learning_active` token after first pack.',
    evidence: [
      'Learning pack path',
      'Performance export references',
      'Reopen recommendation log',
    ],
    nextStages: ['SPPC-12 (new cycle)', 'SPPC-05 (new queries)', 'SPPC-01 (scope change)'],
    rollback:
      'Learning is append-only. Reopen of prior stages follows explicit operator charter — not automatic from learning pack.',
    role: 'Post-launch analyst; Operator sponsor',
    operatorApproval: 'yes — for reopen recommendations and new cycle charters',
    charterNotes: null,
  },
];

function bulletList(items) {
  return items.map((item) => `- ${item}`).join('\n');
}

function renderStage(stage) {
  const lines = [
    `# ${stage.id} — ${stage.name}`,
    '',
    '**Lifecycle:** MARS Search PPC Production v1',
    `**Stage file:** \`${stage.id}-${stage.slug}.md\``,
    '',
    '---',
    '',
    '## Stage ID',
    '',
    stage.id,
    '',
    '## Name',
    '',
    stage.name,
    '',
    '## Purpose',
    '',
    stage.purpose,
    '',
    '## Owning system',
    '',
    stage.owning,
    '',
    '## Participating systems',
    '',
    bulletList(stage.participating),
    '',
    '## Required inputs',
    '',
    bulletList(stage.requiredInputs),
    '',
    '## Optional inputs',
    '',
    bulletList(stage.optionalInputs),
    '',
    '## Source-of-truth rules',
    '',
    bulletList(stage.sourceOfTruth),
    '',
    '## Required processing',
    '',
    bulletList(stage.processing),
    '',
    '## Required outputs',
    '',
    bulletList(stage.requiredOutputs),
    '',
    '## Prohibited outputs',
    '',
    bulletList(stage.prohibitedOutputs),
    '',
    '## Validation rules',
    '',
    bulletList(stage.validation),
    '',
    '## Blocking conditions',
    '',
    bulletList(stage.blocking),
    '',
    '## Completion status',
    '',
    stage.completionStatus,
    '',
    '## Evidence requirements',
    '',
    bulletList(stage.evidence),
    '',
    '## Next allowed stages',
    '',
    bulletList(stage.nextStages),
    '',
    '## Rollback / reopen behavior',
    '',
    stage.rollback,
    '',
    '## Responsible role',
    '',
    stage.role,
    '',
    '## Operator approval required',
    '',
    stage.operatorApproval,
    '',
  ];

  if (stage.charterNotes) {
    lines.push('## Charter notes', '', stage.charterNotes, '');
  }

  return lines.join('\n');
}

function renderReadme() {
  const rows = STAGES.map(
    (s) =>
      `| ${s.num} | [${s.id}](./${s.id}-${s.slug}.md) | ${s.name} | ${s.owning} | ${s.operatorApproval} |`,
  );

  return `# MARS Search PPC Production — Stage Contracts Index

**Generated:** ${new Date().toISOString().split('T')[0]}  
**Generator:** \`tools/generate-stage-contracts.mjs\`  
**Count:** ${STAGES.length} stages (SPPC-01 … SPPC-23)

---

## Purpose

This index lists canonical stage contracts for the MARS Search PPC Production lifecycle. Each contract defines inputs, outputs, validation, blocking conditions, and handoff tokens for human-operated production.

**Honesty boundary:** These contracts describe documented production discipline — not automated orchestration unless future tooling explicitly implements it.

---

## Stage map

| # | Contract | Name | Owning system | Operator approval |
|---|----------|------|---------------|-------------------|
${rows.join('\n')}

---

## Canonical flow (summary)

\`\`\`text
01 Business Intake (ATLAS)
 → 02 Source Registration (MIG)
 → 03 Full Semantic Corpus Intake (MIG/ORCA)
 → 04 Normalization (ORCA)
 → 05 Commercial Intent Admission (ORCA Semantic Intelligence)
 → 06 Demand Priority T1–T5 (ORCA)
 → 07 Service and Meaning Ownership (ORCA)
 → 08 Semantic Clustering (ORCA)
 → 09 Negative Keyword Intelligence (ORCA)
 → 10 Daytime Paid SERP (MIG)
 → 11 Competitor Audit (MIG)
 → 12 Dated Analytical Pack (cross-system)
 → 13 AI PPC Strategist
 → 14 Campaign Architecture
 → 15 Keyword and Negative Distribution
 → 16 Ad Production
 → 17 Landing and Offer Alignment
 → 18 Bidding and Budget Strategy
 → 19 Campaign QA
 → 20 Commander Export (transport only)
 → 21 Dry Run and Operator Approval
 → 22 Import and Launch
 → 23 Post-Launch Learning
\`\`\`

---

## Charter-highlighted rules

| Stage | Rule |
|-------|------|
| SPPC-03 | Full corpus intake — no 200-row pilot substitution |
| SPPC-05 | ACCEPT / REJECT / ABSTAIN; escalation ladder; no regex as final authority |
| SPPC-06 | T1–T5 tier definitions binding |
| SPPC-09 | Negatives after admission and ownership; conflicts block export |
| SPPC-10 | Paid SERP business hours; degraded mode if incomplete |
| SPPC-12 | Dated analytical pack required sections |
| SPPC-13 | Strategy gates; forbidden jump to Commander |
| SPPC-20 | Transport-only export |
| SPPC-21 | Operator approval at campaign/strategy abstraction |

---

## Regeneration

\`\`\`bash
node tools/generate-stage-contracts.mjs
\`\`\`
`;
}

async function main() {
  await mkdir(STAGES_DIR, { recursive: true });

  const created = [];

  for (const stage of STAGES) {
    const filename = `${stage.id}-${stage.slug}.md`;
    const filepath = join(STAGES_DIR, filename);
    await writeFile(filepath, renderStage(stage), 'utf8');
    created.push(filename);
  }

  const readmePath = join(STAGES_DIR, 'README.md');
  await writeFile(readmePath, renderReadme(), 'utf8');
  created.push('README.md');

  console.log(`Wrote ${created.length} files to ${STAGES_DIR}:`);
  for (const f of created) {
    console.log(`  - ${f}`);
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
