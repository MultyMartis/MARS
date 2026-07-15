#!/usr/bin/env python3
"""FP-0002 V9-06D9-D transplant runner — TEMPORARY HELPER, NOT FOR GIT COMMIT."""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(r"X:/AI MARS")
WP = ROOT / "workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS"
THEME = WP / "theme/shpigovsky"
V9_SRC = ROOT / "workspaces/fp-0002-shpigovsky-v9/src"
V9_DIST = ROOT / "workspaces/fp-0002-shpigovsky-v9/dist"
EVIDENCE = WP / "validation/v9-06d9d-home-main-footer-static-v9-transplant"
SHOTS = EVIDENCE / "screenshots"
RUNTIME = Path(r"X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/themes/shpigovsky")
RUNTIME_URL = "http://shpigovsky.test"
STATIC_PORT = 9878

SECTION_ORDER = [
    ("home-recovery-intro.html", "recovery-intro.php", "home/recovery-intro"),
    ("founder-quote.html", "founder-quote.php", "home/founder-quote"),
    ("home-treatment-prevention.html", "treatment-prevention.php", "home/treatment-prevention"),
    ("home-gallery.html", "gallery.php", "home/gallery"),
    ("home-why-us.html", "why-us.php", "home/why-us"),
    ("home-staff-photo.html", "staff-photo.php", "home/staff-photo"),
    ("home-feature-grid.html", "feature-grid.php", "home/feature-grid"),
    ("clinic-landscape.html", "clinic-landscape.php", "home/clinic-landscape"),
    ("home-recovery-life.html", "recovery-life.php", "home/recovery-life"),
    ("reviews.html", "reviews.php", "home/reviews"),
    ("home-rehabilitation-requirements.html", "rehabilitation-requirements.php", "home/rehabilitation-requirements"),
    ("home-rehabilitation-program.html", "rehabilitation-program.php", "home/rehabilitation-program"),
    ("home-genotyping.html", "genotyping.php", "home/genotyping"),
    ("comfort.html", "comfort.php", "home/comfort"),
    ("home-videos.html", "videos.php", "home/videos"),
    ("specialists.html", "specialists.php", "home/specialists"),
    ("home-articles.html", "articles-teaser.php", "home/articles-teaser"),
    ("faq.html", "faq.php", "home/faq"),
]

ASSET_DIRS = [
    "img/content",
    "img/hero",
    "img/decor",
    "svg",
    "video",
    "vendor",
]

FOUNDER_REPLACEMENTS = {
    "@@founderQuoteModifierClass": " founder-quote--variant-b",
    "@@modalSource": "founder-quote",
}

