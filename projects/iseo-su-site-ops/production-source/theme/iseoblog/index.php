<?php
/**
 * The main template file
 *
 * This is the most generic template file in a WordPress theme
 * and one of the two required files for a theme (the other being style.css).
 * It is used to display a page when nothing more specific matches a query.
 * E.g., it puts together the home page when no home.php file exists.
 *
 * @link https://developer.wordpress.org/themes/basics/template-hierarchy/
 *
 * @package iseoblog
 */

get_header();

?>
		<div class="our_blog">
			<div class="container">
				<div class="row">
					<div class="our_blog_inner">
						<div class="our_blog__description">
							<ul class="breadcrumbs">
								<li><a href="/">Главная</a></li>
								<li>Блог</li>
							</ul>
							<h1>Блог</h1>
						</div>
						<div class="our_blog__subscribe_btn">
							<a href="https://t.me/DMarketingIseo" target="_blank">Подписаться</a>
						</div>
					</div>
				</div>
			</div>
		</div>

	</header>

	<main id="SecondScreen">
		<div class="container">
			<div class="row">

				<!-- --- -->
<?
				$posts = get_posts( array(
				    'posts_per_page'    => 1,
				    'post_type'     => 'post',
		            'orderby'     => 'date',
		            'order'     => 'DESC',
				));
				$firstPostID = $posts[0]->ID;
?>
				<div class="our_blog__first_article">

					<div class="our_blog__first_article__wrap">
						<div class="our_blog__first_article__img">
							<a href="<?php the_permalink(); ?>">
								<img src="<?=get_the_post_thumbnail_url()?>" alt="<?php the_title(); ?>">
							</a>
						</div>
						<div class="our_blog__first_article__info">
							<div>

								<div class="our_blog__first_article__descr">
									<div class="our_blog__first_article__meta">
										<span><?=mb_strtolower(get_the_date('d M Y, h:i'))?></span>
										<ul>
											<?foreach(wp_get_post_tags(get_the_ID()) as $tag) { ?>
											<li><?=$tag->name?></li>
											<? } ?>
										</ul>
									</div>
									<div class="our_blog__first_article__title">
										<a href="<?php the_permalink(); ?>"><?the_title()?></a>
									</div>
									<div class="our_blog__first_article__autors">
										<?=get_avatar(get_the_author_meta('ID')); ?>
										<span><?=get_the_author_meta('display_name')?></span>
									</div>
								</div>

								<div class="our_blog__first_article__stat">
									<div>
										<div class="our_blog__first_article__stat_item">
											<img src="/img/blog_stat__view.svg">
											<?$view = get_post_meta(get_the_ID(), 'post_view')[0]?>
											<span><?=$view ? $view : "0"?></span>
										</div>
										<?print_likes_button(get_the_ID())?>
										<?print_sharings_button(get_the_ID())?>
										<div class="our_blog__first_article__stat_item">
											<img src="/img/blog_stat__favorite.svg">
											<?$rat = get_post_meta(get_the_ID(), 'rmp_avg_rating')[0]?>
											<span><?=$rat ? $rat : "0"?></span>
										</div>
									</div>
								</div>

							</div>
						</div>
					</div>

				</div>

				<!-- --- -->



				<!-- --- -->

				<div class="blog_filter">

<?

				$args = array(
				    'posts_per_page'    => -1,
				    'post_type'     => 'post',
				);
				$posts = get_posts($args);

				$all_posts = count($posts) - 1;
				if($all_posts < 0) {
					$all_posts = 0;
				}				

				$all_tags = get_tags();

				if($_GET['tags']) {
					$args['tag'] = $_GET['tags'];
				} else {
					$args['exclude'] = array($firstPostID);
				}

				if($_GET['sort'] == 'date-desc') {
					$args['orderby'] = 'date';
					$args['order'] = 'DESC';
				}
				if($_GET['sort'] == 'date-asc') {
					$args['orderby'] = 'date';
					$args['order'] = 'ASC';
				}
				if($_GET['sort'] == 'popular-desc') {
					$args['orderby'] = 'meta_value';
					$args['meta_key'] = 'post_view';
					$args['order'] = 'DESC';
				}
				if($_GET['sort'] == 'popular-asc') {
					$args['orderby'] = 'meta_value';
					$args['meta_key'] = 'post_view';
					$args['order'] = 'ASC';
				}
				if($_GET['sort'] == 'rating-desc') {
					$args['orderby'] = 'meta_value';
					$args['order'] = 'DESC';
					$args['meta_query'] = array(
				        'relation' => 'OR',
				        array(
				            'key' => 'rmp_avg_rating',
				            'compare' => 'NOT EXISTS',
				        ),
				        array(
				            'key' => 'rmp_avg_rating',
				            'compare' => 'EXISTS',
					        )
					 );
				}
				if($_GET['sort'] == 'rating-asc') {
					$args['orderby'] = 'meta_value';
					$args['order'] = 'ASC';
					$args['meta_query'] = array(
				        'relation' => 'OR',
				        array(
				            'key' => 'rmp_avg_rating',
				            'compare' => 'NOT EXISTS',
				        ),
				        array(
				            'key' => 'rmp_avg_rating',
				            'compare' => 'EXISTS',
					        )
					 );
				}
				$posts = get_posts($args);

?>
					<div class="blog_filter__navigations">
						<div class="blog_filter__label">
							<div>Теги:</div>
						</div>
						<div class="blog_filter__item<?=(!$_GET['tags']) ? " active" : ""?>">
							<a class="blog_filter__btn current" href="/blog<?=($_GET['sort']) ? '?sort=' . $_GET['sort'] : ""?>">
								<div>Все</div>
								<span>(<?=$all_posts?>)</span>
							</a>
						</div>
					<?	$tagCount = 0;
						foreach( $all_tags as $tag) { 
							printTagsItem($tag, $tagCount);
							$tagCount++; 
						} ?>

						<?if($tagCount > 6) { ?>
						<div class="blog_filter__more">
							<a href="#">
								<div class="blog_filter__label">Развернуть все</div>
								<span></span>
							</a>
						</div>
						<? } ?>
					</div>


					<div class="blog_filter__sort">
						<div class="blog_filter_sort__label">
							<div>Сортировать по:</div>
						</div>
						<div class="blog_filter_sort__item">
							<?printSortItem("По дате", "date")?>
						</div>
						<div class="blog_filter_sort__item">
							<?printSortItem("По популярности", "popular")?>
						</div>
						<div class="blog_filter_sort__item">
							<?printSortItem("По рейтингу", "rating")?>
						</div>

					</div>




					<div class="blog_teaser grid" id="blog_teaser_grid">

<?
				$tCount = 0;
				foreach( $posts as $post ) {

?>
						<div class="blog_teaser_block<?=($tCount > 3) ? " hidden" : ""?>">
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
										<?=get_avatar($post->post_author); ?>
										<span><?=get_the_author_meta('display_name', $post->post_author)?></span>
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

					<? $tCount++;
   					} ?>

					</div>
					<? if(count($posts) > 4) { ?>
						<a href="javascript:void(0);" class="to_parent_page see_more">Показать еще</a>
					<? } ?>






				</div>

				<!-- --- -->



<?php
get_footer();
