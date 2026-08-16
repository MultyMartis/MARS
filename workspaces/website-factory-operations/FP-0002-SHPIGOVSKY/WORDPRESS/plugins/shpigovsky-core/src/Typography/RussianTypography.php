<?php
/**
 * Canonical Russian typography processor (FP-0002 PROD-P16).
 *
 * ONE TYPOGRAPHY OWNER for human-facing prose. Idempotent. HTML-aware.
 * Does not rewrite URLs, attributes, shortcodes, or technical identifiers.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Typography;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Pure typography transforms — no WordPress hooks.
 */
final class RussianTypography {

	public const NBSP = "\xC2\xA0";

	/**
	 * Tags whose text descendants must not be typographed.
	 *
	 * @var array<int, string>
	 */
	private const SKIP_TAGS = array(
		'script',
		'style',
		'code',
		'pre',
		'textarea',
		'kbd',
		'samp',
		'tt',
		'svg',
	);

	/**
	 * Process plain text (no HTML). Unicode NBSP representation.
	 *
	 * @param string $text Plain text.
	 * @return string
	 */
	public static function process_plain( $text ) {
		$text = (string) $text;
		if ( '' === $text || ! self::has_cyrillic( $text ) ) {
			// Still normalize entity forms when present without Cyrillic (rare).
			if ( false === strpos( $text, '&nbsp;' ) && false === strpos( $text, '&mdash;' ) && false === strpos( $text, '&ndash;' ) ) {
				return $text;
			}
		}

		if ( self::looks_technical( $text ) ) {
			return $text;
		}

		$before = $text;
		$text   = self::normalize_entities( $text );
		$text   = self::apply_plain_rules( $text );

		// Idempotence guard: second pass must equal first.
		$again = self::apply_plain_rules( self::normalize_entities( $text ) );
		if ( $again !== $text ) {
			$text = $again;
		}

		unset( $before );
		return $text;
	}

	/**
	 * Process HTML / WYSIWYG: text nodes only; preserve markup.
	 *
	 * @param string $html HTML fragment.
	 * @return string
	 */
	public static function process_html( $html ) {
		$html = (string) $html;
		if ( '' === $html ) {
			return $html;
		}

		// Fast path: no Cyrillic and no typography entities.
		if ( ! self::has_cyrillic( $html ) && false === strpos( $html, '&nbsp;' ) && false === stripos( $html, '&mdash;' ) && false === stripos( $html, '&ndash;' ) ) {
			return $html;
		}

		$parts  = preg_split( '/(<[^>]+>)/u', $html, -1, PREG_SPLIT_DELIM_CAPTURE );
		if ( ! is_array( $parts ) ) {
			return $html;
		}

		$skip_depth = 0;
		$out        = '';

		foreach ( $parts as $part ) {
			if ( '' === $part ) {
				continue;
			}

			if ( '<' === $part[0] && '>' === substr( $part, -1 ) ) {
				$tag = self::tag_name( $part );
				if ( '' !== $tag ) {
					if ( '/' === $tag[0] ) {
						$close = strtolower( substr( $tag, 1 ) );
						if ( in_array( $close, self::SKIP_TAGS, true ) && $skip_depth > 0 ) {
							--$skip_depth;
						}
					} elseif ( ! self::is_self_closing( $part ) ) {
						$open = strtolower( $tag );
						if ( in_array( $open, self::SKIP_TAGS, true ) ) {
							++$skip_depth;
						}
					}
				}
				$out .= $part;
				continue;
			}

			if ( $skip_depth > 0 ) {
				$out .= $part;
				continue;
			}

			if ( self::is_protected_text_segment( $part ) ) {
				$out .= $part;
				continue;
			}

			$out .= self::process_plain( $part );
		}

		return $out;
	}