COMFORT_GALLERY = """    <div class="comfort__gallery">
      <div class="comfort__gallery-item comfort__gallery-item_decor">
        <img class="comfort__gallery-image" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/branding/logo.svg' ) ); ?>" width="auto" height="auto" alt="" loading="lazy" decoding="async">
      </div>
      <a class="comfort__gallery-item comfort__gallery-item--wide" href="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-01.webp' ) ); ?>" data-fancybox="comfort">
        <img class="comfort__gallery-image" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-01.webp' ) ); ?>" width="1957" height="1113" alt="" loading="lazy" decoding="async">
      </a>
      <a class="comfort__gallery-item" href="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-02.webp' ) ); ?>" data-fancybox="comfort">
        <img class="comfort__gallery-image" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-02.webp' ) ); ?>" width="1881" height="1246" alt="" loading="lazy" decoding="async">
      </a>
      <a class="comfort__gallery-item" href="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-03.webp' ) ); ?>" data-fancybox="comfort">
        <img class="comfort__gallery-image" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-03.webp' ) ); ?>" width="1623" height="1155" alt="" loading="lazy" decoding="async">
      </a>
      <a class="comfort__gallery-item" href="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-04.webp' ) ); ?>" data-fancybox="comfort">
        <img class="comfort__gallery-image" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-04.webp' ) ); ?>" width="1610" height="1146" alt="" loading="lazy" decoding="async">
      </a>
      <a class="comfort__gallery-item" href="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-05.webp' ) ); ?>" data-fancybox="comfort">
        <img class="comfort__gallery-image" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-05.webp' ) ); ?>" width="1276" height="1136" alt="" loading="lazy" decoding="async">
      </a>
      <a class="comfort__gallery-item comfort__gallery-item--wide" href="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-06.webp' ) ); ?>" data-fancybox="comfort">
        <img class="comfort__gallery-image" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/content/home-comfort/comfort-room-06.webp' ) ); ?>" width="2201" height="1227" alt="" loading="lazy" decoding="async">
      </a>
    </div>"""


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def convert_html_to_php_body(html: str, slug: str) -> str:
    text = html
    for old, new in FOUNDER_REPLACEMENTS.items():
        text = text.replace(old, new)
    text = re.sub(r"@@include\([^)]+\)", "", text)
    text = re.sub(r"@@if \([^)]+\) \{[^}]+\}", "", text)
    text = text.replace("@@sectionModifierClass", "")
    text = text.replace("@@sectionId", "")
    text = text.replace("@@headingId", "comfort-heading")
    text = text.replace("@@headingText", "Комфорт, приватность, забота")
    text = text.replace("@@programHeading", "Программа центра включает 4&nbsp;направления")

    if slug == "comfort.php":
        text = re.sub(
            r"@@include\('partials/components/comfort-gallery\.html'.*?\)",
            "",
            text,
            flags=re.DOTALL,
        )
        text = text.replace(
            '<a class="comfort__all-link" href="/o-centre/galereya-o-dome/">',
            '<a class="comfort__all-link" href="<?php echo esc_url( home_url( \'/o-centre/galereya-o-dome/\' ) ); ?>">',
        )
        text = text.replace(
            '<section data-reveal class="comfort" aria-labelledby="comfort-heading">',
            '<section data-reveal class="comfort" aria-labelledby="comfort-heading">',
        )
        text = text.replace("</div>\n</section>", COMFORT_GALLERY + "\n  </div>\n</section>")

    # asset src/href
    def asset_repl(m: re.Match[str]) -> str:
        attr, path = m.group(1), m.group(2)
        rel = path.replace("assets/", "")
        return (
            f'{attr}="<?php echo esc_url( shpigovsky_asset_uri( \'{rel}\' ) ); ?>"'
        )

    text = re.sub(r'(src|href)="assets/([^"]+)"', asset_repl, text)

    def home_url_repl(m: re.Match[str]) -> str:
        path = m.group(1)
        return f'href="<?php echo esc_url( home_url( \'{path}\' ) ); ?>"'

    text = re.sub(r'href="(/[^"#]*/?)"', home_url_repl, text)

    # strip HTML comments
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    # collapse excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def php_wrap(slug: str, part: str, body: str) -> str:
    name = part.replace("/", "/")
    return f"""<?php
/**
 * Template part: {name}.php
 *
 * D9-D: static V9 visual authority with theme asset fallbacks.
 * Future ACF wiring: D9-E wave.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {{
	exit;
}}

?>
{body}
"""


def copy_assets() -> list[dict]:
    copied = []
    pairs = [
        (V9_SRC / "img", THEME / "assets/img"),
        (V9_SRC / "svg", THEME / "assets/svg"),
        (V9_DIST / "assets/img", THEME / "assets/img"),
        (V9_DIST / "assets/svg", THEME / "assets/svg"),
        (V9_DIST / "assets/video", THEME / "assets/video"),
        (V9_DIST / "assets/vendor", THEME / "assets/vendor"),
    ]
    for src_root, dest_root in pairs:
        if not src_root.exists():
            continue
        for src in src_root.rglob("*"):
            if not src.is_file():
                continue
            rel = src.relative_to(src_root)
            dest = dest_root / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            if dest.exists() and sha256_file(src) == sha256_file(dest):
                continue
            shutil.copy2(src, dest)
            copied.append(
                {
                    "source": str(src).replace("\\", "/"),
                    "target": str(dest).replace("\\", "/"),
                    "sha256": sha256_file(dest),
                }
            )
    return copied


