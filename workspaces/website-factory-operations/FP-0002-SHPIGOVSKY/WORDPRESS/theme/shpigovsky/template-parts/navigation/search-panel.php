<?php
/**
 * Header search dropdown panel — V9-06E62E.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?>
<div
	class="site-header-search"
	id="site-header-search"
	data-search-panel
	data-search-state="closed"
	hidden
>
	<div class="container site-header-search__inner">
		<div class="site-header-search__panel" role="region" aria-label="<?php esc_attr_e( 'Поиск по сайту', 'shpigovsky' ); ?>">
			<button
				type="button"
				class="site-header-search__close"
				data-search-close
				aria-label="<?php esc_attr_e( 'Закрыть поиск', 'shpigovsky' ); ?>"
			>
				<span aria-hidden="true"><i class="fas fa-times"></i></span>
			</button>
			<?php
			get_template_part(
				'searchform',
				null,
				array(
					'input_id'   => 'site-header-search-field',
					'form_class' => 'site-search-form site-search-form--header',
					'show_intro' => true,
					'autofocus'  => true,
					'value'      => '',
				)
			);
			?>
		</div>
	</div>
</div>
