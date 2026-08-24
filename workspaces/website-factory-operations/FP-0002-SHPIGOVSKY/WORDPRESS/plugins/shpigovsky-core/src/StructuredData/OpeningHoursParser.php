<?php
/**
 * Conservative opening-hours parser for Russian free-text schedules.
 *
 * Returns OpeningHoursSpecification nodes or empty array when ambiguous.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\StructuredData;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Parse known FP-0002 hours lines into schema.org opening hours specs.
 */
final class OpeningHoursParser {

	/**
	 * @param string|string[] $input HTML or plain lines.
	 * @return array<int, array<string, mixed>>
	 */
	public static function parse( $input ) {
		$lines = self::normalize_lines( $input );
		$specs = array();

		foreach ( $lines as $line ) {
			$parsed = self::parse_line( $line );
			if ( ! empty( $parsed ) ) {
				$specs = array_merge( $specs, $parsed );
			}
		}

		return $specs;
	}

	/**
	 * @param string|string[] $input Input.
	 * @return string[]
	 */
	private static function normalize_lines( $input ) {
		if ( is_array( $input ) ) {
			$lines = $input;
		} else {
			$text  = wp_strip_all_tags( (string) $input );
			$text  = html_entity_decode( $text, ENT_QUOTES | ENT_HTML5, 'UTF-8' );
			$lines = preg_split( '/\r\n|\r|\n|<br\s*\/?>/i', $text );
		}

		if ( ! is_array( $lines ) ) {
			return array();
		}

		$out = array();
		foreach ( $lines as $line ) {
			$line = trim( preg_replace( '/\s+/u', ' ', (string) $line ) );
			if ( '' !== $line ) {
				$out[] = $line;
			}
		}

		return $out;
	}

	/**
	 * @param string $line One schedule line.
	 * @return array<int, array<string, mixed>>
	 */
	private static function parse_line( $line ) {
		$line = mb_strtolower( $line, 'UTF-8' );

		if ( ! preg_match( '/(\d{1,2})[:\-.](\d{2}).*?(\d{1,2})[:\-.](\d{2})/u', $line, $time_match ) ) {
			return array();
		}

		$opens  = sprintf( '%02d:%02d', (int) $time_match[1], (int) $time_match[2] );
		$closes = sprintf( '%02d:%02d', (int) $time_match[3], (int) $time_match[4] );

		$days = self::extract_days( $line );
		if ( empty( $days ) ) {
			return array();
		}

		return array(
			array(
				'@type'     => 'OpeningHoursSpecification',
				'dayOfWeek' => $days,
				'opens'     => $opens,
				'closes'    => $closes,
			),
		);
	}

	/**
	 * @param string $line Lowercased line.
	 * @return string[]
	 */
	private static function extract_days( $line ) {
		$map = array(
			'пн' => 'Monday',
			'вт' => 'Tuesday',
			'ср' => 'Wednesday',
			'чт' => 'Thursday',
			'пт' => 'Friday',
			'сб' => 'Saturday',
			'вс' => 'Sunday',
		);

		if ( preg_match( '/(пн|вт|ср|чт|пт|сб|вс)\s*-\s*(пн|вт|ср|чт|пт|сб|вс)/u', $line, $range ) ) {
			$order = array( 'пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс' );
			$start = array_search( $range[1], $order, true );
			$end   = array_search( $range[2], $order, true );
			if ( false === $start || false === $end ) {
				return array();
			}

			$days = array();
			if ( $start <= $end ) {
				for ( $i = $start; $i <= $end; $i++ ) {
					$days[] = $map[ $order[ $i ] ];
				}
			} else {
				for ( $i = $start; $i < count( $order ); $i++ ) {
					$days[] = $map[ $order[ $i ] ];
				}
				for ( $i = 0; $i <= $end; $i++ ) {
					$days[] = $map[ $order[ $i ] ];
				}
			}

			return array_values( array_unique( $days ) );
		}

		$days = array();
		foreach ( $map as $ru => $en ) {
			if ( preg_match( '/\b' . preg_quote( $ru, '/' ) . '\b/u', $line ) ) {
				$days[] = $en;
			}
		}

		return array_values( array_unique( $days ) );
	}
}
