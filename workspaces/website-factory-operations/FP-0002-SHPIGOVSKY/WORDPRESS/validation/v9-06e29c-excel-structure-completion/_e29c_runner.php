<?php
/**
 * FP-0002 V9-06E29C — Excel structure completion mutation runner.
 * TEMPORARY HELPER — validation evidence only.
 *
 * Modes: backup-only | apply | validate | all
 */
define( 'WP_USE_THEMES', false );

$root         = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky';
$evidence_dir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/v9-06e29c-excel-structure-completion';
$v9_favicon   = 'X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/src/favicon';
$theme_fav    = $root . '/wp-content/themes/shpigovsky/assets/favicon';
$mode         = isset( $argv[1] ) ? $argv[1] : 'all';

require $root . '/wp-load.php';

if ( ! is_dir( $evidence_dir ) ) {
	mkdir( $evidence_dir, 0777, true );
}

const FP02_E29C_PLACEHOLDER = 'Раздел находится в подготовке. Здесь будет опубликована информация по теме страницы.';
const FP02_E29C_GENERIC_TPL = 'page-templates/generic.php';

function fp02e29c_json_write( $name, $data ) {
	global $evidence_dir;
	$path = trailingslashit( $evidence_dir ) . $name;
	file_put_contents( $path, wp_json_encode( $data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) . "\n" );
	return $path;
}

function fp02e29c_placeholder_block() {
	return '<!-- wp:paragraph --><p>' . esc_html( FP02_E29C_PLACEHOLDER ) . '</p><!-- /wp:paragraph -->';
}

/**
 * @return array<int, array<string, mixed>>
 */
