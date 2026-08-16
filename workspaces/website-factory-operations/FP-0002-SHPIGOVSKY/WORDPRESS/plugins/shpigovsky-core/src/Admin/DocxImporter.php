<?php
/**
 * Blog DOCX → WordPress draft importer — PROD-P13.
 *
 * @package Shpigovsky_Core
 */

namespace Shpigovsky\Core\Admin;

use Shpigovsky\Core\Contracts\ModuleInterface;
use Shpigovsky\Core\ModuleRegistry;

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Admin workflow: upload DOCX, create drafts, review, schedule.
 */
final class DocxImporter implements ModuleInterface {

	public const MENU_SLUG   = 'fp02-docx-import';
	public const ACTION      = 'fp02_docx_import';
	public const DISCARD     = 'fp02_docx_discard';
	public const SCHEDULE    = 'fp02_docx_schedule';
	public const TEMPLATE    = 'fp02_docx_template';
	public const MAX_BYTES   = 15728640;
	public const MAX_FILES   = 8;

	/**
	 * {@inheritdoc}
	 */
	public static function id() {
		return 'admin.docx-importer';
	}

	/**
	 * {@inheritdoc}
	 */
	public static function is_enabled() {
		return ModuleRegistry::is_enabled( self::id() );
	}

	/**
	 * {@inheritdoc}
	 */
	public static function register() {
		add_action( 'admin_menu', array( __CLASS__, 'register_menu' ) );
		add_action( 'admin_post_' . self::ACTION, array( __CLASS__, 'handle_import' ) );
		add_action( 'admin_post_' . self::DISCARD, array( __CLASS__, 'handle_discard' ) );
		add_action( 'admin_post_' . self::SCHEDULE, array( __CLASS__, 'handle_schedule' ) );
		add_action( 'admin_post_' . self::TEMPLATE, array( __CLASS__, 'handle_template_download' ) );
	}

	/**
	 * Posts submenu.
	 */
	public static function register_menu() {
		add_submenu_page(
			'edit.php',
			__( 'Import from Word', 'shpigovsky-core' ),
			__( 'Import from Word', 'shpigovsky-core' ),
			'edit_posts',
			self::MENU_SLUG,
			array( __CLASS__, 'render_page' )
		);
	}

