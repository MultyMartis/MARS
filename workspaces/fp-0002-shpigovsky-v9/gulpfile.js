const { src, dest, watch, series, parallel } = require('gulp');
const { deleteAsync } = require('del');
const fileInclude = require('gulp-file-include');
const plumber = require('gulp-plumber');
const sassCompiler = require('gulp-sass')(require('sass'));
const fs = require('fs');
const path = require('path');

const paths = {
  dist: 'dist',
  fontawesome: {
    root: path.join(
      __dirname,
      '..',
      '..',
      'shared',
      'assets',
      'icon-libraries',
      'Font Awesome Pro 5.15.4'
    ),
    cssBridge: path.join(__dirname, 'src', 'scss', 'vendors', 'fa-all.css'),
    webfontsDest: path.join('dist', 'assets', 'webfonts'),
  },
  html: {
    pages: 'src/pages/**/*.html',
    watch: ['src/pages/**/*.html', 'src/partials/**/*.html'],
    dest: 'dist/_html-staging/',
  },
  styles: {
    src: 'src/scss/style.scss',
    watch: 'src/scss/**/*.scss',
    dest: 'dist/assets/css/',
  },
  scripts: {
    src: 'src/js/main.js',
    watch: 'src/js/**/*.js',
    dest: 'dist/assets/js/',
  },
  images: {
    src: 'src/img/**/*',
    watch: 'src/img/**/*',
    dest: 'dist/assets/img/',
  },
  svg: {
    src: 'src/svg/**/*',
    watch: 'src/svg/**/*',
    dest: 'dist/assets/svg/',
  },
  fonts: {
    src: 'src/fonts/**/*',
    watch: 'src/fonts/**/*',
    dest: 'dist/assets/fonts/',
  },
  favicon: {
    src: 'src/favicon/**/*',
    watch: 'src/favicon/**/*',
    dest: 'dist/assets/favicon/',
  },
  video: {
    src: 'src/video/**/*',
    watch: 'src/video/**/*',
    dest: 'dist/assets/video/',
  },
  vendor: {
    swiperJs: 'node_modules/swiper/swiper-bundle.min.js',
    swiperCss: 'node_modules/swiper/swiper-bundle.min.css',
    swiperDest: 'dist/assets/vendor/swiper/',
    fancyboxJs: 'node_modules/@fancyapps/ui/dist/fancybox/fancybox.umd.js',
    fancyboxCss: 'node_modules/@fancyapps/ui/dist/fancybox/fancybox.css',
    fancyboxDest: 'dist/assets/vendor/fancybox/',
  },
};

function onError(title) {
  return plumber({
    errorHandler(err) {
      console.error(`[${title}]`, err.message || err);
      this.emit('end');
    },
  });
}

function assertFontAwesomeSource() {
  const root = paths.fontawesome.root;
  if (!fs.existsSync(root)) {
    throw new Error(
      `[Font Awesome] Shared source missing: ${root}\n` +
        'Expected: shared/assets/icon-libraries/Font Awesome Pro 5.15.4/'
    );
  }
  const allMin = path.join(root, 'css', 'all.min.css');
  if (!fs.existsSync(allMin)) {
    throw new Error(`[Font Awesome] all.min.css missing in shared source: ${allMin}`);
  }
  const webfontsDir = path.join(root, 'webfonts');
  if (!fs.existsSync(webfontsDir)) {
    throw new Error(`[Font Awesome] webfonts directory missing: ${webfontsDir}`);
  }
  return { root, allMin, webfontsDir };
}

function prepareFaBridge(done) {
  try {
    const { allMin } = assertFontAwesomeSource();
    fs.mkdirSync(path.dirname(paths.fontawesome.cssBridge), { recursive: true });
    fs.copyFileSync(allMin, paths.fontawesome.cssBridge);
    done();
  } catch (err) {
    done(err);
  }
}

function faWebfonts() {
  const { root, webfontsDir } = assertFontAwesomeSource();
  return src(
    [
      path.join(webfontsDir, '**', '*.woff'),
      path.join(webfontsDir, '**', '*.woff2'),
    ],
    { base: webfontsDir, allowEmpty: false }
  )
    .pipe(onError('Font Awesome webfonts'))
    .pipe(dest(paths.fontawesome.webfontsDest));
}

async function cleanDist() {
  await deleteAsync([paths.dist]);
}

function html() {
  return src(paths.html.pages)
    .pipe(onError('HTML'))
    .pipe(
      fileInclude({
        prefix: '@@',
        basepath: __dirname + '/src',
      })
    )
    .pipe(dest(paths.html.dest));
}

function styles() {
  return src(paths.styles.src, { allowEmpty: true })
    .pipe(onError('SCSS'))
    .pipe(sassCompiler({ outputStyle: 'expanded' }).on('error', sassCompiler.logError))
    .pipe(dest(paths.styles.dest));
}

function scripts() {
  return src(paths.scripts.src, { allowEmpty: true })
    .pipe(onError('JS'))
    .pipe(dest(paths.scripts.dest));
}

function images() {
  return src(paths.images.src, { allowEmpty: true })
    .pipe(onError('Images'))
    .pipe(dest(paths.images.dest));
}

function svg() {
  return src(paths.svg.src, { allowEmpty: true })
    .pipe(onError('SVG'))
    .pipe(dest(paths.svg.dest));
}

function fonts() {
  return src(paths.fonts.src, { allowEmpty: true })
    .pipe(onError('Fonts'))
    .pipe(dest(paths.fonts.dest));
}

function favicon() {
  return src(paths.favicon.src, { allowEmpty: true })
    .pipe(onError('Favicon'))
    .pipe(dest(paths.favicon.dest));
}

function video() {
  return src(paths.video.src, { allowEmpty: true })
    .pipe(onError('Video'))
    .pipe(dest(paths.video.dest));
}

function vendorSwiper() {
  return src([paths.vendor.swiperJs, paths.vendor.swiperCss], { allowEmpty: false })
    .pipe(onError('Swiper vendor'))
    .pipe(dest(paths.vendor.swiperDest));
}

function vendorFancybox() {
  return src([paths.vendor.fancyboxJs, paths.vendor.fancyboxCss], { allowEmpty: false })
    .pipe(onError('Fancybox vendor'))
    .pipe(dest(paths.vendor.fancyboxDest));
}

const build = series(
  cleanDist,
  prepareFaBridge,
  parallel(html, series(faWebfonts, styles), scripts, images, svg, fonts, favicon, video, vendorSwiper, vendorFancybox)
);

function watcher() {
  watch(paths.html.watch, html);
  watch(paths.styles.watch, styles);
  watch(paths.scripts.watch, scripts);
  watch(paths.images.watch, images);
  watch(paths.svg.watch, svg);
  watch(paths.fonts.watch, fonts);
  watch(paths.favicon.watch, favicon);
  watch(paths.video.watch, video);
}

const buildIncremental = series(
  prepareFaBridge,
  parallel(html, series(faWebfonts, styles), scripts, images, svg, fonts, favicon, video, vendorSwiper, vendorFancybox)
);

exports.clean = cleanDist;
exports.build = build;
exports.default = build;
exports.watch = series(build, watcher);
exports['watch:dev'] = series(buildIncremental, watcher);
