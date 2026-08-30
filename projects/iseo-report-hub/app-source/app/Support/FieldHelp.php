<?php
declare(strict_types=1);

namespace Iseo\Support;

/**
 * Static field-help copy map for internal SEO forms.
 * No DB — render/UI only.
 */
final class FieldHelp
{
    private static int $instanceCounter = 0;

    /**
     * Canonical keys + aliases from Field Help Copy Pack v0.1.
     *
     * @var array<string, array{title:string,hint:string,example?:string,caution?:string}>
     */
    private const ENTRIES = [
        // Work entry
        'work_entry.category' => [
            'title' => 'Категория',
            'hint' => 'Выберите категорию из каталога работ Никиты, если работа типовая. Если работа разовая или не подходит ни под одну категорию — оставьте «без категории».',
            'example' => 'Техническое SEO / Контент / Коммерческие факторы (как в каталоге).',
        ],
        'work_entry.catalog_item' => [
            'title' => 'Работа из каталога',
            'hint' => 'Можно выбрать готовую работу из каталога — тогда название часто подставится само. Или оставьте пустым и опишите ручную работу в поле «Название».',
            'example' => 'Выбор пункта вроде «Проверка индексации» вместо свободного текста.',
        ],
        'work_entry.title' => [
            'title' => 'Название',
            'hint' => 'Короткое имя работы для списка и сборки отчёта. Если выбрана работа из каталога, поле можно оставить пустым — подставится имя из каталога. Для ручной работы напишите ясный заголовок без внутреннего жаргона задач.',
            'example' => 'Проверка индексации приоритетных URL услуг',
        ],
        'work_entry.description' => [
            'title' => 'Описание',
            'hint' => 'Что именно сделали или планируете: объём, страницы, инструмент, результат. Можно чуть подробнее, чем в «Кратко для клиента».',
            'example' => 'Сверили покрытие в вебмастере по 160 URL раздела услуг. Нашли 18 страниц вне индекса и 6 с мягкими 404 после смены ЧПУ.',
        ],
        'work_entry.status' => [
            'title' => 'Статус',
            'hint' => 'Фактическое состояние работы сейчас. Не путайте со «ролью в периоде»: статус — про жизнь работы, роль — про то, как работа попадает в разделы отчёта.',
            'example' => '«В работе» для текущей задачи; «Выполнено» для закрытой.',
        ],
        'work_entry.period_role' => [
            'title' => 'Роль в периоде',
            'hint' => 'Как эта работа участвует в месячном отчёте: выполненная работа, план, риск или внутренняя заметка. От роли зависит, в какие черновики разделов она попадёт при сборке.',
            'example' => '«Выполнено» для закрытой работы; «План» на следующий месяц; «Риск», если нужен блокер клиенту.',
        ],
        'work_entry.client_visibility' => [
            'title' => 'Видимость для клиента',
            'hint' => 'Показывать ли формулировки клиенту. Внутренние технические детали и сомнения оставляйте во «Внутреннем» режиме.',
            'example' => 'Клиентские работы аудита — «Клиенту»; черновые гипотезы — «Внутреннее».',
        ],
        'work_entry.client_summary' => [
            'title' => 'Кратко для клиента',
            'hint' => 'Короткая формулировка, которую можно показать клиенту в отчёте. Пишите без внутренних деталей, ссылок на задачи и технического жаргона.',
            'example' => 'Проверили индексацию ключевых страниц и нашли страницы, которые требуют доработки мета-тегов.',
        ],
        'work_entry.internal_note' => [
            'title' => 'Внутренняя заметка',
            'hint' => 'Рабочая заметка для команды. Клиент её не увидит. Здесь можно писать технические детали, сомнения, ссылки на внутренние задачи.',
            'example' => 'В Search Console странный всплеск soft 404 на /uslugi/ — проверить редиректы после релиза.',
        ],
        'work_entry.evidence_note' => [
            'title' => 'Заметка по доказательствам',
            'hint' => 'Что подтверждает факт работы: выгрузка, скриншот, файл, ссылка на проверку, дата проверки. Не вставляйте пароли и доступы.',
            'example' => 'Скрин покрытия; таблица URL в общем диске SEO.',
            'caution' => 'Не указывайте пароли, токены и доступы к кабинетам.',
        ],
        'work_entry.sort_order' => [
            'title' => 'Порядок',
            'hint' => 'Число для ручной сортировки в списке работ. Меньше — выше. Drag-and-drop нет.',
            'example' => '10, 20, 30 с шагом 10, чтобы было куда вставить новые.',
        ],

        // Report block
        'report_block.block_key' => [
            'title' => 'Ключ блока',
            'hint' => 'Стабильный технический ключ латиницей (a-z, цифры, _, -). Нужен системе и шаблону, не клиенту. Не меняйте без причины после выхода из черновика.',
            'example' => 'technical_audit, indexation, meta_tags',
        ],
        'report_block.block_type' => [
            'title' => 'Тип блока',
            'hint' => 'Тип влияет на то, как блок участвует в сборке/шаблоне. Выбирайте ближайший смысловой тип; не создавайте дубликаты одного смысла с разными ключами.',
            'example' => 'Текстовый блок результатов или блок плана — по доступному списку типов в форме.',
        ],
        'report_block.title' => [
            'title' => 'Название',
            'hint' => 'Заголовок секции, понятный клиенту и команде.',
            'example' => 'Индексация и покрытие сайта',
        ],
        'report_block.summary' => [
            'title' => 'Кратко',
            'hint' => 'Короткий вывод по блоку (1–3 предложения). Попадает в обзорные места отчёта.',
            'example' => 'Покрытие приоритетных URL выросло; остались исключения в архивных разделах.',
        ],
        'report_block.body' => [
            'title' => 'Текст',
            'hint' => 'Основной текст блока: что проверяли, что нашли, что сделали, что дальше. Пишите связно, без дампа сырых логов.',
            'example' => 'Абзац про метод проверки + абзац про находки + абзац про сделанные правки.',
        ],
        'report_block.status' => [
            'title' => 'Статус блока',
            'hint' => 'Черновик / в работе / готов к ревью / проверен. Для финализации обычно нужны проверенные обязательные блоки.',
            'example' => 'К концу месяца — «Проверено»; mid-month — «В работе».',
        ],
        'report_block.sort_order' => [
            'title' => 'Порядок сортировки',
            'hint' => 'Целое число для порядка блоков в отчёте. Меньше — выше. Drag-and-drop нет.',
            'example' => '10, 20, 30',
        ],
        'report_block.data_json' => [
            'title' => 'data_json',
            'hint' => 'Расширенные структурированные данные для шаблона. Заполняйте только если понимаете формат. Обычный текстовый отчёт можно вести без этого поля.',
            'example' => '{"pages_checked":160,"indexed":142,"demo":true}',
            'caution' => 'Продвинутое поле. Необязательно для обычного текстового отчёта.',
        ],
        'report_block.source_metric_refs' => [
            'title' => 'source_metric_refs',
            'hint' => 'Ссылки/метки на источники цифр. Не указывайте реальные пароли, токены кабинетов и чужие аккаунты. Для демо помечайте вымышленные источники явно.',
            'example' => '{"source":"webmaster_coverage_export","date":"2026-07-18","demo":true}',
            'caution' => 'Без реальных паролей и токенов. Демо-источники помечайте demo:true.',
        ],

        // Monthly / report sections
        'report_section.executive_summary' => [
            'title' => 'Краткое резюме',
            'hint' => 'Самое важное за месяц для клиента: 4–6 предложений. Без внутренних задач и «мы покопались в коде».',
            'example' => 'В июле сфокусировались на техническом фундаменте и индексации. Закрыли критичные мета-теги на приоритетных страницах услуг и согласовали контент-план на август.',
        ],
        'report_section.results_summary' => [
            'title' => 'Результаты',
            'hint' => 'Измеримые или наблюдаемые итоги. Если цифры оценочные/демо — формулируйте осторожно, без вида «официальной аналитики кабинета».',
            'example' => 'Из 160 приоритетных URL в индексе 142; исправлены title/description на 24 страницах.',
            'caution' => 'Не выдавайте оценочные/демо-цифры за официальную аналитику кабинета.',
        ],
        'report_section.work_completed' => [
            'title' => 'Что сделали',
            'hint' => 'Перечень выполненных работ месяца понятным языком. Можно опираться на сборку из работ с ролью «выполнено».',
            'example' => 'Список аудита, индексации, мета, коммерческих факторов, контент-брифов.',
        ],
        'report_section.key_findings' => [
            'title' => 'Ключевые выводы',
            'hint' => '3–5 выводов, которые влияют на решения клиента или следующий месяц.',
            'example' => 'Главный рост отдачи даст доработка коммерческих факторов на посадочных, а не массовая генерация текстов.',
        ],
        'report_section.risks_and_blockers' => [
            'title' => 'Риски и блокеры',
            'hint' => 'Пишите только то, что реально мешает продвижению или требует решения клиента/менеджера. Формулируйте спокойно.',
            'example' => 'Требуется согласовать список приоритетных страниц для следующего этапа работ.',
        ],
        'report_section.next_month_plan' => [
            'title' => 'План на следующий месяц',
            'hint' => 'Конкретный план: что сделаем, в каком порядке, что нужно от клиента.',
            'example' => 'Август: закрыть коммерческие факторы на топ-10 URL, расширить кластеры услуг, подготовить 4 брифа.',
        ],
        'report_section.client_notes' => [
            'title' => 'Заметки для клиента',
            'hint' => 'Координационные заметки, которые можно показать клиенту (сроки согласований, вопросы). Не дублируйте всё резюме.',
            'example' => 'Нужна обратная связь по приоритету городов для посадочных до 28 августа.',
        ],
        'report_section.internal_notes' => [
            'title' => 'Внутренние заметки',
            'hint' => 'Только для команды. Сюда — технические долги, спорные гипотезы, напоминания ревьюеру.',
            'example' => 'Не тащить в клиентский PDF сырой crawl log; оставить summary.',
        ],
        'report_section.title' => [
            'title' => 'Название отчёта',
            'hint' => 'Понятное имя месячного отчёта для списка и шапки.',
            'example' => 'Отчёт SEO — проект — июль 2026',
        ],
        'report_section.status' => [
            'title' => 'Статус отчёта',
            'hint' => 'Жизненный цикл отчёта. Не финализируйте, пока тексты и ключевые работы не готовы к клиенту. Архив — вместо удаления.',
            'example' => 'Готовый месяц — «Финализирован»; текущий mid-month — «В работе».',
        ],

        // Assembly preview (optional surface)
        'assembly.future_block_text' => [
            'title' => 'Будущий текст блока',
            'hint' => 'Черновик текста, который получится из работ месяца по правилам сборки. Это ещё не сохранённый текст отчёта — его можно применить отдельно.',
            'example' => 'Список выполненных работ с клиентскими формулировками.',
        ],
        'assembly.apply_block' => [
            'title' => 'Применить этот блок',
            'hint' => 'Записывает черновик сборки в соответствующий раздел/блок отчёта. На финализированном отчёте применение заблокировано.',
            'caution' => 'Не применяйте на финализированном отчёте без отдельного reopen.',
        ],
    ];

