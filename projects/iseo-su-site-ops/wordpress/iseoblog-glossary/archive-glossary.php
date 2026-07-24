<?php
/**
 * Glossary archive template.
 * Reuses internal-page structure from privacy-policy / content pages:
 * page_scene + breadcrumbs + content_block + blog_filter alphabet nav.
 * Letter groups use plain h2 inside content_block (privacy pattern), not
 * content_block__title (oversized section chrome).
 *
 * @package iseoblog
 */

get_header();

$search_q    = iseo_glossary_search_query();
$posts       = iseo_glossary_get_archive_posts();
$posts       = iseo_glossary_filter_posts( $posts, $search_q );
$groups      = iseo_glossary_group_posts_by_letter( $posts );
$archive_url = get_post_type_archive_link( 'glossary' );
?>

		<div class="page_scene">
			<div class="container">
				<div class="row">
					<div class="page_scene_inner">
						<div class="page_scene__description">
							<ul class="breadcrumbs">
								<li><a href="/">Главная</a></li>
								<li>Глоссарий</li>
							</ul>
							<h1>Глоссарий</h1>
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

				<div class="content_block">
					<p>Словарь терминов SEO и digital-маркетинга. Краткие определения публикуются по мере редакционной подготовки; полный разбор — на странице термина.</p>
					<?php if ( ! iseo_glossary_is_publicly_exposed() && current_user_can( 'edit_posts' ) ) : ?>
						<p>Служебный предпросмотр: публичная индексация отключена, меню и sitemap не подключены.</p>
					<?php endif; ?>

					<form method="get" action="<?php echo esc_url( $archive_url ); ?>">
						<p>
							<label for="glossary_q">Поиск по терминам</label><br />
							<input type="text" name="glossary_q" id="glossary_q" value="<?php echo esc_attr( $search_q ); ?>" placeholder="Начните вводить термин" />
						</p>
						<p>
							<button type="submit">Найти</button>
							<?php if ( $search_q ) : ?>
								<a href="<?php echo esc_url( $archive_url ); ?>">Сбросить</a>
							<?php endif; ?>
						</p>
					</form>
				</div>

				<?php if ( empty( $groups ) ) : ?>
					<div class="content_block">
						<p><?php echo $search_q ? 'По запросу ничего не найдено.' : 'Термины пока не добавлены.'; ?></p>
					</div>
				<?php else : ?>

					<div class="content_block">
						<div class="blog_filter">
							<div class="blog_filter__navigations">
								<div class="blog_filter__label">
									<div>Алфавит:</div>
								</div>
								<?php foreach ( $groups as $letter => $items ) : ?>
									<?php if ( empty( $items ) ) : ?>
										<?php continue; ?>
									<?php endif; ?>
									<div class="blog_filter__item">
										<a class="blog_filter__btn" href="#<?php echo esc_attr( iseo_glossary_letter_anchor( $letter ) ); ?>">
											<div><?php echo esc_html( iseo_glossary_letter_label( $letter ) ); ?></div>
											<span>(<?php echo esc_html( (string) count( $items ) ); ?>)</span>
										</a>
									</div>
								<?php endforeach; ?>
							</div>
						</div>
					</div>

					<?php foreach ( $groups as $letter => $items ) : ?>
						<?php if ( empty( $items ) ) : ?>
							<?php continue; ?>
						<?php endif; ?>
						<div class="content_block" id="<?php echo esc_attr( iseo_glossary_letter_anchor( $letter ) ); ?>">
							<h2><?php echo esc_html( iseo_glossary_letter_label( $letter ) ); ?></h2>
							<ul>
								<?php foreach ( $items as $term_post ) : ?>
									<?php
									$title = iseo_glossary_term_title( $term_post );
									if ( '' === $title ) {
										continue;
									}
									$url = iseo_glossary_term_list_url( $term_post );
									?>
									<li>
										<?php if ( $url ) : ?>
											<a href="<?php echo esc_url( $url ); ?>"><?php echo esc_html( $title ); ?></a>
										<?php else : ?>
											<?php echo esc_html( $title ); ?>
										<?php endif; ?>
										<?php
										$excerpt = trim( (string) $term_post->post_excerpt );
										if ( $excerpt ) :
											?>
											— <?php echo esc_html( $excerpt ); ?>
										<?php endif; ?>
									</li>
								<?php endforeach; ?>
							</ul>
						</div>
					<?php endforeach; ?>

				<?php endif; ?>

<?php
get_footer();
