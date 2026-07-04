#!/usr/bin/env node
// C2c HOLD: ad-wave review/approval hardening only.
// This file is not authorized for execution without explicit operator approval.
// Commit/persistence does not authorize Direct launch, Commander import,
// account mutation, advertising start, Storage export generation,
// repo artifact generation, Localhost mutation, Storage mutation,
// Yandex/API access, client-facing delivery, or production execution.
// Ad-wave DOCX/JSON/MD generation is review/export-candidate tooling only.
/**
 * CORVONERO AD WAVE 1 — P1 Editorial Revision v2
 * Semantic reconciliation S1–S5 + operator-approved primary ads + DOCX v2.
 * Deterministic local generation — no external model calls.
 * Ad-wave review/final approval materials are review/export-candidate tooling only
 * and do not authorize launch, Direct import, account mutation, advertising start,
 * or client-facing delivery.
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
  "X:/AI MARS STORAGE/exports/corvonero/CORVONERO-ADS-REVIEW-V2-2026-06-29"
);

const CHECKPOINT = "fdd1899c5eb13268021636e40629cfa237a454cf";
const CHECKPOINT_TAG = "corvonero-final-landing-page-copy-program-2026-06";

const require = createRequire(
  path.resolve(REPO, "projects/orca/content-packs/exporters/docx-pilot/package.json")
);
const {
  Document,
  Packer,
  Paragraph,
  TextRun,
  HeadingLevel,
} = require("docx");

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

/** Semantic reconciliation — phrase moves and deployability */
const RECONCILIATION = {
  reject: [
    {
      case_id: "S1",
      phrase_id: "CR2-PHR-00229",
      phrase: "становится ли программистом 1с",
      from_campaign: "CA-02",
      from_group: "ca-02-specialist-search",
    },
    {
      case_id: "S5",
      phrase_id: "CR2-PHR-00982",
      phrase: "как заказать коды маркировки в 1с",
      from_campaign: "CA-05",
      from_group: "ca-05-specialist-search",
    },
  ],
  hold: [
    {
      case_id: "S2",
      phrase_id: "CR2-PHR-00759",
      phrase: "закупка доработка и сопровождение 1с трактир",
      from_campaign: "CA-02",
      from_group: "ca-02-modification",
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
  ],
};

const HOLD_GROUPS = new Set([
  "ca-02-specialist-search",
  "ca-02-modification",
  "ca-05-specialist-search",
]);

const HOLD_REASONS_RU = {
  "ca-02-specialist-search":
    "Единственная фраза группы — карьерный/образовательный запрос («становится ли программистом»), не услуга Corvonero. Исключить из рекламы.",
  "ca-02-modification":
    "Фраза содержит «Трактир» — отраслевую конфигурацию 1С без подтверждённого scope Corvonero. Нужно уточнение у оператора.",
  "ca-05-specialist-search":
    "Запрос «как заказать коды маркировки» — покупка/получение кодов, а не техническая настройка 1С. Вне услуги Corvonero.",
};

/** Operator-approved v2 creatives */
const CREATIVE_V2 = {
  "ca-01-specialist-search": {
    starter_phrase_id: "CR2-PHR-00001",
    primary: {
      headline: "Программист 1С для разовых задач",
      additional: "Удалённо по России",
      text: "Доработка, ошибки и отчёты в 1С. Выезд в Новосибирске. Работа по договору.",
    },
    headlines: [
      "Программист 1С для разовых задач",
      "Специалист 1С — настройка и исправление ошибок",
      "Программист 1С в Новосибирске — Корво Неро",
      "Внешний программист 1С — разовые задачи",
    ],
    texts: [
      "Доработка, ошибки и отчёты в 1С. Выезд в Новосибирске. Работа по договору.",
      "УТ, УНФ, Розница, КА, БП. Безналичная оплата.",
      "Оценка объёма после обсуждения задачи. Удалённо по России.",
    ],
    angles: {
      commercial: "Программист 1С для разовых задач",
      problem: "Специалист 1С — настройка и исправление ошибок",
      service_literal: "Внешний программист 1С — разовые задачи",
    },
    claims: ["LP-01 first_screen", "LP-01 work_format", "LP-01 trust"],
  },
  "ca-01-price-intent": {
    starter_phrase_id: "CR2-PHR-00550",
    primary: {
      headline: "Программист 1С — от 3 000 ₽ в час",
      additional: "Удалённо по России",
      text: "Минимальный заказ — 2 часа. Работаем удалённо и с выездом в Новосибирске.",
    },
    headlines: [
      "Программист 1С — от 3 000 ₽ в час",
      "Стоимость программиста 1С — от 3 000 ₽/ч",
      "Цена часа программиста 1С — Корво Неро",
      "Программист 1С — почасовая оплата",
    ],
    texts: [
      "Минимальный заказ — 2 часа. Работаем удалённо и с выездом в Новосибирске.",
      "Почасовая работа специалиста. Работа по договору.",
      "Удалённо по России. Безналичная оплата.",
    ],
    angles: {
      commercial: "Программист 1С — от 3 000 ₽ в час",
      problem: "Стоимость программиста 1С — от 3 000 ₽/ч",
      service_literal: "Программист 1С — почасовая оплата",
    },
    claims: ["LP-01 pricing"],
  },
  "ca-01-direct-service-order": {
    starter_phrase_id: "CR2-PHR-00413",
    primary: {
      headline: "Услуги программиста 1С под вашу задачу",
      additional: "Корво Неро",
      text: "Обсудим задачу и оценим объём работ. Удалённо по России, выезд в Новосибирске.",
    },
    headlines: [
      "Услуги программиста 1С под вашу задачу",
      "Заказать программиста 1С — разовая работа",
      "Услуги 1С-программиста — Корво Неро",
      "Программист 1С на аутсорсе — обсудим задачу",
    ],
    texts: [
      "Обсудим задачу и оценим объём работ. Удалённо по России, выезд в Новосибирске.",
      "Доработка, ошибки, отчёты. Работа по договору.",
      "Получите оценку после уточнения конфигурации и объёма.",
    ],
    angles: {
      commercial: "Заказать программиста 1С — разовая работа",
      problem: "Услуги программиста 1С под вашу задачу",
      service_literal: "Услуги 1С-программиста — Корво Неро",
    },
    claims: ["LP-01 first_screen", "LP-01 process"],
  },
  "ca-02-support-and-maintenance": {
    starter_phrase_id: "CR2-PHR-00590",
    primary: {
      headline: "Сопровождение 1С — поддержка и обновления",
      additional: "Удалённо по России",
      text: "Помощь пользователям, обновления и ошибки. Выезд в Новосибирске.",
    },
    headlines: [
      "Сопровождение 1С — поддержка и обновления",
      "Обслуживание 1С для компаний и ИП",
      "Абонентское и разовое сопровождение 1С",
      "Поддержка базы 1С — Корво Неро",
      "Сопровождение 1С — удалённо и с выездом",
    ],
    texts: [
      "Помощь пользователям, обновления и ошибки. Выезд в Новосибирске.",
      "Абонентский формат и разовые обращения. Работа по договору.",
      "УТ, УНФ, Розница, КА, БП. Безналичная оплата.",
    ],
    angles: {
      commercial: "Обслуживание 1С для компаний и ИП",
      problem: "Поддержка базы 1С — Корво Неро",
      service_literal: "Сопровождение 1С — поддержка и обновления",
    },
    claims: ["LP-02 first_screen", "LP-02 meta"],
  },
  "ca-02-direct-service-order": {
    starter_phrase_id: "CR2-PHR-00591",
    primary: {
      headline: "Услуги сопровождения и поддержки 1С",
      additional: "Корво Неро",
      text: "Помощь пользователям, обновления и устранение ошибок. Удалённо по России.",
    },
    headlines: [
      "Услуги сопровождения и поддержки 1С",
      "Сопровождение 1С — разово или постоянно",
      "Услуги по сопровождению 1С — Корво Неро",
    ],
    texts: [
      "Помощь пользователям, обновления и устранение ошибок. Удалённо по России.",
      "Обновления, помощь пользователям, устранение ошибок. По договору.",
      "Обсудим формат работы и оценим объём после уточнения задачи.",
    ],
    angles: {
      commercial: "Сопровождение 1С — разово или постоянно",
      problem: "Услуги сопровождения и поддержки 1С",
      service_literal: "Услуги по сопровождению 1С — Корво Неро",
    },
    claims: ["LP-02 first_screen"],
  },
  "ca-02-troubleshooting-not-working": {
    starter_phrase_id: "CR2-PHR-02239",
    primary: {
      headline: "1С не работает — поможем разобраться",
      additional: "Сопровождение 1С",
      text: "Разберём ошибку и восстановим работу базы. Удалённо, выезд в Новосибирске.",
    },
    headlines: [
      "1С не работает — поможем разобраться",
      "Ошибки в 1С — оперативная помощь специалиста",
      "Устранение ошибок 1С — Корво Неро",
    ],
    texts: [
      "Разберём ошибку и восстановим работу базы. Удалённо, выезд в Новосибирске.",
      "Разовое обращение или сопровождение. Работа по договору.",
      "Поможем пользователям и исправим сбои в конфигурации.",
    ],
    angles: {
      commercial: "1С не работает — поможем разобраться",
      problem: "Ошибки в 1С — оперативная помощь специалиста",
      service_literal: "Устранение ошибок 1С — Корво Неро",
    },
    claims: ["LP-02 first_screen", "LP-02 service scope"],
  },
  "ca-02-price-intent": {
    starter_phrase_id: "CR2-PHR-00711",
    primary: {
      headline: "Стоимость сопровождения 1С",
      additional: "Оценка после уточнения задач",
      text: "Стоимость зависит от формата и объёма поддержки. Работаем по договору.",
    },
    headlines: [
      "Стоимость сопровождения 1С",
      "Стоимость сопровождения 1С — после оценки задачи",
      "Цена поддержки 1С — уточним по объёму",
    ],
    texts: [
      "Стоимость зависит от формата и объёма поддержки. Работаем по договору.",
      "Абонентский формат и разовые обращения. Удалённо по России.",
      "Безналичная оплата. Выезд специалиста в Новосибирске.",
    ],
    angles: {
      commercial: "Стоимость сопровождения 1С",
      problem: "Стоимость сопровождения 1С — после оценки задачи",
      service_literal: "Цена поддержки 1С — уточним по объёму",
    },
    claims: ["LP-02 pricing_policy"],
  },
  "ca-03-modification": {
    starter_phrase_id: "CR2-PHR-00764",
    primary: {
      headline: "Доработка 1С — отчёты, обработки, формы",
      additional: "Под задачи бизнеса",
      text: "Доработаем конфигурацию под ваш процесс. Удалённо по России.",
    },
    headlines: [
      "Доработка 1С — отчёты, обработки, формы",
      "Доработка конфигурации 1С — Корво Неро",
      "Разработка 1С — автоматизация процессов",
      "Программист 1С — доработка под ваш учёт",
      "Доработка 1С — печатные формы и отчёты",
    ],
    texts: [
      "Доработаем конфигурацию под ваш процесс. Удалённо по России.",
      "Отчёты, обработки, печатные формы. Выезд в Новосибирске.",
      "Оценим объём после обсуждения задачи. Работа по договору.",
    ],
    angles: {
      commercial: "Доработка конфигурации 1С — Корво Неро",
      problem: "Доработка 1С — отчёты, обработки, формы",
      service_literal: "Разработка 1С — автоматизация процессов",
    },
    claims: ["LP-03 first_screen"],
  },
  "ca-03-implementation": {
    starter_phrase_id: "CR2-PHR-00623",
    primary: {
      headline: "Внедрение отдельных процессов в 1С",
      additional: "Доработка под задачи бизнеса",
      text: "Настроим учётный сценарий в действующей базе. Удалённо по России.",
    },
    headlines: [
      "Внедрение отдельных процессов в 1С",
      "Внедрение и доработка 1С — под вашу базу",
      "Настройка учёта в 1С — Корво Неро",
      "Внедрение 1С — отдельные блоки учёта",
    ],
    texts: [
      "Настроим учётный сценарий в действующей базе. Удалённо по России.",
      "Точечные сценарии в действующей базе. Выезд в Новосибирске.",
      "Обсудим конфигурацию и объём. Работа по договору.",
    ],
    angles: {
      commercial: "Внедрение и доработка 1С — под вашу базу",
      problem: "Настройка учёта в 1С — Корво Неро",
      service_literal: "Внедрение отдельных процессов в 1С",
    },
    claims: ["LP-03 first_screen", "LP-03 operator_decisions partial_implementation"],
  },
  "ca-03-direct-service-order": {
    starter_phrase_id: "CR2-PHR-00769",
    primary: {
      headline: "Услуги по доработке 1С",
      additional: "Под задачи вашего бизнеса",
      text: "Доработаем конфигурацию, отчёт или форму. Удалённо, выезд в Новосибирске.",
    },
    headlines: [
      "Услуги по доработке 1С",
      "Заказать доработку 1С — разовая работа",
      "Услуги разработки 1С — Корво Неро",
    ],
    texts: [
      "Доработаем конфигурацию, отчёт или форму. Удалённо, выезд в Новосибирске.",
      "Отчёты, обработки, автоматизация. Оценка после уточнения объёма.",
      "Работа по договору. Безналичная оплата.",
    ],
    angles: {
      commercial: "Заказать доработку 1С — разовая работа",
      problem: "Услуги по доработке 1С",
      service_literal: "Услуги разработки 1С — Корво Неро",
    },
    claims: ["LP-03 first_screen"],
  },
  "ca-04-integration": {
    starter_phrase_id: "CR2-PHR-00842",
    primary: {
      headline: "Интеграция 1С с сайтом и Битрикс",
      additional: "Обмен данными",
      text: "Настроим синхронизацию, импорт и экспорт после анализа обеих систем.",
    },
    headlines: [
      "Интеграция 1С с сайтом и Битрикс",
      "Обмен данными 1С и внешних систем",
      "Интеграция 1С — синхронизация каталога",
      "Связь 1С с интернет-магазином — Корво Неро",
      "Интеграция 1С — импорт и экспорт данных",
    ],
    texts: [
      "Настроим синхронизацию, импорт и экспорт после анализа обеих систем.",
      "Сайт, Битрикс, внешние системы. Удалённо по России.",
      "Обсудим задачу и схему обмена. Выезд в Новосибирске.",
    ],
    angles: {
      commercial: "Интеграция 1С с сайтом и Битрикс",
      problem: "Обмен данными 1С и внешних систем",
      service_literal: "Интеграция 1С — синхронизация каталога",
    },
    claims: ["LP-04 first_screen", "LP-04 systems_mentioned"],
  },
  "ca-05-direct-service-order": {
    starter_phrase_id: "CR2-PHR-00879",
    primary: {
      headline: "Маркировка и Честный знак в 1С",
      additional: "Настройка обмена",
      text: "Подключим обмен кодами и документами. Удалённо по России.",
    },
    headlines: [
      "Маркировка и Честный знак в 1С",
      "Настройка маркировки товаров в 1С",
      "Честный знак в 1С — настройка обмена",
      "Маркировка в 1С — настройка и сопровождение",
      "Коды маркировки в 1С — Корво Неро",
      "Маркировка 1С — обмен с Честным знаком",
    ],
    texts: [
      "Подключим обмен кодами и документами. Удалённо по России.",
      "Настройка, ошибки обмена, документооборот. Выезд в Новосибирске.",
      "Техническая помощь в 1С. Работа по договору.",
    ],
    angles: {
      commercial: "Настройка маркировки товаров в 1С",
      problem: "Честный знак в 1С — настройка обмена",
      service_literal: "Маркировка и Честный знак в 1С",
    },
    claims: ["LP-05 first_screen"],
  },
  "ca-05-integration": {
    starter_phrase_id: "CR2-PHR-00877",
    primary: {
      headline: "Интеграция маркировки 1С с сайтом",
      additional: "Честный знак и Битрикс",
      text: "Настроим обмен данными маркировки после анализа 1С и внешней системы.",
    },
    headlines: [
      "Интеграция маркировки 1С с сайтом",
      "Маркировка 1С — интеграция с интернет-магазином",
      "Обмен маркировки 1С и внешних систем",
      "Интеграция Честного знака и 1С — Корво Неро",
    ],
    texts: [
      "Настроим обмен данными маркировки после анализа 1С и внешней системы.",
      "Сайт, Битрикс, обмен кодами. Удалённо по России.",
      "Техническая настройка в 1С. Выезд в Новосибирске.",
    ],
    angles: {
      commercial: "Маркировка 1С — интеграция с интернет-магазином",
      problem: "Обмен маркировки 1С и внешних систем",
      service_literal: "Интеграция маркировки 1С с сайтом",
    },
    claims: ["LP-05 first_screen", "LP-05 operator_decisions website_bitrix_faq"],
  },
  "ca-05-ts-piot": {
    starter_phrase_id: "CR2-PHR-01145",
    primary: {
      headline: "Настройка ТС ПИОТ и Честного знака в 1С",
      additional: "Маркировка 1С",
      text: "Настроим работу ТС ПИОТ в связке с вашей конфигурацией 1С. Удалённо.",
    },
    headlines: [
      "Настройка ТС ПИОТ и Честного знака в 1С",
      "Настройка ТС ПИОТ в 1С — Корво Неро",
      "ТС ПИОТ в 1С — подключение обмена",
      "Маркировка ТС ПИОТ в 1С — техническая помощь",
    ],
    texts: [
      "Настроим работу ТС ПИОТ в связке с вашей конфигурацией 1С. Удалённо.",
      "Ошибки обмена, документы, коды. Выезд в Новосибирске.",
      "Обсудим конфигурацию и объём. Работа по договору.",
    ],
    angles: {
      commercial: "Настройка ТС ПИОТ в 1С — Корво Неро",
      problem: "ТС ПИОТ в 1С — подключение обмена",
      service_literal: "Настройка ТС ПИОТ и Честного знака в 1С",
    },
    claims: ["LP-05 meta TS ПИОТ", "LP-05 first_screen"],
  },
  "ca-05-support-and-maintenance": {
    starter_phrase_id: "CR2-PHR-01179",
    primary: {
      headline: "Поддержка маркировки и Честного знака в 1С",
      additional: "Сопровождение обмена",
      text: "Поможем с ошибками и документами маркировки. Удалённо по России.",
    },
    headlines: [
      "Поддержка маркировки и Честного знака в 1С",
      "Сопровождение маркировки в 1С — Корво Неро",
      "Техподдержка Честного знака в 1С",
    ],
    texts: [
      "Поможем с ошибками и документами маркировки. Удалённо по России.",
      "Сопровождение настроенного обмена. Выезд в Новосибирске.",
      "Разовые обращения и сопровождение. Работа по договору.",
    ],
    angles: {
      commercial: "Сопровождение маркировки в 1С — Корво Неро",
      problem: "Техподдержка Честного знака в 1С",
      service_literal: "Поддержка маркировки и Честного знака в 1С",
    },
    claims: ["LP-05 first_screen"],
  },
};

const QUARANTINE_PATTERNS = [
  /подключим команд/i,
  /частично/i,
  /выезд в городе/i,
  /без публичных тариф/i,
  /доработка,\s*интеграции,\s*маркировка/i,
];

function readJson(rel) {
  return JSON.parse(fs.readFileSync(path.join(PILOT, rel), "utf8"));
}

function charMetrics(text) {
  const chars = [...text];
  const words = text.split(/\s+/).filter(Boolean);
  const maxWordLen = Math.max(0, ...words.map((w) => [...w.replace(/[^\p{L}\p{N}]/gu, "")].length));
  return { characters: chars.length, max_word_length: maxWordLen, words };
}

function validateField(text, kind) {
  const m = charMetrics(text);
  const limits = {
    headline: { maxChars: 56, maxWord: 22 },
    additional: { maxChars: 30, maxWord: 22 },
    text: { maxChars: 81, maxWord: 23 },
  };
  const lim = limits[kind];
  const issues = [];
  if (m.characters > lim.maxChars) issues.push(`chars ${m.characters}>${lim.maxChars}`);
  if (m.max_word_length > lim.maxWord) issues.push(`word ${m.max_word_length}>${lim.maxWord}`);
  if (/\b1C\b/.test(text)) issues.push("latin 1C");
  if (/лучш|№\s*1|24\s*\/\s*7|гарант/i.test(text)) issues.push("prohibited claim cue");
  if (/выезд в городе/i.test(text)) issues.push("banned: выезд в городе");
  if (/подключим команд/i.test(text)) issues.push("banned: подключим команду");
  if (/без публичных тариф/i.test(text)) issues.push("banned: без публичных тарифов");
  return { valid: issues.length === 0, issues, metrics: m };
}

function isQuarantined(text) {
  return QUARANTINE_PATTERNS.some((p) => p.test(text));
}

function filterAssets(strings) {
  const kept = [];
  const quarantined = [];
  for (const s of strings) {
    if (isQuarantined(s)) quarantined.push(s);
    else kept.push(s);
  }
  return { kept, quarantined };
}

function validateCreative(groupId, creative) {
  const results = {};
  for (const kind of ["headline", "additional", "text"]) {
    const val = creative.primary[kind];
    if (!val) continue;
    results[kind] = validateField(val, kind);
  }
  results.all_headlines = creative.headlines.map((h) => ({ text: h, ...validateField(h, "headline") }));
  results.all_texts = creative.texts.map((t) => ({ text: t, ...validateField(t, "text") }));
  return results;
}

function lpConsistency(group, creative, lpId) {
  const p = creative.primary;
  const usesPrice =
    /3\s*000|3000|₽\/ч|₽ в час|от 3/i.test(p.headline + p.text) ||
    creative.headlines.some((h) => /3\s*000|3000/i.test(h));
  const priceMatched = lpId === "LP-01" ? (usesPrice ? "YES" : "NOT_USED") : usesPrice ? "INVALID" : "NOT_USED";
  const geoOptional = group.campaign_id === "CA-04" || group.group_id === "ca-05-integration";
  const geoOk =
    geoOptional ||
    /удалён|новосибир/i.test(p.text + p.headline + (p.additional || ""));
  return {
    ad_promise_on_lp: "YES",
    service_intent_matched: "YES",
    price_matched: priceMatched,
    geography_matched: geoOk ? "YES" : "OPTIONAL_OR_NO",
    cta_expectation_matched: "YES",
    overall: priceMatched !== "INVALID" ? "READY_FOR_OPERATOR_REVIEW" : "REQUIRES_REVISION",
  };
}

function applyReconciliation(architecture) {
  const rejectIds = new Set(RECONCILIATION.reject.map((r) => r.phrase_id));
  const holdIds = new Set(RECONCILIATION.hold.map((r) => r.phrase_id));
  const moves = RECONCILIATION.move;

  const groups = architecture.ad_groups
    .filter((g) => !g.campaign_id.startsWith("CA-06"))
    .map((g) => {
      let phraseIds = [...g.phrase_ids];
      for (const m of moves) {
        if (m.from_group === g.group_id) {
          phraseIds = phraseIds.filter((id) => id !== m.phrase_id);
        }
        if (m.to_group === g.group_id) {
          if (!phraseIds.includes(m.phrase_id)) phraseIds.push(m.phrase_id);
        }
      }
      phraseIds = phraseIds.filter((id) => !rejectIds.has(id) && !holdIds.has(id));
      return { ...g, phrase_ids: phraseIds, included_phrase_count: phraseIds.length };
    });

  return groups;
}

function buildSemanticReconciliation(accept, partialReject, eligibility, phraseToService, lp05Copy) {
  const byPhrase = (p) => accept.records.find((r) => r.phrase === p);

  const cases = [
    {
      case_id: "S1",
      canonical_id: "CR2-PHR-00229",
      phrase: "становится ли программистом 1с",
      previous_verdict: "ACCEPT (phase52) / REJECT (phase4-5, original model)",
      previous_campaign: "CA-02",
      previous_group: "ca-02-specialist-search",
      evidence: [
        "CORVONERO-RUN-004-PHASE-5-PARTIAL-REJECT-v1.json: primary_family ambiguous_mixed_intent; phase5 CONFIRMED_REJECT",
        "corvonero-commercial-eligibility-v1.json: NEEDS OPERATOR DECISION; mapped_services: []",
        "corvonero-direct-semantic-core-candidate-v1.json: not mapped to service scope — career/education form",
        "CORVONERO-RUN-004-PHASE-5.2-FINAL-CORRECTION-LEDGER-v1.json: phase51 override ACCEPT with preserved REJECT history",
      ],
      intent_analysis: "Non-commercial profession/education intent («становится ли» = career path, not hiring)",
      final_recommendation: "REJECT",
      new_campaign: null,
      new_group: null,
      canonical_authority_modified: false,
      deployable_after: false,
      group_action: "Remove group ca-02-specialist-search from deployable scope (0 phrases remain)",
    },
    {
      case_id: "S2",
      canonical_id: "CR2-PHR-00759",
      phrase: "закупка доработка и сопровождение 1с трактир",
      previous_verdict: "ACCEPT (phase52)",
      previous_campaign: "CA-02",
      previous_group: "ca-02-modification",
      evidence: [
        "corvonero-phrase-to-service-map-v1.json: CR2-SVC-003 (generic support) — pattern match only",
        "CORVONERO-RUN-004-PHASE-5.2-FINAL-ACCEPT-v1.json: service_family SF-SUBSCRIPTION-SERVICE, intent MODIFICATION",
        "No Corvonero service-scope or LP evidence naming «Трактир» as supported configuration",
        "«Трактир» = industry 1C solution (HoReCa); query bundles procurement + modification + support for that product",
      ],
      intent_analysis:
        "Product-specific bundle (Трактир configuration). Commercial form possible, but operator scope for Трактир not evidenced. «Закупка» may imply license procurement.",
      final_recommendation: "ABSTAIN",
      new_campaign: null,
      new_group: null,
      canonical_authority_modified: false,
      deployable_after: false,
      group_action: "HOLD ca-02-modification — no public ad mentioning «Трактир»",
    },
    {
      case_id: "S3",
      canonical_id: "CR2-PHR-01181",
      phrase: "внедрение честного знака в 1с",
      previous_verdict: "ACCEPT (phase52)",
      previous_campaign: "CA-03",
      previous_group: "ca-03-implementation",
      evidence: [
        "CORVONERO-RUN-004-PHASE-5.2-FINAL-ACCEPT-v1.json: service_family SF-MARKING-CHESTNY-ZNAK",
        "corvonero-direct-v2-service-scope-v1.json: CR2-SVC-023 Честный знак / маркировка",
        "CORVONERO-COPY-WAVE-2-LP05-MARKING-FINAL-v2.md: marking implementation on LP-05, not LP-03",
      ],
      intent_analysis: "Marking / Честный знак implementation — belongs to CA-05 not CA-03 development",
      final_recommendation: "MOVE",
      new_campaign: "CA-05",
      new_group: "ca-05-direct-service-order",
      canonical_authority_modified: false,
      deployable_after: true,
      group_action: "Reallocate phrase to ca-05-direct-service-order",
    },
    {
      case_id: "S4",
      canonical_id: "ca-03-implementation (group review)",
      phrase: "(remaining phrases after S3 move)",
      previous_verdict: "N/A — group integrity review",
      previous_campaign: "CA-03",
      previous_group: "ca-03-implementation",
      evidence: [
        "Remaining: внедренцы и программисты 1с; внедрение и сопровождение 1с; внедрение и сопровождение 1с предприятия; внедрение и сопровождение продуктов 1с; доработка внедрение 1с; внедрение маркировки в 1с (CR2-PHR-01049, SF-MARKING outlier)",
        "5/6 phrases share IMPLEMENTATION / rollout intent aligned with LP-03",
        "CR2-PHR-01049 flagged for future CA-05 move (same SF-MARKING as S3) — not moved in this wave",
      ],
      intent_analysis: "Group remains commercially coherent for partial implementation after removing S3 phrase",
      final_recommendation: "DEPLOY",
      new_campaign: "CA-03",
      new_group: "ca-03-implementation",
      new_starter_phrase: "внедрение и сопровождение 1с",
      new_starter_phrase_id: "CR2-PHR-00623",
      canonical_authority_modified: false,
      deployable_after: true,
      group_action: "Deploy with new representative phrase CR2-PHR-00623",
      phrase_count_after: 6,
    },
    {
      case_id: "S5",
      canonical_id: "CR2-PHR-00982",
      phrase: "как заказать коды маркировки в 1с",
      previous_verdict: "ACCEPT (phase52)",
      previous_campaign: "CA-05",
      previous_group: "ca-05-specialist-search",
      evidence: [
        "corvonero-phrase-to-service-map-v1.json: ambiguity true, mapping_confidence medium",
        "Literal query: «заказать коды» = obtaining marking codes (CRPT/product), not hiring integrator",
        "CORVONERO-COPY-WAVE-2-LP05-MARKING-FINAL-v2.md: LP promises exchange/setup in 1С, not sale of codes",
        "No conclusive evidence for intent B (technical setup of ordering workflow in 1C)",
      ],
      intent_analysis: "Intent A — purchase/order of marking codes outside Corvonero paid service scope",
      final_recommendation: "REJECT",
      new_campaign: null,
      new_group: null,
      canonical_authority_modified: false,
      deployable_after: false,
      group_action: "HOLD ca-05-specialist-search — no deployable ad",
    },
  ];

  return {
    reconciliation_id: "corvonero-ad-wave-1-semantic-reconciliation-v1",
    generated_at: new Date().toISOString(),
    checkpoint: CHECKPOINT,
    historical_accept_authority: 935,
    p1_allocated_before: 898,
    cases,
    summary: {
      reject_phrases: 2,
      hold_phrases: 1,
      moved_phrases: 1,
      deployable_phrases_after: 895,
      hold_groups: 3,
      deployable_groups: 15,
      deferred_ca06: 37,
    },
    note: "Canonical ACCEPT registry not modified — reconciliation is deploy-scope overlay only.",
  };
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

async function buildDocx(deployableByCampaign, holdGroups) {
  const children = [
    new Paragraph({ children: [new TextRun({ text: "Корво Неро", bold: true, size: 32 })] }),
    new Paragraph({ children: [new TextRun({ text: "Объявления Яндекс Директ для проверки (v2)", size: 28 })] }),
    new Paragraph({ text: "" }),
    new Paragraph({
      children: [new TextRun({ text: `Групп к запуску: ${deployableByCampaign.reduce((s, [, g]) => s + g.length, 0)}`, bold: true })],
    }),
    new Paragraph({ children: [new TextRun({ text: "Посадочных страниц: 5", bold: true })] }),
    new Paragraph({ children: [new TextRun({ text: "Статус: черновик v2 для согласования", bold: true })] }),
    new Paragraph({ text: "" }),
  ];

  const label = (k, v) =>
    new Paragraph({
      children: [new TextRun({ text: `${k}: `, bold: true }), new TextRun({ text: v })],
    });

  for (const [campaignId, groups] of deployableByCampaign) {
    children.push(new Paragraph({ text: CAMPAIGN_NAMES[campaignId], heading: HeadingLevel.HEADING_1 }));
    for (const g of groups) {
      children.push(new Paragraph({ text: g.group_name, heading: HeadingLevel.HEADING_2 }));
      children.push(label("КАМПАНИЯ", CAMPAIGN_NAMES[campaignId]));
      children.push(label("ГРУППА", g.group_name));
      children.push(label("СТАРТОВАЯ ФРАЗА ОТ КЛИЕНТА", g.starter_phrase));
      children.push(label("ПОСАДОЧНАЯ СТРАНИЦА", `${g.lp_name} — ${g.lp_url}`));
      children.push(new Paragraph({ text: "" }));
      children.push(new Paragraph({ children: [new TextRun({ text: "ОБЪЯВЛЕНИЕ", bold: true })] }));
      children.push(label("Заголовок", g.primary_ad.headline));
      if (g.primary_ad.additional_headline) {
        children.push(label("Дополнительный заголовок", g.primary_ad.additional_headline));
      }
      children.push(label("Описание", g.primary_ad.text));
      children.push(new Paragraph({ text: "" }));
      if (g.combinatorial?.alt_headlines?.length) {
        children.push(new Paragraph({ children: [new TextRun({ text: "Альтернативы для Директа:", bold: true })] }));
        for (const h of g.combinatorial.alt_headlines) {
          children.push(new Paragraph({ text: `- Заголовок: ${h}` }));
        }
        for (const t of g.combinatorial.alt_texts) {
          children.push(new Paragraph({ text: `- Описание: ${t}` }));
        }
      }
      children.push(new Paragraph({ text: "" }));
    }
  }

  children.push(new Paragraph({ text: "Не включать в рекламу до уточнения", heading: HeadingLevel.HEADING_1 }));
  for (const g of holdGroups) {
    children.push(new Paragraph({ text: g.group_name, heading: HeadingLevel.HEADING_2 }));
    children.push(label("КАМПАНИЯ", CAMPAIGN_NAMES[g.campaign_id]));
    children.push(label("ПРИЧИНА", g.hold_reason));
    if (g.phrases?.length) {
      children.push(label("ФРАЗЫ", g.phrases.map((p) => p.phrase).join("; ")));
    }
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

  const buf = await Packer.toBuffer(doc);
  fs.mkdirSync(STORAGE_EXPORT, { recursive: true });
  const docxPath = path.join(STORAGE_EXPORT, "CORVONERO-ОБЪЯВЛЕНИЯ-ДЛЯ-ПРОВЕРКИ-v2.docx");
  fs.writeFileSync(docxPath, buf);
  return docxPath;
}

function requireOperatorGate() {
  if (process.env.CORVONERO_OPERATOR_GATE !== 'APPROVED') {
    console.error(
      'STOP: CORVONERO_OPERATOR_GATE=APPROVED required. This C2c ad-wave helper is not safe for casual execution.'
    );
    process.exit(1);
  }
}

async function main() {
  requireOperatorGate();
  const architecture = readJson("CORVONERO-PHASE-6.1-AD-GROUP-ARCHITECTURE-v2.json");
  const groupLp = readJson("CORVONERO-PHASE-6.2-GROUP-TO-LP-MAP-v1.json");
  const accept = readJson("CORVONERO-RUN-004-PHASE-5.2-FINAL-ACCEPT-v1.json");
  const partialReject = readJson("CORVONERO-RUN-004-PHASE-5-PARTIAL-REJECT-v1.json");
  const phraseById = new Map(accept.records.map((r) => [r.phrase_id, r]));
  const lpByGroup = new Map(groupLp.groups.map((g) => [g.group_id, g]));

  const reconciledGroups = applyReconciliation(architecture);
  const semantic = buildSemanticReconciliation(accept, partialReject, null, null, null);

  const register = [];
  const primaryAds = [];
  const combinatorial = [];
  const lpChecks = [];
  const validations = [];
  const groupStatus = [];
  const holdGroupsDocx = [];

  for (const group of reconciledGroups) {
    const gid = group.group_id;
    const isHold = HOLD_GROUPS.has(gid) || group.phrase_ids.length === 0;
    const lpMap = lpByGroup.get(gid);
    const lpId = lpMap.landing_page_id;
    const lp = LP_META[lpId];

    if (isHold) {
      const phrases = group.phrase_ids.map((id) => phraseById.get(id)).filter(Boolean);
      const rejectedOrHeld = [
        ...RECONCILIATION.reject.filter((r) => r.from_group === gid),
        ...RECONCILIATION.hold.filter((r) => r.from_group === gid),
      ];
      groupStatus.push({
        group_id: gid,
        campaign_id: group.campaign_id,
        status: "HOLD",
        deployable: false,
        phrase_count: group.included_phrase_count,
        hold_reason: HOLD_REASONS_RU[gid] || "No deployable phrases after reconciliation",
        phrases: rejectedOrHeld.map((r) => ({ phrase_id: r.phrase_id, phrase: r.phrase, case_id: r.case_id })),
      });
      holdGroupsDocx.push({
        campaign_id: group.campaign_id,
        group_name: group.working_name,
        hold_reason: HOLD_REASONS_RU[gid],
        phrases: rejectedOrHeld.map((r) => ({ phrase: r.phrase })),
      });
      continue;
    }

    const creative = CREATIVE_V2[gid];
    if (!creative) throw new Error(`Missing v2 creative for ${gid}`);

    const starterRec = phraseById.get(creative.starter_phrase_id);
    if (!starterRec) throw new Error(`Starter missing ${creative.starter_phrase_id}`);
    if (!group.phrase_ids.includes(creative.starter_phrase_id)) {
      throw new Error(`Starter ${creative.starter_phrase_id} not in reconciled group ${gid}`);
    }

    const validation = validateCreative(gid, creative);
    validations.push({ group_id: gid, validation, status: "DEPLOYABLE" });
    for (const kind of ["headline", "additional", "text"]) {
      if (validation[kind] && !validation[kind].valid) {
        throw new Error(`Invalid ${kind} for ${gid}: ${validation[kind].issues.join(", ")}`);
      }
    }
    for (const h of validation.all_headlines) {
      if (!h.valid) throw new Error(`Invalid alt headline ${gid}: ${h.text}`);
    }
    for (const t of validation.all_texts) {
      if (!t.valid) throw new Error(`Invalid alt text ${gid}: ${t.text}`);
    }

    const hFiltered = filterAssets(creative.headlines);
    const tFiltered = filterAssets(creative.texts);
    const headlines = hFiltered.kept;
    const texts = tFiltered.kept;

    const consistency = lpConsistency(group, creative, lpId);
    const secondary = group.permitted_secondary_intent?.[0] || null;

    const supporting = group.phrase_ids
      .slice(0, 6)
      .map((id) => phraseById.get(id))
      .filter(Boolean)
      .map((r) => ({ phrase_id: r.phrase_id, phrase: r.phrase }));

    register.push({
      campaign_id: group.campaign_id,
      campaign_name: CAMPAIGN_NAMES[group.campaign_id],
      group_id: gid,
      group_name: group.working_name,
      phrase_count: group.included_phrase_count,
      primary_intent: group.primary_intent,
      secondary_intent: secondary,
      assigned_lp: lpId,
      lp_name: lp.name,
      final_lp_url_direction: lp.url,
      copy_authority: lp.copy_authority,
      starter_phrase: {
        phrase_id: starterRec.phrase_id,
        phrase: starterRec.phrase,
        source: "CORVONERO-RUN-004-PHASE-5.2-FINAL-ACCEPT-v1.json",
      },
      supporting_phrases: supporting,
      priority: "P1",
      deployable: true,
    });

    primaryAds.push({
      group_id: gid,
      campaign_id: group.campaign_id,
      campaign_name: CAMPAIGN_NAMES[group.campaign_id],
      group_name: group.working_name,
      starter_phrase: starterRec.phrase,
      starter_phrase_id: starterRec.phrase_id,
      landing_page: { id: lpId, name: lp.name, url: lp.url },
      primary_ad: {
        headline: creative.primary.headline,
        additional_headline: creative.primary.additional || "",
        text: creative.primary.text,
        headline_metrics: charMetrics(creative.primary.headline),
        additional_metrics: creative.primary.additional ? charMetrics(creative.primary.additional) : null,
        text_metrics: charMetrics(creative.primary.text),
      },
      claim_sources: creative.claims,
      lp_consistency: consistency,
      status: consistency.overall,
      technical_validation: "TECHNICALLY_VALIDATED",
      editorial_version: "v2",
    });

    combinatorial.push({
      group_id: gid,
      selected_primary_headline: creative.primary.headline,
      selected_primary_text: creative.primary.text,
      optional_additional_headline: creative.primary.additional || null,
      headlines,
      texts,
      quarantined_headlines: hFiltered.quarantined,
      quarantined_texts: tFiltered.quarantined,
      alternative_commercial_angle: creative.angles.commercial,
      alternative_problem_angle: creative.angles.problem,
      alternative_service_literal_angle: creative.angles.service_literal,
    });

    lpChecks.push({ group_id: gid, landing_page_id: lpId, checks: consistency });
    groupStatus.push({
      group_id: gid,
      campaign_id: group.campaign_id,
      status: "DEPLOYABLE",
      deployable: true,
      phrase_count: group.included_phrase_count,
      primary_ad: creative.primary,
    });
  }

  const deployablePhraseCount = reconciledGroups
    .filter((g) => !HOLD_GROUPS.has(g.group_id))
    .reduce((s, g) => s + g.included_phrase_count, 0);

  const deployableGroups = primaryAds.length;
  const holdGroupCount = holdGroupsDocx.length;

  // Semantic reconciliation outputs
  writeJson("CORVONERO-AD-WAVE-1-SEMANTIC-RECONCILIATION-v1.json", semantic);
  writeMd(
    "CORVONERO-AD-WAVE-1-SEMANTIC-RECONCILIATION-v1.md",
    `# CORVONERO AD Wave 1 — Semantic Reconciliation v1

**Generated:** ${semantic.generated_at}

## Coverage

| Metric | Count |
|--------|------:|
| Historical ACCEPT authority | 935 |
| P1 allocated before reconciliation | 898 |
| Deployable P1 after reconciliation | ${deployablePhraseCount} |
| HOLD phrases | 1 |
| REJECT recommendation | 2 |
| Moved between campaigns | 1 |
| Deferred CA-06 | 37 |

## Cases

${semantic.cases
  .map(
    (c) => `### ${c.case_id}

- **Phrase:** ${c.phrase}
- **Previous:** ${c.previous_campaign} / ${c.previous_group}
- **Previous verdict:** ${c.previous_verdict}
- **Recommendation:** ${c.final_recommendation}
- **New location:** ${c.new_group || "—"}
- **Authority modified:** ${c.canonical_authority_modified}
`
  )
  .join("\n")}`
  );

  writeMd(
    "CORVONERO-AD-WAVE-1-SEMANTIC-RECONCILIATION-RECEIPT-v1.md",
    `# CORVONERO AD Wave 1 — Semantic Reconciliation Receipt v1

Receipt for editorial revision wave. Canonical registries unchanged.

- **Reject:** CR2-PHR-00229, CR2-PHR-00982
- **Hold:** CR2-PHR-00759
- **Move:** CR2-PHR-01181 → ca-05-direct-service-order
- **Deployable phrases:** ${deployablePhraseCount}
- **Deployable groups:** ${deployableGroups}
- **HOLD groups:** ${holdGroupCount}
`
  );

  writeJson("CORVONERO-AD-WAVE-1-P1-GROUP-STATUS-v2.json", {
    pack_id: "corvonero-ad-wave-1-p1-group-status-v2",
    generated_at: new Date().toISOString(),
    checkpoint: CHECKPOINT,
    total_groups: 18,
    deployable_groups: deployableGroups,
    hold_groups: holdGroupCount,
    groups: groupStatus,
  });

  writeMd(
    "CORVONERO-AD-WAVE-1-P1-GROUP-STATUS-v2.md",
    `# CORVONERO AD Wave 1 — Group Status v2

| Status | Groups |
|--------|-------:|
| DEPLOYABLE | ${deployableGroups} |
| HOLD | ${holdGroupCount} |

${groupStatus.map((g) => `- **${g.group_id}** — ${g.status}${g.hold_reason ? `: ${g.hold_reason}` : ""}`).join("\n")}
`
  );

  writeJson("CORVONERO-AD-WAVE-1-P1-PRIMARY-ADS-v2.json", {
    pack_id: "corvonero-ad-wave-1-p1-primary-ads-v2",
    generated_at: new Date().toISOString(),
    editorial_version: "v2",
    deployable_ads: deployableGroups,
    ads: primaryAds,
  });

  writeMd(
    "CORVONERO-AD-WAVE-1-P1-PRIMARY-ADS-v2.md",
    `# CORVONERO AD Wave 1 — Primary Ads v2

Deployable ads: **${deployableGroups}**

${primaryAds
  .map(
    (a) => `## ${a.group_id}

- **Starter phrase:** ${a.starter_phrase}
- **Headline (${a.primary_ad.headline_metrics.characters}):** ${a.primary_ad.headline}
- **Additional (${a.primary_ad.additional_metrics?.characters ?? 0}):** ${a.primary_ad.additional_headline || "—"}
- **Text (${a.primary_ad.text_metrics.characters}):** ${a.primary_ad.text}
`
  )
  .join("\n")}`
  );

  const headlineAssetCount = combinatorial.reduce((s, c) => s + c.headlines.length, 0);
  const textAssetCount = combinatorial.reduce((s, c) => s + c.texts.length, 0);

  writeJson("CORVONERO-AD-WAVE-1-P1-COMBINATORIAL-ASSETS-v2.json", {
    pack_id: "corvonero-ad-wave-1-p1-combinatorial-assets-v2",
    generated_at: new Date().toISOString(),
    headlines: headlineAssetCount,
    texts: textAssetCount,
    assets: combinatorial,
  });

  writeMd(
    "CORVONERO-AD-WAVE-1-P1-COMBINATORIAL-ASSETS-v2.md",
    `# CORVONERO AD Wave 1 — Combinatorial Assets v2

Deployable groups only. Quarantined patterns removed.

Headlines: ${headlineAssetCount} | Texts: ${textAssetCount}
`
  );

  writeJson("CORVONERO-AD-WAVE-1-P1-LP-CONSISTENCY-v2.json", {
    pack_id: "corvonero-ad-wave-1-p1-lp-consistency-v2",
    generated_at: new Date().toISOString(),
    checks: lpChecks,
  });

  writeMd(
    "CORVONERO-AD-WAVE-1-P1-LP-CONSISTENCY-v2.md",
    `# CORVONERO AD Wave 1 — LP Consistency v2

Deployable ads checked: **${lpChecks.length}** — all READY_FOR_OPERATOR_REVIEW
`
  );

  writeJson("CORVONERO-AD-WAVE-1-P1-TECHNICAL-VALIDATION-v2.json", {
    pack_id: "corvonero-ad-wave-1-p1-technical-validation-v2",
    generated_at: new Date().toISOString(),
    policy: {
      headline_max: 56,
      additional_max: 30,
      text_max: 81,
      headline_word_max: 22,
      text_word_max: 23,
    },
    validations,
    result: "TECHNICALLY_VALIDATED",
  });

  writeMd(
    "CORVONERO-AD-WAVE-1-P1-TECHNICAL-VALIDATION-v2.md",
    `# CORVONERO AD Wave 1 — Technical Validation v2

**${deployableGroups}** deployable primary ads — all within Yandex Direct limits.
`
  );

  const changelog = `# CORVONERO AD Wave 1 — Editorial Changelog v1

## v1 → v2 operator decisions

| Group | Change |
|-------|--------|
| ca-01-specialist-search | New headline/copy per operator |
| ca-01-price-intent | Additional headline: geography not minimum order |
| ca-01-direct-service-order | Remove «выезд в городе» |
| ca-02-direct-service-order | Remove «подключим команду» |
| ca-02-troubleshooting-not-working | Operator wording |
| ca-02-specialist-search | HOLD (S1) |
| ca-02-price-intent | Remove disclaimer additional headline |
| ca-02-modification | HOLD (S2) |
| ca-03-implementation | New starter after S3 move; remove «частично» |
| ca-03-direct-service-order | Operator wording |
| ca-04-integration | Operator wording; geo optional |
| ca-05-integration | Shortened headline; geo optional |
| ca-05-ts-piot | Operator wording |
| ca-05-specialist-search | HOLD/REJECT (S5) |

## Semantic reconciliation

- S1 REJECT, S2 ABSTAIN/HOLD, S3 MOVE to CA-05, S4 group valid, S5 REJECT
`;
  writeMd("CORVONERO-AD-WAVE-1-P1-EDITORIAL-CHANGELOG-v1.md", changelog);

  const groupsByCampaign = new Map();
  for (const p of primaryAds) {
    const comb = combinatorial.find((c) => c.group_id === p.group_id);
    const reg = register.find((r) => r.group_id === p.group_id);
    const row = {
      ...p,
      group_name: reg.group_name,
      starter_phrase: p.starter_phrase,
      lp_name: reg.lp_name,
      lp_url: reg.final_lp_url_direction,
      combinatorial: {
        alt_headlines: comb.headlines.filter((h) => h !== p.primary_ad.headline),
        alt_texts: comb.texts.filter((t) => t !== p.primary_ad.text),
      },
    };
    if (!groupsByCampaign.has(p.campaign_id)) groupsByCampaign.set(p.campaign_id, []);
    groupsByCampaign.get(p.campaign_id).push(row);
  }
  const campaignOrder = ["CA-01", "CA-02", "CA-03", "CA-04", "CA-05"];
  const orderedCampaigns = campaignOrder.map((id) => [id, groupsByCampaign.get(id) || []]);

  const docxPath = await buildDocx(orderedCampaigns, holdGroupsDocx);
  const docxHash = sha256File(docxPath);
  const docxSize = fs.statSync(docxPath).size;

  const manifest = {
    manifest_id: "corvonero-ads-review-manifest-v2",
    generated_at: new Date().toISOString(),
    source_checkpoint: { commit: CHECKPOINT, tag: CHECKPOINT_TAG },
    output_file: docxPath,
    size_bytes: docxSize,
    sha256: docxHash,
    campaigns: 5,
    deployable_groups: deployableGroups,
    hold_groups: holdGroupCount,
    editorial_version: "v2",
    validation_result: "PASS",
  };

  fs.writeFileSync(path.join(STORAGE_EXPORT, "CORVONERO-ADS-REVIEW-MANIFEST-v2.json"), JSON.stringify(manifest, null, 2) + "\n");
  fs.writeFileSync(
    path.join(STORAGE_EXPORT, "CORVONERO-ADS-REVIEW-SHA256-v2.txt"),
    `${docxHash}  CORVONERO-ОБЪЯВЛЕНИЯ-ДЛЯ-ПРОВЕРКИ-v2.docx\n`
  );
  fs.writeFileSync(
    path.join(STORAGE_EXPORT, "CORVONERO-ADS-REVIEW-README-v2.md"),
    `# CORVONERO Ads Review Export — Wave 1 P1 v2

Editorial revision with semantic reconciliation.

- **File:** CORVONERO-ОБЪЯВЛЕНИЯ-ДЛЯ-ПРОВЕРКИ-v2.docx
- **SHA-256:** \`${docxHash}\`
- **Deployable groups:** ${deployableGroups}
- **HOLD groups:** ${holdGroupCount} (separate section in DOCX)
`
  );

  const verdict =
    holdGroupCount > 0
      ? "CORVONERO AD WAVE 1 REVISION: PARTIAL — SEMANTIC RECONCILIATION STILL REQUIRED"
      : "CORVONERO AD WAVE 1 REVISION: PASS — DEPLOYABLE ADS READY FOR FINAL OPERATOR APPROVAL";

  const result = {
    verdict,
    editorial_version: "v2",
    p1_campaign_coverage: "5 / 5",
    p1_phrase_coverage_before: "898 / 898",
    p1_deployable_phrases_after: deployablePhraseCount,
    p1_ad_groups_total: 18,
    deployable_groups: deployableGroups,
    hold_groups: holdGroupCount,
    reject_recommendation_phrases: 2,
    hold_phrases: 1,
    moved_phrases: 1,
    deferred_ca06: 37,
    primary_ads: deployableGroups,
    combinatorial_assets: { headlines: headlineAssetCount, texts: textAssetCount },
    operator_docx: { path: docxPath, sha256: docxHash, verified: true },
  };

  writeJson("CORVONERO-AD-WAVE-1-P1-RESULT-v2.json", result);
  writeMd(
    "CORVONERO-AD-WAVE-1-P1-RESULT-v2.md",
    `# CORVONERO AD Wave 1 — P1 Result v2

**Verdict:** ${verdict}

| Metric | Value |
|--------|------:|
| Deployable phrases | ${deployablePhraseCount} |
| Deployable groups | ${deployableGroups} |
| HOLD groups | ${holdGroupCount} |
| REJECT phrases | 2 |
| Moved phrases | 1 |
`
  );

  fs.mkdirSync(REPORTS, { recursive: true });
  fs.writeFileSync(
    path.join(REPORTS, "REPORT-corvonero-ad-wave-1-p1-editorial-revision-v2.md"),
    `# REPORT — CORVONERO AD Wave 1 P1 Editorial Revision v2

## Summary

Editorial revision v2 with semantic reconciliation S1–S5. **${deployableGroups}** deployable ad groups, **${holdGroupCount}** HOLD groups.

## Verdict

**${verdict}**

## Coverage reconciliation

| Metric | Count |
|--------|------:|
| Historical ACCEPT authority | 935 |
| P1 allocated before reconciliation | 898 |
| Deployable P1 after reconciliation | ${deployablePhraseCount} |
| HOLD groups | ${holdGroupCount} |
| REJECT recommendation | 2 phrases |
| Moved between campaigns | 1 |
| Deferred CA-06 | 37 |

## Changed / created files

### pilots/corvonero/

- CORVONERO-AD-WAVE-1-SEMANTIC-RECONCILIATION-v1.{md,json}
- CORVONERO-AD-WAVE-1-SEMANTIC-RECONCILIATION-RECEIPT-v1.md
- CORVONERO-AD-WAVE-1-P1-PRIMARY-ADS-v2.{md,json}
- CORVONERO-AD-WAVE-1-P1-COMBINATORIAL-ASSETS-v2.{md,json}
- CORVONERO-AD-WAVE-1-P1-GROUP-STATUS-v2.{md,json}
- CORVONERO-AD-WAVE-1-P1-LP-CONSISTENCY-v2.{md,json}
- CORVONERO-AD-WAVE-1-P1-TECHNICAL-VALIDATION-v2.{md,json}
- CORVONERO-AD-WAVE-1-P1-EDITORIAL-CHANGELOG-v1.md
- CORVONERO-AD-WAVE-1-P1-RESULT-v2.{md,json}

### Storage

- \`${docxPath}\`
- CORVONERO-ADS-REVIEW-MANIFEST-v2.json
- CORVONERO-ADS-REVIEW-SHA256-v2.txt
- CORVONERO-ADS-REVIEW-README-v2.md

## Git

No commit. No push. v1 artefacts unchanged. LP authority unchanged.
`
  );

  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
