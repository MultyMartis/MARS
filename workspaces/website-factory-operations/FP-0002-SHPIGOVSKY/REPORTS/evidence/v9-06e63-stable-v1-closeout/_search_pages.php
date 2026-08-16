<?php
require 'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-load.php';
foreach (['а','е','и','о','у','центр','лечение','зависимости','Шпиговский'] as $term) {
  $q = new WP_Query(['s'=>$term,'post_type'=>['post','page','service'],'posts_per_page'=>12]);
  echo $term."\t".$q->found_posts."\t".$q->max_num_pages."\n";
}