def write_front_page() -> None:
    lines = [
        "<?php",
        "/**",
        " * Front page — V9 Home main orchestration (D9-D static transplant).",
        " *",
        " * @package Shpigovsky",
        " */",
        "",
        "if ( ! defined( 'ABSPATH' ) ) {",
        "\texit;",
        "}",
        "",
        "get_header();",
        "",
        "get_template_part( 'template-parts/home/hero' );",
        "",
        "if ( is_front_page() ) {",
        "\techo '</div>' . \"\\n\"; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped",
        "}",
        "?>",
        '<main class="site-main site-main--front" id="main-content">',
        "\t<?php",
    ]
    for _, php, part in SECTION_ORDER:
        lines.append(f"\tget_template_part( 'template-parts/{part}' );")
    lines += [
        "\tget_template_part( 'template-parts/components/final-form' );",
        "\t?>",
        "</main>",
        "<?php",
        "get_footer();",
        "",
    ]
    (THEME / "front-page.php").write_text("\n".join(lines), encoding="utf-8")


def patch_hero() -> None:
    path = THEME / "template-parts/home/hero.php"
    text = path.read_text(encoding="utf-8")
    old = """$cta_label = shpigovsky_get_site_option( 'default_button_label' );
$cta_label = '' !== $cta_label ? $cta_label : __( 'Записаться на консультацию', 'shpigovsky' );"""
    new = """// D9-D: static V9 CTA authority — options wiring deferred to D9-E.
$cta_label = __( 'Записаться на консультацию', 'shpigovsky' );"""
    if old in text:
        text = text.replace(old, new)
    text = re.sub(
        r"if \( '' === \$hero_title \) \{\s*\$hero_title = get_bloginfo\( 'name', 'display' \);\s*\}",
        "if ( '' === $hero_title ) {\n\t$hero_title = 'Шпиговский дом';\n}",
        text,
    )
    text = re.sub(
        r"if \( '' === \$hero_text \) \{\s*\$hero_text = 'Центр профилактики и&nbsp;лечения зависимостей';\s*\}",
        "if ( '' === $hero_text ) {\n\t$hero_text = 'Центр профилактики и&nbsp;лечения зависимостей';\n}",
        text,
    )
    path.write_text(text, encoding="utf-8")


def write_home_vendors_php() -> None:
    path = THEME / "inc/home-vendors.php"
    path.write_text(
        """<?php
/**
 * Home page vendor enqueue — Swiper, Fancybox, Inputmask (D9-D).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Enqueue V9 home interaction vendors on front page only.
 */
function shpigovsky_enqueue_home_vendors() {
	if ( ! is_front_page() ) {
		return;
	}

	$vendor_base = SHPIGOVSKY_THEME_URI . '/assets/vendor';
	$vendor_dir  = SHPIGOVSKY_THEME_DIR . '/assets/vendor';

	$swiper_css = $vendor_dir . '/swiper/swiper-bundle.min.css';
	if ( is_readable( $swiper_css ) ) {
		wp_enqueue_style( 'shpigovsky-swiper', $vendor_base . '/swiper/swiper-bundle.min.css', array( 'shpigovsky-v9' ), shpigovsky_asset_version( 'vendor/swiper/swiper-bundle.min.css' ) );
	}

	$fancy_css = $vendor_dir . '/fancybox/fancybox.css';
	if ( is_readable( $fancy_css ) ) {
		wp_enqueue_style( 'shpigovsky-fancybox', $vendor_base . '/fancybox/fancybox.css', array( 'shpigovsky-v9' ), shpigovsky_asset_version( 'vendor/fancybox/fancybox.css' ) );
	}

	if ( is_readable( $vendor_dir . '/swiper/swiper-bundle.min.js' ) ) {
		wp_enqueue_script( 'shpigovsky-swiper', $vendor_base . '/swiper/swiper-bundle.min.js', array(), shpigovsky_asset_version( 'vendor/swiper/swiper-bundle.min.js' ), true );
	}

	if ( is_readable( $vendor_dir . '/fancybox/fancybox.umd.js' ) ) {
		wp_enqueue_script( 'shpigovsky-fancybox', $vendor_base . '/fancybox/fancybox.umd.js', array(), shpigovsky_asset_version( 'vendor/fancybox/fancybox.umd.js' ), true );
		wp_enqueue_script( 'shpigovsky-v9-shell', SHPIGOVSKY_THEME_URI . '/assets/js/v9-shell.js', array( 'shpigovsky-fancybox', 'shpigovsky-swiper' ), shpigovsky_asset_version( 'js/v9-shell.js' ), true );
	}

	if ( is_readable( $vendor_dir . '/inputmask/inputmask.min.js' ) ) {
		wp_enqueue_script( 'shpigovsky-inputmask', $vendor_base . '/inputmask/inputmask.min.js', array(), shpigovsky_asset_version( 'vendor/inputmask/inputmask.min.js' ), true );
	}
}
add_action( 'shpigovsky_enqueue_theme_assets', 'shpigovsky_enqueue_home_vendors' );
""",
        encoding="utf-8",
    )
    fn = THEME / "functions.php"
    t = fn.read_text(encoding="utf-8")
    if "home-vendors.php" not in t:
        t = t.replace(
            "require_once SHPIGOVSKY_THEME_DIR . '/inc/home-helpers.php';",
            "require_once SHPIGOVSKY_THEME_DIR . '/inc/home-helpers.php';\nrequire_once SHPIGOVSKY_THEME_DIR . '/inc/home-vendors.php';",
        )
        fn.write_text(t, encoding="utf-8")


