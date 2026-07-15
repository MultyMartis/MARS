<?php
/**
 * Static V9 Home fallback data — D9-H ACF wiring authority.
 *
 * Read-only reference values when ACF fields are empty.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Scalar home text with static fallback.
 *
 * @param string $field_name ACF field name.
 * @param string $fallback   Static V9 fallback.
 * @return string
 */
function shpigovsky_home_text_or_fallback( $field_name, $fallback ) {
	$value = shpigovsky_get_home_field( $field_name );

	return '' !== $value ? $value : $fallback;
}

/**
 * Home repeater rows or static fallback rows.
 *
 * @param string   $field_name    ACF repeater field name.
 * @param array    $fallback_rows Static fallback rows.
 * @return array<int, array<string, mixed>>
 */
function shpigovsky_home_repeater_or_fallback( $field_name, $fallback_rows ) {
	$rows = shpigovsky_get_home_repeater( $field_name );

	return ! empty( $rows ) ? $rows : $fallback_rows;
}

/**
 * Global CTA / button label with site-option then static fallback.
 *
 * @param string $option_name Option field name.
 * @param string $fallback    Static fallback label.
 * @return string
 */
function shpigovsky_chrome_label_or_fallback( $option_name, $fallback ) {
	$value = shpigovsky_get_site_option( $option_name );

	return '' !== $value ? $value : $fallback;
}

/**
 * FAQ static fallback items (full V9 transplant set).
 *
 * @return array<int, array{question:string,answer:string,expanded:bool}>
 */
