<?php
/**
 * iseoblog functions and definitions
 *
 * @link https://developer.wordpress.org/themes/basics/theme-functions/
 *
 * @package iseoblog
 */

if ( ! defined( '_S_VERSION' ) ) {
	// Replace the version number of the theme on each release.
	define( '_S_VERSION', '1.0.0' );
}

/**
 * Sets up theme defaults and registers support for various WordPress features.
 *
 * Note that this function is hooked into the after_setup_theme hook, which
 * runs before the init hook. The init hook is too late for some features, such
 * as indicating support for post thumbnails.
 */
function iseoblog_setup() {
	/*
		* Make theme available for translation.
		* Translations can be filed in the /languages/ directory.
		* If you're building a theme based on iseoblog, use a find and replace
		* to change 'iseoblog' to the name of your theme in all the template files.
		*/
	load_theme_textdomain( 'iseoblog', get_template_directory() . '/languages' );

	// Add default posts and comments RSS feed links to head.
	add_theme_support( 'automatic-feed-links' );

	/*
		* Let WordPress manage the document title.
		* By adding theme support, we declare that this theme does not use a
		* hard-coded <title> tag in the document head, and expect WordPress to
		* provide it for us.
		*/
	add_theme_support( 'title-tag' );

	/*
		* Enable support for Post Thumbnails on posts and pages.
		*
		* @link https://developer.wordpress.org/themes/functionality/featured-images-post-thumbnails/
		*/
	add_theme_support( 'post-thumbnails' );

	// This theme uses wp_nav_menu() in one location.
	register_nav_menus(
		array(
			'menu-1' => esc_html__( 'Primary', 'iseoblog' ),
		)
	);

	/*
		* Switch default core markup for search form, comment form, and comments
		* to output valid HTML5.
		*/
	add_theme_support(
		'html5',
		array(
			'search-form',
			'comment-form',
			'comment-list',
			'gallery',
			'caption',
			'style',
			'script',
		)
	);

	// Set up the WordPress core custom background feature.
	add_theme_support(
		'custom-background',
		apply_filters(
			'iseoblog_custom_background_args',
			array(
				'default-color' => 'ffffff',
				'default-image' => '',
			)
		)
	);

	// Add theme support for selective refresh for widgets.
	add_theme_support( 'customize-selective-refresh-widgets' );

	/**
	 * Add support for core custom logo.
	 *
	 * @link https://codex.wordpress.org/Theme_Logo
	 */
	add_theme_support(
		'custom-logo',
		array(
			'height'      => 250,
			'width'       => 250,
			'flex-width'  => true,
			'flex-height' => true,
		)
	);
}
add_action( 'after_setup_theme', 'iseoblog_setup' );

/**
 * Set the content width in pixels, based on the theme's design and stylesheet.
 *
 * Priority 0 to make it available to lower priority callbacks.
 *
 * @global int $content_width
 */
function iseoblog_content_width() {
	$GLOBALS['content_width'] = apply_filters( 'iseoblog_content_width', 640 );
}
add_action( 'after_setup_theme', 'iseoblog_content_width', 0 );

/**
 * Register widget area.
 *
 * @link https://developer.wordpress.org/themes/functionality/sidebars/#registering-a-sidebar
 */
function iseoblog_widgets_init() {
	register_sidebar(
		array(
			'name'          => esc_html__( 'Sidebar', 'iseoblog' ),
			'id'            => 'sidebar-1',
			'description'   => esc_html__( 'Add widgets here.', 'iseoblog' ),
			'before_widget' => '<section id="%1$s" class="widget %2$s">',
			'after_widget'  => '</section>',
			'before_title'  => '<h2 class="widget-title">',
			'after_title'   => '</h2>',
		)
	);
}
add_action( 'widgets_init', 'iseoblog_widgets_init' );

/**
 * Enqueue scripts and styles.
 */