	/**
	 * Process value by declared content kind.
	 *
	 * @param string $value Value.
	 * @param string $kind  plain|html|auto.
	 * @return string
	 */
	public static function process( $value, $kind = 'auto' ) {
		$value = (string) $value;
		$kind  = (string) $kind;

		if ( 'html' === $kind ) {
			return self::process_html( $value );
		}
		if ( 'plain' === $kind ) {
			return self::process_plain( $value );
		}

		// auto: treat as HTML when tags present.
		if ( false !== strpos( $value, '<' ) && false !== strpos( $value, '>' ) ) {
			return self::process_html( $value );
		}

		return self::process_plain( $value );
	}

	/**
	 * Collapse NBSP to regular space for search/matching.
	 *
	 * @param string $text Text.
	 * @return string
	 */
	public static function collapse_nbsp_for_match( $text ) {
		$text = (string) $text;
		$text = str_replace( array( self::NBSP, '&nbsp;', '&#160;', '&#xA0;', '&#xa0;' ), ' ', $text );
		return $text;
	}

	/**
	 * @param string $text Text.
	 * @return bool
	 */
	private static function has_cyrillic( $text ) {
		return (bool) preg_match( '/[А-Яа-яЁё]/u', $text );
	}

	/**
	 * @param string $text Text.
	 * @return bool
	 */
	private static function looks_technical( $text ) {
		$t = trim( $text );
		if ( '' === $t ) {
			return true;
		}
		if ( preg_match( '#^(https?:|mailto:|tel:|//|#|/|wp-|field_|group_|acf-|fp02-)#i', $t ) ) {
			return true;
		}
		if ( preg_match( '/^[a-z0-9_\-\.\/]+$/i', $t ) && ! self::has_cyrillic( $t ) ) {
			return true;
		}
		// JSON-ish.
		if ( ( '{' === $t[0] && '}' === substr( $t, -1 ) ) || ( '[' === $t[0] && ']' === substr( $t, -1 ) ) ) {
			if ( false !== strpos( $t, '"' ) && false !== strpos( $t, ':' ) ) {
				return true;
			}
		}
		return false;
	}

	/**
	 * @param string $segment Text segment between tags.
	 * @return bool
	 */
	private static function is_protected_text_segment( $segment ) {
		$s = trim( $segment );
		if ( '' === $s ) {
			return true;
		}
		// Shortcode-like payloads.
		if ( preg_match( '/^\[[a-z0-9_\-]+(?:\s|\]|\/)/i', $s ) ) {
			return true;
		}
		if ( preg_match( '#^(https?://|mailto:|tel:)#i', $s ) ) {
			return true;
		}
		// Pure email.
		if ( preg_match( '/^[A-Z0-9._%+\-]+@[A-Z0-9.\-]+\.[A-Z]{2,}$/i', $s ) ) {
			return true;
		}
		return false;
	}

	/**
	 * @param string $tag_html Tag HTML including brackets.
	 * @return string Tag name with optional leading slash.
	 */
	private static function tag_name( $tag_html ) {
		if ( preg_match( '/^<\/?\s*([a-zA-Z0-9:-]+)/', $tag_html, $m ) ) {
			$slash = ( isset( $tag_html[1] ) && '/' === $tag_html[1] ) ? '/' : '';
			// Better: detect closing.
			if ( preg_match( '/^<\s*\//', $tag_html ) ) {
				return '/' . strtolower( $m[1] );
			}
			return strtolower( $m[1] );
		}
		return '';
	}

	/**
	 * @param string $tag_html Tag HTML.
	 * @return bool
	 */
	private static function is_self_closing( $tag_html ) {
		return (bool) preg_match( '/\/\s*>$/', $tag_html )
			|| (bool) preg_match( '/^<\s*(br|hr|img|input|meta|link|source|wbr|area|col|embed|param|track)\b/i', $tag_html );
	}

	/**
	 * @param string $text Text.
	 * @return string
	 */
	private static function normalize_entities( $text ) {
		$text = str_replace( '&nbsp;', self::NBSP, $text );
		$text = str_replace( array( '&#160;', '&#xA0;', '&#xa0;' ), self::NBSP, $text );
		$text = str_replace( array( '&mdash;', '&#8212;' ), '—', $text );
		$text = str_replace( array( '&ndash;', '&#8211;' ), '–', $text );
		$text = str_replace( array( '&laquo;', '&#171;' ), '«', $text );
		$text = str_replace( array( '&raquo;', '&#187;' ), '»', $text );
		return $text;
	}