def write_footer() -> None:
    (THEME / "template-parts/layout/footer.php").write_text(
        """<?php
/**
 * Site footer — static V9 visual authority (D9-D).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$logo_url            = shpigovsky_asset_uri( 'img/branding/logo.svg' );
$brand_label         = shpigovsky_brand_label();
$phone_primary       = shpigovsky_format_phone_display( shpigovsky_get_site_option( 'phone_primary' ) );
$phone_secondary     = shpigovsky_format_phone_display( shpigovsky_get_site_option( 'phone_secondary' ) );
$phone_primary_href  = shpigovsky_phone_href( $phone_primary );
$phone_secondary_href = shpigovsky_phone_href( $phone_secondary );
$site_email          = sanitize_email( shpigovsky_get_site_option( 'site_email' ) );
$address_lines       = shpigovsky_split_option_lines( shpigovsky_get_site_option( 'site_address' ) );
$schedule_lines      = shpigovsky_split_option_lines( shpigovsky_get_site_option( 'opening_hours' ) );

// D9-D static V9 fallbacks when options empty.
if ( '' === $phone_primary ) {
	$phone_primary      = '8 (925) 183-64-64';
	$phone_primary_href = 'tel:+79251836464';
}
if ( '' === $phone_secondary ) {
	$phone_secondary      = '8 (995) 023-92-26';
	$phone_secondary_href = 'tel:+79950239226';
}
if ( '' === $site_email || ! is_email( $site_email ) ) {
	$site_email = 'Info@shpigovsky.ru';
}
if ( empty( $address_lines ) ) {
	$address_lines = array( 'Москва и Московская область' );
}
if ( empty( $schedule_lines ) ) {
	$schedule_lines = array( 'пн-пт 09:00-19:00,', 'сб-вс 09:00-20:00' );
}

$callback_label    = __( 'Заказать звонок', 'shpigovsky' );
$appointment_label = __( 'Записаться', 'shpigovsky' );
?>
<footer class="site-footer" data-reveal role="contentinfo">
	<div class="container">
		<div class="site-footer__top">
			<a class="site-footer__logo" href="<?php echo esc_url( home_url( '/' ) ); ?>">
				<img class="site-footer__logo-image" src="<?php echo esc_url( $logo_url ); ?>" alt="<?php echo esc_attr( $brand_label ); ?>">
			</a>
			<?php get_template_part( 'template-parts/navigation/footer-social' ); ?>
			<div class="site-footer__phones">
				<a class="site-footer__phone" href="<?php echo esc_url( $phone_primary_href ); ?>"><?php echo esc_html( $phone_primary ); ?></a>
				<a class="site-footer__phone site-footer__phone--secondary" href="<?php echo esc_url( $phone_secondary_href ); ?>"><?php echo esc_html( $phone_secondary ); ?></a>
			</div>
			<div class="site-footer__actions">
				<button type="button" class="btn" data-modal-open="consultation" data-modal-source="footer-callback" data-modal-title="<?php echo esc_attr( $callback_label ); ?>" data-modal-submit-text="<?php echo esc_attr( $callback_label ); ?>"><?php echo esc_html( $callback_label ); ?></button>
				<button type="button" class="btn btn_dark btn--primary" data-modal-open="consultation" data-modal-source="footer-appointment" data-modal-title="<?php echo esc_attr( $appointment_label ); ?>" data-modal-submit-text="<?php echo esc_attr( $appointment_label ); ?>"><?php echo esc_html( $appointment_label ); ?></button>
			</div>
		</div>
		<div class="site-footer__main">
			<div class="site-footer__contacts">
				<div class="site-footer__contact-item">
					<span class="site-footer__contact-icon" aria-hidden="true"><i class="fas fa-map-marker-alt"></i></span>
					<div class="site-footer__contact-body">
						<?php foreach ( $address_lines as $line ) : ?>
							<p class="site-footer__contact-label"><?php echo esc_html( $line ); ?></p>
						<?php endforeach; ?>
						<p class="site-footer__contact-meta">
							<em><?php esc_html_e( 'Режим работы:', 'shpigovsky' ); ?></em>
							<?php foreach ( $schedule_lines as $line ) : ?>
								<em><?php echo esc_html( $line ); ?></em>
							<?php endforeach; ?>
						</p>
					</div>
				</div>
				<div class="site-footer__contact-item">
					<span class="site-footer__contact-icon" aria-hidden="true"><i class="fas fa-envelope"></i></span>
					<div class="site-footer__contact-body">
						<a class="site-footer__contact-label" href="<?php echo esc_url( 'mailto:' . $site_email ); ?>"><?php echo esc_html( $site_email ); ?></a>
						<p class="site-footer__contact-meta"><?php esc_html_e( 'почта для заявок', 'shpigovsky' ); ?></p>
					</div>
				</div>
				<div class="site-footer__copyr-privacy">
					<p class="site-footer__privacy">
						<?php
						printf(
							wp_kses_post( __( 'По вопросам, связанным с обработкой ваших персональных данных, обращайтесь на <a href="mailto:%1$s">%2$s</a>', 'shpigovsky' ) ),
							esc_attr( strtolower( $site_email ) ),
							esc_html( $site_email )
						);
						?>
					</p>
				</div>
			</div>
			<nav class="site-footer__nav" aria-label="<?php esc_attr_e( 'Навигация в подвале — услуги', 'shpigovsky' ); ?>">
				<h2 class="site-footer__nav-heading"><?php esc_html_e( 'Услуги', 'shpigovsky' ); ?></h2>
				<?php
				wp_nav_menu(
					array(
						'theme_location'        => 'footer_services',
						'container'             => false,
						'menu_class'            => 'site-footer__nav-list',
						'fallback_cb'           => shpigovsky_footer_nav_fallback_factory( shpigovsky_footer_services_fallback_items() ),
						'shpigovsky_item_class' => 'site-footer__nav-item',
						'shpigovsky_link_class' => 'site-footer__nav-link',
						'depth'                 => 1,
					)
				);
				?>
			</nav>
			<nav class="site-footer__nav" aria-label="<?php esc_attr_e( 'Навигация в подвале — о центре', 'shpigovsky' ); ?>">
				<h2 class="site-footer__nav-heading"><?php esc_html_e( 'О центре', 'shpigovsky' ); ?></h2>
				<?php
				wp_nav_menu(
					array(
						'theme_location'        => 'footer_o_centre',
						'container'             => false,
						'menu_class'            => 'site-footer__nav-list',
						'fallback_cb'           => shpigovsky_footer_nav_fallback_factory( shpigovsky_footer_o_centre_fallback_items() ),
						'shpigovsky_item_class' => 'site-footer__nav-item',
						'shpigovsky_link_class' => 'site-footer__nav-link',
						'depth'                 => 1,
					)
				);
				?>
			</nav>
			<nav class="site-footer__nav" aria-label="<?php esc_attr_e( 'Навигация в подвале — информация', 'shpigovsky' ); ?>">
				<h2 class="site-footer__nav-heading"><?php esc_html_e( 'Информация', 'shpigovsky' ); ?></h2>
				<?php
				wp_nav_menu(
					array(
						'theme_location'        => 'legal',
						'container'             => false,
						'menu_class'            => 'site-footer__nav-list',
						'fallback_cb'           => shpigovsky_footer_nav_fallback_factory( shpigovsky_legal_nav_fallback_items() ),
						'shpigovsky_item_class' => 'site-footer__nav-item',
						'shpigovsky_link_class' => 'site-footer__nav-link',
						'depth'                 => 1,
					)
				);
				?>
			</nav>
		</div>
		<div class="site-footer__legal">
			<p class="site-footer__copyright">&copy; <?php echo esc_html( gmdate( 'Y' ) ); ?> <?php esc_html_e( 'Все права защищены.', 'shpigovsky' ); ?></p>
			<p class="site-footer__credit"><?php esc_html_e( 'Разработка и продвижение: Overseo', 'shpigovsky' ); ?></p>
		</div>
	</div>
</footer>
<?php get_template_part( 'template-parts/components/scroll-to-top' ); ?>
""",
        encoding="utf-8",
    )


