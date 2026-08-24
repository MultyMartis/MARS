<?php
/**
 * Medical organization + branch location graph nodes.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\StructuredData;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Builds MedicalClinic entities from current Admin-owned data.
 */
final class OrganizationBuilder {

	/**
	 * Primary organization + branch location nodes.
	 *
	 * @return array<int, array<string, mixed>>
	 */
	public static function build_nodes() {
		$nodes      = array();
		$main       = self::build_main_organization();
		$locations  = self::build_branch_locations();
		$branch_ids = array();

		foreach ( $locations as $location ) {
			if ( isset( $location['@id'] ) ) {
				$branch_ids[] = array( '@id' => $location['@id'] );
			}
			$nodes[] = $location;
		}

		if ( ! empty( $branch_ids ) ) {
			$main['subOrganization'] = $branch_ids;
		}

		array_unshift( $nodes, $main );

		return $nodes;
	}

	/**
	 * @return array<string, mixed>
	 */
	private static function build_main_organization() {
		$node = array(
			'@type' => 'MedicalClinic',
			'@id'   => EntityIds::organization(),
			'name'  => DataReaders::organization_name(),
			'url'   => EntityIds::base_url(),
		);

		$phone = DataReaders::primary_phone();
		if ( '' !== $phone ) {
			$node['telephone'] = $phone;
		}

		$email = DataReaders::site_email();
		if ( '' !== $email ) {
			$node['email'] = $email;
		}

		$address = self::postal_address( DataReaders::site_option( 'site_address' ) );
		if ( ! empty( $address ) ) {
			$node['address'] = $address;
		}

		$logo = DataReaders::site_logo_url();
		if ( '' !== $logo ) {
			$node['logo'] = $logo;
			$node['image'] = $logo;
		}

		$hours = OpeningHoursParser::parse( DataReaders::site_option( 'opening_hours' ) );
		if ( ! empty( $hours ) ) {
			$node['openingHoursSpecification'] = $hours;
		}

		return self::compact( $node );
	}

	/**
	 * @return array<int, array<string, mixed>>
	 */
	private static function build_branch_locations() {
		$rows  = DataReaders::contact_locations();
		$nodes = array();
		$phone = DataReaders::primary_phone();
		$index = 0;

		foreach ( $rows as $row ) {
			++$index;
			$title   = isset( $row['title'] ) ? trim( (string) $row['title'] ) : '';
			$address = isset( $row['address'] ) ? trim( (string) $row['address'] ) : '';

			if ( '' === $title && '' === $address ) {
				continue;
			}

			$key = '' !== $title ? sanitize_title( $title ) : 'branch-' . $index;
			if ( '' === $key ) {
				$key = 'branch-' . $index;
			}

			$node = array(
				'@type'              => 'MedicalClinic',
				'@id'                => EntityIds::location( $key ),
				'name'               => '' !== $title ? $title : DataReaders::organization_name(),
				'url'                => EntityIds::base_url() . '/kontakty/',
				'parentOrganization' => array(
					'@id' => EntityIds::organization(),
				),
			);

			if ( '' !== $phone ) {
				$node['telephone'] = $phone;
			}

			$email = isset( $row['email'] ) ? sanitize_email( (string) $row['email'] ) : '';
			if ( is_email( $email ) ) {
				$node['email'] = $email;
			} elseif ( '' !== DataReaders::site_email() ) {
				$node['email'] = DataReaders::site_email();
			}

			$postal = self::postal_address( $address );
			if ( ! empty( $postal ) ) {
				$node['address'] = $postal;
			}

			$hours_source = isset( $row['hours_html'] ) ? (string) $row['hours_html'] : '';
			$hours        = OpeningHoursParser::parse( $hours_source );
			if ( ! empty( $hours ) ) {
				$node['openingHoursSpecification'] = $hours;
			}

			$nodes[] = self::compact( $node );
		}

		return $nodes;
	}

	/**
	 * @param string $raw Raw address string.
	 * @return array<string, string>
	 */
	private static function postal_address( $raw ) {
		$raw = trim( (string) $raw );
		if ( '' === $raw ) {
			return array();
		}

		$address = array(
			'@type'          => 'PostalAddress',
			'streetAddress'  => $raw,
			'addressCountry' => 'RU',
		);

		if ( preg_match( '/^москва/u', mb_strtolower( $raw, 'UTF-8' ) ) ) {
			$address['addressLocality'] = 'Москва';
		} elseif ( preg_match( '/московск/u', mb_strtolower( $raw, 'UTF-8' ) ) ) {
			$address['addressRegion'] = 'Московская область';
		}

		return $address;
	}

	/**
	 * Remove empty optional properties.
	 *
	 * @param array<string, mixed> $node Node.
	 * @return array<string, mixed>
	 */
	private static function compact( array $node ) {
		foreach ( $node as $key => $value ) {
			if ( is_string( $value ) && '' === trim( $value ) ) {
				unset( $node[ $key ] );
			}
		}

		return $node;
	}
}
