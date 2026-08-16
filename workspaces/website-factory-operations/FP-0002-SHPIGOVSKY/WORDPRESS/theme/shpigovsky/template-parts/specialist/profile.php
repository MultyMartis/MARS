<?php
/**
 * Template part: specialist/profile.php — PROD-P08 structured specialist page.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$page_id = (int) get_the_ID();
$profile = function_exists( 'shpigovsky_get_specialist_profile' )
	? shpigovsky_get_specialist_profile( $page_id )
	: array();

$name            = isset( $profile['name'] ) ? (string) $profile['name'] : get_the_title( $page_id );
$role            = isset( $profile['role'] ) ? (string) $profile['role'] : '';
$experience      = isset( $profile['experience'] ) ? (string) $profile['experience'] : '';
$specialty       = isset( $profile['specialty'] ) ? (string) $profile['specialty'] : '';
$education       = isset( $profile['education'] ) ? (string) $profile['education'] : '';
$specialization  = isset( $profile['specialization'] ) ? (string) $profile['specialization'] : '';
$principles      = isset( $profile['principles'] ) ? (string) $profile['principles'] : '';
$additional      = isset( $profile['additional'] ) ? (string) $profile['additional'] : '';
$certificates    = isset( $profile['certificates'] ) && is_array( $profile['certificates'] ) ? $profile['certificates'] : array();
$portrait_url    = isset( $profile['portrait_url'] ) ? (string) $profile['portrait_url'] : '';
$portrait_width  = isset( $profile['portrait_width'] ) ? (int) $profile['portrait_width'] : 640;
$portrait_height = isset( $profile['portrait_height'] ) ? (int) $profile['portrait_height'] : 640;
$portrait_alt    = isset( $profile['portrait_alt'] ) ? (string) $profile['portrait_alt'] : $name;

$sections = array(
	array(
		'key'   => 'specialty',
		'title' => __( 'Специальность', 'shpigovsky' ),
		'html'  => $specialty,
	),
	array(
		'key'   => 'education',
		'title' => __( 'Образование', 'shpigovsky' ),
		'html'  => $education,
	),
	array(
		'key'   => 'specialization',
		'title' => __( 'Специализация', 'shpigovsky' ),
		'html'  => $specialization,
	),
	array(
		'key'   => 'principles',
		'title' => __( 'Принципы / подход к работе', 'shpigovsky' ),
		'html'  => $principles,
	),
	array(
		'key'   => 'additional',
		'title' => __( 'Дополнительная информация', 'shpigovsky' ),
		'html'  => $additional,
	),
);

$gallery_id = 'specialist-certs-' . $page_id;
?>
<section class="specialist-profile" data-content-status="specialist-structured">
	<div class="container specialist-profile__container">
		<div class="specialist-profile__identity">
			<?php if ( '' !== $portrait_url ) : ?>
			<figure class="specialist-profile__portrait">
				<img
					class="specialist-profile__portrait-img"
					src="<?php echo esc_url( $portrait_url ); ?>"
					width="<?php echo esc_attr( (string) $portrait_width ); ?>"
					height="<?php echo esc_attr( (string) $portrait_height ); ?>"
					alt="<?php echo esc_attr( $portrait_alt ); ?>"
					loading="eager"
					decoding="async"
				>
			</figure>
			<?php endif; ?>
			<div class="specialist-profile__identity-main">
				<h1 class="specialist-profile__name"><?php echo esc_html( $name ); ?></h1>
				<?php if ( '' !== $role ) : ?>
				<p class="specialist-profile__role"><?php echo esc_html( $role ); ?></p>
				<?php endif; ?>
				<?php if ( '' !== $experience ) : ?>
				<p class="specialist-profile__experience"><?php echo esc_html( $experience ); ?></p>
				<?php endif; ?>
			</div>
		</div>

		<?php foreach ( $sections as $section ) : ?>
			<?php
			$html = trim( (string) $section['html'] );
			if ( '' === $html ) {
				continue;
			}
			?>
		<section class="specialist-profile__block specialist-profile__block--<?php echo esc_attr( $section['key'] ); ?>">
			<h2 class="specialist-profile__block-title"><?php echo esc_html( $section['title'] ); ?></h2>
			<div class="specialist-profile__block-body">
				<?php echo apply_filters( 'the_content', $html ); // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped -- WP content filters. ?>
			</div>
		</section>
		<?php endforeach; ?>

		<?php if ( ! empty( $certificates ) ) : ?>
		<section class="specialist-profile__certificates" aria-labelledby="specialist-certs-heading-<?php echo esc_attr( (string) $page_id ); ?>">
			<h2 class="specialist-profile__block-title" id="specialist-certs-heading-<?php echo esc_attr( (string) $page_id ); ?>">
				<?php echo esc_html__( 'Сертификаты и дипломы', 'shpigovsky' ); ?>
			</h2>
			<ul class="specialist-profile__certs-grid">
				<?php foreach ( $certificates as $img ) : ?>
					<?php
					if ( ! is_array( $img ) ) {
						continue;
					}
					$url = isset( $img['url'] ) ? (string) $img['url'] : '';
					if ( '' === $url && ! empty( $img['ID'] ) ) {
						$url = (string) wp_get_attachment_url( (int) $img['ID'] );
					}
					if ( '' === $url ) {
						continue;
					}
					$full = $url;
					if ( ! empty( $img['ID'] ) ) {
						$full_src = wp_get_attachment_image_src( (int) $img['ID'], 'full' );
						if ( is_array( $full_src ) && ! empty( $full_src[0] ) ) {
							$full = (string) $full_src[0];
						}
					}
					$alt = isset( $img['alt'] ) ? trim( (string) $img['alt'] ) : '';
					if ( '' === $alt ) {
						$alt = __( 'Сертификат / диплом', 'shpigovsky' );
					}
					$thumb = isset( $img['sizes']['medium'] ) ? (string) $img['sizes']['medium'] : $url;
					?>
				<li class="specialist-profile__cert-item">
					<a
						class="specialist-profile__cert-link"
						href="<?php echo esc_url( $full ); ?>"
						data-fancybox="<?php echo esc_attr( $gallery_id ); ?>"
						data-caption="<?php echo esc_attr( $alt ); ?>"
					>
						<img
							class="specialist-profile__cert-img"
							src="<?php echo esc_url( $thumb ); ?>"
							alt="<?php echo esc_attr( $alt ); ?>"
							loading="lazy"
							decoding="async"
						>
					</a>
				</li>
				<?php endforeach; ?>
			</ul>
		</section>
		<?php endif; ?>
	</div>
</section>
