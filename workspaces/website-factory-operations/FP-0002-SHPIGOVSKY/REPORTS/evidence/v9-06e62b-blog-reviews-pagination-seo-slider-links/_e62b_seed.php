<?php
/**
 * FP-0002 V9-06E62B seed runner.
 *
 * - Assign featured images to 10 demo Blog posts (empty-only).
 * - Append 20 idempotent demo Reviews (ACF options repeater; not CPT).
 * - Seed reusable Founder Quote fields if empty.
 * - Adjust featured flags so long demos appear in home slider (top 10 featured).
 *
 * Bootstrap: wp-load.php under local runtime.
 */

declare(strict_types=1);

$wp_root      = 'X:\\MARS-Localhost\\sites\\wordpress\\projects\\shpigovsky';
$wp_load      = $wp_root . '\\wp-load.php';
$evidence_dir = 'X:\\AI MARS\\workspaces\\website-factory-operations\\FP-0002-SHPIGOVSKY\\REPORTS\\evidence\\v9-06e62b-blog-reviews-pagination-seo-slider-links';

if ( ! file_exists( $wp_load ) ) {
	fwrite( STDERR, "wp-load.php not found\n" );
	exit( 1 );
}

if ( ! is_dir( $evidence_dir ) ) {
	mkdir( $evidence_dir, 0777, true );
}

require $wp_load;

if ( ! function_exists( 'update_field' ) || ! function_exists( 'get_field' ) ) {
	fwrite( STDERR, "ACF unavailable\n" );
	exit( 1 );
}

$db_writes       = array();
$blog_images     = array();
$demo_reviews    = array();
$founder_writes  = array();
$featured_tweaks = array();

/**
 * @param mixed $value Value.
 */
function e62b_scalar( $value ): string {
	if ( is_scalar( $value ) || null === $value ) {
		return (string) $value;
	}
	return (string) wp_json_encode( $value, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES );
}

/**
 * @param array<int, array<string, string>> $rows Rows.
 */
function e62b_record( array &$rows, string $scope, string $object_id, string $field, $old, $new, string $action ): void {
	$rows[] = array(
		'scope'     => $scope,
		'object_id' => $object_id,
		'field'     => $field,
		'old_value' => e62b_scalar( $old ),
		'new_value' => e62b_scalar( $new ),
		'action'    => $action,
	);
}

/**
 * @param array<int, string> $headers Headers.
 * @param array<int, array<string, string>> $rows Rows.
 */
function e62b_csv( string $path, array $headers, array $rows ): void {
	$handle = fopen( $path, 'wb' );
	if ( false === $handle ) {
		throw new RuntimeException( "Cannot write {$path}" );
	}
	fputcsv( $handle, $headers );
	foreach ( $rows as $row ) {
		$out = array();
		foreach ( $headers as $h ) {
			$out[] = $row[ $h ] ?? '';
		}
		fputcsv( $handle, $out );
	}
	fclose( $handle );
}

// --- PART A: Blog demo featured images ---
$image_pool = array( 1106, 1089, 1088, 1087, 1086, 1085, 1084, 93, 92, 91 );
foreach ( $image_pool as $aid ) {
	if ( 'attachment' !== get_post_type( $aid ) ) {
		fwrite( STDERR, "Missing attachment {$aid}\n" );
		exit( 1 );
	}
}

for ( $i = 1; $i <= 10; $i++ ) {
	$title    = sprintf( 'Демо-статья для проверки пагинации — %02d', $i );
	$existing = get_page_by_title( $title, OBJECT, 'post' );
	if ( ! ( $existing instanceof WP_Post ) ) {
		$blog_images[] = array(
			'title'         => $title,
			'post_id'       => '',
			'attachment_id' => '',
			'action'        => 'missing_post',
		);
		continue;
	}

	$post_id   = (int) $existing->ID;
	$current   = (int) get_post_thumbnail_id( $post_id );
	$attach_id = (int) $image_pool[ ( $i - 1 ) % count( $image_pool ) ];

	if ( $current > 0 ) {
		$blog_images[] = array(
			'title'         => $title,
			'post_id'       => (string) $post_id,
			'attachment_id' => (string) $current,
			'action'        => 'skip_existing_thumb',
		);
		continue;
	}

	$set = set_post_thumbnail( $post_id, $attach_id );
	e62b_record( $db_writes, 'post_meta', (string) $post_id, '_thumbnail_id', $current, $attach_id, $set ? 'set_featured_image' : 'set_failed' );
	$blog_images[] = array(
		'title'         => $title,
		'post_id'       => (string) $post_id,
		'attachment_id' => (string) $attach_id,
		'action'        => $set ? 'assigned' : 'failed',
	);
}

