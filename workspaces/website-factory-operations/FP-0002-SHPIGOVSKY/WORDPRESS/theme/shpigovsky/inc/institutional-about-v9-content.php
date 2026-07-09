<?php
/**
 * Static V9 /o-centre/ content authority — V9-06E26A.
 *
 * One-to-one copy from workspaces/fp-0002-shpigovsky-v9/src/pages/o-centre.html
 * and related partials. No invented copy.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * About hub sub-navigation anchor items (static V9 order).
 *
 * @return array<int, array{id:string,label:string}>
 */
function shpigovsky_get_v9_about_hub_subnav_items() {
	return array(
		array( 'id' => 'who-we-are', 'label' => 'Кто мы' ),
		array( 'id' => 'who-we-treat', 'label' => 'Кого мы лечим' ),
		array( 'id' => 'our-approach', 'label' => 'Наш подход к лечению' ),
		array( 'id' => 'our-program', 'label' => 'Наша программа лечения' ),
		array( 'id' => 'our-home', 'label' => 'Наш Дом' ),
		array( 'id' => 'specialists', 'label' => 'Специалисты' ),
		array( 'id' => 'reviews', 'label' => 'Отзывы' ),
	);
}

/**
 * Institutional narrative static copy.
 *
 * @return array{heading:string,lead:string,paragraphs:array<int,string>}
 */
function shpigovsky_get_v9_about_narrative_copy() {
	return array(
		'heading'    => 'Шпиговсикй дом — место, где видят человека, а не только диагноз',
		'lead'       => 'Ведем прием и консультируем в Москве и Московской области. Для нас не существует границ в привычном понимании этого слова — к нам приезжают из разных городов и стран, доверяя свое здоровье и благополучие заботливой помощи наших специалистов.',
		'paragraphs' => array(
			'За время нашей работы через нас прошли люди с очень разными историями — но с одним общим опытом: где-то в какой-то момент стало слишком тяжело справляться одному.',
			'Мы не клиника в привычном смысле слова. Мы — социально-психологическое пространство с командой дипломированных специалистов, которые работают согласованно и видят картину целиком. Нет стандартных протоколов, нет потоков. Есть внимательная работа с конкретным человеком — его биологией, его психологией, его жизнью.',
			'В основе нашего подхода — убеждение, что устойчивое восстановление возможно только тогда, когда понята настоящая причина. Не симптом убран, а причина найдена и проработана. Именно поэтому мы начинаем с диагностики: нейропсихологической, психологической, а при необходимости — генетической. И только потом выстраиваем программу — индивидуально, под конкретного человека.',
			'Здесь нет решёток и замков. Нет жёсткого режима. Есть пространство, в котором можно выдохнуть, разобраться в происходящем и начать двигаться вперёд — в своём темпе, с командой рядом.',
		),
	);
}

/**
 * Who-we-treat section static copy.
 *
 * @return array<string,mixed>
 */
function shpigovsky_get_v9_about_who_we_treat_copy() {
	return array(
		'heading'  => 'Разные люди, разные истории — одно общее: что-то пошло не так',
		'intro'    => 'К нам приходят люди, которые устали. Устали бороться с собой, устали притворяться, что всё в порядке, устали от схем, которые перестали работать. Некоторые приходят сами — когда понимают, что дальше так невозможно. Другие приходят с близкими, которые первыми увидели то, что сам человек не мог или не хотел замечать.',
		'lead'     => 'Мы работаем с широким спектром состояний:',
		'spectrum' => array(
			array(
				'title' => 'Зависимости и пристрастия',
				'text'  => '— алкогольная, наркотическая, лекарственная зависимость, а также поведенческие зависимости: игромания (лудомания), шопоголизм, интернет-зависимость, сексуальная зависимость и другие. В основе большинства из них — нарушение работы системы вознаграждения мозга, а именно гипофункция дофаминовой системы (сниженная активность путей, отвечающих за естественное переживание удовольствия и удовлетворения). Это не личностная слабость. Это биология человека, с которой можно и нужно работать.',
			),
			array(
				'title' => 'Психическое здоровье',
				'text'  => '— тревожные расстройства, депрессия, ПТСР (посттравматическое стрессовое расстройство), СДВГ (синдром дефицита внимания и гиперактивности), эмоциональное выгорание, расстройства сна и другие состояния, которые мешают жить так, как хочется.',
			),
			array(
				'title' => 'Расстройства пищевого поведения (РПП)',
				'text'  => '— нервная анорексия (патологический отказ от еды), нервная булимия (провокация вывода из организма съеденной пищи), компульсивное переедание, орторексия (навязчивое стремление к «правильному» питанию) и другие нарушения отношений с едой и собственным телом.',
			),
		),
		'callout'  => 'Нас не беспокоит социальный статус или прошлое человека. Нас беспокоит его настоящее — и то, каким может стать его будущее.',
		'cards'    => array(
			array(
				'title' => 'диагностические инструменты',
				'text'  => 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation Lorem ipsum dolor',
			),
			array(
				'title' => 'Психиатрия',
				'text'  => 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation Lorem ipsum dolor',
			),
			array(
				'title' => 'Функциональная терапия',
				'text'  => 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation Lorem ipsum dolor',
			),
			array(
				'title' => 'комплиментарная терапия',
				'text'  => 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation Lorem ipsum dolor',
			),
		),
	);
}