	/**
	 * Admin screen.
	 */
	public static function render_page() {
		if ( ! current_user_can( 'edit_posts' ) ) {
			wp_die( esc_html__( 'Insufficient permissions.', 'shpigovsky-core' ) );
		}

		$notice = isset( $_GET['fp02_docx_notice'] ) ? sanitize_key( wp_unslash( $_GET['fp02_docx_notice'] ) ) : ''; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		$results = get_transient( 'fp02_docx_last_results_' . get_current_user_id() );

		echo '<div class="wrap">';
		echo '<h1>' . esc_html__( 'Import articles from Word', 'shpigovsky-core' ) . '</h1>';
		echo '<p class="description">' . esc_html__( 'Upload one or more .docx files. Drafts are created for review — nothing is published automatically.', 'shpigovsky-core' ) . '</p>';

		if ( 'discarded' === $notice ) {
			echo '<div class="notice notice-success is-dismissible"><p>' . esc_html__( 'Draft discarded.', 'shpigovsky-core' ) . '</p></div>';
		}
		if ( 'scheduled' === $notice ) {
			echo '<div class="notice notice-success is-dismissible"><p>' . esc_html__( 'Publication date saved.', 'shpigovsky-core' ) . '</p></div>';
		}

		echo '<p><a class="button" href="' . esc_url( admin_url( 'admin-post.php?action=' . self::TEMPLATE . '&_wpnonce=' . wp_create_nonce( self::TEMPLATE ) ) ) . '">' . esc_html__( 'Download article template (.docx)', 'shpigovsky-core' ) . '</a></p>';

		echo '<form method="post" action="' . esc_url( admin_url( 'admin-post.php' ) ) . '" enctype="multipart/form-data" class="card" style="max-width:720px;padding:16px;">';
		wp_nonce_field( self::ACTION );
		echo '<input type="hidden" name="action" value="' . esc_attr( self::ACTION ) . '" />';
		echo '<p><label for="fp02_docx_files"><strong>' . esc_html__( 'Word files (.docx)', 'shpigovsky-core' ) . '</strong></label></p>';
		echo '<input type="file" id="fp02_docx_files" name="fp02_docx_files[]" accept=".docx,application/vnd.openxmlformats-officedocument.wordprocessingml.document" multiple required />';
		submit_button( __( 'Create drafts', 'shpigovsky-core' ) );
		echo '</form>';

		if ( is_array( $results ) && ! empty( $results ) ) {
			echo '<h2>' . esc_html__( 'Last import', 'shpigovsky-core' ) . '</h2>';
			echo '<table class="widefat striped"><thead><tr>';
			echo '<th>' . esc_html__( 'File', 'shpigovsky-core' ) . '</th>';
			echo '<th>' . esc_html__( 'Status', 'shpigovsky-core' ) . '</th>';
			echo '<th>' . esc_html__( 'Draft', 'shpigovsky-core' ) . '</th>';
			echo '<th>' . esc_html__( 'Actions', 'shpigovsky-core' ) . '</th>';
			echo '</tr></thead><tbody>';
			foreach ( $results as $row ) {
				echo '<tr>';
				echo '<td>' . esc_html( isset( $row['file'] ) ? $row['file'] : '' ) . '</td>';
				echo '<td>' . esc_html( isset( $row['status'] ) ? $row['status'] : '' ) . '</td>';
				echo '<td>';
				if ( ! empty( $row['post_id'] ) ) {
					$edit = get_edit_post_link( (int) $row['post_id'], 'raw' );
					$title = get_the_title( (int) $row['post_id'] );
					if ( $edit ) {
						printf( '<a href="%s">%s</a>', esc_url( $edit ), esc_html( $title ) );
					} else {
						echo esc_html( $title );
					}
				} elseif ( ! empty( $row['error'] ) ) {
					echo '<span class="description">' . esc_html( $row['error'] ) . '</span>';
				}
				echo '</td><td>';
				if ( ! empty( $row['post_id'] ) ) {
					self::render_row_actions( (int) $row['post_id'] );
				}
				echo '</td></tr>';
			}
			echo '</tbody></table>';
		}

		echo '</div>';
	}

	/**
	 * Per-draft discard + schedule controls.
	 *
	 * @param int $post_id Post ID.
	 */
	private static function render_row_actions( $post_id ) {
		$discard_url = wp_nonce_url(
			admin_url( 'admin-post.php?action=' . self::DISCARD . '&post_id=' . $post_id ),
			self::DISCARD . '_' . $post_id
		);
		$post = get_post( $post_id );
		$date = $post instanceof \WP_Post ? mysql2date( 'Y-m-d\TH:i', $post->post_date ) : '';

		echo '<a class="button button-small" href="' . esc_url( $discard_url ) . '">' . esc_html__( 'Discard draft', 'shpigovsky-core' ) . '</a> ';
		echo '<form method="post" action="' . esc_url( admin_url( 'admin-post.php' ) ) . '" style="display:inline-block;margin-left:8px;">';
		wp_nonce_field( self::SCHEDULE . '_' . $post_id );
		echo '<input type="hidden" name="action" value="' . esc_attr( self::SCHEDULE ) . '" />';
		echo '<input type="hidden" name="post_id" value="' . (int) $post_id . '" />';
		echo '<input type="datetime-local" name="fp02_publish_at" value="' . esc_attr( $date ) . '" /> ';
		submit_button( __( 'Schedule', 'shpigovsky-core' ), 'secondary small', 'submit', false );
		echo '</form>';
	}

	/**
	 * Import handler.
	 */
	public static function handle_import() {
		if ( ! current_user_can( 'edit_posts' ) ) {
			wp_die( esc_html__( 'Insufficient permissions.', 'shpigovsky-core' ) );
		}
		check_admin_referer( self::ACTION );

		$files   = self::normalize_files( isset( $_FILES['fp02_docx_files'] ) ? $_FILES['fp02_docx_files'] : array() ); // phpcs:ignore WordPress.Security.ValidatedSanitizedInput.InputNotSanitized
		$results = array();

		foreach ( array_slice( $files, 0, self::MAX_FILES ) as $file ) {
			$results[] = self::import_one( $file );
		}

		if ( empty( $results ) ) {
			$results[] = array(
				'file'   => '',
				'status' => __( 'Error', 'shpigovsky-core' ),
				'error'  => __( 'No files received.', 'shpigovsky-core' ),
			);
		}

		set_transient( 'fp02_docx_last_results_' . get_current_user_id(), $results, HOUR_IN_SECONDS );
		wp_safe_redirect( admin_url( 'edit.php?page=' . self::MENU_SLUG ) );
		exit;
	}