function shpigovsky_home_faq_fallback_items() {
	return array(
		array(
			'question'  => 'Как перестать именно хотеть выпить, а&nbsp;не&nbsp;заставлять себя этого не&nbsp;делать?',
			'answer'    => 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do&nbsp;eiusmod tempor incididunt ut&nbsp;labore et&nbsp;dolore magna aliqua. Ut&nbsp;enim ad&nbsp;minim veniam, quis nostrud exercitation .Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do&nbsp;eiusmod tempor incididunt ut&nbsp;labore et&nbsp;dolore magna aliqua. Ut&nbsp;enim ad&nbsp;minim veniam, quis nostrud exercitation .',
			'expanded'  => true,
			'multiline' => false,
		),
		array(
			'question'  => 'Анонимное лечение или нет?',
			'answer'    => "Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ о&nbsp;формате обращения и&nbsp;порядке первичного контакта с&nbsp;центром.\n\nТекст не&nbsp;является маркетинговым обещанием и&nbsp;не&nbsp;заменяет консультацию специалиста. Финальная редакция будет согласована оператором отдельно.",
			'expanded'  => false,
			'multiline' => true,
		),
		array(
			'question'  => 'Как долго длится реабилитация?',
			'answer'    => "Это временный технический текст для проверки высоты аккордеона. В&nbsp;финальной версии здесь будет описан типовой порядок этапов сопровождения без указания конкретных сроков.\n\nДлительность программы зависит от&nbsp;индивидуального запроса и&nbsp;согласуется на&nbsp;консультации. Данный абзац добавлен только для вёрсточной проверки.",
			'expanded'  => false,
			'multiline' => true,
		),
		array(
			'question'  => 'Как уговорить близкого пройти лечение от&nbsp;зависимости?',
			'answer'    => "Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ о&nbsp;том, как семье подготовиться к&nbsp;разговору с&nbsp;близким человеком.\n\nМатериал носит справочный характер и&nbsp;не&nbsp;содержит обещаний результата. Окончательная формулировка будет подготовлена в&nbsp;рамках контентного этапа.",
			'expanded'  => false,
			'multiline' => true,
		),
		array(
			'question'  => 'Можно ли самостоятельно перестать употреблять наркотики?',
			'answer'    => "Это временный технический текст для проверки аккордеона. В&nbsp;финальной версии здесь будет нейтральное описание сценариев, когда самостоятельные попытки требуют дополнительной поддержки.\n\nТекст не&nbsp;содержит медицинских утверждений и&nbsp;не&nbsp;описывает гарантированный исход. Используется только для проверки поведения интерфейса на&nbsp;разных экранах.",
			'expanded'  => false,
			'multiline' => true,
		),
		array(
			'question'  => 'Как понять, что у&nbsp;меня есть проблемы с&nbsp;алкоголем?',
			'answer'    => "Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ с&nbsp;ориентирами для самонаблюдения без диагностических формулировок.\n\nМатериал предназначен для проверки типографики и&nbsp;вертикальных отступов. Контент будет заменён после согласования с&nbsp;оператором.",
			'expanded'  => false,
			'multiline' => true,
		),
		array(
			'question'  => 'Зачем в&nbsp;программу включены занятия йогой?',
			'answer'    => "Это временный технический текст для проверки аккордеона. В&nbsp;финальной версии здесь будет описана роль практик в&nbsp;общей программе сопровождения.\n\nТекст не&nbsp;является рекламным обещанием и&nbsp;не&nbsp;заменяет индивидуальную консультацию. Абзац добавлен для проверки высоты раскрытой панели.",
			'expanded'  => false,
			'multiline' => true,
		),
		array(
			'question'  => 'Какие методы профилактики зависимости используются?',
			'answer'    => "Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ о&nbsp;подходах профилактики в&nbsp;обобщённой форме.\n\nФормулировки носят технический характер и&nbsp;не&nbsp;содержат конкретных методик или гарантий. Используются только для проверки интерфейса.",
			'expanded'  => false,
			'multiline' => true,
		),
		array(
			'question'  => 'Не&nbsp;могу полностью исключить работу. Можно&nbsp;ли совместить процесс реабилитации с&nbsp;работой?',
			'answer'    => "Это временный технический текст для проверки аккордеона. В&nbsp;финальной версии здесь будет описан порядок согласования рабочего графика в&nbsp;общих чертах.\n\nТекст не&nbsp;содержит обещаний по&nbsp;срокам и&nbsp;условиям. Добавлен для проверки многоабзацного ответа и&nbsp;корректной работы клавиатурного управления.",
			'expanded'  => false,
			'multiline' => true,
		),
		array(
			'question'  => 'Как понять, что близкий человек стал наркоманом?',
			'answer'    => "Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ для родственников с&nbsp;нейтральными рекомендациями по&nbsp;наблюдению.\n\nМатериал не&nbsp;содержит диагностических утверждений и&nbsp;не&nbsp;заменяет очную консультацию. Используется только для проверки вёрстки и&nbsp;поведения аккордеона.",
			'expanded'  => false,
			'multiline' => true,
		),
	);
}

/**
 * Normalize FAQ rows from ACF or fallback shape.
 *
 * @param array<int, array<string, mixed>> $rows Raw rows.
 * @return array<int, array{question:string,answer:string,expanded:bool,multiline:bool}>
 */
function shpigovsky_home_normalize_faq_rows( $rows ) {
	$normalized = array();

	foreach ( $rows as $index => $row ) {
		if ( ! is_array( $row ) ) {
			continue;
		}

		$question = isset( $row['question'] ) ? trim( (string) $row['question'] ) : '';
		$answer   = isset( $row['answer'] ) ? trim( (string) $row['answer'] ) : '';

		if ( '' === $question && '' === $answer ) {
			continue;
		}

		$normalized[] = array(
			'question'  => $question,
			'answer'    => $answer,
			'expanded'  => 0 === $index,
			'multiline' => str_contains( $answer, "\n" ),
		);
	}

	return $normalized;
}

/**
 * Gallery static fallback slides.
 *
 * @return array<int, array{title:string,image_path:string,width:int,height:int}>
 */