function fp02e29c_excel_routes() {
	return array(
		array( 'row' => 2, 'path' => '/', 'type' => 'home', 'wp' => 'page', 'title' => 'Главная' ),
		array( 'row' => 3, 'path' => '/uslugi/', 'type' => 'services_index', 'wp' => 'page', 'title' => 'Услуги' ),
		array( 'row' => 4, 'path' => '/uslugi/zavisimosti/', 'type' => 'service_category', 'wp' => 'service', 'title' => 'Зависимости и пристрастия', 'slug' => 'zavisimosti' ),
		array( 'row' => 5, 'path' => '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', 'type' => 'service_page', 'wp' => 'service', 'title' => 'Лечение алкогольной зависимости', 'slug' => 'lechenie-alkogolnoy-zavisimosti', 'parent_slug' => 'zavisimosti' ),
		array( 'row' => 6, 'path' => '/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/', 'type' => 'service_category', 'wp' => 'service', 'title' => 'Лечение наркотической зависимости', 'slug' => 'lechenie-narkoticheskoy-zavisimosti', 'parent_slug' => 'zavisimosti', 'rename_from' => 'narkoticheskaya-zavisimost' ),
		array( 'row' => 7, 'path' => '/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/soli/', 'type' => 'deep_service_page', 'wp' => 'service', 'title' => 'Лечение солевой зависимости', 'slug' => 'soli', 'parent_slug' => 'lechenie-narkoticheskoy-zavisimosti' ),
		array( 'row' => 8, 'path' => '/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/matadon/', 'type' => 'deep_service_page', 'wp' => 'service', 'title' => 'Лечение метадоновой зависимости', 'slug' => 'matadon', 'parent_slug' => 'lechenie-narkoticheskoy-zavisimosti' ),
		array( 'row' => 9, 'path' => '/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/geroin/', 'type' => 'deep_service_page', 'wp' => 'service', 'title' => 'Лечение героиновой зависимости', 'slug' => 'geroin', 'parent_slug' => 'lechenie-narkoticheskoy-zavisimosti' ),
		array( 'row' => 10, 'path' => '/uslugi/zavisimosti/lechenie-narkoticheskoy-zavisimosti/lekarstva/', 'type' => 'deep_service_page', 'wp' => 'service', 'title' => 'Лечение лекарственной зависимости', 'slug' => 'lekarstva', 'parent_slug' => 'lechenie-narkoticheskoy-zavisimosti', 'rename_from' => 'lekarstvennaya-zavisimost' ),
		array( 'row' => 11, 'path' => '/uslugi/zavisimosti/lechenie-povedencheskoy-zavisimosti/', 'type' => 'service_category', 'wp' => 'service', 'title' => 'Поведенческие зависимости', 'slug' => 'lechenie-povedencheskoy-zavisimosti', 'parent_slug' => 'zavisimosti', 'rename_from' => 'povedencheskie-zavisimosti' ),
		array( 'row' => 12, 'path' => '/uslugi/zavisimosti/lechenie-povedencheskoy-zavisimosti/ludomaniya/', 'type' => 'deep_service_page', 'wp' => 'service', 'title' => 'Лечение игровой зависимости', 'slug' => 'ludomaniya', 'parent_slug' => 'lechenie-povedencheskoy-zavisimosti' ),
		array( 'row' => 13, 'path' => '/uslugi/zavisimosti/lechenie-povedencheskoy-zavisimosti/internet-zavisimost/', 'type' => 'deep_service_page', 'wp' => 'service', 'title' => 'Интернет-зависимость', 'slug' => 'internet-zavisimost', 'parent_slug' => 'lechenie-povedencheskoy-zavisimosti' ),
		array( 'row' => 14, 'path' => '/uslugi/zavisimosti/lechenie-povedencheskoy-zavisimosti/sozavisimost/', 'type' => 'deep_service_page', 'wp' => 'service', 'title' => 'Лечение созависимости', 'slug' => 'sozavisimost', 'parent_slug' => 'lechenie-povedencheskoy-zavisimosti' ),
		array( 'row' => 15, 'path' => '/uslugi/zavisimosti/lechenie-povedencheskoy-zavisimosti/shopogolizm/', 'type' => 'deep_service_page', 'wp' => 'service', 'title' => 'Зависимость от постоянных покупок', 'slug' => 'shopogolizm', 'parent_slug' => 'lechenie-povedencheskoy-zavisimosti' ),
		array( 'row' => 18, 'path' => '/uslugi/psihicheskoe-zdorovie/', 'type' => 'service_category', 'wp' => 'service', 'title' => 'Психическое здоровье', 'slug' => 'psihicheskoe-zdorovie' ),
		array( 'row' => 19, 'path' => '/uslugi/psihicheskoe-zdorovie/depressiya/', 'type' => 'service_page', 'wp' => 'service', 'title' => 'Депрессия', 'slug' => 'depressiya', 'parent_slug' => 'psihicheskoe-zdorovie' ),
		array( 'row' => 20, 'path' => '/uslugi/psihicheskoe-zdorovie/ptsr/', 'type' => 'service_page', 'wp' => 'service', 'title' => 'ПТСР', 'slug' => 'ptsr', 'parent_slug' => 'psihicheskoe-zdorovie' ),
		array( 'row' => 21, 'path' => '/uslugi/psihicheskoe-zdorovie/emotsionalnoe-vygoranie/', 'type' => 'service_page', 'wp' => 'service', 'title' => 'Эмоциональное выгорание', 'slug' => 'emotsionalnoe-vygoranie', 'parent_slug' => 'psihicheskoe-zdorovie', 'rename_from' => 'emocionalnoe-vygoranie' ),
		array( 'row' => 22, 'path' => '/uslugi/psihicheskoe-zdorovie/trevozhnye-rasstroystva/', 'type' => 'service_page', 'wp' => 'service', 'title' => 'Тревожные расстройства', 'slug' => 'trevozhnye-rasstroystva', 'parent_slug' => 'psihicheskoe-zdorovie' ),
		array( 'row' => 23, 'path' => '/uslugi/psihicheskoe-zdorovie/rasstroystva-sna/', 'type' => 'service_page', 'wp' => 'service', 'title' => 'Расстройства сна', 'slug' => 'rasstroystva-sna', 'parent_slug' => 'psihicheskoe-zdorovie' ),
		array( 'row' => 24, 'path' => '/uslugi/psihicheskoe-zdorovie/travma/', 'type' => 'service_page', 'wp' => 'service', 'title' => 'Травма', 'slug' => 'travma', 'parent_slug' => 'psihicheskoe-zdorovie' ),
		array( 'row' => 28, 'path' => '/uslugi/rasstroystva-pischevogo-povedeniya/', 'type' => 'service_category', 'wp' => 'service', 'title' => 'Расстройства пищевого поведения', 'slug' => 'rasstroystva-pischevogo-povedeniya' ),
		array( 'row' => 29, 'path' => '/uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya/', 'type' => 'service_page', 'wp' => 'service', 'title' => 'Анорексия', 'slug' => 'anoreksiya', 'parent_slug' => 'rasstroystva-pischevogo-povedeniya' ),
		array( 'row' => 30, 'path' => '/uslugi/rasstroystva-pischevogo-povedeniya/buliniya/', 'type' => 'service_page', 'wp' => 'service', 'title' => 'Булимия', 'slug' => 'buliniya', 'parent_slug' => 'rasstroystva-pischevogo-povedeniya', 'rename_from' => 'nervnaya-bulimiya' ),
		array( 'row' => 31, 'path' => '/uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie/', 'type' => 'service_page', 'wp' => 'service', 'title' => 'Компульсивное переедание', 'slug' => 'kompulsivnoe-pereedanie', 'parent_slug' => 'rasstroystva-pischevogo-povedeniya' ),
		array( 'row' => 32, 'path' => '/uslugi/genotipirovanie/', 'type' => 'service_page', 'wp' => 'service', 'title' => 'Генотипирование', 'slug' => 'genotipirovanie' ),
		array( 'row' => 33, 'path' => '/specyalisty/', 'type' => 'specialists_index', 'wp' => 'page', 'title' => 'Специалисты', 'slug' => 'specyalisty', 'template' => FP02_E29C_GENERIC_TPL ),
		array( 'row' => 34, 'path' => '/specyalisty/shipovsky/', 'type' => 'specialist_page', 'wp' => 'page', 'title' => 'Сергей Шпиговский', 'slug' => 'shipovsky', 'parent_slug' => 'specyalisty', 'template' => FP02_E29C_GENERIC_TPL ),
		array( 'row' => 35, 'path' => '/specyalisty/kazakov/', 'type' => 'specialist_page', 'wp' => 'page', 'title' => 'Казаков', 'slug' => 'kazakov', 'parent_slug' => 'specyalisty', 'template' => FP02_E29C_GENERIC_TPL ),
		array( 'row' => 36, 'path' => '/specyalisty/kostyuk/', 'type' => 'specialist_page', 'wp' => 'page', 'title' => 'Костюк', 'slug' => 'kostyuk', 'parent_slug' => 'specyalisty', 'template' => FP02_E29C_GENERIC_TPL ),
		array( 'row' => 40, 'path' => '/o-centre/', 'type' => 'ocentre_hub', 'wp' => 'page', 'title' => 'О центре', 'slug' => 'o-centre' ),
		array( 'row' => 41, 'path' => '/o-centre/o-nas/', 'type' => 'ocentre_child_page', 'wp' => 'page', 'title' => 'О нас', 'slug' => 'o-nas', 'parent_slug' => 'o-centre', 'template' => FP02_E29C_GENERIC_TPL, 'page_id' => 12 ),
		array( 'row' => 42, 'path' => '/o-centre/programma-lecheniya/', 'type' => 'ocentre_child_page', 'wp' => 'page', 'title' => 'Программа лечения', 'slug' => 'programma-lecheniya', 'parent_slug' => 'o-centre', 'template' => FP02_E29C_GENERIC_TPL, 'page_id' => 13 ),
		array( 'row' => 43, 'path' => '/o-centre/galereya-o-dome/', 'type' => 'ocentre_child_page', 'wp' => 'page', 'title' => 'Галерея о доме', 'slug' => 'galereya-o-dome', 'parent_slug' => 'o-centre', 'template' => FP02_E29C_GENERIC_TPL, 'page_id' => 14 ),
		array( 'row' => 44, 'path' => '/o-centre/specialistam/', 'type' => 'ocentre_child_page', 'wp' => 'page', 'title' => 'Специалистам', 'slug' => 'specialistam', 'parent_slug' => 'o-centre', 'template' => FP02_E29C_GENERIC_TPL, 'page_id' => 15 ),
		array( 'row' => 45, 'path' => '/o-centre/rodstvennikam/', 'type' => 'ocentre_child_page', 'wp' => 'page', 'title' => 'Родственникам', 'slug' => 'rodstvennikam', 'parent_slug' => 'o-centre', 'template' => FP02_E29C_GENERIC_TPL, 'page_id' => 16 ),
		array( 'row' => 46, 'path' => '/o-centre/intervyu-i-smi/', 'type' => 'ocentre_child_page', 'wp' => 'page', 'title' => 'Интервью и СМИ', 'slug' => 'intervyu-i-smi', 'parent_slug' => 'o-centre', 'template' => FP02_E29C_GENERIC_TPL ),
		array( 'row' => 47, 'path' => '/otzyvy/', 'type' => 'reviews', 'wp' => 'page', 'title' => 'Отзывы', 'slug' => 'otzyvy' ),
		array( 'row' => 48, 'path' => '/blog/', 'type' => 'blog_index', 'wp' => 'page', 'title' => 'Блог', 'slug' => 'blog' ),
		array( 'row' => 49, 'path' => '/blog/nazvanie-stati/', 'type' => 'blog_single_demo', 'wp' => 'post', 'title' => 'Название статьи', 'slug' => 'nazvanie-stati' ),
		array( 'row' => 52, 'path' => '/kontakty/', 'type' => 'contacts', 'wp' => 'page', 'title' => 'Контакты', 'slug' => 'kontakty' ),
	);
}

