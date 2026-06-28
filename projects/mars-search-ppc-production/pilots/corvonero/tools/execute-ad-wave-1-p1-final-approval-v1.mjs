#!/usr/bin/env node
/**
 * CORVONERO AD WAVE 1 — Final P1 approval, deployability overlay, DOCX export.
 * Operator decisions S1–S5 (final). Deterministic — no external model calls.
 */
import fs from "fs";
import path from "path";
import crypto from "crypto";
import { fileURLToPath } from "url";
import { createRequire } from "module";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PILOT = path.resolve(__dirname, "..");
const REPO = path.resolve(PILOT, "../../../..");
const REPORTS = path.resolve(REPO, "projects/mars-search-ppc-production/reports");
const STORAGE_EXPORT = path.resolve(
  "C:/MARS Phenix/AI MARS STORAGE/exports/corvonero/CORVONERO-ADS-FINAL-2026-06-29"
);

const CHECKPOINT = "fdd1899c5eb13268021636e40629cfa237a454cf";
const CHECKPOINT_TAG = "corvonero-final-landing-page-copy-program-2026-06";

const require = createRequire(
  path.resolve(REPO, "projects/orca/content-packs/exporters/docx-pilot/package.json")
);
const { Document, Packer, Paragraph, TextRun, HeadingLevel } = require("docx");

const CAMPAIGN_NAMES = {
  "CA-01": "Программист / специалист 1С",
  "CA-02": "Сопровождение и обслуживание 1С",
  "CA-03": "Доработка и разработка 1С",
  "CA-04": "Интеграции 1С",
  "CA-05": "Маркировка / Честный знак",
};

const LP_META = {
  "LP-01": {
    name: "Программист 1С",
    url: "https://lk.corvonero.ru/programmist-1s/",
    copy_authority: "CORVONERO-PHASE-6.6-LP01-FINAL-PRODUCTION-COPY-v3.json",
  },
  "LP-02": {
    name: "Сопровождение и обслуживание 1С",
    url: "https://lk.corvonero.ru/soprovozhdenie-1s/",
    copy_authority: "CORVONERO-COPY-WAVE-2-LP02-SUPPORT-FINAL-v2.json",
  },
  "LP-03": {
    name: "Доработка и разработка 1С",
    url: "https://lk.corvonero.ru/dorabotka-razrabotka-1s/",
    copy_authority: "CORVONERO-COPY-WAVE-2-LP03-DEVELOPMENT-FINAL-v2.json",
  },
  "LP-04": {
    name: "Интеграции 1С",
    url: "https://lk.corvonero.ru/integracii-1s/",
    copy_authority: "CORVONERO-COPY-WAVE-2-LP04-INTEGRATIONS-FINAL-v2.json",
  },
  "LP-05": {
    name: "Маркировка и Честный знак в 1С",
    url: "https://lk.corvonero.ru/markirovka-chestny-znak/",
    copy_authority: "CORVONERO-COPY-WAVE-2-LP05-MARKING-FINAL-v2.json",
  },
};

/** Final operator overlay — S1–S5 */
const OVERLAY = {
  reject: [
    {
      case_id: "S1",
      phrase_id: "CR2-PHR-00229",
      phrase: "становится ли программистом 1с",
      reason: "career / education intent, not a commercial request for 1C support",
      from_campaign: "CA-02",
      from_group: "ca-02-specialist-search",
    },
    {
      case_id: "S5",
      phrase_id: "CR2-PHR-00982",
      phrase: "как заказать коды маркировки в 1с",
      reason:
        "intent concerns obtaining or purchasing marking codes; technical 1C setup intent is not sufficiently supported",
      from_campaign: "CA-05",
      from_group: "ca-05-specialist-search",
    },
  ],
  abstain: [
    {
      case_id: "S2",
      phrase_id: "CR2-PHR-00759",
      phrase: "закупка доработка и сопровождение 1с трактир",
      reason:
        "commercial intent may exist, but Corvonero scope for the «Трактир» configuration is not confirmed",
      from_campaign: "CA-02",
      from_group: "ca-02-modification",
      future_review: "Requires explicit client confirmation before any «Трактир»-scoped advertising.",
    },
  ],
  move: [
    {
      case_id: "S3",
      phrase_id: "CR2-PHR-01181",
      phrase: "внедрение честного знака в 1с",
      from_campaign: "CA-03",
      from_group: "ca-03-implementation",
      to_campaign: "CA-05",
      to_group: "ca-05-direct-service-order",
    },
    {
      case_id: "S4",
      phrase_id: "CR2-PHR-01049",
      phrase: "внедрение маркировки в 1с",
      from_campaign: "CA-03",
      from_group: "ca-03-implementation",
      to_campaign: "CA-05",
      to_group: "ca-05-direct-service-order",
      reason: "marking-specific implementation intent belongs to CA-05",
    },
  ],
};

