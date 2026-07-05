<?php
/**
 * Template part: home/faq.php
 *
 * D9-D: static V9 visual authority with theme asset fallbacks.
 * Future ACF wiring: D9-E wave.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

?>
<section data-reveal class="faq"  aria-labelledby="comfort-heading">
  <div class="container">
    <h2 class="faq__heading" id="comfort-heading">Комфорт, приватность, забота</h2>

    <div class="faq__list" data-accordion>
      <div class="faq__item" data-accordion-item>
        <h3 class="faq__item-title">
          <button
            type="button"
            class="faq__question"
            data-accordion-button
            aria-expanded="true"
            aria-controls="faq-panel-1"
            id="faq-trigger-1"
          >
            <span class="faq__question-label">Как перестать именно хотеть выпить, а&nbsp;не&nbsp;заставлять себя этого не&nbsp;делать?</span>
            <span class="faq__icon" aria-hidden="true"><i class="fas fa-chevron-down"></i></span>
          </button>
        </h3>
        <div
          class="faq__answer-panel"
          data-accordion-panel
          id="faq-panel-1"
          role="region"
          aria-labelledby="faq-trigger-1"
        >
          <p class="faq__answer">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do&nbsp;eiusmod tempor incididunt ut&nbsp;labore et&nbsp;dolore magna aliqua. Ut&nbsp;enim ad&nbsp;minim veniam, quis nostrud exercitation .Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do&nbsp;eiusmod tempor incididunt ut&nbsp;labore et&nbsp;dolore magna aliqua. Ut&nbsp;enim ad&nbsp;minim veniam, quis nostrud exercitation .</p>
        </div>
      </div>

      <div class="faq__item" data-accordion-item>
        <h3 class="faq__item-title">
          <button type="button" class="faq__question" data-accordion-button aria-expanded="false" aria-controls="faq-panel-2" id="faq-trigger-2">
            <span class="faq__question-label">Анонимное лечение или нет?</span>
            <span class="faq__icon" aria-hidden="true"><i class="fas fa-chevron-down"></i></span>
          </button>
        </h3>
        <div class="faq__answer-panel" data-accordion-panel id="faq-panel-2" role="region" aria-labelledby="faq-trigger-2" hidden>
          <p class="faq__answer">Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ о&nbsp;формате обращения и&nbsp;порядке первичного контакта с&nbsp;центром.</p>
          <p class="faq__answer">Текст не&nbsp;является маркетинговым обещанием и&nbsp;не&nbsp;заменяет консультацию специалиста. Финальная редакция будет согласована оператором отдельно.</p>
        </div>
      </div>

      <div class="faq__item" data-accordion-item>
        <h3 class="faq__item-title">
          <button type="button" class="faq__question" data-accordion-button aria-expanded="false" aria-controls="faq-panel-3" id="faq-trigger-3">
            <span class="faq__question-label">Как долго длится реабилитация?</span>
            <span class="faq__icon" aria-hidden="true"><i class="fas fa-chevron-down"></i></span>
          </button>
        </h3>
        <div class="faq__answer-panel" data-accordion-panel id="faq-panel-3" role="region" aria-labelledby="faq-trigger-3" hidden>
          <p class="faq__answer">Это временный технический текст для проверки высоты аккордеона. В&nbsp;финальной версии здесь будет описан типовой порядок этапов сопровождения без указания конкретных сроков.</p>
          <p class="faq__answer">Длительность программы зависит от&nbsp;индивидуального запроса и&nbsp;согласуется на&nbsp;консультации. Данный абзац добавлен только для вёрсточной проверки.</p>
        </div>
      </div>

      <div class="faq__item" data-accordion-item>
        <h3 class="faq__item-title">
          <button type="button" class="faq__question" data-accordion-button aria-expanded="false" aria-controls="faq-panel-4" id="faq-trigger-4">
            <span class="faq__question-label">Как уговорить близкого пройти лечение от&nbsp;зависимости?</span>
            <span class="faq__icon" aria-hidden="true"><i class="fas fa-chevron-down"></i></span>
          </button>
        </h3>
        <div class="faq__answer-panel" data-accordion-panel id="faq-panel-4" role="region" aria-labelledby="faq-trigger-4" hidden>
          <p class="faq__answer">Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ о&nbsp;том, как семье подготовиться к&nbsp;разговору с&nbsp;близким человеком.</p>
          <p class="faq__answer">Материал носит справочный характер и&nbsp;не&nbsp;содержит обещаний результата. Окончательная формулировка будет подготовлена в&nbsp;рамках контентного этапа.</p>
        </div>
      </div>

      <div class="faq__item" data-accordion-item>
        <h3 class="faq__item-title">
          <button type="button" class="faq__question" data-accordion-button aria-expanded="false" aria-controls="faq-panel-5" id="faq-trigger-5">
            <span class="faq__question-label">Можно ли самостоятельно перестать употреблять наркотики?</span>
            <span class="faq__icon" aria-hidden="true"><i class="fas fa-chevron-down"></i></span>
          </button>
        </h3>
        <div class="faq__answer-panel" data-accordion-panel id="faq-panel-5" role="region" aria-labelledby="faq-trigger-5" hidden>
          <p class="faq__answer">Это временный технический текст для проверки аккордеона. В&nbsp;финальной версии здесь будет нейтральное описание сценариев, когда самостоятельные попытки требуют дополнительной поддержки.</p>
          <p class="faq__answer">Текст не&nbsp;содержит медицинских утверждений и&nbsp;не&nbsp;описывает гарантированный исход. Используется только для проверки поведения интерфейса на&nbsp;разных экранах.</p>
        </div>
      </div>

      <div class="faq__item" data-accordion-item>
        <h3 class="faq__item-title">
          <button type="button" class="faq__question" data-accordion-button aria-expanded="false" aria-controls="faq-panel-6" id="faq-trigger-6">
            <span class="faq__question-label">Как понять, что у&nbsp;меня есть проблемы с&nbsp;алкоголем?</span>
            <span class="faq__icon" aria-hidden="true"><i class="fas fa-chevron-down"></i></span>
          </button>
        </h3>
        <div class="faq__answer-panel" data-accordion-panel id="faq-panel-6" role="region" aria-labelledby="faq-trigger-6" hidden>
          <p class="faq__answer">Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ с&nbsp;ориентирами для самонаблюдения без диагностических формулировок.</p>
          <p class="faq__answer">Материал предназначен для проверки типографики и&nbsp;вертикальных отступов. Контент будет заменён после согласования с&nbsp;оператором.</p>
        </div>
      </div>

      <div class="faq__item" data-accordion-item>
        <h3 class="faq__item-title">
          <button type="button" class="faq__question" data-accordion-button aria-expanded="false" aria-controls="faq-panel-7" id="faq-trigger-7">
            <span class="faq__question-label">Зачем в&nbsp;программу включены занятия йогой?</span>
            <span class="faq__icon" aria-hidden="true"><i class="fas fa-chevron-down"></i></span>
          </button>
        </h3>
        <div class="faq__answer-panel" data-accordion-panel id="faq-panel-7" role="region" aria-labelledby="faq-trigger-7" hidden>
          <p class="faq__answer">Это временный технический текст для проверки аккордеона. В&nbsp;финальной версии здесь будет описана роль практик в&nbsp;общей программе сопровождения.</p>
          <p class="faq__answer">Текст не&nbsp;является рекламным обещанием и&nbsp;не&nbsp;заменяет индивидуальную консультацию. Абзац добавлен для проверки высоты раскрытой панели.</p>
        </div>
      </div>

      <div class="faq__item" data-accordion-item>
        <h3 class="faq__item-title">
          <button type="button" class="faq__question" data-accordion-button aria-expanded="false" aria-controls="faq-panel-8" id="faq-trigger-8">
            <span class="faq__question-label">Какие методы профилактики зависимости используются?</span>
            <span class="faq__icon" aria-hidden="true"><i class="fas fa-chevron-down"></i></span>
          </button>
        </h3>
        <div class="faq__answer-panel" data-accordion-panel id="faq-panel-8" role="region" aria-labelledby="faq-trigger-8" hidden>
          <p class="faq__answer">Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ о&nbsp;подходах профилактики в&nbsp;обобщённой форме.</p>
          <p class="faq__answer">Формулировки носят технический характер и&nbsp;не&nbsp;содержат конкретных методик или гарантий. Используются только для проверки интерфейса.</p>
        </div>
      </div>

      <div class="faq__item" data-accordion-item>
        <h3 class="faq__item-title">
          <button type="button" class="faq__question" data-accordion-button aria-expanded="false" aria-controls="faq-panel-9" id="faq-trigger-9">
            <span class="faq__question-label">Не&nbsp;могу полностью исключить работу. Можно&nbsp;ли совместить процесс реабилитации с&nbsp;работой?</span>
            <span class="faq__icon" aria-hidden="true"><i class="fas fa-chevron-down"></i></span>
          </button>
        </h3>
        <div class="faq__answer-panel" data-accordion-panel id="faq-panel-9" role="region" aria-labelledby="faq-trigger-9" hidden>
          <p class="faq__answer">Это временный технический текст для проверки аккордеона. В&nbsp;финальной версии здесь будет описан порядок согласования рабочего графика в&nbsp;общих чертах.</p>
          <p class="faq__answer">Текст не&nbsp;содержит обещаний по&nbsp;срокам и&nbsp;условиям. Добавлен для проверки многоабзацного ответа и&nbsp;корректной работы клавиатурного управления.</p>
        </div>
      </div>

      <div class="faq__item" data-accordion-item>
        <h3 class="faq__item-title">
          <button type="button" class="faq__question" data-accordion-button aria-expanded="false" aria-controls="faq-panel-10" id="faq-trigger-10">
            <span class="faq__question-label">Как понять, что близкий человек стал наркоманом?</span>
            <span class="faq__icon" aria-hidden="true"><i class="fas fa-chevron-down"></i></span>
          </button>
        </h3>
        <div class="faq__answer-panel" data-accordion-panel id="faq-panel-10" role="region" aria-labelledby="faq-trigger-10" hidden>
          <p class="faq__answer">Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ для родственников с&nbsp;нейтральными рекомендациями по&nbsp;наблюдению.</p>
          <p class="faq__answer">Материал не&nbsp;содержит диагностических утверждений и&nbsp;не&nbsp;заменяет очную консультацию. Используется только для проверки вёрстки и&nbsp;поведения аккордеона.</p>
        </div>
      </div>
    </div>
  </div>
</section>
