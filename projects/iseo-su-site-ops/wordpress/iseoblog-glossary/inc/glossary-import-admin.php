<?php
/**
 * Bounded admin-only glossary import (dry-run + draft intake).
 *
 * Enable with ISEO_GLOSSARY_IMPORT_ENABLED true. Disable after successful import.
 * Not a public endpoint.
 *
 * @package iseoblog
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

if ( ! defined( 'ISEO_GLOSSARY_IMPORT_ENABLED' ) ) {
	define( 'ISEO_GLOSSARY_IMPORT_ENABLED', false );
}

/**
 * Register Tools submenu when import is enabled.
 */
function iseo_glossary_import_admin_menu() {
	if ( ! ISEO_GLOSSARY_IMPORT_ENABLED ) {
		return;
	}
	add_management_page(
		'Импорт глоссария',
		'Импорт глоссария',
		'manage_options',
		'iseo-glossary-import',
		'iseo_glossary_import_admin_page'
	);
}
add_action( 'admin_menu', 'iseo_glossary_import_admin_menu' );

/**
 * Resolve inventory JSON path.
 *
 * @return string
 */
function iseo_glossary_import_inventory_path() {
	return get_template_directory() . '/inc/data/glossary-terms-inventory-v1.json';
}

/**
 * Normalize term title for duplicate detection.
 *
 * @param string $title Title.
 * @return string
 */
function iseo_glossary_normalize_title( $title ) {
	$title = trim( wp_strip_all_tags( (string) $title ) );
	$title = preg_replace( '/\s+/u', ' ', $title );
	return mb_strtolower( $title, 'UTF-8' );
}

/**
 * Load inventory terms from JSON.
 *
 * @return array{ok:bool,error?:string,terms?:array<int,array<string,string>>,stats?:array}
 */
function iseo_glossary_import_load_inventory() {
	$path = iseo_glossary_import_inventory_path();
	if ( ! is_readable( $path ) ) {
		return array(
			'ok'    => false,
			'error' => 'Inventory JSON not readable.',
		);
	}
	$raw = file_get_contents( $path );
	if ( false === $raw ) {
		return array(
			'ok'    => false,
			'error' => 'Failed to read inventory JSON.',
		);
	}
	$data = json_decode( $raw, true );
	if ( ! is_array( $data ) || empty( $data['terms'] ) || ! is_array( $data['terms'] ) ) {
		return array(
			'ok'    => false,
			'error' => 'Inventory JSON malformed.',
		);
	}
	$terms = array();
	foreach ( $data['terms'] as $row ) {
		if ( ! is_array( $row ) ) {
			continue;
		}
		$term = isset( $row['term'] ) ? trim( (string) $row['term'] ) : '';
		if ( '' === $term ) {
			continue;
		}
		$terms[] = array(
			'term'         => $term,
			'keywords'     => isset( $row['keywords'] ) ? (string) $row['keywords'] : '',
			'lsi_phrases'  => isset( $row['lsi_phrases'] ) ? (string) $row['lsi_phrases'] : '',
			'synonyms'     => isset( $row['synonyms'] ) ? (string) $row['synonyms'] : '',
		);
	}
	return array(
		'ok'    => true,
		'terms' => $terms,
		'stats' => isset( $data['stats'] ) && is_array( $data['stats'] ) ? $data['stats'] : array(),
	);
}

/**
 * Build normalized-title → post ID map for glossary posts.
 *
 * @return array<string,int>
 */
function iseo_glossary_existing_title_map() {
	static $map = null;
	if ( null !== $map ) {
		return $map;
	}
	$map = array();
	$all = get_posts(
		array(
			'post_type'              => 'glossary',
			'post_status'            => array( 'publish', 'draft', 'pending', 'future', 'private' ),
			'posts_per_page'         => -1,
			'fields'                 => 'ids',
			'no_found_rows'          => true,
			'update_post_meta_cache' => false,
			'update_post_term_cache' => false,
		)
	);
	foreach ( $all as $post_id ) {
		$norm = iseo_glossary_normalize_title( get_the_title( $post_id ) );
		if ( '' !== $norm && ! isset( $map[ $norm ] ) ) {
			$map[ $norm ] = (int) $post_id;
		}
	}
	return $map;
}

/**
 * Run import.
 *
 * @param bool $dry_run Dry run.
 * @return array<string,mixed>
 */
