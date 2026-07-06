<?php
/**
 * Template part: service/team-stats.php
 *
 * Static V9 fallback for service subdivision team/approach block.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$program_url = home_url( '/o-centre/programma-lecheniya/' );
?>
<section data-reveal class="service-subdivision-team-stats-v1" id="service-subdivision-approach" aria-labelledby="service-subdivision-approach-heading">
	<div class="container service-subdivision-team-stats-v1__container">
		<div class="service-subdivision-team-stats-v1__corridor-bleed">
			<img
				class="service-subdivision-team-stats-v1__corridor-image"
				src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/rehabilitation-requirements/shpigovsky-interior-corridor.webp' ) ); ?>"
				width="2187"
				height="1231"
				alt="<?php echo esc_attr__( 'Интерьер клиники — коридор с картинами', 'shpigovsky' ); ?>"
				loading="lazy"
				decoding="async"
			>
		</div>

		<div class="service-subdivision-team-stats-v1__head">
			<h2 class="service-subdivision-team-stats-v1__heading" id="service-subdivision-approach-heading"><?php echo esc_html__( 'Наш подход к лечению зависимостей', 'shpigovsky' ); ?></h2>
			<a class="home-rehabilitation-program__all-link service-subdivision-team-stats-v1__all-link" href="<?php echo esc_url( $program_url ); ?>">
				<span class="home-rehabilitation-program__all-text"><?php echo esc_html__( 'подробнее', 'shpigovsky' ); ?></span>
				<span class="home-rehabilitation-program__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
			</a>
		</div>

		<p class="service-subdivision-team-stats-v1__highlight block-whith-red-line">
			<?php echo esc_html__( 'Мы используем мультидисциплинарный подход — когда лечение одного пациента обеспечивается командой специалистов разных профилей.', 'shpigovsky' ); ?>
		</p>

		<p class="service-subdivision-team-stats-v1__intro">
			<?php echo esc_html__( 'Лечение в нашем реабилитационном центре совмещает современный и мультидисциплинарный подход, направленный на устранение истинных причин зависимости.', 'shpigovsky' ); ?>
		</p>

		<div class="service-subdivision-team-stats-v1__staff-bleed">
			<img
				class="service-subdivision-team-stats-v1__staff-image"
				src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/pre-reviews/shpigovsky-staff-group.webp' ) ); ?>"
				width="1139"
				height="443"
				alt="<?php echo esc_attr__( 'Команда специалистов реабилитационного центра', 'shpigovsky' ); ?>"
				loading="lazy"
				decoding="async"
			>
		</div>

		<ul class="home-feature-grid__card-grid service-subdivision-team-stats-v1__approach-cards">
			<li class="home-feature-grid__card service-subdivision-team-stats-v1__approach-card">
				<h3 class="home-feature-grid__card-title"><?php echo esc_html__( 'диагностические инструменты', 'shpigovsky' ); ?></h3>
				<p class="home-feature-grid__card-text"><?php echo esc_html__( 'Комплексная оценка состояния помогает увидеть картину целиком и выбрать точки воздействия.', 'shpigovsky' ); ?></p>
			</li>
			<li class="home-feature-grid__card service-subdivision-team-stats-v1__approach-card">
				<h3 class="home-feature-grid__card-title"><?php echo esc_html__( 'психиатрия', 'shpigovsky' ); ?></h3>
				<p class="home-feature-grid__card-text"><?php echo esc_html__( 'Медикаментозная и клиническая поддержка при сопутствующих расстройствах и острых состояниях.', 'shpigovsky' ); ?></p>
			</li>
			<li class="home-feature-grid__card service-subdivision-team-stats-v1__approach-card">
				<h3 class="home-feature-grid__card-title"><?php echo esc_html__( 'функциональная терапия', 'shpigovsky' ); ?></h3>
				<p class="home-feature-grid__card-text"><?php echo esc_html__( 'Восстановление телесных ресурсов и режима как часть устойчивой ремиссии.', 'shpigovsky' ); ?></p>
			</li>
			<li class="home-feature-grid__card service-subdivision-team-stats-v1__approach-card">
				<h3 class="home-feature-grid__card-title"><?php echo esc_html__( 'комплементарная терапия', 'shpigovsky' ); ?></h3>
				<p class="home-feature-grid__card-text"><?php echo esc_html__( 'Дополнительные методы, усиливающие основную программу и снижающие риск срыва.', 'shpigovsky' ); ?></p>
			</li>
		</ul>
	</div>
</section>