// --- PART B: 20 demo reviews (ACF options repeater) ---
$services = array( 74, 314, 1019, 1017, 1016, 1013, 1018, 1011, 315, 316 );
$short    = 'Краткий демо-отзыв: спокойно объяснили первые шаги и ответили на вопросы семьи.';
$boundary = "Отзыв на границе пяти строк.\nМы обратились за консультацией и получили понятные рекомендации без давления.\nСпециалисты говорили спокойно и по делу.\nДля семьи это было важно.\nДемо-текст для проверки clamp.";
$long_slider = 'Длинный демо-отзыв для слайдера и архива. Мы долго выбирали центр и сравнивали подходы, потому что для семьи критично было сохранить конфиденциальность и спокойный тон общения. С первого контакта специалисты объясняли этапы помощи простым языком, без запугивания и без обещаний «быстрого чуда». Нас подробно ориентировали по режиму, посещениям и тому, как поддерживать родственника. Отдельно отметили внимательность к вопросам быта и обратной связи: звонки не оставляли без ответа, а план на ближайшие дни был понятен. Этот текст намеренно длиннее пяти визуальных строк, чтобы на карточках слайдера появлялась ссылка «Читать весь отзыв», а на архиве — разворачивание. Материал создан локально в V9-06E62B и не является производственным отзывом клиента.';
$long_archive = 'Ещё один развёрнутый демо-отзыв для пагинации архива. Важно было проверить, что длинный текст корректно обрезается на странице /otzyvy/, а кнопка разворачивания работает только при реальном переполнении. В консультации нам помогли сформулировать запрос и понять, какие шаги можно сделать уже сейчас. Отметили уважительное отношение персонала и понятную структуру сопровождения. Повторяем: это локальный демо-контент для проверки вёрстки, SEO пагинации и якорных ссылок со слайдеров. Дополнительный абзац нужен, чтобы гарантированно превысить лимит строк архивной карточки на нескольких ширинах экрана, включая 480 и 370.';

$names = array(
	'Анна К., Москва',
	'Игорь П., МО',
	'Елена С., Москва',
	'Дмитрий В., МО',
	'Ольга М., Москва',
	'Сергей Н., МО',
	'Мария Л., Москва',
	'Павел Р., МО',
	'Наталья Т., Москва',
	'Алексей Ф., МО',
	'Виктория Г., Москва',
	'Роман Д., МО',
	'Ирина Е., Москва',
	'Кирилл Ж., МО',
	'Светлана З., Москва',
	'Андрей И., МО',
	'Юлия К., Москва',
	'Максим Л., МО',
	'Татьяна М., Москва',
	'Никита О., МО',
);

$length_map = array(
	1  => 'long_slider',
	2  => 'long_slider',
	3  => 'long_slider',
	4  => 'long_archive',
	5  => 'long_archive',
	6  => 'boundary',
	7  => 'boundary',
	8  => 'short',
	9  => 'short',
	10 => 'short',
	11 => 'long_slider',
	12 => 'long_archive',
	13 => 'boundary',
	14 => 'short',
	15 => 'long_slider',
	16 => 'short',
	17 => 'long_archive',
	18 => 'boundary',
	19 => 'short',
	20 => 'long_slider',
);

$text_by_class = array(
	'short'         => $short,
	'boundary'      => $boundary,
	'long_slider'   => $long_slider,
	'long_archive'  => $long_archive,
);

$items = get_field( 'reviews_items', 'fp02-reviews' );
if ( ! is_array( $items ) ) {
	$items = array();
}

