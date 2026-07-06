<?php
/**
 * Static V9 content authority fallbacks — V9-06E8.
 *
 * One-to-one copy from workspaces/fp-0002-shpigovsky-v9/src/ (uslugi-v2.html,
 * usluga-konechnaya-v1.html, kontakty partials). No invented copy.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Hub group static V9 copy keyed by parent service slug.
 *
 * @param string $slug Parent service slug.
 * @return array{title:string,intro:string,lead:string,cta_label:string,subnav_label:string}|null
 */
function shpigovsky_get_v9_services_hub_group_copy( $slug ) {
	$map = array(
		'zavisimosti' => array(
			'title'         => 'Зависимости и пристрастия',
			'intro'         => 'Зависимость не начинается с желания разрушить себе жизнь. Начало в попытках справиться с болью, тревогой, пустотой или просто с ощущением, что иначе не получается. Наша программа направлена не просто на то, чтобы вывести токсичные вещества из организма, а на то, чтобы восстановить способность получать удовольствие, справляться со стрессом. Устойчиво и по-настоящему.',
			'lead'          => 'Мы не работаем с симптомами в отрыве от человека. В основе нашего подхода — мультидисциплинарная команда специалистов, которые видят картину целиком.',
			'cta_label'     => 'Записаться на консультацию',
			'subnav_label'  => 'Зависимости',
		),
		'psihicheskoe-zdorovie' => array(
			'title'         => 'Психическое здоровье',
			'intro'         => 'Тревога, которая не отпускает. Депрессия, из которой не выйти привычными способами. Состояния, которые сложно описать вслух, — но которые реально мешают жить. Психические расстройства почти никогда не бывают «просто в голове»: за ними стоят конкретные нейробиологические процессы, психологические триггеры, невидимые со стороны травмы или хронический стресс.',
			'lead'          => 'Мы работаем с психическим здоровьем без упрощений. Каждое состояние исследуется глубоко. Потому что понять причину — значит уже наполовину найти выход.',
			'cta_label'     => 'Записаться на консультацию',
			'subnav_label'  => 'Психическое здоровье',
		),
		'rasstroystva-pischevogo-povedeniya' => array(
			'title'         => 'Расстройства пищевого поведения',
			'intro'         => 'Взаимоотношения с едой — это отношения с собственным телом, с контролем, с ощущением себя. За ограничениями в еде, перееданием или навязчивыми ритуалами вокруг питания стоит что-то, что ждёт внимания и аккуратной работы, а не порицания.',
			'lead'          => 'Мы работаем с тем, что лежит в основе: тревогой, перфекционизмом, нарушением образа тела (субъективное восприятие собственного тела), а также с нейрохимическими особенностями, которые усиливают эти состояния.',
			'cta_label'     => 'Записаться на консультацию',
			'subnav_label'  => 'Пищевые расстройства',
		),
		'genotipirovanie' => array(
			'title'         => 'Генотипирование',
			'intro'         => '',
			'lead'          => '',
			'cta_label'     => 'Записаться на консультацию',
			'subnav_label'  => 'Генотипирование',
		),
	);

	return isset( $map[ $slug ] ) ? $map[ $slug ] : null;
}

/**
 * Hub child card static V9 copy keyed by child service slug.
 *
 * @param string $slug Child service slug.
 * @return array{title:string,text:string}|null
 */