function iseoblog_scripts() {
	wp_enqueue_style( 'base-style-normalize', 'https://i-seo.su/css/normalize.css' );
	wp_enqueue_style( 'base-style-owl', 'https://i-seo.su/libs/owl/owl.carousel.min.css' );
	wp_enqueue_style( 'base-style-owl-theme', 'https://i-seo.su/libs/owl/owl.theme.default.min.css' );
	wp_enqueue_style( 'base-style-fancybox', 'https://i-seo.su/libs/fancybox/jquery.fancybox.min.css' );
	wp_enqueue_style( 'google-fonts', 'https://fonts.googleapis.com/css2?family=Manrope:wght@200..800&display=swap' );
	wp_enqueue_style( 'base-style-main', 'https://i-seo.su/css/main.css' );
	wp_enqueue_style( 'base-style-media', 'https://i-seo.su/css/media.css' );
	wp_enqueue_style( 'iseoblog-style', get_stylesheet_uri(), array(), _S_VERSION );

	wp_enqueue_script( 'iseoblog-jquery', 'https://i-seo.su/libs/jquery/jquery-3.7.1.min.js', array(), _S_VERSION, false );
	wp_enqueue_script( 'iseoblog-owl', 'https://i-seo.su/libs/owl/owl.carousel.min.js', array(), _S_VERSION, false );
	wp_enqueue_script( 'iseoblog-fancybox', 'https://i-seo.su/libs/fancybox/jquery.fancybox.min.js', array(), _S_VERSION, false );
	wp_enqueue_script( 'jquery-mask', 'https://cdnjs.cloudflare.com/ajax/libs/jquery.mask/1.14.16/jquery.mask.min.js', array(), _S_VERSION, false );

	wp_enqueue_script( 'iseoblog-common', 'https://i-seo.su/js/common.js', array(), _S_VERSION, true );
	wp_enqueue_script( 'iseoblog-script', get_template_directory_uri() . '/js/script.js', array(), _S_VERSION, true );

	if ( is_singular() && comments_open() && get_option( 'thread_comments' ) ) {
		wp_enqueue_script( 'comment-reply' );
	}
}
add_action( 'wp_enqueue_scripts', 'iseoblog_scripts' );

/**
 * Implement the Custom Header feature.
 */
require get_template_directory() . '/inc/custom-header.php';

/**
 * Custom template tags for this theme.
 */
require get_template_directory() . '/inc/template-tags.php';

/**
 * Functions which enhance the theme by hooking into WordPress.
 */
require get_template_directory() . '/inc/template-functions.php';

/**
 * Customizer additions.
 */
require get_template_directory() . '/inc/customizer.php';

/**
 * Load Jetpack compatibility file.
 */
if ( defined( 'JETPACK__VERSION' ) ) {
	require get_template_directory() . '/inc/jetpack.php';
}

add_action('init', 'register_offer_type_init');
function register_offer_type_init() {
    $labels = array(
		'name' => 'Предложения',
		'singular_name' => 'Предложение',
		'add_new' => 'Добавить',
		'add_new_item' => 'Добавить предложение',
		'edit_item' => 'Редактировать предложение',
		'new_item' => 'Новое предложение',
		'all_items' => 'Все предложения',
		'not_found' => 'Ни одного предложения не найдено.',
		'not_found_in_trash' => 'There are no items in the trash.'
	);
	$args = array(
		'labels' => $labels,
		'public' => true,
		'show_ui' => true,
		'has_archive' => true,
		'menu_position' => 5,
		'menu_icon' => 'dashicons-welcome-write-blog',
		'supports' => array('title', 'editor', 'thumbnail'),
		'rewrite' => array('with_front' => false)
	); register_post_type('offer', $args);
}

add_filter('wp_robots', 'add_noindex_filter');
function add_noindex_filter($robots) {
    if (is_singular('offer')) {
        $robots['noindex'] = true;
        $robots['nofollow'] = true;
    }
    return $robots;
}

function print_likes_button($id) {
	$cookies = Array();
	if(isset($_COOKIE['iseo-likes']) && $_COOKIE['iseo-likes']) {
		$cookies = explode(',', $_COOKIE['iseo-likes']);
	}
	$available = true;
	if(count($cookies)) {
		if(in_array($id, $cookies)) {
			$available = false;
		}		
	}
	if($available) {
		echo '<div class="blog_article__stat_item blog_article__like_item js-blog_article__like_item" data-id="' . $id . '">';
	} else {
		echo '<div class="blog_article__stat_item blog_article__like_item dis-blog_article__like_item">';
	}
	echo '<img class="like-icon-1" src="/img/blog_stat__like.svg">';
	echo '<img class="like-icon-2" src="/img/blog_stat__like-fill.svg">';
	echo '<span>' . get_field('likes', $id) . '</span>';
	echo '</div>';
}

function print_sharings_button($id) {
	$cookies = Array();
	if(isset($_COOKIE['iseo-sharings']) && $_COOKIE['iseo-sharings']) {
		$cookies = explode(',', $_COOKIE['iseo-sharings']);
	}
	$available = true;
	if(count($cookies)) {
		if(in_array($id, $cookies)) {
			$available = false;
		}		
	}
	if($available) {
		echo '<div class="blog_article__stat_item blog_article__share_item js-blog_article__share_item" data-id="' . $id . '" data-link="' . get_permalink($id) . '">';
	} else {
		echo '<div class="blog_article__stat_item blog_article__share_item js-blog_article__share_item nocount" data-id="' . $id . '"data-link="' . get_permalink($id) . '">';
	}
	echo '<img src="/img/blog_stat__share.svg">';
	echo '<span>' . get_field('sharings', $id) . '</span>';
	echo '</div>';
}

