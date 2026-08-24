<?php
/**
 * The template for displaying all single posts
 *
 * @link https://developer.wordpress.org/themes/basics/template-hierarchy/#single-post
 *
 * @package iseoblog
 */

get_header();
$categories = get_the_category();
$cat = false;
foreach($categories as $category) {
	if($category->term_id != 1) {
		$cat = $category;
		break;
	}
}

?>

		<div class="blog_article">
			<div class="container">
				<div class="row">
					<div class="blog_article__inner">
						<div class="blog_article__breadcrumbs">
							<ul class="breadcrumbs">
								<li><a href="/">Главная</a></li>
								<li><a href="/blog">Блог</a></li>
							</ul>							
						</div>
						<div class="blog_article__description">
							<div class="blog_article__time"><?=mb_strtolower(get_the_date('d M Y, h:i'))?></div>
							<h1><?=the_title()?></h1>
							<ul class="blog_article__tags">
								<?if($cat) { ?>
									<li><a href="<?=get_category_link($cat->term_id)?>"><?=$cat->name?></a></li>
								<? } else { ?>
									<?foreach(wp_get_post_tags(get_the_ID()) as $tag) { ?>
									<li><?=$tag->name?></li>
									<? } ?>
								<? } ?>
							</ul>
							<div class="blog_teaser__autors">
								<?=get_avatar(get_the_author_meta('ID')); ?>
								<span><?=get_the_author_meta('display_name')?></span>
							</div>
						</div>
						<div class="blog_article__meta">
							<div class="blog_article__stat">
								<div class="blog_article__stat_item">
									<img src="/img/blog_stat__view.svg">
									<span><?=get_post_meta(get_the_ID(), 'post_view')[0]?></span>
								</div>
								<?print_likes_button(get_the_ID())?>
								<?print_sharings_button(get_the_ID())?>
								<div class="blog_article__stat_item">
									<img src="/img/blog_stat__favorite.svg">
									<?$rat = get_post_meta(get_the_ID(), 'rmp_avg_rating')[0]?>
									<span><?=$rat ? $rat : "0"?></span>
								</div>
								<div class="blog_article__stat_item">
									<img src="/img/blog_stat__time_read.svg">
									<span>Читать <?=get_field('read_time')?> мин.</span>
								</div>
							</div>

						</div>
					</div>
				</div>
			</div>
		</div>

		<div class="blog_article__header_img">
			<img src="<?=get_field('big_pic')['url']?>">
		</div>

	</header>

	<main id="SecondScreen">
		<div class="container">
			<div class="row">

				<!-- --- -->

				<div class="blog_article__wrap">
					<div class="blog_article__content">
						<?if(get_field('short_desc')) { ?>
							<div class="short_desc"><?=get_field('short_desc')?><hr></div>
						<? } ?>
						<? the_content() ?>
					</div>
					<?if(get_field('content_table') || $cat) { ?>
					<div class="blog_article__sidebar">
						<?if($cat) { ?>
							<div class="blog_article__sidebar_title">Разделы блога</div>
							<ul>
								<?foreach(get_categories(array('hide_empty' => false, 'orderby' => 'none')) as $category) { ?>
									<li><a href="<?=get_category_link($category->term_id)?>"><?=$category->name?></a></li>
								<? } ?>
							</ul>
						<? } ?>
						<?if(get_field('content_table')) { ?>
							<div class="blog_article__sidebar_title">Содержание</div>
						<? } ?>
						<?=get_field('content_table')?>
					</div>
					<? } ?>
				</div>

				<div class="blog_article__info">

					<div class="blog_article__stat">
						<div class="blog_article__stat_item">
							<img src="/img/blog_stat__view.svg">
							<span><?=do_shortcode('[ngd-single-post-view]')?></span>
						</div>
						<?print_likes_button(get_the_ID())?>
						<?print_sharings_button(get_the_ID())?>
						<div class="blog_article__stat_item">
							<img src="/img/blog_stat__favorite.svg">
							<span><?=do_shortcode('[ratemypost-result id="' . get_the_ID() . '"]')?></span>
						</div>
					</div>

					<div class="blog_article__autor_rate">
						<div class="blog_article__autor">
							<?=get_avatar(get_the_author_meta('ID'), 150, '', get_the_author_meta('display_name')); ?>
							<div class="blog_article__autor_name">
								<div><?=get_the_author_meta('display_name')?></div>
								<span>Автор статьи</span>
							</div>
						</div>
						<div class="blog_article__rate_wrap">
							<?=do_shortcode('[ratemypost]')?>
						</div>
					</div>

				</div>
				<?if(get_field('references')) { ?>
				<div class="blog_article__links">
					<div class="blog_article__links_title">Материалы:</div>
					<ul>
						<?foreach(get_field('references') as $refer) { ?>
						<li><a href="<?=$refer['link']?>"><?=$refer['text']?></a></li>
						<? } ?>
					</ul>
				</div>
				<? } ?>

				<!-- --- -->

				<?
				$posts = get_posts( array(
					'author' => get_the_author_meta('ID'),
				    'posts_per_page'    => 8,
				    'post_type'     => 'post',
				    'exclude' => array(get_the_ID()),
		            'order'     => 'DESC',
		            'meta_key' => 'post_view',
		            'orderby'   => 'meta_value',
				));
				?>
				<!-- --- -->

				<?if(!$cat) { ?>
				<?if (count($posts)) { ?>
				<div class="content_block">
					<div class="content_block__title">
						<h2>Популярные статьи автора</h2>
					</div>

					<div class="blog_teaser owl-carousel owl-theme" id="blog_autors_articles">

				<?
				foreach( $posts as $post ) {
				?>

						<div class="blog_teaser_block">
							<a href="<?php the_permalink(); ?>" class="inner">

								<div class="inner_top">
									<div class="blog_teaser__img" style="background-image:url(<?=get_the_post_thumbnail_url()?>)"></div>
									<div class="blog_teaser__date"><?=mb_strtolower(get_the_date('d M Y, h:i'))?></div>
									<div class="blog_teaser__name"><?php the_title(); ?></div>
								</div>

								<div class="inner_bottom">
									<ul class="blog_teaser__tags">
										<?foreach(wp_get_post_tags(get_the_ID()) as $tag) { ?>
										<li><?=$tag->name?></li>
										<? } ?>
									</ul>
									<div class="blog_teaser__autors">
										<?=get_avatar(get_the_author_meta('ID')); ?>
										<span><?=get_the_author_meta('display_name')?></span>
									</div>
								</div>

							</a>
							<div class="blog_teaser_article__stat">
								<div class="blog_teaser_article__stat_item">
									<img src="/img/blog_stat__view.svg">
									<?$view = get_post_meta(get_the_ID(), 'post_view')[0]?>
									<span><?=$view ? $view : "0"?></span>
								</div>
								<?print_likes_button(get_the_ID())?>
								<?print_sharings_button(get_the_ID())?>
								<div class="blog_teaser_article__stat_item">
									<img src="/img/blog_stat__favorite.svg">
									<?$rat = get_post_meta(get_the_ID(), 'rmp_avg_rating')[0]?>
									<span><?=$rat ? $rat : "0"?></span>
								</div>
							</div>
						</div>

					<? } ?>

					</div>

				</div>
				<? } ?>

				<? } else { ?>

				<div class="content_block">
					<div class="content_block__title">
						<h2>Отзывы</h2>
					</div>
					<?include_once get_template_directory() . "/template-parts/content-reviews.php";?>
										
				</div>

				<div class="content_block">
					<div class="content_block__title">
						<h2>Рекомендации</h2>
					</div>
					<?include_once get_template_directory() . "/template-parts/content-recomendations.php";?>
				</div>


				<div class="content_block">
					<div class="content_block__title">
						<h2>Наши кейсы</h2>
						<div>04</div>
					</div>
					<? switch ($cat->term_id) {
						    case 24:
								include_once get_template_directory() . "/template-parts/cases-context.php";
						        break;
						    case 26:
								include_once get_template_directory() . "/template-parts/cases-develop.php";
						        break;
						    case 27:
								include_once get_template_directory() . "/template-parts/cases-geo.php";
						        break;
						    default: 
								include_once get_template_directory() . "/template-parts/cases-seo.php";
						}						
					?>
				</div>


				<div class="content_block">
					<div class="content_block__title">
						<h2>Тарифы</h2>
					</div>
					<?	$tariff = array("value" => 1);
						switch ($cat->term_id) {
						    case 24:
						        $way = 1;
						        break;
						    case 26:
						        $way = 2;
						        break;
						    case 27:
						        $way = 3;
						        break;
						    default:
					        $way = 0;
						}						
						$need_tarif_buttons = true;
						include_once get_template_directory() . "/template-parts/content-tarifs-main.php"; ?>
				</div>

				<!-- --- -->

				<? } ?>


<?php
get_footer();
