<?php
/**
 * Template part: service/stages.php
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$post_id = shpigovsky_get_current_service_id();
$stages  = shpigovsky_get_service_repeater( $post_id, 'stages' );
$variant = get_query_var( 'shpigovsky_service_layout_variant', shpigovsky_get_service_layout_variant() );
$cta     = shpigovsky_get_service_cta_band( $post_id );

if ( 'subdivision' === $variant ) {
	$section_id = 'service-subdivision-stages';
	$heading_id = 'service-subdivision-stages-heading';
	$section_class = 'service-subdivision-stages-v1';
	$steps_class   = 'service-subdivision-stages-v1__steps';
	$cta_wrap      = 'service-subdivision-stages-v1__cta';
	$support_wrap  = 'service-subdivision-stages-v1__support';
} else {
	$section_id = 'service-leaf-start';
	$heading_id = $section_id . '-heading';
	$section_class = 'service-leaf-stages-v1';
	$steps_class   = 'service-leaf-stages-v1__steps';
	$cta_wrap      = 'service-leaf-stages-v1__cta';
	$support_wrap  = '';
}

if ( empty( $stages ) && 'subdivision' !== $variant ) {
	return;
}

if ( empty( $stages ) && 'subdivision' === $variant ) {
	$stages = array(
		array(
			'title' => __( 'Связаться с нами', 'shpigovsky' ),
			'text'  => __( 'Расскажите нам о своей ситуации — в удобном для вас формате и в удобное время. Первый разговор ни к чему не обязывает, но часто становится началом перемен.', 'shpigovsky' ),
		),
		array(
			'title' => __( 'Определить цели и программу', 'shpigovsky' ),
			'text'  => __( 'Вместе со специалистами центра мы разберёмся, что именно происходит, и составим программу, которая отвечает вашей ситуации.', 'shpigovsky' ),
		),
		array(
			'title' => __( 'Выбрать категорию номера, период стационарного проживания', 'shpigovsky' ),
			'text'  => __( 'Комфорт среды — часть восстановления. Мы подберём условия проживания, которые подойдут именно вам, и согласуем удобные сроки.', 'shpigovsky' ),
		),
		array(
			'title' => __( 'Начать реабилитацию и лечение', 'shpigovsky' ),
			'text'  => __( 'С первого дня рядом с вами будет команда специалистов. Здесь начинается то, ради чего вы пришли.', 'shpigovsky' ),
		),
	);
}
?>
<section data-reveal class="<?php echo esc_attr( $section_class ); ?>" id="<?php echo esc_attr( $section_id ); ?>" aria-labelledby="<?php echo esc_attr( $heading_id ); ?>">
	<div class="container <?php echo esc_attr( $section_class ); ?>__container">
		<h2 class="<?php echo esc_attr( $section_class ); ?>__heading" id="<?php echo esc_attr( $heading_id ); ?>">
			<?php echo esc_html__( 'Что нужно для прохождения реабилитации и лечения', 'shpigovsky' ); ?>
		</h2>

		<?php if ( 'subdivision' === $variant ) : ?>
			<p class="service-subdivision-stages-v1__lead block-whith-red-line">
				<?php echo esc_html__( 'Мы гарантируем конфиденциальность, уважение к личности, поддержание комфортной, психологически безопасной атмосферы.', 'shpigovsky' ); ?>
			</p>
		<?php endif; ?>

		<ol class="home-rehabilitation-requirements__steps <?php echo esc_attr( $steps_class ); ?>">
			<?php foreach ( $stages as $index => $stage ) : ?>
				<?php
				$title = isset( $stage['title'] ) ? trim( (string) $stage['title'] ) : '';
				$text  = isset( $stage['text'] ) ? trim( (string) $stage['text'] ) : '';

				if ( '' === $title && '' === $text ) {
					continue;
				}

				$number = str_pad( (string) ( $index + 1 ), 2, '0', STR_PAD_LEFT );
				?>
				<li class="home-rehabilitation-requirements__step">
					<span class="home-rehabilitation-requirements__step-number" aria-hidden="true"><?php echo esc_html( $number ); ?></span>
					<div class="home-rehabilitation-requirements__step-body">
						<?php if ( '' !== $title ) : ?>
							<h3 class="home-rehabilitation-requirements__step-title"><?php echo esc_html( $title ); ?></h3>
						<?php endif; ?>
						<?php if ( '' !== $text ) : ?>
							<p class="home-rehabilitation-requirements__step-text"><?php echo wp_kses_post( $text ); ?></p>
						<?php endif; ?>
					</div>
				</li>
			<?php endforeach; ?>
		</ol>

		<div class="<?php echo esc_attr( $cta_wrap ); ?>">
			<?php
			set_query_var(
				'shpigovsky_program_cta_band',
				array_merge(
					$cta,
					array(
						'section_id'   => $section_id . '-cta',
						'heading_id'   => $section_id . '-cta-heading',
						'heading_text' => $cta['title'],
						'wrap_section' => false,
						'button_first' => true,
						'margin_flush' => true,
					)
				)
			);
			get_template_part( 'template-parts/components/program-cta-band' );
			?>
		</div>

		<?php if ( 'subdivision' === $variant ) : ?>
			<div class="home-rehabilitation-requirements__support <?php echo esc_attr( $support_wrap ); ?>">
				<p class="home-rehabilitation-requirements__support-heading"><?php echo esc_html__( 'Поддержка осуществляется на всех этапах:', 'shpigovsky' ); ?></p>
				<ul class="home-rehabilitation-requirements__support-list">
					<li class="home-rehabilitation-requirements__support-item"><?php echo esc_html__( 'Интервенция на лечение — мотивация вас или ваших близких;', 'shpigovsky' ); ?></li>
					<li class="home-rehabilitation-requirements__support-item"><?php echo esc_html__( 'Круглосуточная поддержка психологов — в любое время будет оказана помощь;', 'shpigovsky' ); ?></li>
					<li class="home-rehabilitation-requirements__support-item"><?php echo esc_html__( 'Занятия в мини-группах — эффективная работа с каждым;', 'shpigovsky' ); ?></li>
					<li class="home-rehabilitation-requirements__support-item"><?php echo esc_html__( 'По договоренности, возможность удалённой работы в условиях стационара.', 'shpigovsky' ); ?></li>
				</ul>
			</div>
		<?php endif; ?>
	</div>
</section>
