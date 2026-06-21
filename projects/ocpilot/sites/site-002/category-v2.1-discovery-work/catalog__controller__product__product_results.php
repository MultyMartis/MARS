<?php

if (!isset($url)) $url ='';
if (isset($this->request->get['path'])) $path = 'path=' . $this->request->get['path']; else $path ='';

$cartproducts = $this->cart->getProducts();


			
foreach ($results as $result) {
				if ($result['image']) {
					$image = $this->model_tool_image->resize($result['image'], $this->config->get('theme_' . $this->config->get('config_theme') . '_image_product_width'), $this->config->get('theme_' . $this->config->get('config_theme') . '_image_product_height'));
				} else {
					$image = $this->model_tool_image->resize('placeholder.png', $this->config->get('theme_' . $this->config->get('config_theme') . '_image_product_width'), $this->config->get('theme_' . $this->config->get('config_theme') . '_image_product_height'));
				}

				$cartqty = 0;
				if (!empty($cartproducts))
					{
						foreach ($cartproducts as $cp)
							{
								if ($cp['product_id'] == $result['product_id']) $cartqty = $cp['quantity'];
							}
					}

				$pricecalc = 0;

				if ($this->customer->isLogged() || !$this->config->get('config_customer_price')) {
					$pricecalc = $result['price'];
					$price = $this->currency->format($this->tax->calculate($result['price'], $result['tax_class_id'], $this->config->get('config_tax')), $this->session->data['currency']);
				} else {
					$price = false;
				}

				$oldprice = false; $priceproc = false;

				if ($result['special'] !== false && (float)$result['special'] > 0) {
					if ($result['price']!=0)
						$priceproc = "-".intval(( $result['price'] - $result['special']) /  $result['price'] *100)."%";
					
					$oldprice =  $this->currency->format($this->tax->calculate($result['price'], $result['tax_class_id'], $this->config->get('config_tax')), $this->session->data['currency']);
					$pricecalc = $result['special'];
					$price = $this->currency->format($this->tax->calculate($result['special'], $result['tax_class_id'], $this->config->get('config_tax')), $this->session->data['currency']);
					$special = $this->currency->format($this->tax->calculate($result['special'], $result['tax_class_id'], $this->config->get('config_tax')), $this->session->data['currency']);
					$tax_price = (float)$result['special'];
				} else {
					$special = false;
					$tax_price = (float)$result['price'];
				}
	
				if ($this->config->get('config_tax')) {
					$tax = $this->currency->format($tax_price, $this->session->data['currency']);
				} else {
					$tax = false;
				}

				if ($this->config->get('config_review_status')) {
					$rating = (int)$result['rating'];
				} else {
					$rating = false;
				}

				$canCart = true;
				$statusText = "Цена по запросу";
				$deliveryText = '';
				$ctaText = "ctaText";

				$classstatus = 'in-stock';

				
				if ($result['quantity']>0) {
						$statusText = "В наличии: ".$result['quantity']." шт.";						
						$classstatus = 'in-stock';
					} else {

						$statusText = "Под заказ";
						if ($pricecalc >0)
							$deliveryText = "Срок поставки 5–10 дней";
						$canCart = true;
						$classstatus = 'in-stock';
				}

				if ($pricecalc == 0) {
						$canCart = false;
						$classstatus = 'order';
						$price = 'По запросу';
				
				}



				$wishlisted = $this->model_catalog_product->isWishlisted($result['product_id']);
				$compared = $this->model_catalog_product->isCompared($result['product_id']);






				$card = array(
					'product_id'  => $result['product_id'],
					'model'		=> $result['model'],
					'thumb'       => $image,
					'name'        => $result['name'],
					'description' => utf8_substr(trim(strip_tags(html_entity_decode($result['description'], ENT_QUOTES, 'UTF-8'))), 0, $this->config->get('theme_' . $this->config->get('config_theme') . '_product_description_length')) . '..',
					'price'       => $price,
					'special'     => $special,
					'tax'         => $tax,
					'minimum'     => $result['minimum'] > 0 ? $result['minimum'] : 1,
					'rating'      => $result['rating'],
					'href'        => $this->url->link('product/product', $path . '&product_id=' . $result['product_id'] . $url),
					'canCart' 	=> $canCart,
					'statusText' => $statusText,
					'deliveryText' => $deliveryText,
					'ctaText'		=> $ctaText,
					'oldPrice'		=> $oldprice,
					'wishlisted'	=>$wishlisted,
					'compared'		=> $compared,
					'priceproc'		=>$priceproc,
					'classstatus'	=> $classstatus,
					'cartqty'		 =>$cartqty,
				);

				$data['productcards'][$result['product_id']] = $this->load->view('product/productcard', $card);
				
				/*$data['products'][] = array(
					'product_id'  => $result['product_id'],
					'thumb'       => $image,
					'name'        => $result['name'],
					'description' => utf8_substr(trim(strip_tags(html_entity_decode($result['description'], ENT_QUOTES, 'UTF-8'))), 0, $this->config->get('theme_' . $this->config->get('config_theme') . '_product_description_length')) . '..',
					'price'       => $price,
					'special'     => $special,
					'tax'         => $tax,
					'minimum'     => $result['minimum'] > 0 ? $result['minimum'] : 1,
					'rating'      => $result['rating'],
					'href'        => $this->url->link('product/product', $path . '&product_id=' . $result['product_id'] . $url)
				);*/
				
			}