function fp02e29c_get_post_by_slug( $slug, $post_type ) {
	$post = get_page_by_path( $slug, OBJECT, $post_type );
	return $post instanceof WP_Post ? $post : null;
}

function fp02e29c_get_service_by_slug( $slug ) {
	$posts = get_posts(
		array(
			'name'           => $slug,
			'post_type'      => 'service',
			'post_status'    => array( 'publish', 'draft', 'private', 'future' ),
			'posts_per_page' => 1,
			'fields'         => 'all',
		)
	);

	return ! empty( $posts ) ? $posts[0] : null;
}

function fp02e29c_set_page_template( $post_id, $template ) {
	update_post_meta( (int) $post_id, '_wp_page_template', $template );
}

function fp02e29c_ensure_page_content( $post_id, $force_placeholder = false ) {
	$post = get_post( $post_id );
	if ( ! $post instanceof WP_Post ) {
		return false;
	}
	$content = trim( (string) $post->post_content );
	if ( '' === $content || $force_placeholder ) {
		wp_update_post(
			array(
				'ID'           => $post_id,
				'post_content' => fp02e29c_placeholder_block(),
			)
		);
		return true;
	}
	return false;
}

function fp02e29c_ensure_service_intro( $post_id ) {
	if ( ! function_exists( 'get_field' ) || ! function_exists( 'update_field' ) ) {
		return false;
	}
	$intro = get_field( 'intro_text', $post_id );
	if ( is_string( $intro ) && '' !== trim( $intro ) ) {
		return false;
	}
	update_field( 'intro_text', FP02_E29C_PLACEHOLDER, $post_id );
	return true;
}