function shpigovsky_home_gallery_fallback_items() {
	return array(
		array(
			'title'      => 'Лечение зависимости от&nbsp;алкоголя',
			'image_path' => 'img/content/gallery/shpigovsky-gallery-01.webp',
			'width'      => 621,
			'height'     => 938,
			'lazy'       => false,
		),
		array(
			'title'      => 'Лудомания лечение зависимости',
			'image_path' => 'img/content/gallery/shpigovsky-gallery-02.webp',
			'width'      => 1113,
			'height'     => 738,
			'lazy'       => true,
		),
		array(
			'title'      => 'Лечение подростковой зависимости',
			'image_path' => 'img/content/gallery/shpigovsky-gallery-03.webp',
			'width'      => 1171,
			'height'     => 864,
			'lazy'       => true,
		),
		array(
			'title'      => 'Зависимость от&nbsp;постоянных покупок',
			'image_path' => 'img/content/gallery/shpigovsky-gallery-04.webp',
			'width'      => 1296,
			'height'     => 921,
			'lazy'       => true,
		),
	);
}

/**
 * Resolve gallery slide image URL from ACF row or static fallback item.
 *
 * @param array<string, mixed> $row          ACF row.
 * @param array<string, mixed> $fallback_row Static fallback row.
 * @return array{url:string,width:int,height:int}
 */
function shpigovsky_home_gallery_slide_image( $row, $fallback_row ) {
	$media    = isset( $row['media'] ) ? $row['media'] : null;
	$img_url  = shpigovsky_acf_image_url( $media );
	$width    = isset( $fallback_row['width'] ) ? (int) $fallback_row['width'] : 0;
	$height   = isset( $fallback_row['height'] ) ? (int) $fallback_row['height'] : 0;

	if ( '' !== $img_url ) {
		if ( is_array( $media ) ) {
			if ( ! empty( $media['width'] ) ) {
				$width = (int) $media['width'];
			}
			if ( ! empty( $media['height'] ) ) {
				$height = (int) $media['height'];
			}
		}

		return array(
			'url'    => $img_url,
			'width'  => $width,
			'height' => $height,
		);
	}

	$path = isset( $fallback_row['image_path'] ) ? (string) $fallback_row['image_path'] : '';

	return array(
		'url'    => '' !== $path ? shpigovsky_asset_uri( $path ) : '',
		'width'  => $width,
		'height' => $height,
	);
}

/**
 * Feature grid static fallback cards (home_advantages).
 *
 * @return array<int, array{title:string,text:string}>
 */
function shpigovsky_home_advantages_fallback_items() {
	return array(
		array(
			'title' => 'до 15 резидентов',
			'text'  => 'В&nbsp;нашем Доме ценится личное пространство каждого. Такой формат позволяет проявлять заботу о&nbsp;каждом, уделять максимум терапевтического внимания.',
		),
		array(
			'title' => 'нет решеток и&nbsp;замков',
			'text'  => 'В&nbsp;нашем Доме нет запертых дверей и&nbsp;решеток на&nbsp;окнах. Мы не&nbsp;закрываем, не&nbsp;удерживаем насильно&nbsp;— мы успешно работаем с&nbsp;мотивацией.',
		),
		array(
			'title' => 'дипломированные специалисты',
			'text'  => 'Все групповые мероприятия ведут дипломированные специалисты&nbsp;— психологи.',
		),
		array(
			'title' => 'Бассейн и&nbsp;сауна',
			'text'  => 'Для формирования новых полезных привычек и&nbsp;желаний. Находятся на&nbsp;цокольном этаже, доступ к&nbsp;ним открыт всегда.',
		),
		array(
			'title' => 'Тренажерный комплекс',
			'text'  => 'Для поддержания физической формы и&nbsp;получения удовольствия от&nbsp;спортивных нагрузок.',
		),
		array(
			'title' => 'Выбор категории номера',
			'text'  => 'У&nbsp;нас созданы прекрасные условия для комфортного преодоления зависимости и&nbsp;возможности изменить свою жизнь к&nbsp;лучшему.',
		),
	);
}