    /** @var array<string, string> */
    private const ALIASES = [
        'work_entry.category_id' => 'work_entry.category',
        'work_entry.work_item_id' => 'work_entry.catalog_item',
        'monthly.executive_summary' => 'report_section.executive_summary',
        'monthly.results_summary' => 'report_section.results_summary',
        'monthly.work_completed' => 'report_section.work_completed',
        'monthly.key_findings' => 'report_section.key_findings',
        'monthly.risks_and_blockers' => 'report_section.risks_and_blockers',
        'monthly.next_month_plan' => 'report_section.next_month_plan',
        'monthly.client_notes' => 'report_section.client_notes',
        'monthly.internal_notes' => 'report_section.internal_notes',
        'monthly.title' => 'report_section.title',
        'monthly.status' => 'report_section.status',
    ];

    /**
     * @return array{title:string,hint:string,example?:string,caution?:string}|null
     */
    public static function get(string $key): ?array
    {
        $resolved = self::ALIASES[$key] ?? $key;
        return self::ENTRIES[$resolved] ?? null;
    }

    /**
     * Map monthly content field name → help key.
     */
    public static function keyForMonthlyField(string $fieldName): string
    {
        return 'report_section.' . $fieldName;
    }

    public static function nextDomId(string $prefix = 'field-help'): string
    {
        self::$instanceCounter++;
        return $prefix . '-' . self::$instanceCounter;
    }

    /**
     * Render help control HTML (escaped). Empty string if key unknown.
     */
    public static function render(string $key): string
    {
        $entry = self::get($key);
        if ($entry === null) {
            return '';
        }

        $domId = self::nextDomId();
        $title = $entry['title'];
        $hint = $entry['hint'];
        $example = $entry['example'] ?? null;
        $caution = $entry['caution'] ?? null;
        $aria = 'Подсказка: ' . $title;

        ob_start();
        require ISEO_VIEWS_PATH . DIRECTORY_SEPARATOR . 'partials' . DIRECTORY_SEPARATOR . 'field-help.php';
        return (string) ob_get_clean();
    }
}