def write_footer_social() -> None:
    (THEME / "template-parts/navigation/footer-social.php").write_text(
        """<?php
/**
 * Footer social links — static V9 visual fallback (D9-D).
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$rows = shpigovsky_get_social_link_rows();

if ( empty( $rows ) ) {
	$rows = array(
		array( 'label' => 'Telegram', 'url' => '#' ),
		array( 'label' => 'WhatsApp', 'url' => '#' ),
		array( 'label' => 'Max', 'url' => '#' ),
		array( 'label' => 'YouTube', 'url' => '#' ),
	);
}
?>
<div class="site-footer__social">
	<?php foreach ( $rows as $row ) : ?>
		<?php
		$icon  = shpigovsky_social_icon_for_label( $row['label'] );
		$label = '' !== $row['label'] ? $row['label'] : __( 'Социальная сеть', 'shpigovsky' );
		$is_fa = '' === $icon && str_contains( mb_strtolower( $label ), 'youtube' );
		?>
		<a class="site-footer__social-link<?php echo $is_fa ? ' site-footer__social-link--fa' : ''; ?>" href="<?php echo esc_url( $row['url'] ); ?>" aria-label="<?php echo esc_attr( $label ); ?>">
			<?php if ( $is_fa ) : ?>
				<i class="fab fa-youtube site-footer__social-fa" aria-hidden="true"></i>
			<?php elseif ( '' !== $icon ) : ?>
				<img class="site-footer__social-icon" src="<?php echo esc_url( shpigovsky_asset_uri( 'img/social/' . $icon ) ); ?>" alt="">
			<?php else : ?>
				<span class="site-footer__social-fallback"><?php echo esc_html( $label ); ?></span>
			<?php endif; ?>
		</a>
	<?php endforeach; ?>
</div>
""",
        encoding="utf-8",
    )


