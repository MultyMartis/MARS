<?php
/**
 * FP-0002 V9-06E61 cautious DB seed runner.
 *
 * Bootstrap: X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\wp-load.php
 * Scope: empty-only defaults and idempotent demo blog posts.
 */

declare( strict_types=1 );

$wp_root = 'X:\\MARS-Localhost\\sites\\wordpress\\projects\\shpigovsky';
$wp_load = $wp_root . '\\wp-load.php';
$evidence_dir = __DIR__;

if ( ! file_exists( $wp_load ) ) {
	fwrite( STDERR, "wp-load.php not found: {$wp_load}\n" );
	exit( 1 );
}

require $wp_load;

if ( ! function_exists( 'update_field' ) || ! function_exists( 'get_field' ) ) {
	fwrite( STDERR, "ACF get_field/update_field unavailable after bootstrap.\n" );
	exit( 1 );
}

$db_writes  = array();
$demo_posts = array();

/**
 * Append DB write evidence.
 */
function e61_record_db_write( array &$rows, string $scope, string $object_id, string $field, $old_value, $new_value, string $action ): void {
	$rows[] = array(
		'scope'     => $scope,
		'object_id' => $object_id,
		'field'     => $field,
		'old_value' => e61_scalar_for_csv( $old_value ),
		'new_value' => e61_scalar_for_csv( $new_value ),
		'action'    => $action,
	);
}

/**
 * Stable scalar rendering for CSV.
 */