function fp02e29c_create_or_update_page( array $route, $parent_id = 0 ) {
	$slug     = $route['slug'];
	$existing = fp02e29c_get_post_by_slug( $slug, 'page' );

	if ( isset( $route['page_id'] ) && ! $existing ) {
		$existing = get_post( (int) $route['page_id'] );
	}

	if ( $existing instanceof WP_Post ) {
		$action = 'UPDATED_PAGE';
		$post_id = (int) $existing->ID;
		$updates = array( 'ID' => $post_id );
		if ( $parent_id > 0 ) {
			$updates['post_parent'] = $parent_id;
		}
		if ( isset( $route['template'] ) ) {
			fp02e29c_set_page_template( $post_id, $route['template'] );
		}
		wp_update_post( $updates );
	} else {
		$action = 'CREATED_PAGE';
		$post_id = wp_insert_post(
			array(
				'post_type'    => 'page',
				'post_status'  => 'publish',
				'post_title'   => $route['title'],
				'post_name'    => $slug,
				'post_parent'  => $parent_id,
				'post_content' => fp02e29c_placeholder_block(),
			),
			true
		);
		if ( is_wp_error( $post_id ) ) {
			return array( 'action' => 'ERROR', 'error' => $post_id->get_error_message() );
		}
		if ( isset( $route['template'] ) ) {
			fp02e29c_set_page_template( (int) $post_id, $route['template'] );
		}
	}

	if ( isset( $route['template'] ) && FP02_E29C_GENERIC_TPL === $route['template'] ) {
		fp02e29c_ensure_page_content( $post_id, false );
	}

	return array(
		'action'   => $action,
		'id'       => (int) $post_id,
		'parent'   => $parent_id,
		'template' => get_post_meta( $post_id, '_wp_page_template', true ),
	);
}

