<?php
/**
 * Single glossary term template.
 * Reuses internal-page chrome: page_scene, breadcrumbs, content_block.
 * No invented dates, authors, ratings, or FAQ blocks.
 *
 * @package iseoblog
 */

get_header();

$term_id   = get_the_ID();
$synonyms  = function_exists( 'get_field' ) ? (string) get_field( 'glossary_synonyms', $term_id ) : (string) get_post_meta( $term_id, 'glossary_synonyms', true );
$excerpt   = trim( (string) get_the_excerpt( $term_id ) );
$content   = trim( (string) get_post_field( 'post_content', $term_id ) );
$archive   = get_post_type_archive_link( 'glossary' );
?>

		<div class="page_scene">
			<div class="container">
				<div class="row">
					<div class="page_scene_inner">
						<div class="page_scene__description">
							<ul class="breadcrumbs">
								<li><a href="/">Главная</a></li>
								<li><a href="<?php echo esc_url( $archive ); ?>">Глоссарий</a></li>
								<li><?php the_title(); ?></li>
							</ul>
							<h1><?php the_title(); ?></h1>
							<a href="#SecondScreen" class="see_more_btn" title="Далее"></a>
						</div>
					</div>
				</div>
			</div>
		</div>

	</header>

	<main id="SecondScreen">
		<div class="container">
			<div class="row">

				<article <?php post_class( 'content_block' ); ?> id="post-<?php the_ID(); ?>">
					<?php if ( $excerpt ) : ?>
						<p><strong><?php echo esc_html( $excerpt ); ?></strong></p>
					<?php endif; ?>

					<?php if ( $content ) : ?>
						<?php the_content(); ?>
					<?php elseif ( ! $excerpt ) : ?>
						<p>Определение термина готовится редакцией и пока не опубликовано.</p>
					<?php endif; ?>

					<?php if ( trim( $synonyms ) ) : ?>
						<h2>Синонимы</h2>
						<p><?php echo esc_html( $synonyms ); ?></p>
					<?php endif; ?>

					<p><a href="<?php echo esc_url( $archive ); ?>">← Вернуться в глоссарий</a></p>
				</article>

<?php
get_footer();