function shpigovsky_get_v9_services_hub_child_copy( $slug ) {
	$demo_lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation.';

	$map = array(
		'lechenie-alkogolnoy-zavisimosti' => array(
			'title' => 'Алкогольная зависимость',
			'text'  => 'Алкоголь не становится проблемой в один день — зачастую это постепенный процесс, в котором граница между «нормой» и зависимостью стирается незаметно. В основе — нейробиологические изменения в системе вознаграждения мозга, которые делают отказ физически и психологически тяжёлым без посторонней помощи. Мы работаем с причинами и помогаем выйти из замкнутого круга устойчиво.',
		),
		'lechenie-narkoticheskoy-zavisimosti' => array(
			'title' => 'Наркотическая зависимость',
			'text'  => 'Наркотическая зависимость — одно из наиболее сложных состояний: она затрагивает одновременно биохимию мозга, психологию человека и его социальную жизнь. За ней почти всегда стоит что-то, что предшествовало употреблению, — боль, травма, невозможность справиться со стрессом иначе. Наша задача — разобраться и выстроить путь к восстановлению, который будет работать в реальной жизни.',
		),
		'lekarstva' => array(
			'title' => 'Лекарственная зависимость',
			'text'  => 'Лекарственная зависимость нередко формируется там, где меньше всего ждёшь — на фоне лечения тревоги, боли или бессонницы. Это не безответственность: некоторые препараты меняют работу мозга так, что организм перестаёт справляться без них. Мы работаем с этим состоянием бережно и без осуждения — с вниманием к тому, что изначально привело к приёму препаратов.',
		),
		'lechenie-povedencheskoy-zavisimosti' => array(
			'title' => 'Поведенческие зависимости',
			'text'  => 'Игромания, шопоголизм, интернет-зависимость, сексуальная зависимость — эти состояния часто воспринимаются как «ненастоящие», что делает их ещё тяжелее. Между тем механизм здесь тот же, что и при химических зависимостях: нарушение работы системы вознаграждения мозга, то есть когда мозг ищет во внешних стимулах то, что не может получить естественным путём. Мы относимся к поведенческим зависимостям как к действительным состояниям — и работаем с ними соответственно.',
		),
		'depressiya' => array(
			'title' => 'Депрессия',
			'text'  => $demo_lorem,
		),
		'ptrs' => array(
			'title' => 'ПТСР',
			'text'  => $demo_lorem,
		),
		'emocionalnoe-vygoranie' => array(
			'title' => 'Эмоциональное выгорание',
			'text'  => $demo_lorem,
		),
		'trevozhnye-rasstroystva' => array(
			'title' => 'Тревожные расстройства',
			'text'  => $demo_lorem,
		),
		'rasstroystva-sna' => array(
			'title' => 'Расстройства сна',
			'text'  => $demo_lorem,
		),
		'travma' => array(
			'title' => 'Травма',
			'text'  => $demo_lorem,
		),
		'anoreksiya' => array(
			'title' => 'Нервная анорексия',
			'text'  => $demo_lorem,
		),
		'nervnaya-bulimiya' => array(
			'title' => 'Нервная булимия',
			'text'  => $demo_lorem,
		),
		'kompulsivnoe-pereedanie' => array(
			'title' => 'Компульсивное переедание',
			'text'  => $demo_lorem,
		),
		'genotipirovanie' => array(
			'title' => 'Анализ генетической предрасположенности и рисков',
			'text'  => '',
		),
	);

	return isset( $map[ $slug ] ) ? $map[ $slug ] : null;
}

/**
 * Static V9 gallery captions for services hub groups.
 *
 * @param string $slug Parent service slug.
 * @return string[]
 */
function shpigovsky_get_v9_services_hub_gallery_captions( $slug ) {
	$map = array(
		'zavisimosti' => array(
			'Лечение интернет зависимости',
			'Компьютерная зависимость',
			'Лечение опиумной зависимости',
		),
		'psihicheskoe-zdorovie' => array(
			'Хроническая усталось',
			'Стресс',
			'Нарциссизм',
		),
	);

	return isset( $map[ $slug ] ) ? $map[ $slug ] : array();
}

/**
 * Services hub program block static V9 copy (uslugi-v2 services-program-v2).
 *
 * @return array{heading:string,lead:string,intro:string,intro2:string,cta:array<string,string>}
 */
function shpigovsky_get_v9_services_hub_program_copy() {
	return array(
		'heading' => 'Наша программа включает 4 направления',
		'lead'    => 'Боль бывает очень похожей у разных людей — но путь к восстановлению всегда индивидуален. Именно поэтому в нашем центре не существует стандартных программ. Каждый маршрут выстраивается вокруг конкретного человека, его целей и его будущего.',
		'intro'   => 'Каждый человек приходит к нам со своей историей. Со своим сочетанием причин, обстоятельств и состояний, которые привели его туда, где он сейчас находится. Именно поэтому универсальных программ в нашем центре не существует. Программа реабилитации выстраивается из отдельных блоков — каждый из которых направлен на свой уровень работы: генетические предрасположенности, нейрологические паттерны, психологическое состояние и физическое восстановление тела. Вместе они создают целостный, по-настоящему индивидуальный маршрут — такой, который работает именно для вас.',
		'intro2'  => '',
		'cta'     => array(
			'title'        => 'Запишитесь на гостевой визит',
			'subtitle'     => 'Вы сможете все посмотреть и задать вопросы лично',
			'button_label' => 'Записаться',
			'source'       => 'services-program-guest',
		),
		'secondary_cta' => array(
			'title'        => 'Запишитесь на гостевой визит',
			'subtitle'     => 'Вы сможете все посмотреть и задать вопросы лично',
			'button_label' => 'Записаться',
			'source'       => 'services-program-cta-secondary',
		),
	);
}

/**
 * Alcohol service leaf intro static V9 copy.
 *
 * @return array{heading:string,highlight:string}
 */