function e61_scalar_for_csv( $value ): string {
	if ( is_scalar( $value ) || null === $value ) {
		return (string) $value;
	}

	return wp_json_encode( $value, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
}

/**
 * Empty-only ACF update helper.
 */
function e61_seed_acf_if_empty( string $field, $value, $context, string $scope, array &$rows ): bool {
	$current = get_field( $field, $context );

	if ( null !== $current && '' !== $current && array() !== $current ) {
		return false;
	}

	update_field( $field, $value, $context );
	e61_record_db_write( $rows, $scope, (string) $context, $field, $current, $value, 'set_if_empty' );

	return true;
}

/**
 * Write CSV rows.
 */
function e61_write_csv( string $path, array $headers, array $rows ): void {
	$handle = fopen( $path, 'wb' );
	if ( false === $handle ) {
		throw new RuntimeException( "Cannot write CSV: {$path}" );
	}

	fputcsv( $handle, $headers );
	foreach ( $rows as $row ) {
		$out = array();
		foreach ( $headers as $header ) {
			$out[] = $row[ $header ] ?? '';
		}
		fputcsv( $handle, $out );
	}
	fclose( $handle );
}

// Contacts heading on page 20: empty only, derived from current page title.
$contacts_page_id = 20;
$contacts_title   = get_the_title( $contacts_page_id );
$contacts_title   = is_string( $contacts_title ) && '' !== trim( $contacts_title ) ? trim( $contacts_title ) : 'Контакты';
e61_seed_acf_if_empty( 'contacts_heading', $contacts_title, $contacts_page_id, 'post_meta', $db_writes );

// Breadcrumb defaults: do not disable by omission.
e61_seed_acf_if_empty( 'show_breadcrumbs_pages', 1, 'option', 'option', $db_writes );
e61_seed_acf_if_empty( 'show_breadcrumbs_services', 1, 'option', 'option', $db_writes );

// Blog archive pagination: page_for_posts only.
$posts_page_id = (int) get_option( 'page_for_posts' );
if ( $posts_page_id > 0 ) {
	e61_seed_acf_if_empty( 'blog_archive_posts_per_page', 12, $posts_page_id, 'post_meta', $db_writes );
}

// Reviews page pagination.
e61_seed_acf_if_empty( 'reviews_per_page', 10, 'fp02-reviews', 'option', $db_writes );

// Optional first review service relation: set only when row exists and service is empty.
$reviews = get_field( 'reviews_items', 'fp02-reviews' );
if ( is_array( $reviews ) && ! empty( $reviews ) && empty( $reviews[0]['review_service'] ) ) {
	$service_query = new WP_Query(
		array(
			'post_type'              => 'service',
			'post_status'            => 'publish',
			'posts_per_page'         => 100,
			'orderby'                => 'menu_order title',
			'order'                  => 'ASC',
			'no_found_rows'          => true,
			'update_post_meta_cache' => false,
			'update_post_term_cache' => false,
		)
	);

	$service_leaf_id = 0;
	foreach ( $service_query->posts as $service_post ) {
		$children = get_children(
			array(
				'post_parent' => (int) $service_post->ID,
				'post_type'   => 'service',
				'post_status' => 'publish',
				'fields'      => 'ids',
				'numberposts' => 1,
			)
		);

		if ( empty( $children ) ) {
			$service_leaf_id = (int) $service_post->ID;
			break;
		}
	}
	wp_reset_postdata();

	if ( $service_leaf_id > 0 ) {
		$old_reviews = $reviews;
		$reviews[0]['review_service'] = $service_leaf_id;
		update_field( 'reviews_items', $reviews, 'fp02-reviews' );
		e61_record_db_write( $db_writes, 'option_repeater', 'fp02-reviews', 'reviews_items[0].review_service', $old_reviews[0]['review_service'] ?? '', $service_leaf_id, 'set_first_review_service_if_empty' );
	}
}

// Idempotent demo posts for pagination validation.
for ( $i = 1; $i <= 10; $i++ ) {
	$title = sprintf( 'Демо-статья для проверки пагинации — %02d', $i );
	$existing = get_page_by_title( $title, OBJECT, 'post' );

	if ( $existing instanceof WP_Post ) {
		$demo_posts[] = array(
			'title'   => $title,
			'post_id' => (string) $existing->ID,
			'action'  => 'exists',
		);
		continue;
	}

	$post_id = wp_insert_post(
		array(
			'post_title'   => $title,
			'post_name'    => sanitize_title( $title ),
			'post_status'  => 'publish',
			'post_type'    => 'post',
			'post_content' => '<p>Демонстрационная статья для проверки пагинации блога. Материал создан локально в рамках V9-06E61 и не является производственной публикацией.</p><p>Текст нужен только для проверки архива, карточек и второй страницы блога.</p>',
		),
		true
	);

	if ( is_wp_error( $post_id ) ) {
		$demo_posts[] = array(
			'title'   => $title,
			'post_id' => '',
			'action'  => 'error: ' . $post_id->get_error_message(),
		);
		continue;
	}

	$demo_posts[] = array(
		'title'   => $title,
		'post_id' => (string) $post_id,
		'action'  => 'created',
	);
	e61_record_db_write( $db_writes, 'post', (string) $post_id, 'post', '', $title, 'insert_demo_post' );
}

e61_write_csv( $evidence_dir . '\\db-writes.csv', array( 'scope', 'object_id', 'field', 'old_value', 'new_value', 'action' ), $db_writes );
e61_write_csv( $evidence_dir . '\\demo-posts.csv', array( 'title', 'post_id', 'action' ), $demo_posts );

echo wp_json_encode(
	array(
		'status'           => 'ok',
		'db_writes_count'  => count( $db_writes ),
		'demo_posts_count' => count( $demo_posts ),
		'db_writes_csv'    => $evidence_dir . '\\db-writes.csv',
		'demo_posts_csv'   => $evidence_dir . '\\demo-posts.csv',
	),
	JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES
) . PHP_EOL;
<?php
/**
 * V9-06E61 seed — contacts heading, defaults, demo blog posts.
 *
 * Bootstrap: php -d display_errors=1 _e61_seed.php
 *
 * @package Shpigovsky
 */

$wp_load = 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
if ( ! is_readable( $wp_load ) ) {
	fwrite( STDERR, "wp-load missing\n" );
	exit( 1 );
}

require $wp_load;

$report = array(
	'writes'     => array(),
	'skipped'    => array(),
	'demo_posts' => array(),
	'unrelated'  => 0,
);

/**
 * Record a write.
 *
 * @param string $scope Scope.
 * @param mixed  $before Before.
 * @param mixed  $after After.
 * @param string $note Note.
 */
function e61_write( &$report, $scope, $before, $after, $note = '' ) {
	$report['writes'][] = array(
		'scope'  => $scope,
		'before' => $before,
		'after'  => $after,
		'note'   => $note,
	);
}

$contacts_id = 20;
$blog_id     = (int) get_option( 'page_for_posts' );

// Contacts heading — seed if empty.
if ( function_exists( 'get_field' ) && function_exists( 'update_field' ) ) {
	$heading = get_field( 'contacts_heading', $contacts_id );
	if ( null === $heading || '' === trim( (string) $heading ) ) {
		$seed = 'Контакты';
		$title = get_the_title( $contacts_id );
		if ( is_string( $title ) && '' !== trim( $title ) ) {
			$seed = trim( $title );
		}
		update_field( 'contacts_heading', $seed, $contacts_id );
		e61_write( $report, 'postmeta:20:contacts_heading', '', $seed, 'seed empty heading' );
	} else {
		$report['skipped'][] = 'contacts_heading non-empty';
	}

	// Preserve phones — only log.
	$phones = get_field( 'contacts_phones', $contacts_id );
	$report['skipped'][] = 'contacts_phones rows=' . ( is_array( $phones ) ? count( $phones ) : 0 ) . ' (preserved)';

	// Breadcrumb toggles default ON if unset.
	foreach ( array( 'show_breadcrumbs_pages', 'show_breadcrumbs_services' ) as $field ) {
		$val = get_field( $field, 'option' );
		if ( null === $val || '' === $val ) {
			update_field( $field, 1, 'option' );
			e61_write( $report, 'option:' . $field, $val, 1, 'default enabled' );
		} else {
			$report['skipped'][] = $field . '=' . (string) $val;
		}
	}

	if ( $blog_id > 0 ) {
		$ppp = get_field( 'blog_archive_posts_per_page', $blog_id );
		if ( null === $ppp || '' === $ppp || (int) $ppp <= 0 ) {
			update_field( 'blog_archive_posts_per_page', 12, $blog_id );
			e61_write( $report, 'postmeta:' . $blog_id . ':blog_archive_posts_per_page', $ppp, 12, 'default' );
		} else {
			$report['skipped'][] = 'blog_archive_posts_per_page=' . (int) $ppp;
		}
		foreach ( array( 'blog_archive_show_cta', 'blog_archive_show_founder_word' ) as $toggle ) {
			$t = get_field( $toggle, $blog_id );
			if ( null === $t || '' === $t ) {
				update_field( $toggle, 1, $blog_id );
				e61_write( $report, 'postmeta:' . $blog_id . ':' . $toggle, $t, 1, 'default on' );
			}
		}
	}

	$rpp_ctx = 'fp02-reviews';
	$rpp     = get_field( 'reviews_per_page', $rpp_ctx );
	if ( null === $rpp || '' === $rpp || (int) $rpp <= 0 ) {
		update_field( 'reviews_per_page', 10, $rpp_ctx );
		e61_write( $report, 'option:fp02-reviews:reviews_per_page', $rpp, 10, 'default' );
	} else {
		$report['skipped'][] = 'reviews_per_page=' . (int) $rpp;
	}

	// Seed first empty review_service to a published service leaf if available.
	$items = get_field( 'reviews_items', $rpp_ctx );
	if ( is_array( $items ) && ! empty( $items ) ) {
		$service_q = new WP_Query(
			array(
				'post_type'      => 'service',
				'post_status'    => 'publish',
				'posts_per_page' => 1,
				'post_parent__not_in' => array( 0 ),
				'orderby'        => 'menu_order title',
				'order'          => 'ASC',
				'fields'         => 'ids',
			)
		);
		$service_id = ! empty( $service_q->posts ) ? (int) $service_q->posts[0] : 0;
		if ( $service_id <= 0 ) {
			$service_q2 = new WP_Query(
				array(
					'post_type'      => 'service',
					'post_status'    => 'publish',
					'posts_per_page' => 1,
					'orderby'        => 'title',
					'order'          => 'ASC',
					'fields'         => 'ids',
				)
			);
			$service_id = ! empty( $service_q2->posts ) ? (int) $service_q2->posts[0] : 0;
		}
		if ( $service_id > 0 ) {
			$changed = false;
			foreach ( $items as $i => $row ) {
				if ( ! is_array( $row ) ) {
					continue;
				}
				$existing = $row['review_service'] ?? null;
				$empty    = empty( $existing );
				if ( $empty && ! $changed ) {
					$items[ $i ]['review_service'] = $service_id;
					$changed                       = true;
					e61_write( $report, 'fp02-reviews:reviews_items_' . $i . '_review_service', '', $service_id, get_the_title( $service_id ) );
				}
			}
			if ( $changed ) {
				update_field( 'reviews_items', $items, $rpp_ctx );
			} else {
				$report['skipped'][] = 'review_service already set or no empty row';
			}
		}
	}
}

// Demo blog posts 01..10 idempotent.
for ( $n = 1; $n <= 10; $n++ ) {
	$title = sprintf( 'Демо-статья для проверки пагинации — %02d', $n );
	$slug  = sprintf( 'demo-pagination-article-%02d', $n );
	$existing = get_page_by_path( $slug, OBJECT, 'post' );
	if ( ! $existing ) {
		$found = get_posts(
			array(
				'post_type'      => 'post',
				'title'          => $title,
				'post_status'    => 'any',
				'posts_per_page' => 1,
				'fields'         => 'ids',
			)
		);
		if ( ! empty( $found ) ) {
			$existing = get_post( (int) $found[0] );
		}
	}
	if ( $existing ) {
		$report['demo_posts'][] = array(
			'id'     => (int) $existing->ID,
			'slug'   => $existing->post_name,
			'title'  => $existing->post_title,
			'action' => 'exists',
		);
		continue;
	}

	$content = "Это демонстрационная статья №{$n} для проверки пагинации архива блога.\n\n"
		. "Текст написан как реалистичный русский placeholder: краткое введение, несколько абзацев о лечении и реабилитации, без претензии на финальный контент.\n\n"
		. "После проверки пагинации эти материалы можно удалить или заменить оператором.";

	$post_id = wp_insert_post(
		array(
			'post_title'   => $title,
			'post_name'    => $slug,
			'post_content' => $content,
			'post_status'  => 'publish',
			'post_type'    => 'post',
			'post_author'  => 1,
		),
		true
	);

	if ( is_wp_error( $post_id ) ) {
		$report['demo_posts'][] = array(
			'title'  => $title,
			'action' => 'error',
			'error'  => $post_id->get_error_message(),
		);
		continue;
	}

	e61_write( $report, 'posts:demo:' . $post_id, '', $title, $slug );
	$report['demo_posts'][] = array(
		'id'     => (int) $post_id,
		'slug'   => $slug,
		'title'  => $title,
		'action' => 'created',
	);
}

$out = dirname( __FILE__ ) . '/db-writes.json';
file_put_contents( $out, wp_json_encode( $report, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) );
echo wp_json_encode( $report, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) . "\n";
