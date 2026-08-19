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

	$resolved = '' !== $value ? $value : $fallback;

	if ( is_string( $resolved ) && ( false !== strpos( $field_name, '_url' ) || 0 === strpos( $resolved, 'http' ) ) ) {
		$resolved = shpigovsky_normalize_public_url( $resolved );
	}

	return $resolved;
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
			'question'  => 'Как перестать именно хотеть выпить, а не заставлять себя этого не делать?',
			'answer'    => 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation .Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation .',
			'expanded'  => true,
			'multiline' => false,
		),
		array(
			'question'  => 'Анонимное лечение или нет?',
			'answer'    => "Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ о формате обращения и порядке первичного контакта с центром.\n\nТекст не является маркетинговым обещанием и не заменяет консультацию специалиста. Финальная редакция будет согласована оператором отдельно.",
			'expanded'  => false,
			'multiline' => true,
		),
		array(
			'question'  => 'Как долго длится реабилитация?',
			'answer'    => "Это временный технический текст для проверки высоты аккордеона. В финальной версии здесь будет описан типовой порядок этапов сопровождения без указания конкретных сроков.\n\nДлительность программы зависит от индивидуального запроса и согласуется на консультации. Данный абзац добавлен только для вёрсточной проверки.",
			'expanded'  => false,
			'multiline' => true,
		),
		array(
			'question'  => 'Как уговорить близкого пройти лечение от зависимости?',
			'answer'    => "Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ о том, как семье подготовиться к разговору с близким человеком.\n\nМатериал носит справочный характер и не содержит обещаний результата. Окончательная формулировка будет подготовлена в рамках контентного этапа.",
			'expanded'  => false,
			'multiline' => true,
		),
		array(
			'question'  => 'Можно ли самостоятельно перестать употреблять наркотики?',
			'answer'    => "Это временный технический текст для проверки аккордеона. В финальной версии здесь будет нейтральное описание сценариев, когда самостоятельные попытки требуют дополнительной поддержки.\n\nТекст не содержит медицинских утверждений и не описывает гарантированный исход. Используется только для проверки поведения интерфейса на разных экранах.",
			'expanded'  => false,
			'multiline' => true,
		),
		array(
			'question'  => 'Как понять, что у меня есть проблемы с алкоголем?',
			'answer'    => "Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ с ориентирами для самонаблюдения без диагностических формулировок.\n\nМатериал предназначен для проверки типографики и вертикальных отступов. Контент будет заменён после согласования с оператором.",
			'expanded'  => false,
			'multiline' => true,
		),
		array(
			'question'  => 'Зачем в программу включены занятия йогой?',
			'answer'    => "Это временный технический текст для проверки аккордеона. В финальной версии здесь будет описана роль практик в общей программе сопровождения.\n\nТекст не является рекламным обещанием и не заменяет индивидуальную консультацию. Абзац добавлен для проверки высоты раскрытой панели.",
			'expanded'  => false,
			'multiline' => true,
		),
		array(
			'question'  => 'Какие методы профилактики зависимости используются?',
			'answer'    => "Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ о подходах профилактики в обобщённой форме.\n\nФормулировки носят технический характер и не содержат конкретных методик или гарантий. Используются только для проверки интерфейса.",
			'expanded'  => false,
			'multiline' => true,
		),
		array(
			'question'  => 'Не могу полностью исключить работу. Можно ли совместить процесс реабилитации с работой?',
			'answer'    => "Это временный технический текст для проверки аккордеона. В финальной версии здесь будет описан порядок согласования рабочего графика в общих чертах.\n\nТекст не содержит обещаний по срокам и условиям. Добавлен для проверки многоабзацного ответа и корректной работы клавиатурного управления.",
			'expanded'  => false,
			'multiline' => true,
		),
		array(
			'question'  => 'Как понять, что близкий человек стал наркоманом?',
			'answer'    => "Это временный технический текст для проверки блока FAQ. Здесь будет размещён финальный ответ для родственников с нейтральными рекомендациями по наблюдению.\n\nМатериал не содержит диагностических утверждений и не заменяет очную консультацию. Используется только для проверки вёрстки и поведения аккордеона.",
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
			'title'      => 'Лечение зависимости от алкоголя',
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
			'title'      => 'Зависимость от постоянных покупок',
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
			'title' => 'до 15 резидентов',
			'text'  => 'В нашем Доме ценится личное пространство каждого. Такой формат позволяет проявлять заботу о каждом, уделять максимум терапевтического внимания.',
		),
		array(
			'title' => 'нет решеток и замков',
			'text'  => 'В нашем Доме нет запертых дверей и решеток на окнах. Мы не закрываем, не удерживаем насильно — мы успешно работаем с мотивацией.',
		),
		array(
			'title' => 'дипломированные специалисты',
			'text'  => 'Все групповые мероприятия ведут дипломированные специалисты — психологи.',
		),
		array(
			'title' => 'Бассейн и сауна',
			'text'  => 'Для формирования новых полезных привычек и желаний. Находятся на цокольном этаже, доступ к ним открыт всегда.',
		),
		array(
			'title' => 'Тренажерный комплекс',
			'text'  => 'Для поддержания физической формы и получения удовольствия от спортивных нагрузок.',
		),
		array(
			'title' => 'Выбор категории номера',
			'text'  => 'У нас созданы прекрасные условия для комфортного преодоления зависимости и возможности изменить свою жизнь к лучшему.',
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
			'text'  => 'Восстановление требует комплексного взгляда на проблему. С каждым клиентом работает команда специалистов: аддиктолог, психотера-певт, психолог, консультанты по химической зависимости и специалисты по работе с семьёй.',
		),
		array(
			'title' => 'Персонализированная программа',
			'text'  => 'Мы не используем универсальные схемы лечения. Программа строится с учётом жизненной истории человека, его психологических особенностей, семейной ситуации, состояния здоровья и поставленных целей. Это позволяет сделать процесс устойчивым в долгосрочной перспективе.',
		),
		array(
			'title' => 'Выявление и устранение причины зависимости',
			'text'  => 'Зависимость редко бывает основной проблемой — чаще она становится способом справляться со стрессом, внутренней болью или жизненными трудностями. Поэтому мы работаем не только с симптомами, но и помогаем понять причины сформировавшегося поведения.',
		),
		array(
			'title' => 'Семья как часть выздоровления',
			'text'  => 'Зависимость затрагивает не только самого человека, но и его близких. Мы вовлекаем семью в процесс восстановления через консультации, семейные сессии и совместную работу со специалистами. Это помогает восстановить доверие, улучшить взаимопонимание и создать поддерживающую среду.',
		),
		array(
			'title' => 'Реабилитаация без потери связи с жизнью',
			'text'  => 'Мы понимаем, насколько важно для многих людей сохранять связь с семьёй, работой и привычной жизнью. В зависимости от этапа программы и индивидуальных задач возможно использование гаджетов, решение рабочих вопросов и участие в значимых семейных событиях.',
		),
		array(
			'title' => 'Долгосрочное сопровождение после',
			'text'  => 'Завершение программы — это не конец работы, а начало нового этапа жизни. После прохождения реабилитации мы продолжаем сопровождать выпускников, помогая справляться с возникающими трудностями, сохранять мотивацию и укреплять навыки трезвой жизни.',
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
		array( 'text' => 'Мультидисциплинарный подход и команда специалистов;', 'item_enabled' => 1 ),
		array( 'text' => 'Персонализированная программа восстановления;', 'item_enabled' => 1 ),
		array( 'text' => 'Работа с причинами зависимости, а не только с её проявлениями;', 'item_enabled' => 1 ),
		array( 'text' => 'Вовлечение семьи и близких в процессвыздоровления;', 'item_enabled' => 1 ),
		array( 'text' => 'Реабилитация без потери связи с жизнью;', 'item_enabled' => 1 ),
		array( 'text' => 'Постлечебное сопровождение и поддержка ремиссии.', 'item_enabled' => 1 ),
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
			'text'         => 'Лечение в нашем реабилитационном центре совмещает современный и мультидисциплинарный подход направленный на устранение истинных причин зависимости.',
			'item_enabled' => 1,
		),
		array(
			'text'         => 'Мультидисциплинарный подход — это когда лечение одного пациента обеспечивается командой специалистов разных профилей. Такой подход становится залогом понимания и решения проблемы.',
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
			'title'        => 'От выживания к стабильности',
			'items_text'   => "уменьшается внутреннее напряжение;\nнормализуется сон;\nснижается выраженность тяги;\nпоявляется чувство безопасности;\nвозникает готовность принимать помощь.",
			'item_enabled' => 1,
		),
		array(
			'stage_label'  => '2 месяц',
			'title'        => 'От зависимости к пониманию себя',
			'items_text'   => "человек начинает понимать причины своего состояния;\nпоявляются навыки управления эмоциями;\nснижается потребность убегать от переживаний через вещества или поведение;\nформируется внутренняя опора;\nвозвращается способность получать удовольствие от жизни.",
			'item_enabled' => 1,
		),
		array(
			'stage_label'  => '3 месяц',
			'title'        => 'От контроля к свободе',
			'items_text'   => "восстанавливаются отношения с близкими;\nпоявляются новые цели и интересы;\nповышается стрессоустойчивость;\nформируется уверенность в собственных силах;\nчеловек строит новую систему жизни;\nсохраняет устойчивую ремиссию;\nреализует личные и профессиональные цели;\nподдерживает эмоциональное благополучие;\nпродолжает развитие личности.",
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
			'text'         => 'Анализ позволяет выявить особенности чувствительности рецепторов к ключевым нейромедиаторам: дофамину, эндогенным опиатам, серотонину и другим. В основе концепции Синдрома Дефицита Удовлетворенности именно гипофункция этих систем — в частности мезолимбического дофаминового пути — объясняет, почему одни люди более уязвимы к развитию зависимостей, а другие нет.',
			'item_enabled' => 1,
		),
		array(
			'text'         => 'Результат генотипирования становится основой для построения персонализированной программы: мы знаем, с чем именно работаем, — и это меняет всё.',
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
		array( 'text' => 'Люди с алкогольной или наркотической зависимостью;', 'item_enabled' => 1 ),
		array( 'text' => 'Люди с нехимическими зависимостями (например, страдающие от переедания, игромании (лудомании), шопоголизма, интернет- или сексуальной зависимости);', 'item_enabled' => 1 ),
		array( 'text' => 'Профильные специалисты (врачи-психиатры, аддиктологи, психотерапевты, нутрициологи и др);', 'item_enabled' => 1 ),
		array( 'text' => 'Люди с компульсивным и дивиантны поведением.', 'item_enabled' => 1 ),
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
			'title'         => 'Интервью с Сергеем Шпиговским',
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