add_action( 'wp_ajax_like_action', 'like_action' );
add_action( 'wp_ajax_nopriv_like_action', 'like_action' );

function like_action() {
	$id = $_POST['id'];
	$likes = (int)get_field('likes', $id) + 1;	
	$output = array('status' => 'error');
	$output['id'] = $id;
	$output['count'] = $likes;
	if(update_post_meta($id, 'likes', $likes)){
		$cookies = array();
		if($_COOKIE['iseo-likes']) {
			$cookies = explode(',', $_COOKIE['iseo-likes']);
		}
		if(!in_array($id, $cookies)) {
			$cookies[] = $id;
			setcookie("iseo-likes", implode(',', $cookies), time()+31536000, '/'); 
		}		
		$output['status'] = "ok";
	}
	echo json_encode($output);
	die();	
}

add_action( 'wp_ajax_share_action', 'share_action' );
add_action( 'wp_ajax_nopriv_share_action', 'share_action' );

function share_action() {
	$id = $_POST['id'];
	$likes = (int)get_field('sharings', $id) + 1;	
	$output = array('status' => 'error');
	$output['id'] = $id;
	$output['count'] = $likes;
	if(update_post_meta($id, 'sharings', $likes)){
		$cookies = array();
		if($_COOKIE['iseo-sharings']) {
			$cookies = explode(',', $_COOKIE['iseo-sharings']);
		}
		if(!in_array($id, $cookies)) {
			$cookies[] = $id;
			setcookie("iseo-sharings", implode(',', $cookies), time()+31536000, '/'); 
		}		
		$output['status'] = "ok";
	}
	echo json_encode($output);
	die();	
}

function printTagsItem($tag, $count) {
	$link = '/blog?tags=' . $tag->slug;
	$class = "";

	if($tag->slug == $_GET['tags']) {
		$class = " active";
	} elseif($count > 5) {
		$class = " hidden";
	}

	if($_GET['sort']) {
		$link .= '&sort=' . $_GET['sort'];
	}

	echo '<div class="blog_filter__item' . $class . '">';
	echo '<a class="blog_filter__btn" href="' . $link . '">';
	echo '<div>' . $tag->name . '</div>';
	echo '<span>(' . $tag->count . ')</span>';
	echo '</a>';
	echo '</div>';
}

function printSortItem($name, $param) {
	$sort = $_GET['sort'];
	if(!$sort) {
		$sort = "date-desc";
	}
	$link = '/blog';
	if($_GET['tags']) {
		$link .= '?tags=' . $_GET['tags'];
		$sep = "&sort=";
	} else {
		$sep = "?sort=";
	}

	$class = "blog_filter_sort__btn";
	if($sort == $param . '-desc') {
		$class .= " current";
		$link .= $sep . $param . '-asc';
	} elseif($sort == $param . '-asc') {
		$class .= " current reverse";
		$link .= $sep . $param . '-desc';
	} else {
		$link .= $sep . $param . '-desc';
	}

	echo '<a class="' . $class . '" href="' . $link . '">';
	echo '<div>' . $name . '</div>';
	echo '<span></span>';
	echo '</a>';
}

function my_custom_body_classes( $classes ) {
    if ( is_page(1730) || is_category() ) {
        $classes[] = 'blog';
    }
    return $classes;
}
add_filter( 'body_class', 'my_custom_body_classes' );

/**
 * Glossary CPT, ACF metadata, archive helpers, gated admin import.
 */
require get_template_directory() . '/inc/glossary-bootstrap.php';

/**
 * Date archive URLs currently 301 to homepage; point archive widgets at /blog instead
 * so internal anchors do not target redirecting URLs (LINK-TO-REDIR cleanup).
 */
add_filter( 'get_archives_link', 'iseo_rewrite_dead_date_archive_links' );
function iseo_rewrite_dead_date_archive_links( $link_html ) {
	if ( ! is_string( $link_html ) || $link_html === '' ) {
		return $link_html;
	}
	$updated = preg_replace(
		'#https?://(?:www\.)?i-seo\.su/blog/\d{4}(?:/\d{1,2})?#',
		'https://i-seo.su/blog',
		$link_html
	);
	$updated = preg_replace(
		'#(href=["\'])/blog/\d{4}(?:/\d{1,2})?(["\'])#',
		'$1/blog$2',
		$updated
	);
	return is_string( $updated ) ? $updated : $link_html;
}

