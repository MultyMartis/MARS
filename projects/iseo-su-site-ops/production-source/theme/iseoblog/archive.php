<?php
/*
Template Name: Рубрика
*/

get_header();
$categories = get_the_category();
$categoryID = 1;
foreach($categories as $category) {
	if($category->term_id != 1) {
		$categoryID = $category->term_id;
		break;
	}
}
$categoryName = get_cat_name($categoryID);
?>
		<div class="our_blog">
			<div class="container">
				<div class="row">
					<div class="our_blog_inner">
						<div class="our_blog__description">
							<ul class="breadcrumbs">
								<li><a href="/">Главная</a></li>
								<li><a href="/blog">Блог</a></li>
								<li><?=$categoryName?></li>
							</ul>
							<h1><?=$categoryName?></h1>
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
					'category' 		=> $categoryID,
		            'orderby'     => 'date',
		            'order'     => 'DESC',
				));
				$firstPostID = $posts[0]->ID;
?>              
				<? foreach( $posts as $post) { ?>
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
									<h2 class="our_blog__first_article__title">
										<a href="<?php the_permalink(); ?>"><?the_title()?></a>
									</h2>
									<div class="our_blog__first_article__autors">
										<?=get_avatar($post->post_author); ?>
										<span><?=get_the_author_meta('display_name', $post->post_author)?></span>
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
				<? } ?>
				<!-- --- -->



				<!-- --- -->

				<div class="blog_filter">

<?
				$category_posts = get_posts([
			        'category'   => $categoryID,
			        'numberposts' => -1,
					'fields'     => 'ids',
			    ]);


			    $all_tags = array();
			    foreach ($category_posts as $post_id) {
			        $post_tags = wp_get_post_tags($post_id);
			        foreach ($post_tags as $tag) {
			            $tag_id = $tag->term_id;
			            if (!isset($all_tags[$tag_id])) {
							$entry = new stdClass();
							$entry->term_id = $tag->term_id;
			                $entry->name = $tag->name;
			                $entry->slug = $tag->slug;
			                $entry->count = 0;
			                $all_tags[$tag_id] = $entry;
			            }
			            $all_tags[$tag_id]->count++;
			        }
			    }





				$args = array(
				    'posts_per_page'    => -1,
					'category' 		=> $categoryID,
				    'post_type'     => 'post',
				);
				$posts = get_posts($args);

				$all_posts = count($posts);
				if($all_posts < 0) {
					$all_posts = 0;
				}				

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
						<div class="blog_teaser_block<?=($tCount > 11) ? " hidden" : ""?>">
							<a href="<?php the_permalink(); ?>" class="inner">

								<div class="inner_top">
									<div class="blog_teaser__img" style="background-image:url(<?=get_the_post_thumbnail_url()?>)"></div>
									<div class="blog_teaser__date"><?=mb_strtolower(get_the_date('d M Y, h:i'))?></div>
									<h2 class="blog_teaser__name"><?php the_title(); ?></h2>
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