/**
 * Recovery intro card-grid static fallback (home_intro_bands).
 *
 * @return array<int, array{title:string,text:string}>
 */
function shpigovsky_home_intro_bands_fallback_items() {
	return array(
		array(
			'title' => 'Мультидисциплинарный подход',
			'text'  => 'Восстановление требует комплексного взгляда на&nbsp;проблему. С&nbsp;каждым клиентом работает команда специалистов: аддиктолог, психотера-певт, психолог, консультанты по&nbsp;химической зависимости и&nbsp;специалисты по&nbsp;работе с&nbsp;семьёй.',
		),
		array(
			'title' => 'Персонализированная программа',
			'text'  => 'Мы&nbsp;не&nbsp;используем универсальные схемы лечения. Программа строится с&nbsp;учётом жизненной истории человека, его психологических особенностей, семейной ситуации, состояния здоровья и&nbsp;поставленных целей. Это позволяет сделать процесс устойчивым в&nbsp;долгосрочной перспективе.',
		),
		array(
			'title' => 'Выявление и устранение причины зависимости',
			'text'  => 'Зависимость редко бывает основной проблемой&nbsp;&mdash; чаще она становится способом справляться со&nbsp;стрессом, внутренней болью или жизненными трудностями. Поэтому мы&nbsp;работаем не&nbsp;только с&nbsp;симптомами, но&nbsp;и&nbsp;помогаем понять причины сформировавшегося поведения.',
		),
		array(
			'title' => 'Семья как часть выздоровления',
			'text'  => 'Зависимость затрагивает не&nbsp;только самого человека, но&nbsp;и&nbsp;его близких. Мы&nbsp;вовлекаем семью в&nbsp;процесс восстановления через консультации, семейные сессии и&nbsp;совместную работу со&nbsp;специалистами. Это помогает восстановить доверие, улучшить взаимопонимание и&nbsp;создать поддерживающую среду.',
		),
		array(
			'title' => 'Реабилитаация без потери связи с&nbsp;жизнью',
			'text'  => 'Мы&nbsp;понимаем, насколько важно для многих людей сохранять связь с&nbsp;семьёй, работой и&nbsp;привычной жизнью. В&nbsp;зависимости от&nbsp;этапа программы и&nbsp;индивидуальных задач возможно использование гаджетов, решение рабочих вопросов и&nbsp;участие в&nbsp;значимых семейных событиях.',
		),
		array(
			'title' => 'Долгосрочное сопровождение после',
			'text'  => 'Завершение программы&nbsp;&mdash; это не&nbsp;конец работы, а&nbsp;начало нового этапа жизни. После прохождения реабилитации мы&nbsp;продолжаем сопровождать выпускников, помогая справляться с&nbsp;возникающими трудностями, сохранять мотивацию и&nbsp;укреплять навыки трезвой жизни.',
		),
	);
}

/**
 * Recovery intro benefits list static fallback.
 *
 * @return string[]
 */
function shpigovsky_home_recovery_intro_benefits_fallback() {
	$rows = shpigovsky_home_recovery_intro_benefits_fallback_rows();
	$out  = array();

	foreach ( $rows as $row ) {
		$text = isset( $row['text'] ) ? trim( (string) $row['text'] ) : '';
		if ( '' !== $text ) {
			$out[] = $text;
		}
	}

	return $out;
}

/**
 * Recovery intro benefits as repeater-shaped rows (V9-06E40).
 *
 * @return array<int, array{text:string,item_enabled:int}>
 */
