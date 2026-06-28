#!/usr/bin/env python3
"""Build self-contained corp CTA section HTML for each corporate page."""
from __future__ import annotations

from pathlib import Path

WORK = Path(r"C:\MARS Phenix\AI MARS\projects\ocpilot\sites\site-002\reports\corp-cta-v2-work")

PAGES = {
    "about": {
        "modifier": "zpm-corp-cta--about",
        "id": "zpm-about-cta",
        "title_id": "zpm-about-cta-title",
        "data": "about",
        "fancybox": "certificates-about",
        "form_id": "zpm-about-cta-form",
        "label": "Связаться с&nbsp;заводом",
        "title": "Получите прайс-лист, консультацию или подбор оборудования",
        "lead": "Поможем подобрать оборудование под задачу предприятия, рассчитаем стоимость и&nbsp;сроки, подготовим коммерческое предложение и&nbsp;ответим по&nbsp;документам для закупки.",
        "benefits": [
            ("fa-file-spreadsheet", "Получить прайс-лист", "Отправим актуальный прайс со&nbsp;всеми сериями и&nbsp;размерами."),
            ("fa-comments-alt", "Консультация", "Ответим по&nbsp;комплектации, срокам и&nbsp;документам до&nbsp;оплаты."),
            ("fa-drafting-compass", "Подбор оборудования", "Подберём решение под кухню, цех или производственный участок."),
        ],
        "form_title": 'Получить <em class="no_wrap--word">прайс-лист</em>',
        "form_note": 'Отправим <em class="zpm-accent-text">актуальный <em class="no_wrap--word">прайс-лист</em></em> и&nbsp;поможем подобрать оптимальное решение под ваши задачи.',
        "form_file": "corpcta-form-about.twig",
    },
    "delivery": {
        "modifier": "zpm-corp-cta--delivery",
        "id": "zpm-delivery-cta",
        "title_id": "zpm-delivery-cta-title",
        "data": "delivery",
        "fancybox": "certificates-delivery",
        "form_id": "zpm-delivery-form",
        "label": "Доставка оборудования",
        "title": "Уточнить условия поставки для вашего региона",
        "lead": "Опишите регион, состав заказа и&nbsp;предпочтительный способ получения — менеджер подскажет точку отгрузки, варианты перевозки и&nbsp;что учесть при планировании поставки на&nbsp;объект.",
        "benefits": [
            ("fa-truck-moving", "Доставка по&nbsp;России", "Отгружаем оборудование транспортными компаниями в&nbsp;регионы России."),
            ("fa-warehouse", "Две точки отгрузки", "Барнаул — производство; Московская область — склад партнёра для центрального региона."),
            ("fa-clock", "Сроки и&nbsp;маршрут", "Подскажем сроки комплектации, передачу перевозчику и&nbsp;самовывоз."),
        ],
        "form_title": "Запрос по&nbsp;доставке",
        "form_note": "Укажите регион и&nbsp;состав заказа — мы&nbsp;перезвоним или ответим на&nbsp;e-mail с&nbsp;вариантами отгрузки и&nbsp;перевозки.",
        "form_file": "corpcta-form-delivery.twig",
    },
    "payment": {
        "modifier": "zpm-corp-cta--payment",
        "id": "zpm-payment-cta",
        "title_id": "zpm-payment-cta-title",
        "data": "payment",
        "fancybox": "certificates-payment",
        "form_id": "zpm-payment-form",
        "label": "Оплата оборудования",
        "title": "Получить счёт или уточнить условия оплаты",
        "lead": "Опишите состав заказа, организацию-плательщика и&nbsp;сроки — менеджер подготовит коммерческое предложение, выставит счёт или ответит на&nbsp;вопросы по&nbsp;документам и&nbsp;порядку оплаты.",
        "benefits": [
            ("fa-file-invoice", "Счёт и&nbsp;КП", "Выставим счёт или подготовим коммерческое предложение под ваш заказ."),
            ("fa-building", "Для организаций", "Работаем с&nbsp;юридическими лицами и&nbsp;ИП по&nbsp;договору поставки."),
            ("fa-file-contract", "Документы для закупки", "Ответим по&nbsp;НДС, УПД, счёту-фактуре и&nbsp;сопроводительным документам."),
        ],
        "form_title": "Запрос счёта или консультации по&nbsp;оплате",
        "form_note": "Укажите контакты и&nbsp;организацию — менеджер выставит счёт, подготовит коммерческое предложение или ответит на&nbsp;вопросы по&nbsp;документам и&nbsp;порядку оплаты.",
        "form_file": "corpcta-form-payment.twig",
    },
    "guarantee": {
        "modifier": "zpm-corp-cta--warranty",
        "id": "zpm-warranty-cta",
        "title_id": "zpm-warranty-cta-title",
        "data": "warranty",
        "fancybox": "certificates-warranty",
        "form_id": "zpm-warranty-form",
        "label": "Гарантийная поддержка",
        "title": "Связаться по&nbsp;вопросу гарантии",
        "lead": "Опишите неисправность и&nbsp;оставьте контакты — менеджер завода примет обращение, уточнит модель и&nbsp;документы на&nbsp;покупку и&nbsp;подскажет следующий шаг. Не&nbsp;обязательно заранее знать все формальности: мы&nbsp;поможем собрать информацию для рассмотрения.",
        "benefits": [
            ("fa-tools", "Гарантийное обращение", "Примем обращение, уточним неисправность и&nbsp;следующий шаг по&nbsp;гарантии."),
            ("fa-shield-check", "Документы на&nbsp;покупку", "Поможем собрать информацию по&nbsp;модели, дате покупки и&nbsp;сопроводительным документам."),
            ("fa-phone-alt", "Быстрая связь", "Перезвоним или ответим на&nbsp;e-mail после обработки обращения в&nbsp;рабочее время."),
        ],
        "form_title": "Обращение по&nbsp;гарантии",
        "form_note": "Заполните форму — менеджер свяжется с&nbsp;вами, уточнит обстоятельства неисправности и&nbsp;подскажет, какие документы подготовить для рассмотрения обращения.",
        "form_file": "corpcta-form-guarantee.twig",
    },
    "dealers": {
        "modifier": "zpm-corp-cta--dealers",
        "id": "zpm-dealers-cta",
        "title_id": "zpm-dealers-cta-title",
        "data": "dealers",
        "fancybox": "certificates-dealers",
        "form_id": "zpm-dealers-form",
        "label": "Партнёрская программа",
        "title": "Получить условия сотрудничества",
        "lead": "Расскажите о&nbsp;компании, регионе и&nbsp;направлении работы — менеджер завода свяжется с&nbsp;вами, уточнит профиль партнёра и&nbsp;предложит формат взаимодействия. После знакомства вы&nbsp;получите понимание следующих шагов: коммерческие материалы, порядок заказов и&nbsp;документов.",
        "benefits": [
            ("fa-handshake", "Партнёрская работа", "Обсудим формат сотрудничества под ваш регион и&nbsp;направление продаж."),
            ("fa-boxes", "Ассортимент завода", "Серийное оборудование и&nbsp;изготовление по&nbsp;параметрам заказчика."),
            ("fa-chart-line", "Коммерческие условия", "Предоставим материалы и&nbsp;порядок заказов после первичного знакомства."),
        ],
        "form_title": "Заявка на&nbsp;сотрудничество",
        "form_note": "Заполните форму — менеджер свяжется с&nbsp;вами, уточнит профиль компании и&nbsp;направление работы и&nbsp;предложит формат взаимодействия с&nbsp;заводом.",
        "form_file": "corpcta-form-dealers.twig",
    },
    "custom_equipment": {
        "modifier": "zpm-corp-cta--custom",
        "id": "zpm-custom-cta",
        "title_id": "zpm-custom-cta-title",
        "data": "custom",
        "fancybox": "certificates-custom",
        "form_id": "zpm-custom-form",
        "label": "Оборудование на&nbsp;заказ",
        "title": "Получить расчёт изделия под ваш объект",
        "lead": "Опишите задачу — тип изделия, размеры, назначение и&nbsp;регион поставки. Менеджер свяжется с&nbsp;вами, уточнит параметры и&nbsp;подготовит расчёт. Если удобнее начать с&nbsp;телефона — позвоните по&nbsp;номеру, указанному в&nbsp;шапке сайта.",
        "benefits": [
            ("fa-ruler-combined", "Нестандартные размеры", "Изготовим изделие по&nbsp;вашим параметрам и&nbsp;условиям объекта."),
            ("fa-cogs", "Производство на&nbsp;заказ", "Полный цикл на&nbsp;площадке в&nbsp;Барнауле без посредников."),
            ("fa-calculator", "Расчёт стоимости", "Подготовим предварительный расчёт после уточнения параметров."),
        ],
        "form_title": "Заявка на&nbsp;расчёт",
        "form_note": "Заполните поля ниже. Поля, отмеченные звёздочкой, обязательны.",
        "form_file": "corpcta-form-custom_equipment.twig",
    },
}


