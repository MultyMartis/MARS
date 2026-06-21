/**
 * Stage 2 live SERP artifact generator — bounded web search pass.
 * NOT live Playwright/R1 capture. Yandex direct fetch blocked (captcha).
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const outDir = path.join(__dirname, "..", "serp_results_live");
fs.mkdirSync(outDir, { recursive: true });

const CAPTURE_META = {
  captured_at: "2026-06-22T14:00:00.000Z",
  collection_date: "2026-06-22",
  search_engine: "yandex",
  region: "Новосибирск",
  region_lr: 65,
  city: "Новосибирск",
  device: "mobile",
  source_mode: "bounded_web_search_stage2",
  evidence_grade: "C",
  acquisition_limitations: [
    "Direct Yandex HTTP fetch blocked by captcha (af-004) — not R1/R2 live SERP",
    "Results from bounded web search synthesis; ad blocks and exact rank order not verified",
    "Personalization and logged-in state: SAFE UNKNOWN",
    "Maps/local pack visibility: partial — Yandex Maps org pages may appear in synthesis only"
  ],
  separated_from: "serp_results/ (Stage 1 bounded capture q01-q09)"
};

const queries = [
  { id: "lq01", group: "broad_services", query: "программист 1С Новосибирск", label: "commercial", serp_type: "mixed_commercial", ads: { present: "SAFE UNKNOWN", block_count: "SAFE UNKNOWN" }, maps: "partial_via_synthesis", commercial: "strong", organic: [
    { position: 1, title: "Услуги программиста 1С — Shift Company", url: "https://novosib.shift-company.ru/services/programmist/", surface_type: "commercial_service", player_scope: "local_company" },
    { position: 2, title: "Заказать Программист 1С — Avanta Pro", url: "https://avanta-pro.ru/services/uslugi-1s/programmist-1s/", surface_type: "commercial_service", player_scope: "local_franchisee" },
    { position: 3, title: "Услуги программиста 1С — ITsVsem", url: "https://itsvsem.ru/uslugi/uslugi-programmista-1s/", surface_type: "commercial_service", player_scope: "local_company" },
    { position: 4, title: "Яндекс Услуги — разработчики 1С ERP", url: "https://uslugi.yandex.ru/65-novosibirsk/category?text=услуги+разработчика+1с", surface_type: "aggregator", player_scope: "aggregator" },
    { position: 5, title: "1С в Новосибирске — Somsk", url: "https://somsk.ru/novosibirsk", surface_type: "commercial_service", player_scope: "federal_remote" }
  ]},
  { id: "lq02", group: "broad_services", query: "услуги программиста 1С Новосибирск", label: "commercial", serp_type: "mixed_commercial", ads: { present: "SAFE UNKNOWN", block_count: "SAFE UNKNOWN" }, maps: "not_observed", commercial: "strong", organic: [
    { position: 1, title: "Shift Company — программист 1С", url: "https://novosib.shift-company.ru/services/programmist/", surface_type: "commercial_service", player_scope: "local_company" },
    { position: 2, title: "Avanta Pro — услуги 1С", url: "https://avanta-pro.ru/services/uslugi-1s/programmist-1s/", surface_type: "commercial_service", player_scope: "local_franchisee" },
    { position: 3, title: "Profinfoservice — IT услуги", url: "https://profinfoservice.ru/novosibirsk/", surface_type: "commercial_service", player_scope: "local_company" }
  ]},
  { id: "lq03", group: "broad_services", query: "доработка 1С Новосибирск", label: "commercial", serp_type: "commercial", ads: { present: "SAFE UNKNOWN", block_count: "SAFE UNKNOWN" }, maps: "not_observed", commercial: "strong", organic: [
    { position: 1, title: "Доработка 1С — ITLlekt", url: "https://www.itllekt.ru/1c/services/maintenance/dorabotka-1s/", surface_type: "commercial_service", player_scope: "local_franchisee" },
    { position: 2, title: "Доработка 1С — Infotech", url: "https://it-russia.com/services/dorabotka-1s/", surface_type: "commercial_service", player_scope: "local_company" },
    { position: 3, title: "1С программирование — Vigyana", url: "https://vigyana.ru/uslugi/1s-programmirovanie/", surface_type: "commercial_service", player_scope: "local_company" }
  ]},
  { id: "lq04", group: "broad_services", query: "сопровождение 1С Новосибирск", label: "commercial", serp_type: "commercial", ads: { present: "SAFE UNKNOWN", block_count: "SAFE UNKNOWN" }, maps: "not_observed", commercial: "strong", organic: [
    { position: 1, title: "Сопровождение 1С — Profinfoservice", url: "https://profinfoservice.ru/novosibirsk/soprovozhdenie-1c/", surface_type: "commercial_service", player_scope: "local_company" },
    { position: 2, title: "Сопровождение 1С — KKM.Center", url: "https://novosibirsk.kkm.center/klientam/soprovozhdenie-1s/", surface_type: "commercial_service", player_scope: "local_franchisee" },
    { position: 3, title: "1С сопровождение — Vigyana", url: "https://vigyana.ru/uslugi/1s-programmirovanie/", surface_type: "commercial_service", player_scope: "local_company" },
    { position: 4, title: "Техподдержка 1С — RDN Group", url: "https://novosibirsk.rdn-service.ru/services/podderzhka/tekhnicheskaya-podderzhka-1s/", surface_type: "commercial_service", player_scope: "federal_remote" }
  ]},
  { id: "lq05", group: "urgent_troubleshooting", query: "срочно программист 1С Новосибирск", label: "urgent", serp_type: "mixed_vacancy_noise", ads: { present: "SAFE UNKNOWN", block_count: "SAFE UNKNOWN" }, maps: "not_observed", commercial: "weak", noise: "high_vacancy", organic: [
    { position: 1, title: "Вакансии программист 1С — hh.ru", url: "https://novosibirsk.hh.ru/vacancies/programmist-1s", surface_type: "vacancy_aggregator", player_scope: "non_service" },
    { position: 2, title: "Срочно работа программистом 1С — GdeJob", url: "https://gdejob.com/работа-программист-1с-новосибирск", surface_type: "vacancy_aggregator", player_scope: "non_service" },
    { position: 3, title: "Яндекс Услуги — программист 1С", url: "https://uslugi.yandex.ru/65-novosibirsk/category?text=программист+1с", surface_type: "aggregator", player_scope: "aggregator" }
  ]},
  { id: "lq06", group: "urgent_troubleshooting", query: "1С не работает Новосибирск", label: "urgent", serp_type: "mixed", ads: { present: "SAFE UNKNOWN", block_count: "SAFE UNKNOWN" }, maps: "not_observed", commercial: "moderate", noise: "moderate_informational", organic: [
    { position: 1, title: "Ошибки в 1С — Mikos", url: "https://www.mikos.ru/services/service/oshibki-v-1s-8-3-i-ikh-ispravlenie/", surface_type: "commercial_service", player_scope: "local_company" },
    { position: 2, title: "ITsVsem — блог об ошибках 1С", url: "https://itsvsem.ru/", surface_type: "informational_mixed", player_scope: "local_company" },
    { position: 3, title: "Avanta Pro — программист 1С", url: "https://avanta-pro.ru/services/uslugi-1s/programmist-1s/", surface_type: "commercial_service", player_scope: "local_franchisee" }
  ]},
  { id: "lq07", group: "urgent_troubleshooting", query: "исправить ошибку 1С Новосибирск", label: "urgent", serp_type: "mixed", commercial: "moderate", noise: "moderate", organic: [
    { position: 1, title: "Исправление ошибок 1С — Mikos", url: "https://www.mikos.ru/services/service/oshibki-v-1s-8-3-i-ikh-ispravlenie/", surface_type: "commercial_service", player_scope: "local_company" },
    { position: 2, title: "Vigyana — 1С сопровождение", url: "https://vigyana.ru/uslugi/1s-programmirovanie/", surface_type: "commercial_service", player_scope: "local_company" }
  ]},
  { id: "lq08", group: "urgent_troubleshooting", query: "восстановить работу 1С Новосибирск", label: "urgent", serp_type: "mixed", commercial: "moderate", noise: "moderate", organic: [
    { position: 1, title: "Profinfoservice — сопровождение 1С", url: "https://profinfoservice.ru/novosibirsk/soprovozhdenie-1c/", surface_type: "commercial_service", player_scope: "local_company" },
    { position: 2, title: "Avanta Pro — обслуживание 1С", url: "https://avanta-pro.ru/services/uslugi-1s/obsluzhivanie-1s/", surface_type: "commercial_service", player_scope: "local_franchisee" }
  ]},
  { id: "lq09", group: "reports_modifications", query: "доработка отчёта 1С Новосибирск", label: "commercial", serp_type: "commercial", commercial: "strong", organic: [
    { position: 1, title: "Vigyana — доработка отчётов", url: "https://vigyana.ru/uslugi/1s-programmirovanie/", surface_type: "commercial_service", player_scope: "local_company" },
    { position: 2, title: "ITLlekt — доработка 1С", url: "https://www.itllekt.ru/1c/services/maintenance/dorabotka-1s/", surface_type: "commercial_service", player_scope: "local_franchisee" },
    { position: 3, title: "Avanta Pro — программист 1С", url: "https://avanta-pro.ru/services/uslugi-1s/programmist-1s/", surface_type: "commercial_service", player_scope: "local_franchisee" }
  ]},
  { id: "lq10", group: "reports_modifications", query: "доработка печатной формы 1С Новосибирск", label: "commercial", serp_type: "commercial", commercial: "strong", organic: [
    { position: 1, title: "ITLlekt — печатные формы от 1500 руб", url: "https://www.itllekt.ru/1c/services/maintenance/dorabotka-1s/", surface_type: "commercial_service", player_scope: "local_franchisee" },
    { position: 2, title: "Vigyana — печатные формы", url: "https://vigyana.ru/uslugi/1s-programmirovanie/", surface_type: "commercial_service", player_scope: "local_company" }
  ]},
  { id: "lq11", group: "reports_modifications", query: "настройка отчёта 1С Новосибирск", label: "commercial", serp_type: "commercial", commercial: "moderate", organic: [
    { position: 1, title: "Vigyana — настройка отчётов", url: "https://vigyana.ru/uslugi/1s-programmirovanie/", surface_type: "commercial_service", player_scope: "local_company" },
    { position: 2, title: "ITLlekt — настройка отчётов", url: "https://www.itllekt.ru/1c/services/maintenance/dorabotka-1s/", surface_type: "commercial_service", player_scope: "local_franchisee" }
  ]},
  { id: "lq12", group: "reports_modifications", query: "доработка РМК 1С Новосибирск", label: "commercial", serp_type: "mixed", commercial: "moderate", noise: "low", organic: [
    { position: 1, title: "Vigyana — доработка 1С", url: "https://vigyana.ru/uslugi/1s-programmirovanie/", surface_type: "commercial_service", player_scope: "local_company" },
    { position: 2, title: "Infotech — доработка 1С", url: "https://it-russia.com/services/dorabotka-1s/", surface_type: "commercial_service", player_scope: "local_company" }
  ]},
  { id: "lq13", group: "integrations", query: "интеграция 1С с сайтом Новосибирск", label: "integration", serp_type: "commercial", commercial: "strong", organic: [
    { position: 1, title: "Студия ЯЛ — интеграция 1С", url: "https://www.yalstudio.ru/razrabotka/integratsiya-1s/", surface_type: "commercial_service", player_scope: "web_studio" },
    { position: 2, title: "Direct Line — интеграция сайта с 1С", url: "https://www.directline.pro/razrabotka/integratsiya-sayta-s-1c/", surface_type: "commercial_service", player_scope: "web_studio" },
    { position: 3, title: "Studio Expert — integration_1c", url: "https://novosibirsk.studio-expert.ru/services/integration_1c/", surface_type: "commercial_service", player_scope: "web_studio" },
    { position: 4, title: "REDBE Agency — интеграция 1С", url: "https://redbe-agency.ru/razrabotka-sajtov/razrabotka-sajtov-s-integracziej-1s", surface_type: "commercial_service", player_scope: "web_studio" }
  ]},
  { id: "lq14", group: "integrations", query: "интеграция 1С Битрикс Новосибирск", label: "integration", serp_type: "commercial", commercial: "strong", organic: [
    { position: 1, title: "Interland — 1С и Битрикс24", url: "https://ilsib.ru/services/1c-exchange/", surface_type: "commercial_service", player_scope: "web_studio" },
    { position: 2, title: "Студия ЯЛ — интеграция 1С", url: "https://www.yalstudio.ru/razrabotka/integratsiya-1s/", surface_type: "commercial_service", player_scope: "web_studio" },
    { position: 3, title: "Studio Expert — Bitrix 1C", url: "https://novosibirsk.studio-expert.ru/services/integration_1c/", surface_type: "commercial_service", player_scope: "web_studio" },
    { position: 4, title: "Яндекс Услуги — интеграция Битрикс24", url: "https://uslugi.yandex.ru/65-novosibirsk/category?text=интеграция+битрикс24", surface_type: "aggregator", player_scope: "aggregator" }
  ]},
  { id: "lq15", group: "integrations", query: "интеграция 1С с кассой Новосибирск", label: "integration", serp_type: "mixed", commercial: "moderate", organic: [
    { position: 1, title: "AB OnlineKassa — кассы и маркировка", url: "https://novosibirsk.ab-onlinekassa.ru/", surface_type: "commercial_service", player_scope: "labeling_specialist" },
    { position: 2, title: "KKM.Center — сопровождение 1С", url: "https://novosibirsk.kkm.center/", surface_type: "commercial_service", player_scope: "local_franchisee" }
  ]},
  { id: "lq16", group: "integrations", query: "обмен 1С с сайтом Новосибирск", label: "integration", serp_type: "commercial", commercial: "strong", organic: [
    { position: 1, title: "SAWeb — интеграция сайта с 1С", url: "https://nvsb.saweb.ru/integratsiya-sajta-s-1s", surface_type: "commercial_service", player_scope: "web_studio" },
    { position: 2, title: "Студия ЯЛ", url: "https://www.yalstudio.ru/razrabotka/integratsiya-1s/", surface_type: "commercial_service", player_scope: "web_studio" }
  ]},
  { id: "lq17", group: "labeling", query: "маркировка в 1С Новосибирск", label: "regulated-labeling", serp_type: "mixed_commercial", commercial: "moderate", noise: "moderate_informational", organic: [
    { position: 1, title: "AB OnlineKassa — маркировка Новосибирск", url: "https://novosibirsk.ab-onlinekassa.ru/markirovka/", surface_type: "commercial_service", player_scope: "labeling_specialist" },
    { position: 2, title: "Vigyana — маркировка в прайсе", url: "https://vigyana.ru/uslugi/1s-programmirovanie/", surface_type: "commercial_service", player_scope: "local_company" },
    { position: 3, title: "Мой бизнес НСО — Честный знак FAQ", url: "https://mbnso.ru/support/voprosy-po-rabote-v-sisteme-chestnyy-znak/", surface_type: "informational_official", player_scope: "non_competitor" }
  ]},
  { id: "lq18", group: "labeling", query: "настройка маркировки в 1С Новосибирск", label: "regulated-labeling", serp_type: "mixed", commercial: "moderate", noise: "high_informational", organic: [
    { position: 1, title: "AB OnlineKassa — Честный знак", url: "https://novosibirsk.ab-onlinekassa.ru/markirovka/", surface_type: "commercial_service", player_scope: "labeling_specialist" },
    { position: 2, title: "online-kassa.ru blog — how-to", url: "https://online-kassa.ru/blog/kak-nastroit-rabotu-s-chestnym-znakom-v-1s-upravlenie-torgovlej/", surface_type: "informational", player_scope: "non_competitor" }
  ]},
  { id: "lq19", group: "labeling", query: "Честный знак 1С Новосибирск", label: "regulated-labeling", serp_type: "mixed", commercial: "moderate", organic: [
    { position: 1, title: "AB OnlineKassa — Честный знак под ключ", url: "https://novosibirsk.ab-onlinekassa.ru/markirovka/", surface_type: "commercial_service", player_scope: "labeling_specialist" },
    { position: 2, title: "1С-Архитектор бизнеса — blog", url: "https://www.1ab.ru/blog/detail/integratsiya-1s-s-sistemoy-markirovki-chestnyy-znak/", surface_type: "informational_mixed", player_scope: "federal_franchisee" }
  ]},
  { id: "lq20", group: "labeling", query: "подключение Честного знака к 1С", label: "regulated-labeling", serp_type: "informational-heavy", commercial: "weak", noise: "high_informational", organic: [
    { position: 1, title: "Cleverence — инструкция маркировка 1С", url: "https://www.cleverence.ru/articles/markirovka-tovarov/", surface_type: "informational", player_scope: "vendor_content" },
    { position: 2, title: "online-kassa.ru blog", url: "https://online-kassa.ru/blog/kak-nastroit-rabotu-s-chestnym-znakom-v-1s-upravlenie-torgovlej/", surface_type: "informational", player_scope: "non_competitor" },
    { position: 3, title: "AB OnlineKassa — commercial", url: "https://novosibirsk.ab-onlinekassa.ru/markirovka/", surface_type: "commercial_service", player_scope: "labeling_specialist" }
  ]},
  { id: "lq21", group: "labeling", query: "настройка ТС ПИОТ", label: "regulated-labeling", serp_type: "informational-heavy", commercial: "weak", noise: "high_informational", organic: [
    { position: 1, title: "online-kassa.ru — ТС ПИоТ в 1С", url: "https://online-kassa.ru/blog/kak-nastroit-1s-dlya-raboty-s-markirovkoj-podrobnye-instruktsii/", surface_type: "informational", player_scope: "non_competitor" },
    { position: 2, title: "LegaSoft — TS PIOT SPb", url: "https://spb.legasoft.ru/services/markirovka/ts-piot-esm-podklyuchenie-registratsiya-i-nastroyka/", surface_type: "commercial_service", player_scope: "federal_pattern" }
  ]},
  { id: "lq22", group: "labeling", query: "ТС ПИОТ 1С", label: "regulated-labeling", serp_type: "informational-heavy", commercial: "weak", noise: "high_informational", organic: [
    { position: 1, title: "LegaSoft — TS PIOT", url: "https://spb.legasoft.ru/services/markirovka/ts-piot-esm-podklyuchenie-registratsiya-i-nastroyka/", surface_type: "commercial_service", player_scope: "federal_pattern" },
    { position: 2, title: "online-kassa.ru blog", url: "https://online-kassa.ru/blog/kak-nastroit-1s-dlya-raboty-s-markirovkoj-podrobnye-instruktsii/", surface_type: "informational", player_scope: "non_competitor" }
  ]},
  { id: "lq23", group: "product_labeling", query: "маркировка пива 1С", label: "product-specific", serp_type: "mixed", commercial: "moderate", organic: [
    { position: 1, title: "AB OnlineKassa — маркировка", url: "https://novosibirsk.ab-onlinekassa.ru/markirovka/", surface_type: "commercial_service", player_scope: "labeling_specialist" },
    { position: 2, title: "Vigyana — ЕГАИС/маркировка прайс", url: "https://vigyana.ru/uslugi/1s-programmirovanie/", surface_type: "commercial_service", player_scope: "local_company" }
  ]},
  { id: "lq24", group: "product_labeling", query: "маркировка воды 1С", label: "product-specific", serp_type: "mixed", commercial: "moderate", organic: [
    { position: 1, title: "AB OnlineKassa", url: "https://novosibirsk.ab-onlinekassa.ru/markirovka/", surface_type: "commercial_service", player_scope: "labeling_specialist" },
    { position: 2, title: "SENSU — маркировка federal", url: "https://sensu.ru/markirovka", surface_type: "commercial_service", player_scope: "federal_pattern" }
  ]},
  { id: "lq25", group: "product_labeling", query: "маркировка лекарств 1С", label: "product-specific", serp_type: "informational-heavy", commercial: "weak", noise: "high_informational", organic: [
    { position: 1, title: "Cleverence — маркировка лекарств", url: "https://www.cleverence.ru/articles/markirovka-tovarov/", surface_type: "informational", player_scope: "vendor_content" },
    { position: 2, title: "Oxtron — chestniy znak", url: "https://oxtron.ru/chestniy-znak", surface_type: "commercial_service", player_scope: "federal_pattern" }
  ]},
  { id: "lq26", group: "product_labeling", query: "маркировка автозапчастей 1С", label: "product-specific", serp_type: "mixed", commercial: "moderate", organic: [
    { position: 1, title: "AB OnlineKassa — маркировка", url: "https://novosibirsk.ab-onlinekassa.ru/markirovka/", surface_type: "commercial_service", player_scope: "labeling_specialist" },
    { position: 2, title: "Vigyana — маркировка", url: "https://vigyana.ru/uslugi/1s-programmirovanie/", surface_type: "commercial_service", player_scope: "local_company" }
  ]},
  { id: "lq27", group: "product_labeling", query: "маркировка строительных материалов 1С", label: "product-specific", serp_type: "informational-heavy", commercial: "weak", noise: "moderate", organic: [
    { position: 1, title: "AB OnlineKassa", url: "https://novosibirsk.ab-onlinekassa.ru/markirovka/", surface_type: "commercial_service", player_scope: "labeling_specialist" },
    { position: 2, title: "1ab.ru blog — Честный знак", url: "https://www.1ab.ru/blog/detail/integratsiya-1s-s-sistemoy-markirovki-chestnyy-znak/", surface_type: "informational_mixed", player_scope: "federal_franchisee" }
  ]}
];

const index = {
  schema_version: "0.1",
  session_id: "mig-20260622-corv01",
  capture_pass: "stage_2_live_bounded",
  generated_at: CAPTURE_META.captured_at,
  ...CAPTURE_META,
  query_count: queries.length,
  queries: queries.map((q) => ({
    query_id: q.id,
    query_text: q.query,
    query_group: q.group,
    research_label: q.label,
    artifact: `serp_results_live/${q.id}.json`,
    evidence_grade: "C"
  })),
  acquisition_failure_refs: ["af-004"]
};

for (const q of queries) {
  const doc = {
    schema_version: "0.1",
    session_id: "mig-20260622-corv01",
    query_id: q.id,
    stage: "mig_research_stage_2",
    ...CAPTURE_META,
    query: q.query,
    query_group: q.group,
    research_label: q.label,
    serp_type: q.serp_type,
    ads_blocks: q.ads || { top_count: "SAFE UNKNOWN", bottom_count: "SAFE UNKNOWN", visible_patterns: [] },
    maps_local_pack: q.maps || "not_observed",
    aggregators: (q.organic || []).filter((r) => r.surface_type === "aggregator").map((r) => new URL(r.url).hostname),
    organic_results: q.organic || [],
    commercial_signal: q.commercial || "SAFE UNKNOWN",
    noise_signal: q.noise || "low"
  };
  fs.writeFileSync(path.join(outDir, `${q.id}.json`), JSON.stringify(doc, null, 2), "utf8");
}

fs.writeFileSync(path.join(__dirname, "..", "serp_live_index.json"), JSON.stringify(index, null, 2), "utf8");
console.log(`Generated ${queries.length} live SERP files + index`);