def write_scroll_to_top() -> None:
    (THEME / "template-parts/components/scroll-to-top.php").write_text(
        """<?php
/**
 * Scroll-to-top control — V9 static transplant.
 *
 * @package Shpigovsky
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}
?>
<button type="button" class="scroll-to-top" data-scroll-to-top aria-label="<?php esc_attr_e( 'Прокрутить страницу наверх', 'shpigovsky' ); ?>" aria-hidden="true">
	<svg class="scroll-to-top__icon" width="20" height="20" viewBox="0 0 20 20" aria-hidden="true" focusable="false">
		<path fill="currentColor" d="M10 4.5a.75.75 0 0 1 .53.22l5.5 5.5a.75.75 0 1 1-1.06 1.06L10.75 7.56V15a.75.75 0 0 1-1.5 0V7.56L5.03 11.28a.75.75 0 0 1-1.06-1.06l5.5-5.5A.75.75 0 0 1 10 4.5Z"/>
	</svg>
</button>
""",
        encoding="utf-8",
    )


def patch_final_form() -> None:
    path = THEME / "template-parts/components/final-form.php"
    t = path.read_text(encoding="utf-8")
    t = t.replace(
        "$submit_label = shpigovsky_get_site_option( 'default_button_label' );\n$submit_label = '' !== $submit_label ? $submit_label : __( 'Записаться на консультацию', 'shpigovsky' );",
        "// D9-D: static V9 submit label.\n$submit_label = __( 'Записаться на консультацию', 'shpigovsky' );",
    )
    path.write_text(t, encoding="utf-8")