	/**
	 * Discard one draft created by this importer.
	 */
	public static function handle_discard() {
		if ( ! current_user_can( 'delete_posts' ) ) {
			wp_die( esc_html__( 'Insufficient permissions.', 'shpigovsky-core' ) );
		}
		$post_id = isset( $_GET['post_id'] ) ? absint( $_GET['post_id'] ) : 0; // phpcs:ignore WordPress.Security.NonceVerification.Recommended
		check_admin_referer( self::DISCARD . '_' . $post_id );
		$post = get_post( $post_id );
		if ( $post instanceof \WP_Post && 'post' === $post->post_type && 'fp02-docx' === get_post_meta( $post_id, '_fp02_docx_import', true ) ) {
			wp_delete_post( $post_id, true );
		}
		wp_safe_redirect( admin_url( 'edit.php?page=' . self::MENU_SLUG . '&fp02_docx_notice=discarded' ) );
		exit;
	}

	/**
	 * Schedule / set publication date via normal WP status.
	 */
	public static function handle_schedule() {
		if ( ! current_user_can( 'publish_posts' ) ) {
			wp_die( esc_html__( 'Insufficient permissions.', 'shpigovsky-core' ) );
		}
		$post_id = isset( $_POST['post_id'] ) ? absint( $_POST['post_id'] ) : 0;
		check_admin_referer( self::SCHEDULE . '_' . $post_id );
		$post = get_post( $post_id );
		if ( ! $post instanceof \WP_Post || 'post' !== $post->post_type ) {
			wp_safe_redirect( admin_url( 'edit.php?page=' . self::MENU_SLUG ) );
			exit;
		}

		$raw = isset( $_POST['fp02_publish_at'] ) ? sanitize_text_field( wp_unslash( $_POST['fp02_publish_at'] ) ) : '';
		$ts  = $raw !== '' ? strtotime( $raw ) : false;
		if ( false === $ts ) {
			wp_safe_redirect( admin_url( 'edit.php?page=' . self::MENU_SLUG ) );
			exit;
		}

		$mysql = wp_date( 'Y-m-d H:i:s', $ts );
		$now   = current_time( 'timestamp' );
		$status = $ts > $now ? 'future' : 'publish';

		wp_update_post(
			array(
				'ID'            => $post_id,
				'post_date'     => $mysql,
				'post_date_gmt' => get_gmt_from_date( $mysql ),
				'post_status'   => $status,
			)
		);

		wp_safe_redirect( admin_url( 'edit.php?page=' . self::MENU_SLUG . '&fp02_docx_notice=scheduled' ) );
		exit;
	}

	/**
	 * Serve the bundled author template.
	 */
	public static function handle_template_download() {
		if ( ! current_user_can( 'edit_posts' ) ) {
			wp_die( esc_html__( 'Insufficient permissions.', 'shpigovsky-core' ) );
		}
		check_admin_referer( self::TEMPLATE );

		$path = SHPIGOVSKY_CORE_DIR . 'assets/docx/fp02-article-template.docx';
		if ( ! is_readable( $path ) ) {
			wp_die( esc_html__( 'Template is not available.', 'shpigovsky-core' ) );
		}

		header( 'Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document' );
		header( 'Content-Disposition: attachment; filename="fp02-shablon-stati.docx"' );
		header( 'Content-Length: ' . (string) filesize( $path ) );
		readfile( $path ); // phpcs:ignore WordPress.WP.AlternativeFunctions.file_system_operations_readfile
		exit;
	}

