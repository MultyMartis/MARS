<?php
/**
 * Glossary page_scene hero.
 *
 * Structural copy of production /services.html page_scene.
 * Omits .page_scene__rates. CTA is in-page #SecondScreen (not modalbox).
 *
 * @package iseoblog
 *
 * @var array $args {
 *     @type string $context archive|single
 * }
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$context     = ( isset( $args['context'] ) && 'single' === $args['context'] ) ? 'single' : 'archive';
$is_archive  = ( 'archive' === $context );
$archive_url = get_post_type_archive_link( 'glossary' );
$img_alt     = $is_archive ? 'Глоссарий' : wp_strip_all_tags( get_the_title() );
$archive_desc = 'Словарь терминов SEO и digital-маркетинга. Краткие определения публикуются по мере редакционной подготовки; полный разбор — на странице термина.';
?>
		<div class="page_scene">
			<div class="container">
				<div class="row">
					<div class="page_scene_inner">
						<div class="page_scene__description">
							<ul class="breadcrumbs">
								<li><a href="/">Главная</a></li>
								<?php if ( $is_archive ) : ?>
								<li>Глоссарий</li>
								<?php else : ?>
								<li><a href="<?php echo esc_url( $archive_url ); ?>">Глоссарий</a></li>
								<li><?php the_title(); ?></li>
								<?php endif; ?>
							</ul>
							<?php if ( $is_archive ) : ?>
							<h1>Глоссарий</h1>
							<span><?php echo esc_html( $archive_desc ); ?></span>
							<?php else : ?>
							<h1><?php the_title(); ?></h1>
							<?php endif; ?>
							<div class="page_scene__btns">
								<a href="#SecondScreen" class="page_scene__btn_order">Подробнее</a>
							</div>
							<a href="#SecondScreen" class="see_more_btn" title="Далее"></a>
						</div>
						<div class="page_scene__info">
							<div class="page_scene__info_wrap">
								<img src="/img/services_title_img.svg" alt="<?php echo esc_attr( $img_alt ); ?>">
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