/**
 * Program approach band static copy.
 *
 * @return array{heading:string,highlight:string,intro:string}
 */
function shpigovsky_get_v9_about_approach_copy() {
	return array(
		'heading'   => 'Наш подход к лечению',
		'highlight' => 'Мы используем мультидисциплинарный подход — когда лечение одного пациента обеспечивается командой специалистов разных профилей. Такой подход становится залогом понимания и решения проблемы.',
		'intro'     => 'Лечение в нашем реабилитационном центре совмещает современный и мультидисциплинарный подход направленный на устранение истинных причин зависимости.',
	);
}

/**
 * About hub program section static copy (o-centre variant).
 *
 * @return array{heading:string,lead:string,intro:string,intro2:string,items:array<int,array{title:string,image:string,width:int,height:int,alt:string}>}
 */
function shpigovsky_get_v9_about_program_copy() {
	return array(
		'heading' => 'Наша программа включает 4 направления',
		'lead'    => 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
		'intro'   => 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
		'intro2'  => 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
		'items'   => array(
			array(
				'title'  => '01 — Генотипирование',
				'image'  => 'img/content/rehabilitation-program/program-genotyping.webp',
				'width'  => 1216,
				'height' => 1632,
				'alt'    => 'Генотипирование',
			),
			array(
				'title'  => '02 — Нейропсихологическая коррекция',
				'image'  => 'img/content/rehabilitation-program/program-neuropsychology.webp',
				'width'  => 1632,
				'height' => 1216,
				'alt'    => 'Нейропсихологическая коррекция',
			),
			array(
				'title'  => '03 — Психокоррекция',
				'image'  => 'img/content/rehabilitation-program/program-psychocorrection.webp',
				'width'  => 880,
				'height' => 1184,
				'alt'    => 'Психокоррекция',
			),
			array(
				'title'  => '04 — Кинезиотерапия',
				'image'  => 'img/content/rehabilitation-program/program-kinesiotherapy.webp',
				'width'  => 880,
				'height' => 1184,
				'alt'    => 'Кинезиотерапия',
			),
		),
	);
}

/**
 * Guest visit CTA band defaults for about hub.
 *
 * @return array{title:string,subtitle:string,button_label:string,source:string}
 */
function shpigovsky_get_v9_about_guest_cta_copy() {
	return array(
		'title'        => 'Запишитесь на гостевой визит',
		'subtitle'     => 'Вы сможете все посмотреть и задать вопросы лично',
		'button_label' => 'Записаться',
		'source'       => 'o-centre-guest-cta',
	);
}

/**
 * Infrastructure narrative static copy keyed by group slug.
 *
 * @return array<string,array{heading?:string,lead?:string,bullet?:string}>
 */