def generate_partials() -> list[str]:
    created = []
    src_dir = V9_SRC / "partials/sections"
    out_dir = THEME / "template-parts/home"
    out_dir.mkdir(parents=True, exist_ok=True)
    for html_name, php_name, part in SECTION_ORDER:
        src = src_dir / html_name
        body = convert_html_to_php_body(src.read_text(encoding="utf-8"), php_name)
        out = out_dir / php_name
        out.write_text(php_wrap(php_name, part, body), encoding="utf-8")
        created.append(str(out.relative_to(THEME)).replace("\\", "/"))
    return created


def http_get(url: str) -> tuple[int, str]:
    try:
        req = Request(url, headers={"User-Agent": "D9D-Validator/1.0"})
        with urlopen(req, timeout=20) as resp:
            return resp.status, resp.read(8000).decode("utf-8", "ignore")
    except Exception as e:
        return 0, str(e)


def deliver_runtime(changed_files: list[Path]) -> dict:
    results = []
    for src in changed_files:
        rel = src.relative_to(THEME)
        dest = RUNTIME / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        results.append(
            {
                "relative": str(rel).replace("\\", "/"),
                "source_sha256": sha256_file(src),
                "runtime_sha256": sha256_file(dest),
                "match": sha256_file(src) == sha256_file(dest),
            }
        )
    return {"files": results, "count": len(results)}


def collect_changed_theme_files() -> list[Path]:
    files = []
    for p in THEME.rglob("*"):
        if p.is_file():
            files.append(p)
    return files


def main() -> int:
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    SHOTS.mkdir(parents=True, exist_ok=True)

    assets = copy_assets()
    partials = generate_partials()
    write_front_page()
    patch_hero()
    patch_final_form()
    write_home_vendors_php()
    write_footer()
    write_footer_social()
    write_scroll_to_top()

    # Determine changed files for delivery (only theme files touched in this run)
    touched = set()
    for rel in partials:
        touched.add(THEME / rel)
    for name in [
        "front-page.php",
        "template-parts/home/hero.php",
        "template-parts/components/final-form.php",
        "template-parts/layout/footer.php",
        "template-parts/navigation/footer-social.php",
        "template-parts/components/scroll-to-top.php",
        "inc/home-vendors.php",
        "functions.php",
    ]:
        touched.add(THEME / name)
    for a in assets:
        touched.add(Path(a["target"]))

    delivery = deliver_runtime(sorted(touched))

    routes = [
        ("/", "home"),
        ("/uslugi/", "services-hub"),
        ("/uslugi/zavisimosti/", "service-73"),
        ("/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/", "service-74"),
        ("/uslugi/psihicheskoe-zdorovie/", "service-77"),
        ("/uslugi/rasstroystva-pischevogo-povedeniya/", "service-84"),
        ("/kontakty/", "contacts"),
    ]
    smoke = []
    for path, key in routes:
        code, body = http_get(RUNTIME_URL + path)
        smoke.append(
            {
                "route": path,
                "key": key,
                "status": code,
                "has_header": "site-header" in body or "header" in body,
                "has_footer": "site-footer" in body,
                "has_v9_css": "v9-style" in body,
                "ok": code == 200 and "site-footer" in body,
            }
        )

    home_code, home_body = http_get(RUNTIME_URL + "/")
    sections = re.findall(r'<section[^>]*class="([^"]+)"', home_body)
    hero_cta = "Записаться на консультацию" in home_body or "Записаться на&nbsp;консультацию" in home_body

    summary = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "partials_created": partials,
        "assets_copied": len(assets),
        "delivery": delivery,
        "route_smoke": smoke,
        "home_section_count": len(sections),
        "hero_cta_static_v9": hero_cta,
        "all_routes_200": all(r["status"] == 200 for r in smoke),
    }

    (EVIDENCE / "home-main-transplant-result.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    (EVIDENCE / "asset-vendor-transplant-result.json").write_text(json.dumps({"assets": assets}, indent=2, ensure_ascii=False), encoding="utf-8")
    (EVIDENCE / "runtime-delivery-result.json").write_text(json.dumps(delivery, indent=2), encoding="utf-8")
    (EVIDENCE / "post-repair-route-smoke.json").write_text(json.dumps(smoke, indent=2, ensure_ascii=False), encoding="utf-8")
    (EVIDENCE / "post-repair-hero-cta-check.json").write_text(
        json.dumps({"static_label": "Записаться на консультацию", "runtime_match": hero_cta}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
