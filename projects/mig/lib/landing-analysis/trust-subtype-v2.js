"use strict";

const MAX_TRUST_LINE_CHARS = 200;

const PLATFORM_PATTERNS = [
  { platform: "yandex", re: /яндекс/i },
  { platform: "avito", re: /авито/i },
  { platform: "google", re: /google/i },
  { platform: "2gis", re: /2\s*гис|2gis/i },
];

function detectPlatform(text) {
  if (!text) {
    return null;
  }
  for (const { platform, re } of PLATFORM_PATTERNS) {
    if (re.test(text)) {
      return platform;
    }
  }
  return null;
}

function parseRatingNumbers(text) {
  const ratingMatch = text.match(/(?:рейтинг|оценк|★|⭐).*?(\d+[,.]?\d*)/i);
  const countMatch = text.match(/(\d+)\s*\+?\s*(?:оценок|отзыв)/i);
  return {
    numeric_value: ratingMatch ? Number(ratingMatch[1].replace(",", ".")) : null,
    numeric_secondary: countMatch ? Number(countMatch[1]) : null,
    numeric_unit: countMatch ? "ratings_count" : null,
  };
}

function isStandaloneMetricLine(text) {
  if (!text || text.length > 120) {
    return false;
  }
  return /(?:\d+\+?\s*(?:клиент|заказ|проект|выполн)|\d+\s*(?:лет|год))/i.test(text);
}

/**
 * v2 trust subtype — statistics deprecated for long prose.
 */
function isTrustBoilerplate(text) {
  const lower = (text || "").toLowerCase();
  if (/(?:cookie|метаданные.*ip-адрес|функционирования сайта)/i.test(lower)) {
    return true;
  }
  const navHits = ["о сервисе", "акции", "контакты", "частые вопросы", "отзывы", "услуги"].filter((p) =>
    lower.includes(p)
  );
  return navHits.length >= 3;
}

function classifyTrustSubtypeV2(text, registry = {}) {
  const lower = (text || "").toLowerCase();
  if (!text || text.length > MAX_TRUST_LINE_CHARS || isTrustBoilerplate(text)) {
    return null;
  }

  if (/рейтинг|★|⭐|оценок|отзывов/i.test(text) && detectPlatform(text)) {
    return "rating_display";
  }
  if (/рейтинг|★|⭐|\b[45][,.]\d/i.test(text) && /\d+\+?\s*(?:оценок|отзыв)/i.test(text)) {
    return "rating_display";
  }
  if (/отзыв|review/i.test(lower) && text.length < 120) {
    return "review_snippet";
  }
  if (/(?:машин|автопарк|единиц|газел)/i.test(text) && /\d+/.test(text)) {
    return "fleet_size";
  }
  if (/(?:лет на рынке|с\s+(?:19|20)\d{2}|на рынке)/i.test(text)) {
    return "experience_claim";
  }
  if (/(?:гарант|warranty)/i.test(lower)) {
    return "guarantee";
  }
  if (/(?:инн|огрн|ооо\s|ип\s)/i.test(lower)) {
    return "legal_entity";
  }
  if (/(?:лиценз|сертификат|iso)/i.test(lower)) {
    return "certificate";
  }
  if (/(?:партнер|partner|банк)/i.test(lower)) {
    return "partner_badge";
  }
  if (isStandaloneMetricLine(text)) {
    return "completed_orders";
  }

  const legacyRules = registry.trust_classification || {};
  for (const [trustType, patterns] of Object.entries(legacyRules)) {
    if (trustType === "statistics") {
      continue;
    }
    for (const pattern of patterns) {
      const isRegex = pattern.startsWith("\\");
      if (isRegex) {
        try {
          if (new RegExp(pattern, "i").test(text)) {
            return trustType === "case_reference" ? "review_snippet" : trustType;
          }
        } catch {
          /* skip */
        }
      } else if (lower.includes(pattern.toLowerCase())) {
        return trustType === "case_reference" ? "review_snippet" : trustType;
      }
    }
  }

  if (/(?:отзыв|рейтинг)/i.test(text)) {
    return "review_snippet";
  }
  return null;
}

function splitTrustLines(text) {
  if (!text || text.length <= MAX_TRUST_LINE_CHARS) {
    return [text].filter(Boolean);
  }
  const parts = text
    .split(/(?=Рейтинг|рейтинг|Яндекс|Авито|Google)/i)
    .map((s) => s.trim())
    .filter((s) => s.length > 0 && s.length <= MAX_TRUST_LINE_CHARS);
  if (parts.length) {
    return parts;
  }
  return [];
}

module.exports = {
  MAX_TRUST_LINE_CHARS,
  detectPlatform,
  parseRatingNumbers,
  classifyTrustSubtypeV2,
  splitTrustLines,
  isStandaloneMetricLine,
  isTrustBoilerplate,
};