function shpigovsky_get_v9_about_infrastructure_copy() {
	return array(
		'g0' => array(
			'heading' => 'Место, где лечение начинается с ощущения безопасности',
			'lead'    => '«Шпиговский Дом» расположен в ближнем Подмосковье, к северу от Москвы — в тихом месте, окружённом зеленью. Здесь нет ощущения учреждения: нет казённой обстановки, нет жёсткого режима, нет изоляции. Это действительно дом — тёплый, продуманный, в котором можно расслабиться и быть собой.',
		),
		'g1' => array(
			'bullet' => 'Мы убеждены, что физическое движение и качество отдыха — такая же часть программы, как психотерапия и нейрокоррекция. Поэтому на территории центра есть всё необходимое для полноценной реабилитации: бассейн и сауна для восстановления тела и снятия физического напряжения, теннисный корт для тех, кто хочет двигаться и соревноваться с собой, тренажёрный зал, обустроенные места для прогулок и отдыха на открытом воздухе.',
		),
		'g2' => array(
			'bullet' => 'Клиенты размещаются в комфортных комнатах с возможностью выбора категории — от индивидуального до совместного размещения, в зависимости от предпочтений и задач программы. Всего в доме одновременно живёт не более 15 человек — это принципиально: нам важно сохранять атмосферу внимания и заботы к каждому.',
		),
		'g3' => array(
			'bullet' => 'Повар готовит три раза в день по специальному меню, составленному с учётом задач восстановления: сбалансированное, вкусное, поддерживающее физическое и эмоциональное состояние. Еда — тоже часть реабилитации.',
		),
		'g4' => array(
			'bullet' => 'Территория огорожена и находится под круглосуточным видеонаблюдением. Психологи-консультанты доступны 24/7 — в любое время суток рядом будет кто-то, кому можно позвонить и с кем можно поговорить.',
		),
	);
}

/**
 * Infrastructure slider image sets (static V9 asset paths).
 *
 * @return array<string,array<int,array{src:string,width:int,height:int,alt:string}>>
 */
function shpigovsky_get_v9_about_infrastructure_gallery_sets() {
	$base = 'img/content/o-centre/';

	return array(
		'g1' => array(
			array( 'src' => $base . 'o-centre-infrastructure-01.webp', 'width' => 600, 'height' => 451, 'alt' => '' ),
			array( 'src' => $base . 'o-centre-infrastructure-02.webp', 'width' => 1209, 'height' => 911, 'alt' => '' ),
			array( 'src' => $base . 'o-centre-infrastructure-03.webp', 'width' => 596, 'height' => 448, 'alt' => '' ),
		),
		'g2' => array(
			array( 'src' => $base . 'o-centre-infrastructure-04.webp', 'width' => 895, 'height' => 671, 'alt' => '' ),
			array( 'src' => $base . 'o-centre-infrastructure-05.webp', 'width' => 904, 'height' => 676, 'alt' => '' ),
			array( 'src' => $base . 'o-centre-infrastructure-06.webp', 'width' => 903, 'height' => 678, 'alt' => '' ),
		),
		'g3' => array(
			array( 'src' => $base . 'o-centre-infrastructure-07.webp', 'width' => 1812, 'height' => 1312, 'alt' => '' ),
			array( 'src' => $base . 'o-centre-infrastructure-08.webp', 'width' => 1623, 'height' => 1155, 'alt' => '' ),
			array( 'src' => $base . 'o-centre-infrastructure-09.webp', 'width' => 1610, 'height' => 1146, 'alt' => '' ),
		),
		'g4' => array(
			array( 'src' => $base . 'o-centre-infrastructure-10.webp', 'width' => 1212, 'height' => 892, 'alt' => '' ),
			array( 'src' => $base . 'o-centre-infrastructure-11.webp', 'width' => 957, 'height' => 892, 'alt' => '' ),
			array( 'src' => $base . 'o-centre-infrastructure-12.webp', 'width' => 1189, 'height' => 888, 'alt' => '' ),
		),
		'g5' => array(
			array( 'src' => $base . 'o-centre-infrastructure-13.webp', 'width' => 2477, 'height' => 1394, 'alt' => 'Территория реабилитационного центра' ),
			array( 'src' => $base . 'o-centre-infrastructure-14.webp', 'width' => 1881, 'height' => 1246, 'alt' => '' ),
			array( 'src' => $base . 'o-centre-infrastructure-15.webp', 'width' => 891, 'height' => 1086, 'alt' => '' ),
			array( 'src' => $base . 'o-centre-infrastructure-16.webp', 'width' => 902, 'height' => 681, 'alt' => '' ),
			array( 'src' => $base . 'o-centre-infrastructure-17.webp', 'width' => 1992, 'height' => 1237, 'alt' => 'Пространство реабилитационного центра' ),
			array( 'src' => $base . 'o-centre-infrastructure-18.webp', 'width' => 2201, 'height' => 1227, 'alt' => '' ),
		),
	);
}