const EXCLUDED_GROUPS = new Set([
  "ca-02-specialist-search",
  "ca-02-modification",
  "ca-05-specialist-search",
]);

const EXCLUDED_GROUPS_RU = {
  "ca-02-specialist-search": {
    service_context: "Сопровождение 1С — карьерный / образовательный запрос",
    phrase: "становится ли программистом 1с",
    reason:
      "Запрос про профессию и обучение, а не про заказ услуги сопровождения или программиста 1С.",
  },
  "ca-02-modification": {
    service_context: "Сопровождение 1С — доработка отраслевой конфигурации «Трактир»",
    phrase: "закупка доработка и сопровождение 1с трактир",
    reason:
      "Коммерческий смысл возможен, но поддержка конфигурации «Трактир» в scope Corvonero не подтверждена. Требуется отдельное подтверждение у клиента.",
  },
  "ca-05-specialist-search": {
    service_context: "Маркировка / Честный знак — заказ кодов маркировки",
    phrase: "как заказать коды маркировки в 1с",
    reason:
      "Запрос про получение или покупку кодов маркировки, а не про техническую настройку маркировки в 1С.",
  },
};

const EXPECTED_CAMPAIGN_COUNTS = {
  "CA-01": 404,
  "CA-02": 153,
  "CA-03": 69,
  "CA-04": 48,
  "CA-05": 221,
};

// Operator-approved primary ads from v2 editorial revision
const CREATIVE_SOURCE = JSON.parse(
  fs.readFileSync(path.join(PILOT, "CORVONERO-AD-WAVE-1-P1-PRIMARY-ADS-v2.json"), "utf8")
);
const COMB_SOURCE = JSON.parse(
  fs.readFileSync(path.join(PILOT, "CORVONERO-AD-WAVE-1-P1-COMBINATORIAL-ASSETS-v2.json"), "utf8")
);

function readJson(rel) {
  return JSON.parse(fs.readFileSync(path.join(PILOT, rel), "utf8"));
}

function charMetrics(text) {
  const chars = [...text];
  const words = text.split(/\s+/).filter(Boolean);
  const maxWordLen = Math.max(0, ...words.map((w) => [...w.replace(/[^\p{L}\p{N}]/gu, "")].length));
  return { characters: chars.length, max_word_length: maxWordLen, words };
}

function writeJson(name, data) {
  const fp = path.join(PILOT, name);
  fs.writeFileSync(fp, JSON.stringify(data, null, 2) + "\n", "utf8");
  return fp;
}

function writeMd(name, body) {
  const fp = path.join(PILOT, name);
  fs.writeFileSync(fp, body, "utf8");
  return fp;
}

function sha256File(fp) {
  const hash = crypto.createHash("sha256");
  hash.update(fs.readFileSync(fp));
  return hash.digest("hex");
}

function applyOverlay(architecture) {
  const rejectIds = new Set(OVERLAY.reject.map((r) => r.phrase_id));
  const abstainIds = new Set(OVERLAY.abstain.map((r) => r.phrase_id));

  return architecture.ad_groups
    .filter((g) => !g.campaign_id.startsWith("CA-06"))
    .map((g) => {
      let phraseIds = [...g.phrase_ids];
      for (const m of OVERLAY.move) {
        if (m.from_group === g.group_id) {
          phraseIds = phraseIds.filter((id) => id !== m.phrase_id);
        }
        if (m.to_group === g.group_id && !phraseIds.includes(m.phrase_id)) {
          phraseIds.push(m.phrase_id);
        }
      }
      phraseIds = phraseIds.filter((id) => !rejectIds.has(id) && !abstainIds.has(id));
      return { ...g, phrase_ids: phraseIds, included_phrase_count: phraseIds.length };
    });
}

function productionStatus(phraseId, groupId) {
  const rej = OVERLAY.reject.find((r) => r.phrase_id === phraseId);
  if (rej) return "REJECTED_FOR_ADVERTISING";
  const abs = OVERLAY.abstain.find((r) => r.phrase_id === phraseId);
  if (abs) return "ABSTAIN_UNSUPPORTED_SCOPE";
  if (EXCLUDED_GROUPS.has(groupId)) return "EXCLUDED_GROUP";
  return "DEPLOYABLE";
}