function iseo_glossary_run_import( $dry_run = true ) {
	$loaded = iseo_glossary_import_load_inventory();
	if ( empty( $loaded['ok'] ) ) {
		return array(
			'ok'    => false,
			'error' => $loaded['error'] ?? 'load_failed',
		);
	}

	$created   = 0;
	$skipped   = 0;
	$updated   = 0;
	$errors    = 0;
	$duplicates_in_file = 0;
	$seen      = array();
	$samples   = array();
	$existing_map = iseo_glossary_existing_title_map();

	foreach ( $loaded['terms'] as $row ) {
		$norm = iseo_glossary_normalize_title( $row['term'] );
		if ( isset( $seen[ $norm ] ) ) {
			++$duplicates_in_file;
			++$skipped;
			continue;
		}
		$seen[ $norm ] = true;

		$existing = isset( $existing_map[ $norm ] ) ? (int) $existing_map[ $norm ] : 0;
		if ( $existing ) {
			++$skipped;
			if ( count( $samples ) < 5 ) {
				$samples[] = array(
					'action' => 'skip_existing',
					'term'   => $row['term'],
					'id'     => $existing,
				);
			}
			continue;
		}

		if ( $dry_run ) {
			++$created;
			if ( count( $samples ) < 5 ) {
				$samples[] = array(
					'action' => 'would_create',
					'term'   => $row['term'],
				);
			}
			continue;
		}

		$post_id = wp_insert_post(
			array(
				'post_type'    => 'glossary',
				'post_status'  => 'draft',
				'post_title'   => $row['term'],
				'post_content' => '',
				'post_excerpt' => '',
			),
			true
		);

		if ( is_wp_error( $post_id ) ) {
			++$errors;
			continue;
		}

		if ( function_exists( 'update_field' ) ) {
			update_field( 'glossary_synonyms', $row['synonyms'], $post_id );
			update_field( 'glossary_keywords', $row['keywords'], $post_id );
			update_field( 'glossary_lsi_phrases', $row['lsi_phrases'], $post_id );
		} else {
			update_post_meta( $post_id, 'glossary_synonyms', $row['synonyms'] );
			update_post_meta( $post_id, 'glossary_keywords', $row['keywords'] );
			update_post_meta( $post_id, 'glossary_lsi_phrases', $row['lsi_phrases'] );
		}

		$existing_map[ $norm ] = (int) $post_id;
		++$created;
		if ( count( $samples ) < 5 ) {
			$samples[] = array(
				'action' => 'created',
				'term'   => $row['term'],
				'id'     => $post_id,
			);
		}
	}

	return array(
		'ok'                  => true,
		'dry_run'             => (bool) $dry_run,
		'inventory_terms'     => count( $loaded['terms'] ),
		'workbook_stats'      => $loaded['stats'],
		'created'             => $created,
		'skipped'             => $skipped,
		'updated'             => $updated,
		'errors'              => $errors,
		'duplicates_in_file'  => $duplicates_in_file,
		'status_forced'       => 'draft',
		'definitions_present' => false,
		'samples'             => $samples,
	);
}

/**
 * Admin page renderer.
 */
function iseo_glossary_import_admin_page() {
	if ( ! current_user_can( 'manage_options' ) ) {
		wp_die( esc_html__( 'Insufficient permissions.', 'iseoblog' ) );
	}

	$result = null;
	if ( isset( $_POST['iseo_glossary_import_action'] ) ) {
		check_admin_referer( 'iseo_glossary_import' );
		$action  = sanitize_text_field( wp_unslash( $_POST['iseo_glossary_import_action'] ) );
		$dry_run = ( 'run' !== $action );
		$result  = iseo_glossary_run_import( $dry_run );
	}

	$loaded = iseo_glossary_import_load_inventory();
	$path   = iseo_glossary_import_inventory_path();
	?>
	<div class="wrap">
		<h1>Импорт глоссария</h1>
		<p>Импорт создаёт только <strong>черновики</strong> без определений. Публичные пустые страницы не создаются.</p>
		<p>Файл инвентаря: <code><?php echo esc_html( $path ); ?></code></p>
		<?php if ( empty( $loaded['ok'] ) ) : ?>
			<div class="notice notice-error"><p><?php echo esc_html( $loaded['error'] ?? 'Inventory unavailable' ); ?></p></div>
		<?php else : ?>
			<p>Терминов в инвентаре: <strong><?php echo esc_html( (string) count( $loaded['terms'] ) ); ?></strong></p>
		<?php endif; ?>

		<?php if ( is_array( $result ) ) : ?>
			<div class="notice notice-<?php echo ! empty( $result['ok'] ) ? 'success' : 'error'; ?>">
				<pre><?php echo esc_html( wp_json_encode( $result, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT ) ); ?></pre>
			</div>
		<?php endif; ?>

		<form method="post">
			<?php wp_nonce_field( 'iseo_glossary_import' ); ?>
			<p>
				<button type="submit" class="button button-secondary" name="iseo_glossary_import_action" value="dry-run">Dry-run</button>
				<button type="submit" class="button button-primary" name="iseo_glossary_import_action" value="run" onclick="return confirm('Создать черновики терминов?');">Импортировать черновики</button>
			</p>
		</form>
		<p>После успешного импорта отключите импорт: <code>ISEO_GLOSSARY_IMPORT_ENABLED</code> → <code>false</code>.</p>
	</div>
	<?php
}