// Unfeature last 5 existing short rows so long demos enter home slider top-10 featured.
$existing_count = count( $items );
for ( $idx = max( 0, $existing_count - 5 ); $idx < $existing_count; $idx++ ) {
	$author = (string) ( $items[ $idx ]['review_author'] ?? '' );
	if ( 0 === strpos( $author, 'Демо-отзыв для проверки пагинации' ) ) {
		continue;
	}
	$old_featured = $items[ $idx ]['review_featured'] ?? null;
	if ( ! empty( $old_featured ) ) {
		$items[ $idx ]['review_featured'] = 0;
		$featured_tweaks[] = array(
			'index'  => (string) ( $idx + 1 ),
			'author' => $author,
			'action' => 'set_featured_0_for_slider_slot',
		);
		e62b_record( $db_writes, 'option_repeater', 'fp02-reviews', "reviews_items[{$idx}].review_featured", $old_featured, 0, 'unfeature_for_slider_demo_slots' );
	}
}

$created = 0;
$skipped = 0;

for ( $n = 1; $n <= 20; $n++ ) {
	$marker = sprintf( 'Демо-отзыв для проверки пагинации — %02d', $n );
	$found  = false;
	foreach ( $items as $row ) {
		$author = (string) ( $row['review_author'] ?? '' );
		$source = (string) ( $row['review_source'] ?? '' );
		$src_key = 'e62b-demo-' . sprintf( '%02d', $n );
		if ( $source === $src_key || 0 === strpos( $author, $marker ) ) {
			$found = true;
			break;
		}
	}

	$len_class = $length_map[ $n ];
	$service   = $services[ ( $n - 1 ) % count( $services ) ];

	if ( $found ) {
		$skipped++;
		$demo_reviews[] = array(
			'n'            => (string) $n,
			'author'       => $marker,
			'service_id'   => (string) $service,
			'length_class' => $len_class,
			'action'       => 'exists',
		);
		continue;
	}

	$items[] = array(
		'review_author'   => sprintf( 'Демо-отзыв для проверки пагинации — %02d (%s)', $n, $names[ $n - 1 ] ),
		'review_text'     => $text_by_class[ $len_class ],
		'review_service'  => $service,
		'review_context'  => '',
		'review_source'   => 'e62b-demo-' . sprintf( '%02d', $n ),
		'review_date'     => sprintf( '2026-07-%02d', min( 17, $n ) ),
		'review_rating'   => 5,
		'review_visible'  => 1,
		'review_featured' => 1,
	);

	$created++;
	$demo_reviews[] = array(
		'n'            => (string) $n,
		'author'       => sprintf( 'Демо-отзыв для проверки пагинации — %02d (%s)', $n, $names[ $n - 1 ] ),
		'service_id'   => (string) $service,
		'length_class' => $len_class,
		'action'       => 'created',
		'reviewer'     => $names[ $n - 1 ],
	);
}

// Prefer reviewer names in author while keeping stable prefix for idempotency:
for ( $i = 0; $i < count( $items ); $i++ ) {
	// no-op rename pass removed — authors set at create time
}
if ( $created > 0 || ! empty( $featured_tweaks ) ) {
	$old_count = $existing_count;
	update_field( 'reviews_items', $items, 'fp02-reviews' );
	e62b_record( $db_writes, 'option_repeater', 'fp02-reviews', 'reviews_items', "count:{$old_count}", 'count:' . count( $items ), 'update_reviews_items' );
}

// Fix author names for newly created rows that still lack parenthetical names — already applied above.

// Rebuild demo_reviews matrix with final review_id (1-based index)
$final_items = get_field( 'reviews_items', 'fp02-reviews' );
$matrix      = array();
if ( is_array( $final_items ) ) {
	foreach ( $final_items as $idx => $row ) {
		$author = (string) ( $row['review_author'] ?? '' );
		$source = (string) ( $row['review_source'] ?? '' );
		if ( 0 !== strpos( $author, 'Демо-отзыв для проверки пагинации' ) && false === strpos( $source, 'e62b-demo-' ) ) {
			continue;
		}
		$nn = 0;
		if ( preg_match( '/e62b-demo-(\d{2})/', $source, $m ) ) {
			$nn = (int) $m[1];
		} elseif ( preg_match( '/— (\d{2})/', $author, $m ) ) {
			$nn = (int) $m[1];
		}
		$matrix[] = array(
			'review_id'    => (string) ( $idx + 1 ),
			'n'            => (string) $nn,
			'slug_marker'  => $source,
			'author'       => $author,
			'service_id'   => e62b_scalar( $row['review_service'] ?? '' ),
			'length_class' => $length_map[ $nn ] ?? '',
			'featured'     => e62b_scalar( $row['review_featured'] ?? '' ),
			'page'         => (string) ( (int) floor( $idx / 10 ) + 1 ),
		);
	}
}