	/**
	 * Normalize $_FILES multi-upload.
	 *
	 * @param array<string, mixed> $bag Files bag.
	 * @return array<int, array<string, mixed>>
	 */
	private static function normalize_files( $bag ) {
		$out = array();
		if ( empty( $bag['name'] ) ) {
			return $out;
		}
		$names = is_array( $bag['name'] ) ? $bag['name'] : array( $bag['name'] );
		foreach ( $names as $i => $name ) {
			$out[] = array(
				'name'     => (string) $name,
				'tmp_name' => is_array( $bag['tmp_name'] ) ? (string) $bag['tmp_name'][ $i ] : (string) $bag['tmp_name'],
				'size'     => is_array( $bag['size'] ) ? (int) $bag['size'][ $i ] : (int) $bag['size'],
				'error'    => is_array( $bag['error'] ) ? (int) $bag['error'][ $i ] : (int) $bag['error'],
				'type'     => is_array( $bag['type'] ) ? (string) $bag['type'][ $i ] : (string) $bag['type'],
			);
		}
		return $out;
	}

	/**
	 * Import a single DOCX into a draft post.
	 *
	 * @param array<string, mixed> $file File row.
	 * @return array<string, mixed>
	 */
	private static function import_one( $file ) {
		$name = isset( $file['name'] ) ? (string) $file['name'] : 'file.docx';
		$base = array( 'file' => $name, 'status' => __( 'Error', 'shpigovsky-core' ) );

		if ( ! empty( $file['error'] ) ) {
			$base['error'] = __( 'Upload failed.', 'shpigovsky-core' );
			return $base;
		}
		if ( (int) $file['size'] > self::MAX_BYTES ) {
			$base['error'] = __( 'File is too large (15 MB max).', 'shpigovsky-core' );
			return $base;
		}

		$tmp = isset( $file['tmp_name'] ) ? (string) $file['tmp_name'] : '';
		if ( '' === $tmp || ! is_uploaded_file( $tmp ) ) {
			$base['error'] = __( 'Temporary file is missing.', 'shpigovsky-core' );
			return $base;
		}

		$ext = strtolower( pathinfo( $name, PATHINFO_EXTENSION ) );
		if ( 'docx' !== $ext ) {
			$base['error'] = __( 'Only .docx is supported.', 'shpigovsky-core' );
			return $base;
		}

		$ft = wp_check_filetype_and_ext( $tmp, $name );
		$ok_types = array(
			'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
			'application/zip',
		);
		if ( ! empty( $ft['type'] ) && ! in_array( $ft['type'], $ok_types, true ) ) {
			$base['error'] = __( 'MIME type is not a Word document.', 'shpigovsky-core' );
			return $base;
		}

		$parsed = self::parse_docx( $tmp, $name );
		if ( is_wp_error( $parsed ) ) {
			$base['error'] = $parsed->get_error_message();
			return $base;
		}

		$post_id = wp_insert_post(
			array(
				'post_type'    => 'post',
				'post_status'  => 'draft',
				'post_title'   => $parsed['title'],
				'post_content' => $parsed['content'],
				'post_author'  => get_current_user_id(),
			),
			true
		);

		if ( is_wp_error( $post_id ) || ! $post_id ) {
			$base['error'] = __( 'Could not create the draft.', 'shpigovsky-core' );
			return $base;
		}

		update_post_meta( (int) $post_id, '_fp02_docx_import', 'fp02-docx' );
		update_post_meta( (int) $post_id, '_fp02_docx_source', sanitize_file_name( $name ) );

		foreach ( $parsed['attachment_ids'] as $att_id ) {
			wp_update_post(
				array(
					'ID'          => (int) $att_id,
					'post_parent' => (int) $post_id,
				)
			);
		}

		return array(
			'file'    => $name,
			'status'  => __( 'Draft created', 'shpigovsky-core' ),
			'post_id' => (int) $post_id,
		);
	}