def benefit_li(icon: str, title: str, text: str) -> str:
    return f"""                <li class="zpm-corp-cta__benefit">
                  <span class="zpm-corp-cta__benefit-icon" aria-hidden="true"><i class="fad {icon}"></i></span>
                  <span class="zpm-corp-cta__benefit-body">
                    <strong class="zpm-corp-cta__benefit-title">{title}</strong>
                    <span class="zpm-corp-cta__benefit-text">{text}</span>
                  </span>
                </li>"""


def build_section(cfg: dict) -> str:
    benefits = "\n".join(benefit_li(*b) for b in cfg["benefits"])
    form = (WORK / cfg["form_file"]).read_text(encoding="utf-8").strip()
    return f"""  <section class="zpm-corp-cta {cfg['modifier']}" id="{cfg['id']}" aria-labelledby="{cfg['title_id']}" data-corp-cta="{cfg['data']}">
    <div class="container">
      <div class="zpm-corp-cta__card">
        <div class="zpm-corp-cta__wrap">
          <div class="zpm-corp-cta__info">
            <div class="zpm-corp-cta__header">
              <p class="zpm-corp-cta__label">{cfg['label']}</p>
              <h2 class="zpm-corp-cta__title" id="{cfg['title_id']}">{cfg['title']}</h2>
              <p class="zpm-corp-cta__lead">{cfg['lead']}</p>
            </div>
            <div class="zpm-corp-cta__main">
              <div class="zpm-corp-cta__cert-col" aria-label="Сертификаты">
                <div class="zpm-corp-cta__cert-card">
                  <div class="swiper js-commercial-trust-certs">
                    <div class="swiper-wrapper">
                      <div class="swiper-slide">
                        <a
                          class="zpm-corp-cta__cert-link"
                          href="/assets/img/certificates/certificat_00.jpg"
                          data-fancybox="{cfg['fancybox']}"
                          data-caption="Сертификат «Сделано в России»"
                        >
                          <img
                            class="zpm-corp-cta__cert-img"
                            src="/assets/img/certificates/thumb_00.png"
                            alt="Сертификат «Сделано в России»"
                            width="200"
                            height="280"
                            loading="lazy"
                          />
                        </a>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="zpm-corp-cta__cert-card--base">
                  <img src="/assets/img/sert-base.jpg" alt="" width="250" height="40" loading="lazy" />
                </div>
              </div>
              <div class="zpm-corp-cta__benefits">
                <ul class="zpm-corp-cta__benefits-grid">
{benefits}
                </ul>
              </div>
            </div>
          </div>
          <div class="zpm-corp-cta__form-wrap">
            <div class="zpm-decoration-with-logo">
              <img src="/assets/img/decor-logo.svg" alt="" width="120" height="120" loading="lazy" />
            </div>
            <div class="zpm-corp-cta__form-col">
              <div class="zpm-corp-cta__form-card" id="{cfg['form_id']}">
                <h3 class="zpm-corp-cta__form-title">{cfg['form_title']}</h3>
                <p class="zpm-corp-cta__form-note">{cfg['form_note']}</p>
{form}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>"""


def main() -> None:
    for key, cfg in PAGES.items():
        out = WORK / f"corpcta-section-{key}.twig"
        out.write_text(build_section(cfg) + "\n", encoding="utf-8")
        print(f"wrote {out.name} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
