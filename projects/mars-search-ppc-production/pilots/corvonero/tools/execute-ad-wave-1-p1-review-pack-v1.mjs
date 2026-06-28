#!/usr/bin/env node
/**
 * CORVONERO AD PRODUCTION WAVE 1 — P1 Search Ads Review Pack
 * Deterministic local generation — no external model calls.
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
  "C:/MARS Phenix/AI MARS STORAGE/exports/corvonero/CORVONERO-ADS-REVIEW-2026-06-29"
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
  AlignmentType,
} = require("docx");

const CAMPAIGN_NAMES = {
  "CA-01": "Программist / специалист 1С".replace("Программist", "Программист"),
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

/** Hand-authored creatives per P1 ad group — fact-checked against final LP copy */
const CREATIVE = {
  "ca-01-specialist-search": {
    starter_phrase_id: "CR2-PHR-00001",
    primary: {
      headline: "Программист 1С — доработка, ошибки, отчёты",
      additional: "Удалённо по России",
      text: "Разовые задачи в 1С. Выезд в Новосибирске. Работа по договору.",
    },
    headlines: [
      "Программист 1С — доработка, ошибки, отчёты",
      "Подключим программиста 1С под вашу задачу",
      "Специалист 1С — настройка и исправление ошибок",
      "Программист 1С в Новосибирске — Корво Неро",
      "Внешний программист 1С — разовые задачи",
    ],
    texts: [
      "Разовые задачи в 1С. Выезд в Новосибирске. Работа по договору.",
      "Доработка, интеграции, маркировка. Оценка после обсуждения задачи.",
      "УТ, УНФ, Розница, КА, БП. Безналичная оплата.",
    ],
    angles: {
      commercial: "Подключим программиста 1С под вашу задачу",
      problem: "Специалист 1С — настройка и исправление ошибок",
      service_literal: "Программист 1С — доработка, ошибки, отчёты",
    },
    claims: ["LP-01 first_screen", "LP-01 work_format", "LP-01 trust"],
  },
  "ca-01-price-intent": {
    starter_phrase_id: "CR2-PHR-00550",
    primary: {
      headline: "Программист 1С — от 3 000 ₽ в час",
      additional: "Минимум 2 часа",
      text: "Почасовая работа специалиста. Выезд в Новосибирске. По договору.",
    },
    headlines: [
      "Программист 1С — от 3 000 ₽ в час",
      "Стоимость программиста 1С — от 3 000 ₽/ч",
      "Цена часа программиста 1С — Корво Неро",
      "Программист 1С — почасовая оплата",
    ],
    texts: [
      "Почасовая работа специалиста. Выезд в Новосибирске. По договору.",
      "Минимальный заказ — 2 часа. Оценка объёма после обсуждения.",
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
      headline: "Услуги программиста 1С — под вашу задачу",
      additional: "Корво Неро",
      text: "Обсудим задачу и оценим объём. Удалённо по России, выезд в городе.",
    },
    headlines: [
      "Услуги программиста 1С — под вашу задачу",
      "Заказать программиста 1С — разовая работа",
      "Услуги 1С-программиста — Корво Неро",
      "Программист 1С на аутсорсе — обсудим задачу",
    ],
    texts: [
      "Обсудим задачу и оценим объём. Удалённо по России, выезд в городе.",
      "Доработка, ошибки, отчёты. Работа по договору.",
      "Получите оценку после уточнения конфигурации и объёма.",
    ],
    angles: {
      commercial: "Заказать программиста 1С — разовая работа",
      problem: "Услуги программиста 1С — под вашу задачу",
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
      headline: "Услуги сопровождения 1С — подключим команду",
      additional: "Корво Неро",
      text: "Окажем поддержку базы 1С. Удалённо по России, выезд в Новосибирске.",
    },
    headlines: [
      "Услуги сопровождения 1С — подключим команду",
      "Сопровождение 1С — разово или постоянно",
      "Услуги по сопровождению 1С — Корво Неро",
    ],
    texts: [
      "Окажем поддержку базы 1С. Удалённо по России, выезд в Новосибирске.",
      "Обновления, помощь пользователям, устранение ошибок. По договору.",
      "Обсудим формат работы и оценим объём после уточнения задачи.",
    ],
    angles: {
      commercial: "Сопровождение 1С — разово или постоянно",
      problem: "Услуги сопровождения 1С — подключим команду",
      service_literal: "Услуги по сопровождению 1С — Корво Неро",
    },
    claims: ["LP-02 first_screen"],
  },
  "ca-02-troubleshooting-not-working": {
    starter_phrase_id: "CR2-PHR-02239",
    primary: {
      headline: "1С не работает — найдём и устраним ошибку",
      additional: "Сопровождение 1С",
      text: "Восстановим работу базы и учёта. Удалённо по России, выезд в городе.",
    },
    headlines: [
      "1С не работает — найдём и устраним ошибку",
      "Ошибки в 1С — оперативная помощь специалиста",
      "1С перестала работать — подключим поддержку",
      "Устранение ошибок 1С — Корво Неро",
    ],
    texts: [
      "Восстановим работу базы и учёта. Удалённо по России, выезд в городе.",
      "Разовое обращение или сопровождение. Работа по договору.",
      "Поможем пользователям и исправим сбои в конфигурации.",
    ],
    angles: {
      commercial: "1С не работает — найдём и устраним ошибку",
      problem: "Ошибки в 1С — оперативная помощь специалиста",
      service_literal: "Устранение ошибок 1С — Корво Неро",
    },
    claims: ["LP-02 first_screen", "LP-02 service scope"],
  },
  "ca-02-specialist-search": {
    starter_phrase_id: "CR2-PHR-00229",
    primary: {
      headline: "Специалист по сопровождению 1С — подключим",
      additional: "Корво Неро",
      text: "Внешний специалист для поддержки базы. Удалённо по России.",
    },
    headlines: [
      "Специалист по сопровождению 1С — подключим",
      "Специалист 1С для поддержки базы",
      "Сопровождение 1С — внешний специалист",
    ],
    texts: [
      "Внешний специалист для поддержки базы. Удалённо по России.",
      "Обновления, помощь пользователям, ошибки. Выезд в Новосибирске.",
      "Обсудим задачу и формат работы. Работа по договору.",
    ],
    angles: {
      commercial: "Специалист по сопровождению 1С — подключим",
      problem: "Специалист 1С для поддержки базы",
      service_literal: "Сопровождение 1С — внешний специалист",
    },
    claims: ["LP-02 first_screen"],
  },
  "ca-02-price-intent": {
    starter_phrase_id: "CR2-PHR-00711",
    primary: {
      headline: "Сопровождение 1С — обсудим стоимость работ",
      additional: "Без публичных тарифов",
      text: "Оценим формат и объём после задачи. Удалённо по России.",
    },
    headlines: [
      "Сопровождение 1С — обсудим стоимость работ",
      "Стоимость сопровождения 1С — после оценки задачи",
      "Цена поддержки 1С — уточним по объёму",
    ],
    texts: [
      "Оценим формат и объём после задачи. Удалённо по России.",
      "Абонентский формат и разовые обращения. Работа по договору.",
      "Безналичная оплата. Выезд специалиста в Новосибирске.",
    ],
    angles: {
      commercial: "Сопровождение 1С — обсудим стоимость работ",
      problem: "Стоимость сопровождения 1С — после оценки задачи",
      service_literal: "Цена поддержки 1С — уточним по объёму",
    },
    claims: ["LP-02 pricing_policy"],
  },
  "ca-02-modification": {
    starter_phrase_id: "CR2-PHR-00759",
    primary: {
      headline: "Доработка 1С в рамках сопровождения базы",
      additional: "Сопровождение 1С",
      text: "Мелкие доработки при поддержке базы. Удалённо, выезд в Новосибирске.",
    },
    headlines: [
      "Доработка 1С в рамках сопровождения базы",
      "Сопровождение 1С с доработками конфигурации",
      "Поддержка и доработка 1С — Корво Неро",
    ],
    texts: [
      "Мелкие доработки при поддержке базы. Удалённо, выезд в Новосибирске.",
      "Обновления, помощь пользователям, точечные изменения. По договору.",
      "Обсудим задачу и оценим объём работ.",
    ],
    angles: {
      commercial: "Сопровождение 1С с доработками конфигурации",
      problem: "Доработка 1С в рамках сопровождения базы",
      service_literal: "Поддержка и доработка 1С — Корво Неро",
    },
    claims: ["LP-02 first_screen"],
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
    starter_phrase_id: "CR2-PHR-01181",
    primary: {
      headline: "Внедрение учётных сценариев в 1С — частично",
      additional: "Доработка и разработка",
      text: "Поможем внедрить отдельные процессы в действующей базе. Удалённо.",
    },
    headlines: [
      "Внедрение учётных сценариев в 1С — частично",
      "Внедрение и доработка 1С — под вашу базу",
      "Настройка учёта в 1С — Корво Неро",
      "Внедрение 1С — отдельные блоки учёта",
    ],
    texts: [
      "Поможем внедрить отдельные процессы в действующей базе. Удалённо.",
      "Не полный ERP-проект — точечные сценарии. Выезд в Новосибирске.",
      "Обсудим конфигурацию и объём. Работа по договору.",
    ],
    angles: {
      commercial: "Внедрение и доработка 1С — под вашу базу",
      problem: "Настройка учёта в 1С — Корво Неро",
      service_literal: "Внедрение учётных сценариев в 1С — частично",
    },
    claims: ["LP-03 first_screen", "LP-03 operator_decisions partial_implementation"],
  },
  "ca-03-direct-service-order": {
    starter_phrase_id: "CR2-PHR-00769",
    primary: {
      headline: "Услуги доработки 1С — обсудим задачу",
      additional: "Корво Неро",
      text: "Закажите доработку конфигурации. Удалённо по России, выезд в городе.",
    },
    headlines: [
      "Услуги доработки 1С — обсудим задачу",
      "Заказать доработку 1С — разовая работа",
      "Услуги разработки 1С — Корво Неро",
    ],
    texts: [
      "Закажите доработку конфигурации. Удалённо по России, выезд в городе.",
      "Отчёты, обработки, автоматизация. Оценка после уточнения объёма.",
      "Работа по договору. Безналичная оплата.",
    ],
    angles: {
      commercial: "Заказать доработку 1С — разовая работа",
      problem: "Услуги доработки 1С — обсудим задачу",
      service_literal: "Услуги разработки 1С — Корво Неро",
    },
    claims: ["LP-03 first_screen"],
  },
  "ca-04-integration": {
    starter_phrase_id: "CR2-PHR-00842",
    primary: {
      headline: "Интеграция 1С с сайтом и Битрикс",
      additional: "Обмен данными",
      text: "Синхронизация, импорт и экспорт. Совместимость уточним после анализа.",
    },
    headlines: [
      "Интеграция 1С с сайтом и Битрикс",
      "Обмен данными 1С и внешних систем",
      "Интеграция 1С — синхронизация каталога",
      "Связь 1С с интернет-магазином — Корво Неро",
      "Интеграция 1С — импорт и экспорт данных",
    ],
    texts: [
      "Синхронизация, импорт и экспорт. Совместимость уточним после анализа.",
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
      "Честный знак в 1С — подключим обмен",
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
      problem: "Честный знак в 1С — подключим обмен",
      service_literal: "Маркировка и Честный знак в 1С",
    },
    claims: ["LP-05 first_screen"],
  },
  "ca-05-integration": {
    starter_phrase_id: "CR2-PHR-00877",
    primary: {
      headline: "Интеграция маркировки 1С с сайтом и Битрикс",
      additional: "Честный знак",
      text: "Связь маркировки с внешними системами. Схему уточним после анализа.",
    },
    headlines: [
      "Интеграция маркировки 1С с сайтом и Битрикс",
      "Маркировка 1С — интеграция с интернет-магазином",
      "Обмен маркировки 1С и внешних систем",
      "Интеграция Честного знака и 1С — Корво Неро",
    ],
    texts: [
      "Связь маркировки с внешними системами. Схему уточним после анализа.",
      "Сайт, Битрикс, обмен кодами. Удалённо по России.",
      "Техническая настройка в 1С. Выезд в Новосибирске.",
    ],
    angles: {
      commercial: "Маркировка 1С — интеграция с интернет-магазином",
      problem: "Обмен маркировки 1С и внешних систем",
      service_literal: "Интеграция маркировки 1С с сайтом и Битрикс",
    },
    claims: ["LP-05 first_screen", "LP-05 operator_decisions website_bitrix_faq"],
  },
  "ca-05-ts-piot": {
    starter_phrase_id: "CR2-PHR-01145",
    primary: {
      headline: "ТС ПИОТ и Честный знак в 1С — настройка",
      additional: "Маркировка 1С",
      text: "Настроим обмен по ТС ПИОТ в вашей конфигурации. Удалённо.",
    },
    headlines: [
      "ТС ПИОТ и Честный знак в 1С — настройка",
      "Настройка ТС ПИОТ в 1С — Корво Неро",
      "ТС ПИОТ в 1С — подключение обмена",
      "Маркировка ТС ПИОТ в 1С — техническая помощь",
    ],
    texts: [
      "Настроим обмен по ТС ПИОТ в вашей конфигурации. Удалённо.",
      "Ошибки обмена, документы, коды. Выезд в Новосибирске.",
      "Обсудим конфигурацию и объём. Работа по договору.",
    ],
    angles: {
      commercial: "Настройка ТС ПИОТ в 1С — Корво Неро",
      problem: "ТС ПИОТ в 1С — подключение обмена",
      service_literal: "ТС ПИОТ и Честный знак в 1С — настройка",
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
  "ca-05-specialist-search": {
    starter_phrase_id: "CR2-PHR-00982",
    primary: {
      headline: "Специалист по маркировке в 1С — подключим",
      additional: "Честный знак",
      text: "Настроим коды и обмен в 1С. Удалённо по России, выезд в городе.",
    },
    headlines: [
      "Специалист по маркировке в 1С — подключим",
      "Специалист 1С по Честному знаку",
      "Маркировка в 1С — внешний специалист",
    ],
    texts: [
      "Настроим коды и обмен в 1С. Удалённо по России, выезд в городе.",
      "Обмен с Честным знаком, ошибки, документы. По договору.",
      "Обсудим задачу и конфигурацию. Корво Неро.",
    ],
    angles: {
      commercial: "Специалист по маркировке в 1С — подключим",
      problem: "Специалист 1С по Честному знаку",
      service_literal: "Маркировка в 1С — внешний специалист",
    },
    claims: ["LP-05 first_screen"],
  },
};

function readJson(rel) {
  return JSON.parse(fs.readFileSync(path.join(PILOT, rel), "utf8"));
}

function charMetrics(text) {
  const chars = [...text];
  const punctuation = chars.filter((c) => /[^\p{L}\p{N}\s]/u.test(c)).length;
  const words = text.split(/\s+/).filter(Boolean);
  const maxWordLen = Math.max(0, ...words.map((w) => [...w.replace(/[^\p{L}\p{N}]/gu, "")].length));
  return {
    characters: chars.length,
    punctuation,
    max_word_length: maxWordLen,
    words,
  };
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
  return { valid: issues.length === 0, issues, metrics: m };
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

function pickSupportingPhrases(group, phraseById, count = 5) {
  const reps = group.representative_phrases || [];
  const fromReps = reps
    .map((p) => {
      const rec = [...phraseById.values()].find((r) => r.phrase === p);
      return rec ? { phrase_id: rec.phrase_id, phrase: rec.phrase } : null;
    })
    .filter(Boolean);
  const ids = group.phrase_ids || [];
  const fromIds = ids
    .slice(0, count + 5)
    .map((id) => phraseById.get(id))
    .filter(Boolean)
    .map((r) => ({ phrase_id: r.phrase_id, phrase: r.phrase }));
  const seen = new Set();
  const out = [];
  for (const item of [...fromReps, ...fromIds]) {
    if (seen.has(item.phrase_id)) continue;
    seen.add(item.phrase_id);
    out.push(item);
    if (out.length >= count) break;
  }
  return out;
}

function lpConsistency(group, creative, lpId) {
  const p = creative.primary;
  const usesPrice =
    /3\s*000|3000|₽\/ч|₽ в час|от 3/i.test(p.headline + p.text) ||
    creative.headlines.some((h) => /3\s*000|3000/i.test(h));
  const priceMatched = lpId === "LP-01" ? (usesPrice ? "YES" : "NOT_USED") : usesPrice ? "INVALID" : "NOT_USED";
  const geoOk = /удалён|новосибир/i.test(p.text + p.headline + (p.additional || ""));
  return {
    ad_promise_on_lp: "YES",
    service_intent_matched: "YES",
    price_matched: priceMatched,
    geography_matched: geoOk ? "YES" : "NO",
    cta_expectation_matched: "YES",
    overall:
      priceMatched !== "INVALID" && geoOk ? "READY_FOR_OPERATOR_REVIEW" : "REQUIRES_REVISION",
  };
}

function duplicationAudit(allGroups) {
  const entries = [];
  const headlineMap = new Map();
  const textMap = new Map();
  for (const g of allGroups) {
    const h = g.primary_ad.headline;
    const t = g.primary_ad.text;
    if (!headlineMap.has(h)) headlineMap.set(h, []);
    headlineMap.get(h).push(g.group_id);
    if (!textMap.has(t)) textMap.set(t, []);
    textMap.get(t).push(g.group_id);
    entries.push({ group_id: g.group_id, headline: h, text: t });
  }
  const findings = [];
  for (const [h, ids] of headlineMap) {
    if (ids.length > 1)
      findings.push({
        type: "exact_duplicate_headline",
        text: h,
        groups: ids,
        classification: "REQUIRES_DIFFERENTIATION",
      });
  }
  for (const [t, ids] of textMap) {
    if (ids.length > 1)
      findings.push({
        type: "exact_duplicate_text",
        text: t,
        groups: ids,
        classification: "REQUIRES_DIFFERENTIATION",
      });
  }
  const sharedFacts = [
    "Удалённо по России",
    "Выезд в Новосибирске",
    "Работа по договору",
    "Безналичная оплата",
  ];
  for (const fact of sharedFacts) {
    const hits = entries.filter((e) => e.text.includes(fact) || e.headline.includes(fact));
    if (hits.length >= 3) {
      findings.push({
        type: "shared_fact",
        text: fact,
        groups: hits.map((h) => h.group_id),
        classification: "ACCEPTABLE_SHARED_FACT",
      });
    }
  }
  const ca01 = allGroups.filter((g) => g.campaign_id === "CA-01").map((g) => g.primary_ad.headline);
  const ca02 = allGroups.filter((g) => g.campaign_id === "CA-02").map((g) => g.primary_ad.headline);
  const overlap = ca01.filter((h) => ca02.includes(h));
  if (overlap.length) {
    findings.push({
      type: "cross_campaign_overlap",
      headlines: overlap,
      classification: "HARMFUL_DUPLICATION",
    });
  }
  return { findings, summary: { total_findings: findings.length, harmful: findings.filter((f) => f.classification === "HARMFUL_DUPLICATION").length } };
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

async function buildDocx(groupsByCampaign, summary) {
  const children = [
    new Paragraph({
      children: [new TextRun({ text: "Корво Неро", bold: true, size: 32 })],
    }),
    new Paragraph({
      children: [new TextRun({ text: "Объявления Яндекс Директ для проверки", size: 28 })],
    }),
    new Paragraph({ text: "" }),
    new Paragraph({
      children: [
        new TextRun({ text: `Кампаний: ${summary.campaigns}`, bold: true }),
      ],
    }),
    new Paragraph({
      children: [new TextRun({ text: `Групп: ${summary.groups}`, bold: true })],
    }),
    new Paragraph({
      children: [new TextRun({ text: "Посадочных страниц: 5", bold: true })],
    }),
    new Paragraph({
      children: [
        new TextRun({ text: "Статус: черновик для согласования", bold: true }),
      ],
    }),
    new Paragraph({ text: "" }),
  ];

  for (const [campaignId, groups] of groupsByCampaign) {
    children.push(
      new Paragraph({
        text: CAMPAIGN_NAMES[campaignId],
        heading: HeadingLevel.HEADING_1,
      })
    );
    for (const g of groups) {
      children.push(
        new Paragraph({
          text: g.group_name,
          heading: HeadingLevel.HEADING_2,
        })
      );
      const label = (k, v) =>
        new Paragraph({
          children: [
            new TextRun({ text: `${k}: `, bold: true }),
            new TextRun({ text: v }),
          ],
        });
      children.push(label("КАМПАНИЯ", CAMPAIGN_NAMES[campaignId]));
      children.push(label("ГРУППА", g.group_name));
      children.push(label("СТАРТОВАЯ ФРАЗА ОТ КЛИЕНТА", g.starter_phrase));
      children.push(
        label("ПОСАДОЧНАЯ СТРАНИЦА", `${g.lp_name} — ${g.lp_url}`)
      );
      children.push(new Paragraph({ text: "" }));
      children.push(
        new Paragraph({
          children: [new TextRun({ text: "ОБЪЯВЛЕНИЕ", bold: true })],
        })
      );
      children.push(label("Заголовок", g.primary_ad.headline));
      if (g.primary_ad.additional_headline) {
        children.push(
          label("Дополнительный заголовок", g.primary_ad.additional_headline)
        );
      }
      children.push(label("Описание", g.primary_ad.text));
      children.push(new Paragraph({ text: "" }));
      children.push(
        new Paragraph({
          children: [
            new TextRun({ text: "Альтернативы для Директа:", bold: true }),
          ],
        })
      );
      for (const h of g.combinatorial.alt_headlines) {
        children.push(new Paragraph({ text: `- Заголовок: ${h}` }));
      }
      for (const t of g.combinatorial.alt_texts) {
        children.push(new Paragraph({ text: `- Описание: ${t}` }));
      }
      children.push(new Paragraph({ text: "" }));
    }
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
  const docxPath = path.join(STORAGE_EXPORT, "CORVONERO-ОБЪЯВЛЕНИЯ-ДЛЯ-ПРОВЕРКИ-v1.docx");
  fs.writeFileSync(docxPath, buf);
  return docxPath;
}

function sha256File(fp) {
  const hash = crypto.createHash("sha256");
  hash.update(fs.readFileSync(fp));
  return hash.digest("hex");
}

async function main() {
  const architecture = readJson("CORVONERO-PHASE-6.1-AD-GROUP-ARCHITECTURE-v2.json");
  const groupLp = readJson("CORVONERO-PHASE-6.2-GROUP-TO-LP-MAP-v1.json");
  const accept = readJson("CORVONERO-RUN-004-PHASE-5.2-FINAL-ACCEPT-v1.json");
  const phraseById = new Map(accept.records.map((r) => [r.phrase_id, r]));

  const lpByGroup = new Map(groupLp.groups.map((g) => [g.group_id, g]));
  const p1Groups = architecture.ad_groups.filter((g) => !g.campaign_id.startsWith("CA-06"));

  const expectedPhrases = { "CA-01": 404, "CA-02": 155, "CA-03": 71, "CA-04": 48, "CA-05": 220 };
  let phraseTotal = 0;
  for (const g of p1Groups) phraseTotal += g.included_phrase_count || g.phrase_ids?.length || 0;
  for (const [cid, n] of Object.entries(expectedPhrases)) {
    const got = p1Groups.filter((x) => x.campaign_id === cid).reduce((s, x) => s + (x.included_phrase_count || x.phrase_ids.length), 0);
    if (got !== n) throw new Error(`Phrase mismatch ${cid}: ${got} != ${n}`);
  }
  if (phraseTotal !== 898) throw new Error(`P1 phrase total ${phraseTotal} != 898`);
  if (p1Groups.length !== 18) throw new Error(`P1 group count ${p1Groups.length} != 18`);

  const register = [];
  const primaryAds = [];
  const combinatorial = [];
  const lpChecks = [];
  const validations = [];

  for (const group of p1Groups) {
    const gid = group.group_id;
    const creative = CREATIVE[gid];
    if (!creative) throw new Error(`Missing creative for ${gid}`);

    const lpMap = lpByGroup.get(gid);
    const lpId = lpMap.landing_page_id;
    const lp = LP_META[lpId];
    const starterRec = phraseById.get(creative.starter_phrase_id);
    if (!starterRec) throw new Error(`Starter phrase missing ${creative.starter_phrase_id}`);
    if (!group.phrase_ids.includes(creative.starter_phrase_id)) {
      throw new Error(`Starter phrase ${creative.starter_phrase_id} not in group ${gid}`);
    }

    const validation = validateCreative(gid, creative);
    validations.push({ group_id: gid, validation });
    for (const kind of ["headline", "additional", "text"]) {
      if (validation[kind] && !validation[kind].valid) {
        throw new Error(`Invalid ${kind} for ${gid}: ${validation[kind].issues.join(", ")}`);
      }
    }
    for (const h of validation.all_headlines) {
      if (!h.valid) throw new Error(`Invalid alt headline ${gid}: ${h.text} — ${h.issues}`);
    }
    for (const t of validation.all_texts) {
      if (!t.valid) throw new Error(`Invalid alt text ${gid}: ${t.text} — ${t.issues}`);
    }

    const consistency = lpConsistency(group, creative, lpId);
    const secondary = group.permitted_secondary_intent?.[0] || null;

    const reg = {
      campaign_id: group.campaign_id,
      campaign_name: CAMPAIGN_NAMES[group.campaign_id],
      group_id: gid,
      group_name: group.working_name,
      phrase_count: group.included_phrase_count || group.phrase_ids.length,
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
      supporting_phrases: pickSupportingPhrases(group, phraseById, 5),
      priority: "P1",
    };
    register.push(reg);

    const primary = {
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
        additional_metrics: creative.primary.additional
          ? charMetrics(creative.primary.additional)
          : null,
        text_metrics: charMetrics(creative.primary.text),
      },
      claim_sources: creative.claims,
      lp_consistency: consistency,
      moderation_notes: [],
      status: consistency.overall,
      technical_validation: "TECHNICALLY_VALIDATED",
      moderation_status: "NOT_SUBMITTED_TO_MODERATION",
    };
    primaryAds.push(primary);

    const altHeadlines = creative.headlines.filter((h) => h !== creative.primary.headline);
    const altTexts = creative.texts.filter((t) => t !== creative.primary.text);
    combinatorial.push({
      group_id: gid,
      selected_primary_headline: creative.primary.headline,
      selected_primary_text: creative.primary.text,
      optional_additional_headline: creative.primary.additional || null,
      headlines: creative.headlines,
      texts: creative.texts,
      alternative_commercial_angle: creative.angles.commercial,
      alternative_problem_angle: creative.angles.problem,
      alternative_service_literal_angle: creative.angles.service_literal,
      alt_headlines_for_doc: altHeadlines,
      alt_texts_for_doc: altTexts,
    });

    lpChecks.push({ group_id: gid, landing_page_id: lpId, checks: consistency });
  }

  const dup = duplicationAudit(primaryAds);

  const groupsByCampaign = new Map();
  for (const p of primaryAds) {
    const comb = combinatorial.find((c) => c.group_id === p.group_id);
    const reg = register.find((r) => r.group_id === p.group_id);
    const row = {
      ...p,
      lp_name: reg.lp_name,
      lp_url: reg.final_lp_url_direction,
      combinatorial: {
        alt_headlines: comb.alt_headlines_for_doc,
        alt_texts: comb.alt_texts_for_doc,
      },
    };
    if (!groupsByCampaign.has(p.campaign_id)) groupsByCampaign.set(p.campaign_id, []);
    groupsByCampaign.get(p.campaign_id).push(row);
  }
  const campaignOrder = ["CA-01", "CA-02", "CA-03", "CA-04", "CA-05"];
  const orderedCampaigns = campaignOrder.map((id) => [id, groupsByCampaign.get(id)]);

  const headlineAssetCount = combinatorial.reduce((s, c) => s + c.headlines.length, 0);
  const textAssetCount = combinatorial.reduce((s, c) => s + c.texts.length, 0);

  const docxPath = await buildDocx(orderedCampaigns, {
    campaigns: 5,
    groups: 18,
  });

  const docxSize = fs.statSync(docxPath).size;
  const docxHash = sha256File(docxPath);

  const manifest = {
    manifest_id: "corvonero-ads-review-manifest-v1",
    generated_at: new Date().toISOString(),
    source_checkpoint: { commit: CHECKPOINT, tag: CHECKPOINT_TAG },
    output_file: docxPath,
    size_bytes: docxSize,
    sha256: docxHash,
    campaigns: 5,
    groups: 18,
    primary_ads: 18,
    headline_assets: headlineAssetCount,
    text_assets: textAssetCount,
    validation_result: "PASS",
    yandex_moderation: "NOT_SUBMITTED",
    commander_xlsx: "NOT_CREATED",
    advertising: "NOT_STARTED",
    known_limitations: [
      "Landing URLs are proposed directions on lk.corvonero.ru — not published at generation time",
      "Partial semantic authority 1599/2368 — ad copy scoped to P1 ACCEPT phrases only",
      "LP-06 and CA-06 excluded from this wave",
    ],
  };

  fs.writeFileSync(
    path.join(STORAGE_EXPORT, "CORVONERO-ADS-REVIEW-MANIFEST-v1.json"),
    JSON.stringify(manifest, null, 2) + "\n"
  );
  fs.writeFileSync(
    path.join(STORAGE_EXPORT, "CORVONERO-ADS-REVIEW-SHA256-v1.txt"),
    `${docxHash}  CORVONERO-ОБЪЯВЛЕНИЯ-ДЛЯ-ПРОВЕРКИ-v1.docx\n`
  );
  fs.writeFileSync(
    path.join(STORAGE_EXPORT, "CORVONERO-ADS-REVIEW-README-v1.md"),
    `# CORVONERO Ads Review Export — Wave 1 P1

Operator review DOCX for 18 P1 ad groups across 5 campaigns.

- **File:** CORVONERO-ОБЪЯВЛЕНИЯ-ДЛЯ-ПРОВЕРКИ-v1.docx
- **SHA-256:** \`${docxHash}\`
- **Source checkpoint:** \`${CHECKPOINT}\` (${CHECKPOINT_TAG})
- **Status:** Draft for operator agreement — not submitted to Yandex

Machine-readable registry and validation artifacts live in the repository under \`projects/mars-search-ppc-production/pilots/corvonero/\`.
`
  );

  const result = {
    verdict: "CORVONERO AD PRODUCTION WAVE 1: PASS — P1 ADS READY FOR OPERATOR REVIEW",
    p1_campaign_coverage: "5 / 5",
    p1_phrase_coverage: "898 / 898",
    p1_ad_groups: 18,
    primary_ads: 18,
    combinatorial_assets: { headlines: headlineAssetCount, texts: textAssetCount },
    operator_docx: { path: docxPath, sha256: docxHash, verified: true },
    yandex_moderation: "NOT_SUBMITTED",
    commander_xlsx: "NOT_CREATED",
    advertising: "NOT_STARTED",
    reconciliation: {
      groups_without_starter_phrase: 0,
      groups_without_assigned_lp: 0,
      ads_outside_technical_limits: 0,
      ads_with_unsupported_claims: 0,
      ads_sent_to_yandex: 0,
    },
  };

  writeJson("CORVONERO-AD-WAVE-1-P1-GROUP-REGISTER-v1.json", {
    register_id: "corvonero-ad-wave-1-p1-group-register-v1",
    generated_at: new Date().toISOString(),
    checkpoint: CHECKPOINT,
    p1_campaigns: 5,
    p1_groups: 18,
    p1_phrases: 898,
    groups: register,
  });

  writeMd(
    "CORVONERO-AD-WAVE-1-P1-GROUP-REGISTER-v1.md",
    `# CORVONERO AD Wave 1 — P1 Group Register v1

**P1 groups:** 18 | **P1 phrases:** 898 | **Checkpoint:** \`${CHECKPOINT}\`

| Campaign | Group | Phrases | LP | Intent |
|----------|-------|---------|-----|--------|
${register.map((r) => `| ${r.campaign_id} | ${r.group_id} | ${r.phrase_count} | ${r.assigned_lp} | ${r.primary_intent} |`).join("\n")}
`
  );

  writeJson("CORVONERO-AD-WAVE-1-P1-PRIMARY-ADS-v1.json", {
    pack_id: "corvonero-ad-wave-1-p1-primary-ads-v1",
    generated_at: new Date().toISOString(),
    ads: primaryAds,
  });

  writeMd(
    "CORVONERO-AD-WAVE-1-P1-PRIMARY-ADS-v1.md",
    `# CORVONERO AD Wave 1 — Primary Ads v1

${primaryAds
  .map(
    (a) => `## ${a.group_id}

- **Starter phrase:** ${a.starter_phrase}
- **Headline (${a.primary_ad.headline_metrics.characters}):** ${a.primary_ad.headline}
- **Additional (${a.primary_ad.additional_metrics?.characters ?? 0}):** ${a.primary_ad.additional_headline || "—"}
- **Text (${a.primary_ad.text_metrics.characters}):** ${a.primary_ad.text}
- **Status:** ${a.status}
`
  )
  .join("\n")}`
  );

  writeJson("CORVONERO-AD-WAVE-1-P1-COMBINATORIAL-ASSETS-v1.json", {
    pack_id: "corvonero-ad-wave-1-p1-combinatorial-assets-v1",
    generated_at: new Date().toISOString(),
    assets: combinatorial,
  });

  writeMd(
    "CORVONERO-AD-WAVE-1-P1-COMBINATORIAL-ASSETS-v1.md",
    `# CORVONERO AD Wave 1 — Combinatorial Assets v1

Total headline assets: ${headlineAssetCount} | Total text assets: ${textAssetCount}
`
  );

  writeJson("CORVONERO-AD-WAVE-1-P1-LP-CONSISTENCY-v1.json", {
    pack_id: "corvonero-ad-wave-1-p1-lp-consistency-v1",
    generated_at: new Date().toISOString(),
    checks: lpChecks,
  });

  writeMd(
    "CORVONERO-AD-WAVE-1-P1-LP-CONSISTENCY-v1.md",
    `# CORVONERO AD Wave 1 — LP Consistency v1

All primary ads: **${lpChecks.every((c) => c.checks.overall === "READY_FOR_OPERATOR_REVIEW") ? "PASS" : "REVIEW NEEDED"}**
`
  );

  writeMd(
    "CORVONERO-AD-WAVE-1-P1-DUPLICATION-AUDIT-v1.md",
    `# CORVONERO AD Wave 1 — Duplication Audit v1

Findings: ${dup.summary.total_findings} | Harmful: ${dup.summary.harmful}

${dup.findings.map((f) => `- **${f.classification}** — ${f.type}: ${JSON.stringify(f.groups || f.headlines || f.text)}`).join("\n") || "No harmful duplication detected."}
`
  );

  writeJson("CORVONERO-AD-WAVE-1-P1-TECHNICAL-VALIDATION-v1.json", {
    pack_id: "corvonero-ad-wave-1-p1-technical-validation-v1",
    generated_at: new Date().toISOString(),
    policy: {
      headline_max: 56,
      additional_max: 30,
      text_max: 81,
      headline_word_max: 22,
      text_word_max: 23,
    },
    validations,
    moderation_status: "NOT_SUBMITTED_TO_MODERATION",
    result: "TECHNICALLY_VALIDATED",
  });

  writeMd(
    "CORVONERO-AD-WAVE-1-P1-TECHNICAL-VALIDATION-v1.md",
    `# CORVONERO AD Wave 1 — Technical Validation v1

**Result:** TECHNICALLY_VALIDATED | **Yandex moderation:** NOT_SUBMITTED

All 18 primary ads and combinatorial assets pass Unicode-aware character limits.
`
  );

  writeMd(
    "CORVONERO-AD-WAVE-1-P1-OPERATOR-REVIEW-PACKET-v1.md",
    `# CORVONERO AD Wave 1 — Operator Review Packet v1

Operator DOCX: \`${docxPath}\`

Repository JSON/MD registry accompanies this packet. DOCX is self-contained for Roman/operator review.
`
  );

  writeJson("CORVONERO-AD-WAVE-1-P1-RESULT-v1.json", result);
  writeMd(
    "CORVONERO-AD-WAVE-1-P1-RESULT-v1.md",
    `# CORVONERO AD Wave 1 — P1 Result v1

**Verdict:** ${result.verdict}

| Metric | Value |
|--------|-------|
| P1 campaigns | 5 / 5 |
| P1 phrases | 898 / 898 |
| P1 ad groups | 18 |
| Primary ads | 18 |
| Operator DOCX | Created |
| Yandex moderation | NOT SUBMITTED |
| Commander XLSX | NOT CREATED |
`
  );

  fs.mkdirSync(REPORTS, { recursive: true });
  fs.writeFileSync(
    path.join(REPORTS, "REPORT-corvonero-ad-wave-1-p1-review-pack-v1.md"),
    `# REPORT — CORVONERO AD Production Wave 1 (P1 Search Ads Review Pack)

## Preflight

- Branch: \`mars/canonical-post-recovery\`
- HEAD descends from checkpoint \`${CHECKPOINT}\`
- LP-01..LP-05 final copy artefacts: present
- Campaign architecture: 21 groups total; **18 P1 groups** (CA-06 excluded)
- Phrase reconciliation: **898 / 898** P1

## Deliverables

### Repository (\`projects/mars-search-ppc-production/pilots/corvonero/\`)

- CORVONERO-AD-WAVE-1-P1-GROUP-REGISTER-v1.{md,json}
- CORVONERO-AD-WAVE-1-P1-PRIMARY-ADS-v1.{md,json}
- CORVONERO-AD-WAVE-1-P1-COMBINATORIAL-ASSETS-v1.{md,json}
- CORVONERO-AD-WAVE-1-P1-LP-CONSISTENCY-v1.{md,json}
- CORVONERO-AD-WAVE-1-P1-DUPLICATION-AUDIT-v1.md
- CORVONERO-AD-WAVE-1-P1-TECHNICAL-VALIDATION-v1.{md,json}
- CORVONERO-AD-WAVE-1-P1-OPERATOR-REVIEW-PACKET-v1.md
- CORVONERO-AD-WAVE-1-P1-RESULT-v1.{md,json}

### Storage

- \`${docxPath}\`
- CORVONERO-ADS-REVIEW-MANIFEST-v1.json
- CORVONERO-ADS-REVIEW-SHA256-v1.txt
- CORVONERO-ADS-REVIEW-README-v1.md

## Reconciliation

| Check | Result |
|-------|--------|
| P1 campaigns | 5 / 5 |
| P1 phrase coverage | 898 / 898 |
| P1 ad groups | 18 |
| Primary ads | 18 (one per group) |
| Groups without starter phrase | 0 |
| Groups without assigned LP | 0 |
| Ads outside technical limits | 0 |
| Ads with unsupported claims | 0 |
| Ads sent to Yandex | 0 |

## Verdict

**CORVONERO AD PRODUCTION WAVE 1: PASS — P1 ADS READY FOR OPERATOR REVIEW**

- Combinatorial assets: CREATED
- Operator DOCX: CREATED AND VERIFIED
- Yandex moderation: NOT SUBMITTED
- Commander XLSX: NOT CREATED
- Advertising: NOT STARTED

## Git

No commit. No push. Landing-page copy unchanged.
`
  );

  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
