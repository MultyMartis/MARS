<?php
/**
 * Glossary bootstrap requires — append to theme functions.php.
 *
 * Source of truth for deploy lives in this package; production functions.php
 * receives the require block only (see DEPLOY notes).
 *
 * @package iseoblog
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

require get_template_directory() . '/inc/glossary-helpers.php';
require get_template_directory() . '/inc/glossary-cpt.php';
require get_template_directory() . '/inc/glossary-acf.php';
require get_template_directory() . '/inc/glossary-import-admin.php';
