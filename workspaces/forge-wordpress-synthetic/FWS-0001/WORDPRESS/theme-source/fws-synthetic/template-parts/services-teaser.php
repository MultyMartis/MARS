<?php
/**
 * Services teaser section (front page).
 *
 * @package FWS_Synthetic
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$query = new WP_Query(
	array(
		'post_type'      => 'service',
		'posts_per_page' => 3,
		'orderby'        => 'menu_order',
		'order'          => 'ASC',
		'no_found_rows'  => true,
	)
);
?>
<section class="services-teaser">
	<div class="container">
		<h2 class="section-title"><?php esc_html_e( 'Тестовые услуги', 'fws-synthetic' ); ?></h2>
		<div class="services-grid">
			<?php if ( $query->have_posts() ) : ?>
				<?php
				while ( $query->have_posts() ) :
					$query->the_post();
					get_template_part(
						'template-parts/service-card',
						null,
						array(
							'title' => get_the_title(),
							'text'  => fws_get_service_excerpt( get_the_ID() ),
							'url'   => get_permalink(),
						)
					);
				endwhile;
				wp_reset_postdata();
				?>
			<?php else : ?>
				<?php
				$fallback = array(
					array(
						'title' => __( 'Тестовая услуга A', 'fws-synthetic' ),
						'text'  => __( 'Синтетическое описание для карточки услуги.', 'fws-synthetic' ),
					),
					array(
						'title' => __( 'Тестовая услуга B', 'fws-synthetic' ),
						'text'  => __( 'Демонстрационный проект без клиентского брендинга.', 'fws-synthetic' ),
					),
					array(
						'title' => __( 'Тестовая услуга C', 'fws-synthetic' ),
						'text'  => __( 'Контент для проверки responsive output.', 'fws-synthetic' ),
					),
				);
				foreach ( $fallback as $item ) :
					get_template_part(
						'template-parts/service-card',
						null,
						array(
							'title' => $item['title'],
							'text'  => $item['text'],
							'url'   => fws_get_services_url(),
						)
					);
				endforeach;
				?>
			<?php endif; ?>
		</div>
		<a class="btn btn--ghost services-teaser__more" href="<?php echo esc_url( fws_get_services_url() ); ?>">
			<?php esc_html_e( 'Все услуги', 'fws-synthetic' ); ?>
		</a>
	</div>
</section>
