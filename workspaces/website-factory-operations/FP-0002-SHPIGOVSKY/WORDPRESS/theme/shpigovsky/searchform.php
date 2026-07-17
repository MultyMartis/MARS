<?php
/**
 * Site search form — V9-06E62E.
 *
 * Used by the header search panel and the search results empty state.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$args = wp_parse_args(
	isset( $args ) && is_array( $args ) ? $args : array(),
	array(
		'input_id'    => 'site-search-field',
		'form_class'  => 'site-search-form',
		'show_intro'  => true,
		'autofocus'   => false,
		'value'       => get_search_query( false ),
	)
);

$input_id   = sanitize_html_class( (string) $args['input_id'] );
$form_class = trim( (string) $args['form_class'] );
$value      = is_string( $args['value'] ) ? $args['value'] : '';
?>
<form
	role="search"
	method="get"
	class="<?php echo esc_attr( $form_class ); ?>"
	action="<?php echo esc_url( home_url( '/' ) ); ?>"
	data-site-search-form
>
	<?php if ( ! empty( $args['show_intro'] ) ) : ?>
		<p class="site-search-form__heading" id="<?php echo esc_attr( $input_id ); ?>-heading"><?php esc_html_e( 'Поиск по сайту', 'shpigovsky' ); ?></p>
		<p class="site-search-form__hint" id="<?php echo esc_attr( $input_id ); ?>-hint"><?php esc_html_e( 'Начните вводить название услуги, специалиста или статьи', 'shpigovsky' ); ?></p>
	<?php endif; ?>

	<div class="site-search-form__row">
		<label class="site-search-form__label" for="<?php echo esc_attr( $input_id ); ?>">
			<span class="screen-reader-text"><?php esc_html_e( 'Поисковый запрос', 'shpigovsky' ); ?></span>
		</label>
		<input
			type="search"
			id="<?php echo esc_attr( $input_id ); ?>"
			class="site-search-form__input"
			name="s"
			value="<?php echo esc_attr( $value ); ?>"
			placeholder="<?php echo esc_attr__( 'Поиск…', 'shpigovsky' ); ?>"
			enterkeyhint="search"
			<?php echo ! empty( $args['show_intro'] ) ? 'aria-describedby="' . esc_attr( $input_id . '-hint' ) . '"' : ''; ?>
			<?php echo ! empty( $args['autofocus'] ) ? 'data-search-focus' : ''; ?>
			required
		>
		<button type="submit" class="btn btn_dark btn--primary site-search-form__submit">
			<?php esc_html_e( 'Поиск', 'shpigovsky' ); ?>
		</button>
	</div>
</form>