function fp02e29c_create_or_update_service( array $route, $parent_id = 0 ) {
	$slug = $route['slug'];
	$post = null;

	if ( ! empty( $route['rename_from'] ) ) {
		$post = fp02e29c_get_service_by_slug( $route['rename_from'] );
		if ( $post instanceof WP_Post ) {
			wp_update_post(
				array(
					'ID'          => $post->ID,
					'post_name'   => $slug,
					'post_parent' => $parent_id,
					'post_title'  => $route['title'],
				)
			);
			fp02e29c_ensure_service_intro( (int) $post->ID );
			return array(
				'action' => 'RENAMED_SERVICE',
				'id'     => (int) $post->ID,
				'parent' => $parent_id,
				'from'   => $route['rename_from'],
			);
		}
	}

	$post = fp02e29c_get_service_by_slug( $slug );
	if ( $post instanceof WP_Post ) {
		if ( $parent_id > 0 && (int) $post->post_parent !== $parent_id ) {
			wp_update_post(
				array(
					'ID'          => $post->ID,
					'post_parent' => $parent_id,
				)
			);
		}
		fp02e29c_ensure_service_intro( (int) $post->ID );
		return array(
			'action' => 'EXISTS_OK',
			'id'     => (int) $post->ID,
			'parent' => $parent_id,
		);
	}

	$post_id = wp_insert_post(
		array(
			'post_type'   => 'service',
			'post_status' => 'publish',
			'post_title'  => $route['title'],
			'post_name'   => $slug,
			'post_parent' => $parent_id,
		),
		true
	);
	if ( is_wp_error( $post_id ) ) {
		return array( 'action' => 'ERROR', 'error' => $post_id->get_error_message() );
	}
	fp02e29c_ensure_service_intro( (int) $post_id );
	return array(
		'action' => 'CREATED_SERVICE',
		'id'     => (int) $post_id,
		'parent' => $parent_id,
	);
}

function fp02e29c_resolve_parent_id( $parent_slug, $post_type = 'service' ) {
	if ( '' === $parent_slug ) {
		return 0;
	}
	if ( 'service' === $post_type ) {
		$parent = fp02e29c_get_service_by_slug( $parent_slug );
		return $parent instanceof WP_Post ? (int) $parent->ID : 0;
	}
	$parent = fp02e29c_get_post_by_slug( $parent_slug, 'page' );
	return $parent instanceof WP_Post ? (int) $parent->ID : 0;
}

function fp02e29c_copy_favicon_assets() {
	global $v9_favicon, $theme_fav;
	if ( ! is_dir( $theme_fav ) ) {
		wp_mkdir_p( $theme_fav );
	}
	$copied = array();
	foreach ( array( 'favicon.svg', 'favicon-32x32.png', 'favicon.ico', 'apple-touch-icon.png' ) as $file ) {
		$src = trailingslashit( $v9_favicon ) . $file;
		$dst = trailingslashit( $theme_fav ) . $file;
		if ( is_readable( $src ) ) {
			copy( $src, $dst );
			$copied[] = $file;
		}
	}
	return $copied;
}

function fp02e29c_import_site_icon() {
	global $v9_favicon;
	require_once ABSPATH . 'wp-admin/includes/file.php';
	require_once ABSPATH . 'wp-admin/includes/media.php';
	require_once ABSPATH . 'wp-admin/includes/image.php';

	$source = trailingslashit( $v9_favicon ) . 'apple-touch-icon.png';
	if ( ! is_readable( $source ) ) {
		return array( 'ok' => false, 'error' => 'source_missing' );
	}

	$upload_dir = wp_upload_dir();
	$dest       = trailingslashit( $upload_dir['path'] ) . 'fp02-site-icon-apple-touch-icon.png';
	copy( $source, $dest );

	$filetype = wp_check_filetype( basename( $dest ), null );
	$attach_id = wp_insert_attachment(
		array(
			'post_mime_type' => $filetype['type'],
			'post_title'     => 'FP-0002 Site Icon',
			'post_status'    => 'inherit',
		),
		$dest
	);
	if ( is_wp_error( $attach_id ) || ! $attach_id ) {
		return array( 'ok' => false, 'error' => 'insert_failed' );
	}
	$metadata = wp_generate_attachment_metadata( $attach_id, $dest );
	wp_update_attachment_metadata( $attach_id, $metadata );
	update_option( 'site_icon', (int) $attach_id );
	return array( 'ok' => true, 'attachment_id' => (int) $attach_id );
}

function fp02e29c_inventory_export() {
	$routes = fp02e29c_excel_routes();
	$posts  = get_posts(
		array(
			'post_type'      => array( 'page', 'service', 'post' ),
			'post_status'    => array( 'publish', 'draft', 'private' ),
			'posts_per_page' => -1,
			'orderby'        => 'ID',
			'order'          => 'ASC',
		)
	);
	$inventory = array();
	foreach ( $posts as $post ) {
		$inventory[] = array(
			'id'       => $post->ID,
			'type'     => $post->post_type,
			'slug'     => $post->post_name,
			'title'    => $post->post_title,
			'parent'   => (int) $post->post_parent,
			'status'   => $post->post_status,
			'template' => 'page' === $post->post_type ? get_post_meta( $post->ID, '_wp_page_template', true ) : 'single-service.php',
			'url'      => get_permalink( $post ),
		);
	}
	return array(
		'manifest_count' => count( $routes ),
		'posts'          => $inventory,
	);
}