function shpigovsky_get_v9_alcohol_leaf_intro_copy() {
	return array(
		'heading'   => 'Алкогольная зависимость — это не персональный выбор',
		'highlight' => 'ЗАВИСИМОСТЬ — НЕ ПРОСТУПОК И НЕ ЧЕРТА ХАРАКТЕРА: ЗА НЕЙ СТОЯТ ОПРЕДЕЛЕННЫЕ НЕЙРОБИОЛОГИЧЕСКИЕ ПРОЦЕССЫ И ПСИХОЛОГИЧЕСКИЕ ПРИЧИНЫ.',
	);
}

/**
 * Alcohol bordered-info subsections — static V9 authority.
 *
 * @return array<int, array{heading:string,text:string}>
 */
function shpigovsky_get_v9_alcohol_bordered_info_subsections() {
	return array(
		array(
			'heading' => 'ЗАВИСИМОСТЬ НЕ НАЧИНАЕТСЯ С ЖЕЛАНИЯ РАЗРУШИТЬ СЕБЯ',
			'text'    => 'Большинство из тех, у кого развивается алкогольная зависимость, начинают пить в подростковом возрасте. В этот период остро нужно чувство принадлежности, понимания кто мы, где наше место. Если внутри живёт тревога, низкая самооценка или непрожитая боль, алкоголь даёт то, чего не хватало: ощущение «я нормальный, я как все». Его опьяняющее действие увеличивает количество нейрохимических веществ в организме, вызывающих чувство эйфории. Мозг запоминает это и связь закрепляется.',
		),
		array(
			'heading' => 'КАК ДВА БОКАЛА ПРЕВРАЩАЮТСЯ В БУТЫЛКУ С УТРА',
			'text'    => 'С ростом ответственности, занятости, статуса стресс нарастает — доза растёт. Алкоголь нарушает сон, усиливает тревогу, а тревога требует новой дозы. Появляется стыд, человек скрывает происходящее, отдаляется от близких и единственным облегчением остаётся то, что уже разрушает. Нейрологическая связь усиливается, поскольку мозг начинает ассоциировать употребление алкоголя с облегчением стресса. В какой-то момент без алкоголя становится физически невыносимо и бутылка открывается уже с утра.',
		),
		array(
			'heading' => 'ЭТО НЕ ВАША ВИНА — И ВЫХОД ЕСТЬ',
			'text'    => 'Этот цикл случается с людьми каждый день. Попытки справиться с болью, тревогой и стрессом не делают человека плохим. Вырваться из замкнутого круга в одиночку очень трудно. Но с правильной поддержкой — возможно.',
		),
	);
}

/**
 * Alcohol signs block static V9 copy.
 *
 * @return array{heading:string,intro:string,items:string[],editorial:string}
 */
function shpigovsky_get_v9_alcohol_signs_copy() {
	return array(
		'heading'   => 'Признаки алкогольной зависимости',
		'intro'     => 'Если вы подозреваете у себя или вашего близкого человека алкогольную зависимость, обратите внимание на следующие утверждения. Если вы согласны хотя бы с одним из нижеперечисленных утверждений, возможно, проблемы с употреблением алкоголя присутствуют.',
		'items'     => array(
			'В последние несколько месяцев вам не удавалось уложиться в сроки или выполнить поставленные задачи из-за употребления алкоголя?',
			'Вам когда-нибудь требовался алкоголь, чтобы нормально функционировать после ночи обильного употребления спиртного?',
			'Вам часто бывает трудно определить, что вы чувствуете во время или после употребления алкоголя?',
			'У вас когда-нибудь случались провалы в памяти из-за употребления алкоголя?',
			'Вы думаете или знаете ли вы, что ваши родственники и друзья обеспокоены вашим пристрастием к алкоголю?',
			'Бывает ли так, что вы продолжаете пить до тех пор, пока не потеряете сознание?',
			'Вы часто испытываете сильную тягу к алкоголю?',
			'Вы нарушили обещание, данное близким, из-за своего пристрастия к алкоголю?',
			'Вы опасаетесь, что можете быть алкоголиком?',
		),
		'editorial' => 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tem',
	);
}

/**
 * Alcohol leaf program block demo copy from V9 fixture (lorem — classified DEMO).
 *
 * @return array{lead:string,intro:string,intro2:string}
 */
function shpigovsky_get_v9_alcohol_leaf_program_demo_copy() {
	return array(
		'lead'   => 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
		'intro'  => 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
		'intro2' => 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
	);
}

/**
 * Contacts location map image paths (theme assets).
 *
 * @return array{mo:string,moscow:string}
 */
function shpigovsky_get_v9_contacts_map_images() {
	return array(
		'mo'     => 'img/content/contacts/contacts-map-mo-region.png',
		'moscow' => 'img/content/contacts/contacts-map-moscow.png',
	);
}
