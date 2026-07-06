<?php
/**
 * Template part: service/nature.php
 *
 * Static V9 fallback for service subdivision nature block.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?>
<section data-reveal class="service-subdivision-nature-v1" id="service-subdivision-nature" aria-labelledby="service-subdivision-nature-heading">
	<div class="container service-subdivision-nature-v1__container">
		<h2 class="service-subdivision-nature-v1__heading" id="service-subdivision-nature-heading"><?php echo esc_html__( 'Природа зависимости', 'shpigovsky' ); ?></h2>

		<p class="services-category-section-v2__lead service-subdivision-nature-v1__lead">
			<?php echo esc_html__( 'Зависимость формируется на пересечении биологических, психологических и социальных факторов. Мы рассматриваем её как состояние, которое можно исследовать и корректировать.', 'shpigovsky' ); ?>
		</p>

		<div class="service-subdivision-nature-v1__subsection">
			<h3 class="service-subdivision-nature-v1__subsection-heading"><?php echo esc_html__( 'Нейробиология', 'shpigovsky' ); ?></h3>
			<p class="service-subdivision-nature-v1__text">
				<?php echo esc_html__( 'Нарушения в системе вознаграждения мозга делают отказ от вещества или поведения физически и психологически трудным без профессиональной поддержки.', 'shpigovsky' ); ?>
			</p>
		</div>

		<div class="service-subdivision-nature-v1__subsection">
			<h3 class="service-subdivision-nature-v1__subsection-heading"><?php echo esc_html__( 'Генотипирование', 'shpigovsky' ); ?></h3>
			<p class="service-subdivision-nature-v1__text">
				<?php echo esc_html__( 'Генетические предрасположенности помогают точнее выстроить индивидуальную схему лечения и реабилитации.', 'shpigovsky' ); ?>
			</p>
			<p class="service-subdivision-nature-v1__genotyping-link">
				<a class="home-rehabilitation-program__all-link" href="<?php echo esc_url( home_url( '/uslugi/zavisimosti/profilakticheskiy-analiz/' ) ); ?>">
					<span class="home-rehabilitation-program__all-text"><?php echo esc_html__( 'Подробнее о генотипировании', 'shpigovsky' ); ?></span>
					<span class="home-rehabilitation-program__all-icon" aria-hidden="true"><i class="fas fa-play"></i></span>
				</a>
			</p>
		</div>

		<ul class="service-subdivision-nature-v1__cards">
			<li class="home-recovery-intro__card service-subdivision-nature-v1__card">
				<div class="home-recovery-intro__card-head">
					<span class="home-recovery-intro__card-icon" aria-hidden="true"><i class="fas fa-check"></i></span>
					<h3 class="home-recovery-intro__card-title"><?php echo esc_html__( 'Физиологическое проявление', 'shpigovsky' ); ?></h3>
				</div>
				<p class="home-recovery-intro__card-text">
					<?php echo esc_html__( 'Толерантность, абстиненция и соматические нарушения отражают биохимические изменения, требующие медицинского сопровождения.', 'shpigovsky' ); ?>
				</p>
			</li>
			<li class="home-recovery-intro__card service-subdivision-nature-v1__card">
				<div class="home-recovery-intro__card-head">
					<span class="home-recovery-intro__card-icon" aria-hidden="true"><i class="fas fa-check"></i></span>
					<h3 class="home-recovery-intro__card-title"><?php echo esc_html__( 'Поведенческое проявление', 'shpigovsky' ); ?></h3>
				</div>
				<p class="home-recovery-intro__card-text">
					<?php echo esc_html__( 'Компульсивные паттерны, утрата контроля и избегание работают как защитные стратегии, которые мы разбираем в терапии.', 'shpigovsky' ); ?>
				</p>
			</li>
		</ul>
	</div>
</section>