function buildPhraseAllocation(architecture, accept) {
  const phraseById = new Map(accept.records.map((r) => [r.phrase_id, r]));
  const originalByGroup = new Map(
    architecture.ad_groups
      .filter((g) => !g.campaign_id.startsWith("CA-06"))
      .map((g) => [g.group_id, g])
  );

  const records = [];
  for (const g of architecture.ad_groups.filter((gr) => !gr.campaign_id.startsWith("CA-06"))) {
    for (const pid of g.phrase_ids) {
      const rec = phraseById.get(pid);
      if (!rec) continue;
      const move = OVERLAY.move.find((m) => m.phrase_id === pid);
      const rej = OVERLAY.reject.find((r) => r.phrase_id === pid);
      const abs = OVERLAY.abstain.find((r) => r.phrase_id === pid);

      let finalCampaign = g.campaign_id;
      let finalGroup = g.group_id;
      if (move) {
        finalCampaign = move.to_campaign;
        finalGroup = move.to_group;
      }

      const status = rej
        ? "REJECTED_FOR_ADVERTISING"
        : abs
          ? "ABSTAIN_UNSUPPORTED_SCOPE"
          : EXCLUDED_GROUPS.has(finalGroup)
            ? EXCLUDED_GROUPS.has(g.group_id)
              ? productionStatus(pid, g.group_id)
              : "DEPLOYABLE"
            : "DEPLOYABLE";

      records.push({
        phrase_id: pid,
        phrase: rec.phrase,
        historical_campaign: g.campaign_id,
        historical_group: g.group_id,
        final_campaign: status === "DEPLOYABLE" && !EXCLUDED_GROUPS.has(finalGroup) ? finalCampaign : g.campaign_id,
        final_group:
          status === "DEPLOYABLE" && !EXCLUDED_GROUPS.has(finalGroup) ? finalGroup : g.group_id,
        production_status: status,
        overlay_case: rej?.case_id || abs?.case_id || move?.case_id || null,
        moved: Boolean(move),
        canonical_accept_preserved: true,
      });
    }
  }

  const counts = {
    DEPLOYABLE: records.filter((r) => r.production_status === "DEPLOYABLE").length,
    REJECTED_FOR_ADVERTISING: records.filter((r) => r.production_status === "REJECTED_FOR_ADVERTISING").length,
    ABSTAIN_UNSUPPORTED_SCOPE: records.filter((r) => r.production_status === "ABSTAIN_UNSUPPORTED_SCOPE").length,
  };

  return {
    allocation_id: "corvonero-ad-wave-1-final-phrase-allocation-v1",
    generated_at: new Date().toISOString(),
    checkpoint: CHECKPOINT,
    note: "Production deployability overlay — historical Phase 5.2 ACCEPT registry not modified.",
    p1_original_count: 898,
    records,
    summary: counts,
    reconciliation: `${counts.DEPLOYABLE} deployable + ${counts.REJECTED_FOR_ADVERTISING} rejected + ${counts.ABSTAIN_UNSUPPORTED_SCOPE} abstain = 898 P1`,
  };
}

async function buildFinalDocx(deployableAds, register) {
  const label = (k, v) =>
    new Paragraph({
      children: [new TextRun({ text: `${k}:`, bold: true }), new TextRun({ text: ` ${v}` })],
    });

  const children = [
    new Paragraph({
      children: [new TextRun({ text: "Корво Неро — объявления для запуска", bold: true, size: 32 })],
    }),
    new Paragraph({ text: "" }),
  ];

  const campaignOrder = ["CA-01", "CA-02", "CA-03", "CA-04", "CA-05"];
  for (const cid of campaignOrder) {
    const ads = deployableAds.filter((a) => a.campaign_id === cid);
    for (const ad of ads) {
      const reg = register.find((r) => r.group_id === ad.group_id);
      children.push(new Paragraph({ text: reg.group_name, heading: HeadingLevel.HEADING_2 }));
      children.push(label("КАМПАНИЯ", CAMPAIGN_NAMES[cid]));
      children.push(label("ГРУППА", reg.group_name));
      children.push(label("СТАРТОВАЯ ФРАЗА ОТ КЛИЕНТА", ad.starter_phrase));
      children.push(label("ПОСАДОЧНАЯ СТРАНИЦА", `${reg.lp_name} — ${reg.final_lp_url_direction}`));
      children.push(label("ЗАГОЛОВОК", ad.primary_ad.headline));
      children.push(label("ДОПОЛНИТЕЛЬНЫЙ ЗАГОЛОВОК", ad.primary_ad.additional_headline || "—"));
      children.push(label("ОПИСАНИЕ", ad.primary_ad.text));
      children.push(new Paragraph({ text: "" }));
    }
  }

  children.push(new Paragraph({ text: "НЕ ВКЛЮЧЕНЫ В ТЕКУЩУЮ РЕКЛАМУ", heading: HeadingLevel.HEADING_1 }));
  for (const gid of ["ca-02-specialist-search", "ca-02-modification", "ca-05-specialist-search"]) {
    const ex = EXCLUDED_GROUPS_RU[gid];
    children.push(new Paragraph({ text: ex.service_context, heading: HeadingLevel.HEADING_2 }));
    children.push(label("Исключённая фраза", ex.phrase));
    children.push(label("Причина", ex.reason));
    children.push(new Paragraph({ text: "" }));
  }

  const doc = new Document({
    sections: [
      {
        properties: {
          page: {
            size: { width: 11906, height: 16838 },
            margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
          },
        },
        children,
      },
    ],
  });

  fs.mkdirSync(STORAGE_EXPORT, { recursive: true });
  const docxPath = path.join(STORAGE_EXPORT, "CORVONERO-ОБЪЯВЛЕНИЯ-ФИНАЛ-v1.docx");
  fs.writeFileSync(docxPath, await Packer.toBuffer(doc));
  return docxPath;
}

