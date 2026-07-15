<?php
/**
 * Program direction map — shared Home / services / about program blocks.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Canonical program direction page paths under /o-centre/programma-lecheniya/.
 *
 * @return array<int, array{slug:string,title:string,marker:string,image:string,width:int,height:int,alt:string,text:string}>
 */
function shpigovsky_get_program_direction_definitions() {
	return array(
		array(
			'slug'   => 'genotipirovanie',
			'title'  => 'Генотипирование',
			'marker' => '01',
			'image'  => 'img/content/rehabilitation-program/program-genotyping.webp',
			'width'  => 1216,
			'height' => 1632,
			'alt'    => 'Генотипирование',
			'text'   => 'Выявление причин эндогенной природы зависимости служит дополнительным инструментом в&nbsp;индивидуальной схеме лечения и&nbsp;реабилитации. В&nbsp;основе большинства зависимостей лежит нарушение работы системы вознаграждения мозга&nbsp;— в&nbsp;частности, гипофункция мезолимбической дофаминовой системы. Это не&nbsp;слабость характера. Это биология, с&nbsp;которой можно и&nbsp;нужно работать.',
		),
		array(
			'slug'   => 'neyropsihologicheskaya-korrektsiya',
			'title'  => 'Нейропсихологическая коррекция',
			'marker' => '02',
			'image'  => 'img/content/rehabilitation-program/program-neuropsychology.webp',
			'width'  => 1632,
			'height' => 1216,
			'alt'    => 'Нейропсихологическая коррекция',
			'text'   => 'БОС-терапия (биологическая обратная связь) проводится с&nbsp;использованием специального оборудования. На&nbsp;этом этапе лечения и&nbsp;реабилитации происходит обучение сознательно контролировать функции своего тела (пульс, дыхание, напряжение мышц, артериальное давление). Специальные датчики оборудования выполняют функцию «физиологического зеркала».',
		),
		array(
			'slug'   => 'psihokorrektsiya',
			'title'  => 'Психокоррекция',
			'marker' => '03',
			'image'  => 'img/content/rehabilitation-program/program-psychocorrection.webp',
			'width'  => 880,
			'height' => 1184,
			'alt'    => 'Психокоррекция',
			'text'   => 'Зависимость редко бывает просто привычкой. За&nbsp;ней почти всегда стоит что-то глубже: тревога, которую не&nbsp;удаётся унять, боль, которую проще приглушить, чем прожить, или пустота там, где должно быть что-то важное. Психокоррекция формирует внутреннюю опору и&nbsp;новую стратегию совладания со&nbsp;стрессом.',
		),
		array(
			'slug'   => 'kinezioterapiya',
			'title'  => 'Кинезиотерапия',
			'marker' => '04',
			'image'  => 'img/content/rehabilitation-program/program-kinesiotherapy.webp',
			'width'  => 880,
			'height' => 1184,
			'alt'    => 'Кинезиотерапия',
			'text'   => 'Движение меняет химию мозга. Это не&nbsp;вдохновляющая цитата&nbsp;— это факт, подтверждённый десятилетиями исследований в&nbsp;области нейробиологии и&nbsp;аддиктологии. Физическая нагрузка стимулирует выработку эндорфинов (создающих ощущение благополучия), дофамина (системы вознаграждения) и&nbsp;серотонина (регулирующего настроение, аппетит и&nbsp;сон). Именно эти нейромедиаторы зависимость «научила» организм получать извне&nbsp;— мы помогаем восстановить их естественную выработку.',
		),
	);
}

/**
 * Resolve permalink for a program direction page under programma-lecheniya.
 *
 * @param string $slug Child page slug.
 * @return string Absolute URL (falls back to expected path when page missing).
 */
function shpigovsky_get_program_direction_url( $slug ) {
	$slug = sanitize_title( (string) $slug );
	$path = 'o-centre/programma-lecheniya/' . $slug;
	$page = get_page_by_path( $path );

	if ( $page instanceof WP_Post ) {
		$url = get_permalink( $page );
		if ( is_string( $url ) && '' !== $url ) {
			return $url;
		}
	}

	return home_url( '/' . $path . '/' );
}

/**
 * Program direction items with resolved URLs and asset URIs.
 *
 * @param string $variant home|service|about — controls whether body text is included.
 * @return array<int, array{slug:string,title:string,marker:string,title_display:string,url:string,image:string,width:int,height:int,alt:string,text:string}>
 */
function shpigovsky_get_program_direction_items( $variant = 'service' ) {
	$items = array();

	foreach ( shpigovsky_get_program_direction_definitions() as $def ) {
		$title_display = $def['marker'] . ' — ' . $def['title'];
		$item          = array(
			'slug'          => $def['slug'],
			'title'         => $def['title'],
			'marker'        => $def['marker'],
			'title_display' => $title_display,
			'url'           => shpigovsky_get_program_direction_url( $def['slug'] ),
			'image'         => shpigovsky_asset_uri( $def['image'] ),
			'width'         => (int) $def['width'],
			'height'        => (int) $def['height'],
			'alt'           => $def['alt'],
			'text'          => '',
		);

		if ( 'home' === $variant ) {
			$item['text'] = $def['text'];
		}

		$items[] = $item;
	}

	return $items;
}