function fp02e29c_apply_mutations() {
	$results  = array();
	$services = array();
	$pages    = array();

	foreach ( fp02e29c_excel_routes() as $route ) {
		$wp_type = $route['wp'];
		if ( in_array( $route['type'], array( 'home', 'services_index', 'ocentre_hub', 'reviews', 'blog_index', 'blog_single_demo', 'contacts' ), true ) ) {
			$results[] = array_merge(
				array( 'path' => $route['path'], 'action' => 'SKIP_ACCEPTED' ),
				array( 'type' => $route['type'] )
			);
			continue;
		}

		$parent_id = isset( $route['parent_slug'] ) ? fp02e29c_resolve_parent_id( $route['parent_slug'], $wp_type ) : 0;

		if ( 'service' === $wp_type ) {
			$mutation = fp02e29c_create_or_update_service( $route, $parent_id );
			$services[] = array_merge( array( 'path' => $route['path'] ), $mutation );
		} elseif ( 'page' === $wp_type ) {
			$mutation = fp02e29c_create_or_update_page( $route, $parent_id );
			$pages[] = array_merge( array( 'path' => $route['path'] ), $mutation );
		}
	}

	flush_rewrite_rules( false );

	$favicon_copy = fp02e29c_copy_favicon_assets();
	$site_icon    = fp02e29c_import_site_icon();

	return array(
		'services'     => $services,
		'pages'        => $pages,
		'favicon_copy' => $favicon_copy,
		'site_icon'    => $site_icon,
		'db_writes'    => count( $services ) + count( $pages ) + ( $site_icon['ok'] ? 1 : 0 ),
	);
}

function fp02e29c_http_validate() {
	$rows = array();
	foreach ( fp02e29c_excel_routes() as $route ) {
		$path = $route['path'];
		$url  = home_url( $path === '/' ? '/' : ltrim( $path, '/' ) );
		$resp = wp_remote_get( $url, array( 'timeout' => 20, 'redirection' => 5 ) );
		$code = is_wp_error( $resp ) ? 0 : (int) wp_remote_retrieve_response_code( $resp );
		$rows[] = array(
			'path'   => $path,
			'url'    => $url,
			'status' => $code,
			'ok'     => in_array( $code, array( 200, 301, 302 ), true ),
		);
	}
	$regression = array( '/', '/o-centre/', '/blog/', '/blog/nazvanie-stati/', '/uslugi/zavisimosti/', '/uslugi/psihicheskoe-zdorovie/', '/uslugi/rasstroystva-pischevogo-povedeniya/', '/privacy-policy/' );
	$reg_rows   = array();
	foreach ( $regression as $path ) {
		$url  = home_url( $path === '/' ? '/' : ltrim( $path, '/' ) );
		$resp = wp_remote_get( $url, array( 'timeout' => 20 ) );
		$code = is_wp_error( $resp ) ? 0 : (int) wp_remote_retrieve_response_code( $resp );
		$reg_rows[] = array( 'path' => $path, 'status' => $code, 'ok' => 200 === $code );
	}
	return array( 'routes' => $rows, 'regression' => $reg_rows );
}

$summary = array( 'mode' => $mode, 'phase' => 'V9-06E29C' );

if ( in_array( $mode, array( 'backup-only', 'all' ), true ) ) {
	$summary['inventory_before'] = fp02e29c_inventory_export();
	fp02e29c_json_write( 'pre-mutation-inventory.json', $summary['inventory_before'] );
}

if ( in_array( $mode, array( 'apply', 'all' ), true ) ) {
	$summary['mutations'] = fp02e29c_apply_mutations();
	fp02e29c_json_write( 'mutation-result.json', $summary['mutations'] );
	$summary['inventory_after'] = fp02e29c_inventory_export();
	fp02e29c_json_write( 'post-mutation-inventory.json', $summary['inventory_after'] );
}

if ( in_array( $mode, array( 'validate', 'all' ), true ) ) {
	$summary['http_validation'] = fp02e29c_http_validate();
	fp02e29c_json_write( 'http-validation.json', $summary['http_validation'] );
}

fp02e29c_json_write( '_runner_summary.json', $summary );
echo wp_json_encode( $summary, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE ) . "\n";