function shpigovsky_home_recovery_intro_benefits_fallback_rows() {
	return array(
		array( 'text' => 'Мультидисциплинарный подход и&nbsp;команда специалистов;', 'item_enabled' => 1 ),
		array( 'text' => 'Персонализированная программа восстановления;', 'item_enabled' => 1 ),
		array( 'text' => 'Работа с&nbsp;причинами зависимости, а&nbsp;не&nbsp;только с&nbsp;её&nbsp;проявлениями;', 'item_enabled' => 1 ),
		array( 'text' => 'Вовлечение семьи и&nbsp;близких в&nbsp;процессвыздоровления;', 'item_enabled' => 1 ),
		array( 'text' => 'Реабилитация без потери связи с&nbsp;жизнью;', 'item_enabled' => 1 ),
		array( 'text' => 'Постлечебное сопровождение и&nbsp;поддержка ремиссии.', 'item_enabled' => 1 ),
	);
}

/**
 * Why-us body paragraphs fallback.
 *
 * @return array<int, array{text:string,item_enabled:int}>
 */
function shpigovsky_home_why_us_body_fallback_rows() {
	return array(
		array(
			'text'         => 'Лечение в&nbsp;нашем реабилитационном центре совмещает современный и&nbsp;мультидисциплинарный подход направленный на&nbsp;устранение истинных причин зависимости.',
			'item_enabled' => 1,
		),
		array(
			'text'         => 'Мультидисциплинарный подход&nbsp;— это когда лечение одного пациента обеспечивается командой специалистов разных профилей. Такой подход становится залогом понимания и&nbsp;решения проблемы.',
			'item_enabled' => 1,
		),
	);
}

/**
 * Why-us link items fallback.
 *
 * @return array<int, array{title:string,url:string,item_enabled:int}>
 */
function shpigovsky_home_why_us_items_fallback_rows() {
	return array(
		array(
			'title'        => 'Диагностические инструменты',
			'url'          => home_url( '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/' ),
			'item_enabled' => 1,
		),
		array(
			'title'        => 'Психиатрия',
			'url'          => home_url( '/uslugi/zavisimosti/' ),
			'item_enabled' => 1,
		),
		array(
			'title'        => 'Функциональная терапия',
			'url'          => home_url( '/uslugi/zavisimosti/' ),
			'item_enabled' => 1,
		),
		array(
			'title'        => 'Комплементарная терапия',
			'url'          => home_url( '/uslugi/zavisimosti/' ),
			'item_enabled' => 1,
		),
	);
}

/**
 * Recovery-life intro paragraphs fallback.
 *
 * @return array<int, array{text:string,item_enabled:int}>
 */
function shpigovsky_home_recovery_life_intro_fallback_rows() {
	return shpigovsky_home_why_us_body_fallback_rows();
}

/**
 * Recovery-life stages fallback.
 *
 * @return array<int, array{stage_label:string,title:string,items_text:string,item_enabled:int}>
 */
function shpigovsky_home_recovery_life_stages_fallback_rows() {
	return array(
		array(
			'stage_label'  => '1 месяц',
			'title'        => 'От выживания к&nbsp;стабильности',
			'items_text'   => "уменьшается внутреннее напряжение;\nнормализуется сон;\nснижается выраженность тяги;\nпоявляется чувство безопасности;\nвозникает готовность принимать помощь.",
			'item_enabled' => 1,
		),
		array(
			'stage_label'  => '2 месяц',
			'title'        => 'От зависимости к&nbsp;пониманию себя',
			'items_text'   => "человек начинает понимать причины своего состояния;\nпоявляются навыки управления эмоциями;\nснижается потребность убегать от&nbsp;переживаний через вещества или поведение;\nформируется внутренняя опора;\nвозвращается способность получать удовольствие от&nbsp;жизни.",
			'item_enabled' => 1,
		),
		array(
			'stage_label'  => '3 месяц',
			'title'        => 'От контроля к&nbsp;свободе',
			'items_text'   => "восстанавливаются отношения с&nbsp;близкими;\nпоявляются новые цели и&nbsp;интересы;\nповышается стрессоустойчивость;\nформируется уверенность в&nbsp;собственных силах;\nчеловек строит новую систему жизни;\nсохраняет устойчивую ремиссию;\nреализует личные и&nbsp;профессиональные цели;\nподдерживает эмоциональное благополучие;\nпродолжает развитие личности.",
			'item_enabled' => 1,
		),
	);
}