// --- PART E: Founder quote seed if empty ---
$ctx = 'fp02-block-founder-quote';
$paras = get_field( 'founder_quote_paragraphs', $ctx );
if ( empty( $paras ) ) {
	$seed_paras = array(
		array( 'text' => 'Мы создавали «Шпиговский Дом» как место, где человек может получить профессиональную помощь, не теряя связь с собственной жизнью.' ),
		array( 'text' => 'Многие боятся обратиться за лечением, потому что опасаются потерять семью, работу и привычный уклад жизни.' ),
		array( 'text' => 'Мы считаем, что современная реабилитация должна помогать человеку восстанавливать себя, сохраняя то, что для него действительно важно.' ),
		array( 'text' => '«Наша цель — создать безопасное пространство для изменений. Наша задача — не изолировать человека от жизни, а помочь ему вернуть контроль над ней.»' ),
	);
	update_field( 'founder_quote_paragraphs', $seed_paras, $ctx );
	e62b_record( $db_writes, 'option', $ctx, 'founder_quote_paragraphs', '', '4 paragraphs', 'seed_if_empty' );
	$founder_writes[] = array( 'field' => 'founder_quote_paragraphs', 'action' => 'seeded' );
} else {
	$founder_writes[] = array( 'field' => 'founder_quote_paragraphs', 'action' => 'kept_existing' );
}

$scalars = array(
	'founder_quote_name'      => 'Сергей Юрьевич Шпиговский',
	'founder_quote_role'      => 'Основатель центра. Аддиктолог, интервенционист',
	'founder_quote_cta_label' => 'Записаться на консультацию',
);
foreach ( $scalars as $field => $value ) {
	$cur = get_field( $field, $ctx );
	if ( null === $cur || '' === $cur ) {
		update_field( $field, $value, $ctx );
		e62b_record( $db_writes, 'option', $ctx, $field, $cur, $value, 'seed_if_empty' );
		$founder_writes[] = array( 'field' => $field, 'action' => 'seeded' );
	} else {
		$founder_writes[] = array( 'field' => $field, 'action' => 'kept_existing' );
	}
}

$photo = get_field( 'founder_quote_photo', $ctx );
if ( empty( $photo ) && get_post_type( 754 ) === 'attachment' ) {
	update_field( 'founder_quote_photo', 754, $ctx );
	e62b_record( $db_writes, 'option', $ctx, 'founder_quote_photo', '', 754, 'seed_if_empty' );
	$founder_writes[] = array( 'field' => 'founder_quote_photo', 'action' => 'seeded_754' );
} else {
	$founder_writes[] = array( 'field' => 'founder_quote_photo', 'action' => empty( $photo ) ? 'empty_no_seed_asset' : 'kept_existing' );
}

e62b_csv( $evidence_dir . '\\db-writes.csv', array( 'scope', 'object_id', 'field', 'old_value', 'new_value', 'action' ), $db_writes );
e62b_csv( $evidence_dir . '\\demo-blog-image-mapping.csv', array( 'title', 'post_id', 'attachment_id', 'action' ), $blog_images );
e62b_csv( $evidence_dir . '\\demo-reviews-matrix.csv', array( 'review_id', 'n', 'slug_marker', 'author', 'service_id', 'length_class', 'featured', 'page' ), $matrix );
e62b_csv( $evidence_dir . '\\founder-ownership.csv', array( 'field', 'action' ), $founder_writes );
e62b_csv( $evidence_dir . '\\featured-tweaks.csv', array( 'index', 'author', 'action' ), $featured_tweaks );

echo wp_json_encode(
	array(
		'status'            => 'ok',
		'blog_images'       => count( $blog_images ),
		'reviews_total'     => is_array( $final_items ) ? count( $final_items ) : 0,
		'demo_reviews'      => count( $matrix ),
		'demo_created'      => $created,
		'demo_skipped'      => $skipped,
		'db_writes'         => count( $db_writes ),
		'founder_writes'    => $founder_writes,
	),
	JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT
) . "\n";
