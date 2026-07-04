<?php
/**
 * Template part: services-hub/rehabilitation-program.php
 *
 * V9 services hub variant of the rehabilitation program block.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$program_url = home_url( '/o-centre/programma-lecheniya/' );

$directions = array(
	array(
		'title' => '01 — Генотипирование',
		'text'  => 'Выявление причин эндогенной природы зависимости служит дополнительным инструментом в индивидуальной схеме лечения и реабилитации.',
	),
	array(
		'title' => '02 — Нейропсихологическая коррекция',
		'text'  => 'БОС-терапия проводится с использованием специального оборудования для обучения сознательному контролю функций организма.',
	),
	array(
		'title' => '03 — Психокоррекция',
		'text'  => 'Работа с глубинными причинами зависимости и формирование внутренней опоры и новой стратегии совладания со стрессом.',
	),
	array(
		'title' => '04 — Кинезиотерапия',
		'text'  => 'Физическая нагрузка поддерживает восстановление естественной выработки нейромедиаторов в рамках программы сопровождения.',
	),
);
?>
<section data-reveal class="home-rehabilitation-program" aria-labelledby="services-hub-rehabilitation-program-heading">
	<div class="container">
		<div class="home-rehabilitation-program__head">
			<h2 class="home-rehabilitation-program__heading" id="services-hub-rehabilitation-program-heading">
				<?php echo esc_html__( 'Наша программа включает 4 направления', 'shpigovsky' ); ?>
			</h2>
			<a class="home-rehabilitation-program__all-link" href="<?php echo esc_url( $program_url ); ?>">
				<span class="home-rehabilitation-program__all-text"><?php echo esc_html__( 'подробнее', 'shpigovsky' ); ?></span>
				<span class="home-rehabilitation-program__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
			</a>
		</div>

		<p class="home-rehabilitation-program__lead">
			<?php echo esc_html__( 'Не просто снимаем симптомы. Мы помогаем разобраться в том, что именно в жизни и истории привело к этой точке.', 'shpigovsky' ); ?>
		</p>

		<p class="home-rehabilitation-program__intro">
			<?php echo esc_html__( 'Каждый человек приходит к нам со своей историей. Именно поэтому универсальных программ в нашем центре не существует.', 'shpigovsky' ); ?>
		</p>

		<div class="home-rehabilitation-program__directions">
			<?php foreach ( $directions as $direction ) : ?>
				<article class="home-rehabilitation-program__direction">
					<div class="home-rehabilitation-program__direction--wrapper">
						<h3 class="home-rehabilitation-program__direction-title"><?php echo esc_html( $direction['title'] ); ?></h3>
						<p class="home-rehabilitation-program__direction-text"><?php echo esc_html( $direction['text'] ); ?></p>
					</div>
				</article>
			<?php endforeach; ?>
		</div>
	</div>
</section>