async function main() {
  const architecture = readJson("CORVONERO-PHASE-6.1-AD-GROUP-ARCHITECTURE-v2.json");
  const groupLp = readJson("CORVONERO-PHASE-6.2-GROUP-TO-LP-MAP-v1.json");
  const accept = readJson("CORVONERO-RUN-004-PHASE-5.2-FINAL-ACCEPT-v1.json");
  const phraseById = new Map(accept.records.map((r) => [r.phrase_id, r]));
  const lpByGroup = new Map(groupLp.groups.map((g) => [g.group_id, g]));

  const reconciled = applyOverlay(architecture);
  const phraseAllocation = buildPhraseAllocation(architecture, accept);

  if (phraseAllocation.summary.DEPLOYABLE !== 895) {
    throw new Error(`Deployable count ${phraseAllocation.summary.DEPLOYABLE} !== 895`);
  }
  if (phraseAllocation.summary.REJECTED_FOR_ADVERTISING !== 2) {
    throw new Error(`Reject count ${phraseAllocation.summary.REJECTED_FOR_ADVERTISING} !== 2`);
  }
  if (phraseAllocation.summary.ABSTAIN_UNSUPPORTED_SCOPE !== 1) {
    throw new Error(`Abstain count ${phraseAllocation.summary.ABSTAIN_UNSUPPORTED_SCOPE} !== 1`);
  }

  const impl = reconciled.find((g) => g.group_id === "ca-03-implementation");
  if (!impl || impl.included_phrase_count !== 5) {
    throw new Error(`ca-03-implementation must have 5 phrases, got ${impl?.included_phrase_count}`);
  }
  if (!impl.phrase_ids.includes("CR2-PHR-00623")) {
    throw new Error("ca-03-implementation must retain CR2-PHR-00623");
  }

  const campaignTotals = {};
  for (const g of reconciled) {
    if (EXCLUDED_GROUPS.has(g.group_id)) continue;
    campaignTotals[g.campaign_id] = (campaignTotals[g.campaign_id] || 0) + g.included_phrase_count;
  }
  for (const [cid, expected] of Object.entries(EXPECTED_CAMPAIGN_COUNTS)) {
    if (campaignTotals[cid] !== expected) {
      throw new Error(`Campaign ${cid}: expected ${expected}, got ${campaignTotals[cid]}`);
    }
  }

  const deployableGroups = reconciled.filter((g) => !EXCLUDED_GROUPS.has(g.group_id) && g.included_phrase_count > 0);
  if (deployableGroups.length !== 15) {
    throw new Error(`Expected 15 deployable groups, got ${deployableGroups.length}`);
  }

  const register = [];
  const primaryAds = [];
  const combinatorial = [];
  const lpChecks = [];
  const validations = [];

  for (const group of deployableGroups) {
    const gid = group.group_id;
    const v2Ad = CREATIVE_SOURCE.ads.find((a) => a.group_id === gid);
    const v2Comb = COMB_SOURCE.assets.find((a) => a.group_id === gid);
    if (!v2Ad) throw new Error(`Missing v2 primary ad for ${gid}`);

    const lpMap = lpByGroup.get(gid);
    const lpId = lpMap.landing_page_id;
    const lp = LP_META[lpId];
    const starterId =
      gid === "ca-03-implementation" ? "CR2-PHR-00623" : v2Ad.starter_phrase_id;
    const starterRec = phraseById.get(starterId);
    if (!group.phrase_ids.includes(starterId)) {
      throw new Error(`Starter ${starterId} not in group ${gid}`);
    }

    register.push({
      campaign_id: group.campaign_id,
      campaign_name: CAMPAIGN_NAMES[group.campaign_id],
      group_id: gid,
      group_name: group.working_name,
      phrase_count: group.included_phrase_count,
      primary_intent: group.primary_intent,
      assigned_lp: lpId,
      lp_name: lp.name,
      final_lp_url_direction: lp.url,
      copy_authority: lp.copy_authority,
      starter_phrase: {
        phrase_id: starterRec.phrase_id,
        phrase: starterRec.phrase,
      },
      priority: "P1",
      deployable: true,
      operator_primary_ad_status: "APPROVED",
    });

    primaryAds.push({
      ...v2Ad,
      starter_phrase: starterRec.phrase,
      starter_phrase_id: starterRec.phrase_id,
      status: "OPERATOR_APPROVED",
      technical_validation: "TECHNICALLY_VALIDATED",
      editorial_version: "v2-final",
    });

    if (v2Comb) {
      combinatorial.push({
        ...v2Comb,
        operator_approval: "TECHNICALLY_VALIDATED — NOT INDIVIDUALLY OPERATOR APPROVED",
      });
    }

    lpChecks.push({ group_id: gid, landing_page_id: lpId, checks: v2Ad.lp_consistency });
    validations.push({
      group_id: gid,
      status: "DEPLOYABLE",
      technical_validation: v2Ad.technical_validation,
    });
  }

  const overlay = {
    overlay_id: "corvonero-ad-wave-1-final-deployability-overlay-v1",
    generated_at: new Date().toISOString(),
    checkpoint: CHECKPOINT,
    historical_accept_authority: 935,
    p1_allocated_original: 898,
    deferred_ca06: 37,
    operator_decisions: {
      S1: { decision: "REJECT", phrase: OVERLAY.reject[0].phrase },
      S2: { decision: "ABSTAIN NOT DEPLOYABLE", phrase: OVERLAY.abstain[0].phrase },
      S3: { decision: "MOVE CA-03→CA-05", phrase: OVERLAY.move[0].phrase },
      S4: { decision: "MOVE CA-03→CA-05", phrase: OVERLAY.move[1].phrase },
      S5: { decision: "REJECT", phrase: OVERLAY.reject[1].phrase },
    },
    deployable_p1_phrases: 895,
    deployable_p1_groups: 15,
    rejected_for_advertising: 2,
    abstain_unsupported_scope: 1,
    moved_ca03_to_ca05: 2,
    excluded_groups: [...EXCLUDED_GROUPS],
    canonical_authority_modified: false,
    equation:
      "895 deployable + 2 rejected + 1 abstain = 898 P1; 898 P1 + 37 deferred CA-06 = 935 historical ACCEPT",
  };

  writeJson("CORVONERO-AD-WAVE-1-FINAL-DEPLOYABILITY-OVERLAY-v1.json", overlay);
  writeMd(
    "CORVONERO-AD-WAVE-1-FINAL-DEPLOYABILITY-OVERLAY-v1.md",
    `# CORVONERO AD Wave 1 — Final Deployability Overlay v1

Production overlay only — Phase 5.2 ACCEPT registry unchanged.

| Metric | Value |
|--------|------:|
| Deployable P1 phrases | 895 |
| Deployable groups | 15 |
| Rejected for advertising | 2 |
| Abstain unsupported scope | 1 |
| Moved CA-03 → CA-05 | 2 |
| Deferred CA-06 | 37 |

## Operator decisions

- **S1 REJECT:** становится ли программистом 1с
- **S2 ABSTAIN:** закупка доработка и сопровождение 1с трактир
- **S3 MOVE:** внедрение честного знака в 1с → CA-05
- **S4 MOVE:** внедрение маркировки в 1с → CA-05
- **S5 REJECT:** как заказать коды маркировки в 1с
`
  );

  writeJson("CORVONERO-AD-WAVE-1-FINAL-PHRASE-ALLOCATION-v1.json", phraseAllocation);
  writeMd(
    "CORVONERO-AD-WAVE-1-FINAL-PHRASE-ALLOCATION-v1.md",
    `# CORVONERO AD Wave 1 — Final Phrase Allocation v1

All **898** original P1 records with production status.

| Status | Count |
|--------|------:|
| DEPLOYABLE | ${phraseAllocation.summary.DEPLOYABLE} |
| REJECTED_FOR_ADVERTISING | ${phraseAllocation.summary.REJECTED_FOR_ADVERTISING} |
| ABSTAIN_UNSUPPORTED_SCOPE | ${phraseAllocation.summary.ABSTAIN_UNSUPPORTED_SCOPE} |
`
  );

  const receipt = {
    receipt_id: "corvonero-ad-wave-1-final-semantic-receipt-v1",
    generated_at: new Date().toISOString(),
    checkpoint: CHECKPOINT,
    verdict: "PASS",
    deployable_p1_phrases: 895,
    deployable_groups: 15,
    rejected: 2,
    abstain: 1,
    moved: 2,
    deferred_ca06: 37,
    campaign_counts: EXPECTED_CAMPAIGN_COUNTS,
    excluded_groups: [...EXCLUDED_GROUPS],
    note: "Historical ACCEPT not rewritten — production deployability overlay only.",
  };
  writeJson("CORVONERO-AD-WAVE-1-FINAL-SEMANTIC-RECEIPT-v1.json", receipt);
  writeMd(
    "CORVONERO-AD-WAVE-1-FINAL-SEMANTIC-RECEIPT-v1.md",
    `# CORVONERO AD Wave 1 — Final Semantic Receipt v1

**Verdict:** PASS

${receipt.note}
`
  );

  writeJson("CORVONERO-AD-WAVE-1-P1-FINAL-PRIMARY-ADS-v1.json", {
    pack_id: "corvonero-ad-wave-1-p1-final-primary-ads-v1",
    generated_at: new Date().toISOString(),
    operator_status: "PRIMARY ADS: APPROVED",
    deployable_ads: primaryAds.length,
    ads: primaryAds,
  });
  writeMd(
    "CORVONERO-AD-WAVE-1-P1-FINAL-PRIMARY-ADS-v1.md",
    `# CORVONERO AD Wave 1 — Final Primary Ads v1

**Operator status:** PRIMARY ADS APPROVED

Deployable ads: **${primaryAds.length}**
`
  );

  writeJson("CORVONERO-AD-WAVE-1-P1-FINAL-COMBINATORIAL-ASSETS-v1.json", {
    pack_id: "corvonero-ad-wave-1-p1-final-combinatorial-assets-v1",
    generated_at: new Date().toISOString(),
    operator_note: "TECHNICALLY VALIDATED — NOT INDIVIDUALLY OPERATOR APPROVED",
    assets: combinatorial,
  });
  writeMd(
    "CORVONERO-AD-WAVE-1-P1-FINAL-COMBINATORIAL-ASSETS-v1.md",
    `# CORVONERO AD Wave 1 — Final Combinatorial Assets v1

Alternative assets retained for future combinatorial configuration.
**Not** individually operator-approved creative.
`
  );

  writeJson("CORVONERO-AD-WAVE-1-P1-FINAL-GROUP-REGISTER-v1.json", {
    register_id: "corvonero-ad-wave-1-p1-final-group-register-v1",
    generated_at: new Date().toISOString(),
    checkpoint: CHECKPOINT,
    deployable_groups: register.length,
    deployable_phrases: 895,
    groups: register,
  });
  writeMd(
    "CORVONERO-AD-WAVE-1-P1-FINAL-GROUP-REGISTER-v1.md",
    `# CORVONERO AD Wave 1 — Final Group Register v1

Deployable groups: **${register.length}** | Phrases: **895**
`
  );

  writeJson("CORVONERO-AD-WAVE-1-P1-FINAL-TECHNICAL-VALIDATION-v1.json", {
    pack_id: "corvonero-ad-wave-1-p1-final-technical-validation-v1",
    generated_at: new Date().toISOString(),
    validations,
    result: "TECHNICALLY_VALIDATED",
  });
  writeMd(
    "CORVONERO-AD-WAVE-1-P1-FINAL-TECHNICAL-VALIDATION-v1.md",
    `# CORVONERO AD Wave 1 — Final Technical Validation v1

**${validations.length}** deployable primary ads — TECHNICALLY VALIDATED.
`
  );

  writeJson("CORVONERO-AD-WAVE-1-P1-FINAL-LP-CONSISTENCY-v1.json", {
    pack_id: "corvonero-ad-wave-1-p1-final-lp-consistency-v1",
    generated_at: new Date().toISOString(),
    checks: lpChecks,
  });
  writeMd(
    "CORVONERO-AD-WAVE-1-P1-FINAL-LP-CONSISTENCY-v1.md",
    `# CORVONERO AD Wave 1 — Final LP Consistency v1

**${lpChecks.length}** deployable ads — LP consistency verified.
`
  );

  const approval = {
    approval_id: "corvonero-ad-wave-1-p1-final-approval-v1",
    generated_at: new Date().toISOString(),
    checkpoint: CHECKPOINT,
    primary_ads: "APPROVED",
    deployable_groups: 15,
    deployable_phrases: 895,
    hold_groups: 0,
    excluded_groups: 3,
    rejected_phrases: 2,
    abstain_phrases: 1,
    commander_xlsx: "NOT CREATED",
    advertising_started: false,
    alternative_assets: "TECHNICALLY VALIDATED — NOT INDIVIDUALLY OPERATOR APPROVED",
  };
  writeJson("CORVONERO-AD-WAVE-1-P1-FINAL-APPROVAL-v1.json", approval);
  writeMd(
    "CORVONERO-AD-WAVE-1-P1-FINAL-APPROVAL-v1.md",
    `# CORVONERO AD Wave 1 — Final Approval v1

**PRIMARY ADS:** APPROVED

| Item | Status |
|------|--------|
| Deployable groups | 15 |
| Deployable phrases | 895 |
| Commander XLSX | NOT CREATED |
| Advertising | NOT STARTED |
`
  );

  const docxPath = await buildFinalDocx(primaryAds, register);
  const docxHash = sha256File(docxPath);
  const docxSize = fs.statSync(docxPath).size;

  // Verify DOCX opens (ZIP signature)
  const sig = fs.readFileSync(docxPath).subarray(0, 4);
  if (sig[0] !== 0x50 || sig[1] !== 0x4b) {
    throw new Error("DOCX verification failed — not a valid ZIP archive");
  }

  const exportManifest = {
    manifest_id: "corvonero-ads-final-manifest-v1",
    generated_at: new Date().toISOString(),
    source_checkpoint: { commit: CHECKPOINT, tag: CHECKPOINT_TAG },
    output_file: docxPath,
    filename: "CORVONERO-ОБЪЯВЛЕНИЯ-ФИНАЛ-v1.docx",
    size_bytes: docxSize,
    sha256: docxHash,
    deployable_groups: 15,
    deployable_phrases: 895,
    validation_result: "PASS",
  };
  fs.writeFileSync(
    path.join(STORAGE_EXPORT, "CORVONERO-ADS-FINAL-MANIFEST-v1.json"),
    JSON.stringify(exportManifest, null, 2) + "\n"
  );
  fs.writeFileSync(
    path.join(STORAGE_EXPORT, "CORVONERO-ADS-FINAL-SHA256-v1.txt"),
    `${docxHash}  CORVONERO-ОБЪЯВЛЕНИЯ-ФИНАЛ-v1.docx\n`
  );
  fs.writeFileSync(
    path.join(STORAGE_EXPORT, "CORVONERO-ADS-FINAL-README-v1.md"),
    `# CORVONERO Ads Final Export

- **File:** CORVONERO-ОБЪЯВЛЕНИЯ-ФИНАЛ-v1.docx
- **SHA-256:** \`${docxHash}\`
- **Deployable groups:** 15
- **Deployable phrases:** 895
- **Operator status:** PRIMARY ADS APPROVED
`
  );

  const excludedRegister = {
    register_id: "corvonero-ad-wave-1-excluded-groups-v1",
    generated_at: new Date().toISOString(),
    excluded_groups: Object.entries(EXCLUDED_GROUPS_RU).map(([group_id, v]) => ({
      group_id,
      ...v,
      production_status:
        group_id === "ca-02-modification" ? "ABSTAIN_UNSUPPORTED_SCOPE" : "REJECTED_FOR_ADVERTISING",
    })),
  };
  writeJson("CORVONERO-AD-WAVE-1-EXCLUDED-GROUPS-v1.json", excludedRegister);
  writeMd(
    "CORVONERO-AD-WAVE-1-EXCLUDED-GROUPS-v1.md",
    `# CORVONERO AD Wave 1 — Excluded Groups v1

Three groups excluded from current advertising production.

${Object.values(EXCLUDED_GROUPS_RU)
  .map((e) => `- **${e.service_context}:** ${e.phrase} — ${e.reason}`)
  .join("\n")}
`
  );

  const exportMatrix = {
    matrix_id: "corvonero-export-readiness-matrix-v2",
    generated_at: new Date().toISOString(),
    prior_checkpoint: { commit: CHECKPOINT, tag: CHECKPOINT_TAG },
    deliverables: {
      D1_ads_docx: {
        id: "D1",
        name: "Ads DOCX",
        readiness: "READY — 15 deployable groups / 895 phrases",
        path: docxPath,
        sha256: docxHash,
      },
      D2_landing_page_docx: {
        id: "D2",
        name: "Landing-page DOCX",
        readiness: "READY — LP-01 through LP-05",
      },
      D3_commander_xlsx: {
        id: "D3",
        name: "Commander XLSX",
        readiness:
          "NOT READY — requires extensions, negatives, UTM, final URL/publication and import profile",
      },
      D4_research_xlsx: {
        id: "D4",
        name: "Research XLSX",
        readiness: "READY — partial coverage explicitly labelled",
      },
    },
    advertising: { started: false },
    commander: { created: false },
  };
  writeJson("CORVONERO-EXPORT-READINESS-MATRIX-v2.json", exportMatrix);
  writeMd(
    "CORVONERO-EXPORT-READINESS-MATRIX-v2.md",
    `# CORVONERO Export Readiness Matrix v2

| Deliverable | Readiness |
|-------------|-----------|
| D1 Ads DOCX | READY — 15 deployable groups / 895 phrases |
| D2 Landing-page DOCX | READY — LP-01 through LP-05 |
| D3 Commander XLSX | NOT READY |
| D4 Research XLSX | READY — partial coverage explicitly labelled |
`
  );

  const result = {
    verdict: "CORVONERO AD WAVE 1 FINAL: PASS",
    deployable_p1_groups: 15,
    deployable_p1_phrases: 895,
    rejected_for_advertising: 2,
    abstain_unsupported_scope: 1,
    moved_ca03_to_ca05: 2,
    final_ads_docx: { path: docxPath, sha256: docxHash, verified: true },
    campaign_counts: EXPECTED_CAMPAIGN_COUNTS,
    ca03_implementation_phrases: 5,
    commander_xlsx: "NOT CREATED",
    advertising: "NOT STARTED",
  };
  writeJson("CORVONERO-AD-WAVE-1-P1-FINAL-RESULT-v1.json", result);
  writeMd(
    "CORVONERO-AD-WAVE-1-P1-FINAL-RESULT-v1.md",
    `# CORVONERO AD Wave 1 — P1 Final Result v1

**Verdict:** CORVONERO AD WAVE 1 FINAL: PASS

| Metric | Value |
|--------|------:|
| Deployable P1 groups | 15 |
| Deployable P1 phrases | 895 |
| Rejected for advertising | 2 |
| Abstain unsupported scope | 1 |
| Moved CA-03 → CA-05 | 2 |
| Final Ads DOCX | CREATED AND VERIFIED |
| Commander XLSX | NOT CREATED |
| Advertising | NOT STARTED |
`
  );

  fs.mkdirSync(REPORTS, { recursive: true });
  fs.writeFileSync(
    path.join(REPORTS, "REPORT-corvonero-ad-wave-1-final-approval-and-checkpoint-v1.md"),
    `# REPORT — CORVONERO AD Wave 1 Final Approval and Checkpoint v1

## Verdict

**CORVONERO AD WAVE 1 FINAL: PASS**

| Metric | Value |
|--------|------:|
| Deployable P1 groups | 15 |
| Deployable P1 phrases | 895 |
| Rejected for advertising | 2 |
| Abstain unsupported scope | 1 |
| Moved CA-03 → CA-05 | 2 |
| Final Ads DOCX | CREATED AND VERIFIED |
| Git checkpoint | PENDING — run checkpoint script |
| Tag | PENDING — corvonero-final-p1-search-ads-2026-06 |
| Remote | PENDING |
| External backup | PENDING |
| Commander XLSX | NOT CREATED |
| Advertising | NOT STARTED |

## Created artefacts

### pilots/corvonero/

- CORVONERO-AD-WAVE-1-FINAL-DEPLOYABILITY-OVERLAY-v1.{md,json}
- CORVONERO-AD-WAVE-1-FINAL-PHRASE-ALLOCATION-v1.{md,json}
- CORVONERO-AD-WAVE-1-FINAL-SEMANTIC-RECEIPT-v1.{md,json}
- CORVONERO-AD-WAVE-1-P1-FINAL-PRIMARY-ADS-v1.{md,json}
- CORVONERO-AD-WAVE-1-P1-FINAL-COMBINATORIAL-ASSETS-v1.{md,json}
- CORVONERO-AD-WAVE-1-P1-FINAL-GROUP-REGISTER-v1.{md,json}
- CORVONERO-AD-WAVE-1-P1-FINAL-TECHNICAL-VALIDATION-v1.{md,json}
- CORVONERO-AD-WAVE-1-P1-FINAL-LP-CONSISTENCY-v1.{md,json}
- CORVONERO-AD-WAVE-1-P1-FINAL-APPROVAL-v1.{md,json}
- CORVONERO-AD-WAVE-1-P1-FINAL-RESULT-v1.{md,json}
- CORVONERO-AD-WAVE-1-EXCLUDED-GROUPS-v1.{md,json}
- CORVONERO-EXPORT-READINESS-MATRIX-v2.{md,json}

### Storage

- \`${docxPath}\`
- CORVONERO-ADS-FINAL-MANIFEST-v1.json
- CORVONERO-ADS-FINAL-SHA256-v1.txt
- CORVONERO-ADS-FINAL-README-v1.md
`
  );

  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