/**
 * Genotyping body paragraphs fallback.
 *
 * @return array<int, array{text:string,item_enabled:int}>
 */
function shpigovsky_home_genotyping_body_fallback_rows() {
	return array(
		array(
			'text'         => 'Анализ позволяет выявить особенности чувствительности рецепторов к&nbsp;ключевым нейромедиаторам: дофамину, эндогенным опиатам, серотонину и&nbsp;другим. В&nbsp;основе концепции Синдрома Дефицита Удовлетворенности именно гипофункция этих систем&nbsp;— в&nbsp;частности мезолимбического дофаминового пути&nbsp;— объясняет, почему одни люди более уязвимы к&nbsp;развитию зависимостей, а&nbsp;другие нет.',
			'item_enabled' => 1,
		),
		array(
			'text'         => 'Результат генотипирования становится основой для построения персонализированной программы: мы знаем, с&nbsp;чем именно работаем,&nbsp;— и&nbsp;это меняет всё.',
			'item_enabled' => 1,
		),
	);
}

/**
 * Genotyping list items fallback.
 *
 * @return array<int, array{text:string,item_enabled:int}>
 */
function shpigovsky_home_genotyping_items_fallback_rows() {
	return array(
		array( 'text' => 'Люди с&nbsp;алкогольной или наркотической зависимостью;', 'item_enabled' => 1 ),
		array( 'text' => 'Люди с&nbsp;нехимическими зависимостями (например, страдающие от&nbsp;переедания, игромании (лудомании), шопоголизма, интернет- или сексуальной зависимости);', 'item_enabled' => 1 ),
		array( 'text' => 'Профильные специалисты (врачи-психиатры, аддиктологи, психотерапевты, нутрициологи и&nbsp;др);', 'item_enabled' => 1 ),
		array( 'text' => 'Люди с&nbsp;компульсивным и&nbsp;дивиантны поведением.', 'item_enabled' => 1 ),
	);
}

/**
 * Home videos fallback (theme assets when Media Library empty).
 *
 * @return array<int, array{title:string,video_url:string,poster_url:string,item_enabled:int,width:int,height:int}>
 */
function shpigovsky_home_videos_fallback_rows() {
	return array(
		array(
			'title'         => 'Интервью с&nbsp;Сергеем Шпиговским',
			'video_url'     => shpigovsky_asset_uri( 'video/sergey-shpigovsky-interview.mp4' ),
			'poster_url'    => shpigovsky_asset_uri( 'img/content/videos/sergey-shpigovsky-interview-poster.webp' ),
			'item_enabled'  => 1,
			'width'         => 1280,
			'height'        => 720,
		),
		array(
			'title'         => 'Центр профилактики зависимостей Сергея Шпиговского',
			'video_url'     => shpigovsky_asset_uri( 'video/shpigovsky-center.mp4' ),
			'poster_url'    => shpigovsky_asset_uri( 'img/content/videos/shpigovsky-center-poster.webp' ),
			'item_enabled'  => 1,
			'width'         => 1920,
			'height'        => 1080,
		),
	);
}

/**
 * Split FAQ answer into paragraphs for multiline rendering.
 *
 * @param string $answer Answer text.
 * @return string[]
 */
function shpigovsky_home_faq_answer_paragraphs( $answer ) {
	$parts = preg_split( "/\n\s*\n/", trim( (string) $answer ) );

	if ( ! is_array( $parts ) ) {
		return array( trim( (string) $answer ) );
	}

	return array_values(
		array_filter(
			array_map(
				static function ( $part ) {
					return trim( (string) $part );
				},
				$parts
			)
		)
	);
}