	/**
	 * Core plain-text rule set (conservative).
	 *
	 * @param string $s Text.
	 * @return string
	 */
	private static function apply_plain_rules( $s ) {
		$nbsp = self::NBSP;

		// Collapse accidental duplicate regular spaces (not newlines/tabs in intentional blocks).
		$s = preg_replace( '/[ ]{2,}/u', ' ', $s );

		// Numbers + common Russian units / currency-ish.
		$s = preg_replace(
			'/(\d+)[ \t]+(года|лет|год|года|минуты|минут|минута|часа|часов|час|дней|дня|день|мес\.?|%|₽|руб\.?)/ui',
			'$1' . $nbsp . '$2',
			$s
		);

		// Initials: А. Б. and А. Фамилия
		$s = preg_replace( '/([А-ЯЁ]\.)[ \t]+([А-ЯЁ]\.)/u', '$1' . $nbsp . '$2', $s );
		$s = preg_replace( '/([А-ЯЁ]\.)[ \t]+([А-ЯЁ][а-яё]+)/u', '$1' . $nbsp . '$2', $s );

		// Sentence dash: space-hyphen-space used as dash → em dash with NBSP before.
		$s = preg_replace( '/(?<=[\wА-Яа-яЁё»”\)])[ \t]+-[ \t]+(?=[\wА-Яа-яЁё«\"„(])/u', $nbsp . '— ', $s );

		// NBSP before existing em/en dashes.
		$s = preg_replace( '/(?<=[\wА-Яа-яЁё»\"”\)])[ \t]+([—–])/u', $nbsp . '$1', $s );

		// Russian quotes: straight "..." when both sides look like prose (not inches/code).
		$s = self::normalize_russian_quotes( $s );

		// Short prepositions / conjunctions.
		$prep = 'в|во|к|ко|с|со|у|о|об|от|до|по|на|за|из|без|для|и|а|не|ни|но|же|ли|бы';
		$s    = preg_replace_callback(
			'/(^|[^\wА-Яа-яЁё' . preg_quote( $nbsp, '/' ) . '])(' . $prep . ')[ \t]+(?=[\wА-Яа-яЁё0-9«\"„(])/u',
			static function ( $m ) use ( $nbsp ) {
				return $m[1] . $m[2] . $nbsp;
			},
			$s
		);

		// Cleanup mixed space/NBSP.
		$s = preg_replace( '/[ \t]+' . preg_quote( $nbsp, '/' ) . '/u', $nbsp, $s );
		$s = preg_replace( '/' . preg_quote( $nbsp, '/' ) . '[ \t]+/u', $nbsp, $s );
		$s = preg_replace( '/' . preg_quote( $nbsp, '/' ) . '{2,}/u', $nbsp, $s );

		return $s;
	}

	/**
	 * Convert clear straight double quotes to «».
	 *
	 * @param string $s Text.
	 * @return string
	 */
	private static function normalize_russian_quotes( $s ) {
		// Skip if already balanced guillemets-only or no ASCII quotes.
		if ( false === strpos( $s, '"' ) ) {
			return $s;
		}

		// Pair ASCII quotes that wrap Cyrillic-containing spans.
		return (string) preg_replace_callback(
			'/"([^"\n]{1,200})"/u',
			static function ( $m ) {
				$inner = $m[1];
				if ( ! preg_match( '/[А-Яа-яЁё]/u', $inner ) ) {
					return $m[0];
				}
				// Skip if looks like inches or technical.
				if ( preg_match( '/^\d/', $inner ) || preg_match( '/https?:|www\.|@|\//', $inner ) ) {
					return $m[0];
				}
				return '«' . $inner . '»';
			},
			$s
		);
	}
}
