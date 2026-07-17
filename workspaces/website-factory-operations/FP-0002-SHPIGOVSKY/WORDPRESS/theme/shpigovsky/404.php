<?php
/**
 * 404 template — Figma PG-011 / frames `404` + `404 - моб`.
 *
 * Authority: INCOMING/01_DESIGN/26.06.2026 PNG pair (Spig_v1.2.fig).
 * Decor asset (V9-06E62E): INCOMING/OPERATOR-ASSETS/404/404-decor.png
 * Uses the global site shell (header / floating header / footer / lifebuoy).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

get_header();

$visual_uri = function_exists( 'shpigovsky_asset_uri' )
	? shpigovsky_asset_uri( 'img/404/404-decor.png' )
	: get_template_directory_uri() . '/assets/img/404/404-decor.png';
$logo_uri   = function_exists( 'shpigovsky_asset_uri' )
	? shpigovsky_asset_uri( 'img/branding/logo.svg' )
	: get_template_directory_uri() . '/assets/img/branding/logo.svg';
?>
<main class="page-404" id="main-content">
	<section class="page-404__content" aria-labelledby="page-404-title">
		<div class="container page-404__container">
			<h1 class="page-404__title" id="page-404-title"><?php esc_html_e( 'Мы не смогли найти эту страницу…', 'shpigovsky' ); ?></h1>
			<p class="page-404__lead"><?php esc_html_e( 'Но мы можем найти и устранить причины вашей зависимости', 'shpigovsky' ); ?></p>

			<div class="page-404__brand">
				<img
					class="page-404__logo"
					src="<?php echo esc_url( $logo_uri ); ?>"
					alt="<?php echo esc_attr__( 'Дом Шпиговский — центр профилактики зависимостей', 'shpigovsky' ); ?>"
					width="220"
					height="72"
					decoding="async"
				>
			</div>

			<p class="page-404__actions">
				<a class="btn btn_dark btn--primary page-404__home-link" href="<?php echo esc_url( home_url( '/' ) ); ?>">
					<span class="page-404__home-label page-404__home-label--desktop"><?php esc_html_e( 'Вернуться на главную', 'shpigovsky' ); ?></span>
					<span class="page-404__home-label page-404__home-label--mobile"><?php esc_html_e( 'На главную', 'shpigovsky' ); ?></span>
				</a>
			</p>

			<figure class="page-404__visual" aria-hidden="true">
				<img
					class="page-404__visual-img"
					src="<?php echo esc_url( $visual_uri ); ?>"
					alt=""
					width="670"
					height="425"
					decoding="async"
					role="presentation"
				>
			</figure>
		</div>
	</section>
</main>
<?php
get_footer();