	/**
	 * Parse DOCX into title + safe HTML + attachment IDs.
	 *
	 * @param string $path Temp path.
	 * @param string $filename Original name.
	 * @return array{title:string,content:string,attachment_ids:array<int,int>}|\WP_Error
	 */
	private static function parse_docx( $path, $filename ) {
		if ( ! class_exists( 'ZipArchive' ) ) {
			return new \WP_Error( 'fp02_docx_zip', __( 'ZipArchive is required.', 'shpigovsky-core' ) );
		}

		$zip = new \ZipArchive();
		if ( true !== $zip->open( $path ) ) {
			return new \WP_Error( 'fp02_docx_open', __( 'The file is not a valid DOCX archive.', 'shpigovsky-core' ) );
		}

		$document = $zip->getFromName( 'word/document.xml' );
		$rels     = $zip->getFromName( 'word/_rels/document.xml.rels' );
		if ( false === $document ) {
			$zip->close();
			return new \WP_Error( 'fp02_docx_xml', __( 'document.xml is missing.', 'shpigovsky-core' ) );
		}

		$rel_map = self::parse_rels( is_string( $rels ) ? $rels : '' );
		$media   = array();
		$used_media = array();

		libxml_use_internal_errors( true );
		$dom = new \DOMDocument();
		$dom->loadXML( $document, LIBXML_NONET | LIBXML_NOCDATA );
		$xpath = new \DOMXPath( $dom );
		$xpath->registerNamespace( 'w', 'http://schemas.openxmlformats.org/wordprocessingml/2006/main' );
		$xpath->registerNamespace( 'a', 'http://schemas.openxmlformats.org/drawingml/2006/main' );
		$xpath->registerNamespace( 'r', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships' );

		$title   = '';
		$blocks  = array();
		$list    = null;

		foreach ( $xpath->query( '//w:body/*' ) as $node ) {
			if ( ! $node instanceof \DOMElement ) {
				continue;
			}
			if ( 'p' === $node->localName ) {
				$style = self::paragraph_style( $xpath, $node );
				$is_list = self::is_list_item( $xpath, $node );
				$num_fmt = self::list_format( $xpath, $node );
				$html_inline = self::inline_html( $xpath, $node, $zip, $rel_map, $media, $used_media );
				$text = trim( wp_strip_all_tags( $html_inline ) );

				if ( in_array( $style, array( 'Title', 'heading 1', 'Heading1' ), true ) && '' === $title && '' !== $text ) {
					$title = $text;
					continue;
				}

				if ( $is_list && '' !== $text ) {
					$tag = ( 'decimal' === $num_fmt || 'ordered' === $num_fmt ) ? 'ol' : 'ul';
					if ( null === $list || $list['tag'] !== $tag ) {
						if ( null !== $list ) {
							$blocks[] = '<' . $list['tag'] . '>' . implode( '', $list['items'] ) . '</' . $list['tag'] . '>';
						}
						$list = array( 'tag' => $tag, 'items' => array() );
					}
					$list['items'][] = '<li>' . $html_inline . '</li>';
					continue;
				}

				if ( null !== $list ) {
					$blocks[] = '<' . $list['tag'] . '>' . implode( '', $list['items'] ) . '</' . $list['tag'] . '>';
					$list     = null;
				}

				if ( in_array( $style, array( 'Heading2', 'heading 2' ), true ) && '' !== $text ) {
					$blocks[] = '<h2>' . $html_inline . '</h2>';
					continue;
				}
				if ( in_array( $style, array( 'Heading3', 'heading 3' ), true ) && '' !== $text ) {
					$blocks[] = '<h3>' . $html_inline . '</h3>';
					continue;
				}
				if ( in_array( $style, array( 'Quote', 'IntenseQuote', 'BlockText' ), true ) && '' !== $html_inline ) {
					$blocks[] = '<blockquote>' . $html_inline . '</blockquote>';
					continue;
				}

				$images = self::paragraph_images( $xpath, $node, $zip, $rel_map, $media, $used_media );
				if ( '' === $text && ! empty( $images ) ) {
					foreach ( $images as $img_html ) {
						$blocks[] = $img_html;
					}
					continue;
				}

				if ( '' !== $html_inline ) {
					$blocks[] = '<p>' . $html_inline . '</p>';
				}
			}
		}

		if ( null !== $list ) {
			$blocks[] = '<' . $list['tag'] . '>' . implode( '', $list['items'] ) . '</' . $list['tag'] . '>';
		}

		$zip->close();

		if ( '' === $title ) {
			$title = preg_replace( '/\.docx$/i', '', $filename );
			$title = trim( str_replace( array( '-', '_' ), ' ', (string) $title ) );
		}

		$content = wp_kses_post( implode( "\n\n", $blocks ) );

		return array(
			'title'          => $title !== '' ? $title : __( 'Imported article', 'shpigovsky-core' ),
			'content'        => $content,
			'attachment_ids' => array_values( $media ),
		);
	}

	/**
	 * Relationship Id → target.
	 *
	 * @param string $xml Rels XML.
	 * @return array<string, string>
	 */
	private static function parse_rels( $xml ) {
		$map = array();
		if ( '' === $xml ) {
			return $map;
		}
		libxml_use_internal_errors( true );
		$dom = new \DOMDocument();
		$dom->loadXML( $xml, LIBXML_NONET | LIBXML_NOCDATA );
		foreach ( $dom->getElementsByTagName( 'Relationship' ) as $rel ) {
			$id  = $rel->getAttribute( 'Id' );
			$tgt = $rel->getAttribute( 'Target' );
			if ( '' !== $id && '' !== $tgt ) {
				$map[ $id ] = $tgt;
			}
		}
		return $map;
	}

	/**
	 * Paragraph style id.
	 *
	 * @param \DOMXPath  $xpath XPath.
	 * @param \DOMElement $p     Paragraph.
	 * @return string
	 */
	private static function paragraph_style( \DOMXPath $xpath, \DOMElement $p ) {
		$nodes = $xpath->query( './w:pPr/w:pStyle/@w:val', $p );
		if ( $nodes && $nodes->length ) {
			return (string) $nodes->item( 0 )->nodeValue;
		}
		return '';
	}

	/**
	 * Whether paragraph is a list item.
	 *
	 * @param \DOMXPath  $xpath XPath.
	 * @param \DOMElement $p     Paragraph.
	 * @return bool
	 */
	private static function is_list_item( \DOMXPath $xpath, \DOMElement $p ) {
		$nodes = $xpath->query( './w:pPr/w:numPr', $p );
		return $nodes && $nodes->length > 0;
	}

	/**
	 * Best-effort ordered vs unordered.
	 *
	 * @param \DOMXPath  $xpath XPath.
	 * @param \DOMElement $p     Paragraph.
	 * @return string
	 */
	private static function list_format( \DOMXPath $xpath, \DOMElement $p ) {
		$ilvl = $xpath->query( './w:pPr/w:numPr/w:ilvl/@w:val', $p );
		unset( $ilvl );
		$style = self::paragraph_style( $xpath, $p );
		if ( preg_match( '/number|decimal|ordered/i', $style ) ) {
			return 'decimal';
		}
		return 'bullet';
	}

	/**
	 * Inline runs to HTML.
	 *
	 * @param \DOMXPath              $xpath XPath.
	 * @param \DOMElement            $p     Paragraph.
	 * @param \ZipArchive            $zip   Zip.
	 * @param array<string, string>  $rel_map Rels.
	 * @param array<string, int>     $media Media map.
	 * @param array<string, bool>    $used_media Dedup.
	 * @return string
	 */
	private static function inline_html( \DOMXPath $xpath, \DOMElement $p, \ZipArchive $zip, array $rel_map, array &$media, array &$used_media ) {
		$html = '';
		foreach ( $xpath->query( './w:r|./w:hyperlink', $p ) as $node ) {
			if ( ! $node instanceof \DOMElement ) {
				continue;
			}
			if ( 'hyperlink' === $node->localName ) {
				$rid = $node->getAttributeNS( 'http://schemas.openxmlformats.org/officeDocument/2006/relationships', 'id' );
				$inner = '';
				foreach ( $xpath->query( './/w:t', $node ) as $t ) {
					$inner .= $t->textContent;
				}
				$href = '';
				if ( '' !== $rid && isset( $rel_map[ $rid ] ) && 0 === strpos( $rel_map[ $rid ], 'http' ) ) {
					$href = $rel_map[ $rid ];
				}
				if ( '' !== $href && '' !== $inner ) {
					$html .= '<a href="' . esc_url( $href ) . '">' . esc_html( $inner ) . '</a>';
				} else {
					$html .= esc_html( $inner );
				}
				continue;
			}

			$bold   = $xpath->query( './w:rPr/w:b', $node )->length > 0;
			$italic = $xpath->query( './w:rPr/w:i', $node )->length > 0;
			$text   = '';
			foreach ( $xpath->query( './w:t', $node ) as $t ) {
				$text .= $t->textContent;
			}
			if ( '' === $text ) {
				continue;
			}
			$chunk = esc_html( $text );
			if ( $bold ) {
				$chunk = '<strong>' . $chunk . '</strong>';
			}
			if ( $italic ) {
				$chunk = '<em>' . $chunk . '</em>';
			}
			$html .= $chunk;
		}

		foreach ( self::paragraph_images( $xpath, $p, $zip, $rel_map, $media, $used_media ) as $img ) {
			$html .= $img;
		}

		return trim( $html );
	}

	/**
	 * Extract images in a paragraph into WP media HTML.
	 *
	 * @param \DOMXPath             $xpath XPath.
	 * @param \DOMElement           $p     Paragraph.
	 * @param \ZipArchive           $zip   Zip.
	 * @param array<string, string> $rel_map Rels.
	 * @param array<string, int>    $media Media map.
	 * @param array<string, bool>   $used_media Dedup.
	 * @return array<int, string>
	 */
	private static function paragraph_images( \DOMXPath $xpath, \DOMElement $p, \ZipArchive $zip, array $rel_map, array &$media, array &$used_media ) {
		$out = array();
		$blips = $xpath->query( './/a:blip[@r:embed]', $p );
		if ( ! $blips ) {
			return $out;
		}
		foreach ( $blips as $blip ) {
			if ( ! $blip instanceof \DOMElement ) {
				continue;
			}
			$rid = $blip->getAttributeNS( 'http://schemas.openxmlformats.org/officeDocument/2006/relationships', 'embed' );
			if ( '' === $rid || ! isset( $rel_map[ $rid ] ) ) {
				continue;
			}
			$target = ltrim( str_replace( '\\', '/', $rel_map[ $rid ] ), '/' );
			if ( 0 === strpos( $target, '../' ) ) {
				continue;
			}
			$zip_path = 'word/' . $target;
			if ( 0 !== strpos( $zip_path, 'word/media/' ) ) {
				continue;
			}
			if ( isset( $used_media[ $zip_path ] ) ) {
				$att_id = $media[ $zip_path ];
			} else {
				$bytes = $zip->getFromName( $zip_path );
				if ( false === $bytes ) {
					continue;
				}
				$att_id = self::sideload_image( $zip_path, $bytes );
				if ( ! $att_id ) {
					continue;
				}
				$media[ $zip_path ]      = $att_id;
				$used_media[ $zip_path ] = true;
			}
			$html = wp_get_attachment_image( $att_id, 'large', false, array( 'class' => 'alignnone size-large' ) );
			if ( is_string( $html ) && '' !== $html ) {
				$caption = '';
				$doc_pr  = $xpath->query( './/wp:docPr/@descr|.//wp:docPr/@title', $p );
				unset( $doc_pr );
				$out[] = '<figure class="wp-block-image">' . $html . '</figure>';
			}
		}
		return $out;
	}

	/**
	 * Sideload image bytes into the Media Library.
	 *
	 * @param string $zip_path Zip path.
	 * @param string $bytes    Bytes.
	 * @return int
	 */
	private static function sideload_image( $zip_path, $bytes ) {
		$filename = sanitize_file_name( basename( $zip_path ) );
		if ( '' === $filename ) {
			$filename = 'docx-image.bin';
		}

		$upload = wp_upload_bits( $filename, null, $bytes );
		if ( ! empty( $upload['error'] ) ) {
			return 0;
		}

		$filetype = wp_check_filetype( $filename, null );
		$att_id   = wp_insert_attachment(
			array(
				'post_mime_type' => $filetype['type'] ? $filetype['type'] : 'image/jpeg',
				'post_title'     => preg_replace( '/\.[^.]+$/', '', $filename ),
				'post_status'    => 'inherit',
			),
			$upload['file']
		);
		if ( is_wp_error( $att_id ) || ! $att_id ) {
			return 0;
		}

		require_once ABSPATH . 'wp-admin/includes/image.php';
		$meta = wp_generate_attachment_metadata( $att_id, $upload['file'] );
		wp_update_attachment_metadata( $att_id, $meta );

		return (int) $att_id;
	}
}
