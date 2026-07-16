# Home gallery Swiper authority snapshot

From `v9-shell.js` `gallerySwiperOptions` / `shpigovskyGallerySwiperOptions`:

- slidesPerView: 4 (base; applies <431px)
- spaceBetween: 30
- loop: false
- autoplay: false
- navigation: false
- watchOverflow: true
- grabCursor: true
- pagination: clickable dots via `[data-gallery-pagination]`
- breakpoints:
  - 431: slidesPerView 2.15 / spaceBetween 10
  - 768: slidesPerView 3.15 / spaceBetween 20
  - 1025: slidesPerView 3.5 / spaceBetween 30

CSS authority (Home):

- `.home-gallery__wrapper { display:flex }`
- slide `min-width:0`
- image height 372px / max-height 310px; @1024 height 280px
- object-fit cover

Service category galleries already called the same options factory; FU01 aligned CSS image/wrapper chrome to Home.
