const { src, dest, watch, series, parallel } = require('gulp');

const fileInclude = require('gulp-file-include');
const sass = require('gulp-sass')(require('sass'));
const postcss = require('gulp-postcss');
const autoprefixer = require('autoprefixer');
const cssnano = require('cssnano');
const sourcemaps = require('gulp-sourcemaps');

const { deleteAsync } = require('del');

const rename = require('gulp-rename');
const terser = require('gulp-terser');

const svgSprite = require('gulp-svg-sprite');

const plumber = require('gulp-plumber');

const yargs = require('yargs');
const argv = yargs.argv;
const isProd = !!argv.prod;

const paths = {
  dist: 'dist',
  html: {
    pages: 'src/pages/**/*.html',
    watch: ['src/pages/**/*.html', 'src/partials/**/*.html'],
    dest: 'dist/',
  },
  styles: {
    src: 'src/scss/style.scss',
    watch: 'src/scss/**/*.scss',
    dest: 'dist/assets/css/',
  },
  vendorCss: {
    src: 'src/css/vendor/**/*.css',
    watch: 'src/css/vendor/**/*.css',
    dest: 'dist/assets/css/vendor/',
  },
  scripts: {
    src: 'src/js/**/*.js',
    watch: 'src/js/**/*.js',
    dest: 'dist/assets/js/',
  },
  images: {
    src: [
      'src/img/**/*.{jpg,jpeg,png,gif,svg,webp,avif}',
      '!src/img/**/sprite.svg',
    ],
    watch: 'src/img/**/*.{jpg,jpeg,png,gif,svg,webp,avif}',
    dest: 'dist/assets/img/',
  },
  fonts: {
    src: 'src/fonts/**/*.{woff,woff2}',
    watch: 'src/fonts/**/*.{woff,woff2}',
    dest: 'dist/assets/fonts/',
  },
  favicon: {
    src: 'src/favicon/**/*.*',
    watch: 'src/favicon/**/*.*',
    dest: 'dist/assets/favicon/',
  },
  svg: {
    src: 'src/svg/**/*.svg',
    watch: 'src/svg/**/*.svg',
    dest: 'dist/assets/img/',
  },
};

function onError(title) {
  return plumber({
    errorHandler: function (err) {
      const msg =
        (err && err.message) ||
        (err && err.toString && err.toString()) ||
        'Unknown error';

      console.error(`[${title}]`, msg);
      this.emit('end');
    },
  });
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
        context: {
          includeJquery: !isProd,
        },
      })
    )
    .pipe(dest(paths.html.dest));
}

function styles() {
  return src(paths.styles.src, { allowEmpty: true })
    .pipe(onError('SCSS'))
    .pipe(sass({ outputStyle: 'expanded' }))
    .pipe(dest(paths.styles.dest));
}

function vendorCss() {
  return src(paths.vendorCss.src, { allowEmpty: true })
    .pipe(onError('VENDOR CSS'))
    .pipe(dest(paths.vendorCss.dest));
}

function scripts() {
  return src(paths.scripts.src, { sourcemaps: true, allowEmpty: true })
    .pipe(onError('JS'))
    .pipe(dest(paths.scripts.dest))
    .pipe(terser({ module: true }))
    .pipe(rename({ suffix: '.min' }))
    .pipe(dest(paths.scripts.dest));
}

function images() {
  return src(paths.images.src, { buffer: true, encoding: false, allowEmpty: true })
    .pipe(onError('IMG'))
    .pipe(dest(paths.images.dest));
}

function fonts() {
  return src(paths.fonts.src, { buffer: true, encoding: false, allowEmpty: true })
    .pipe(onError('FONTS'))
    .pipe(dest(paths.fonts.dest));
}

function favicon() {
  return src(paths.favicon.src, { buffer: true, encoding: false, allowEmpty: true })
    .pipe(onError('FAVICON'))
    .pipe(dest(paths.favicon.dest));
}

function sprite() {
  return src(paths.svg.src, { allowEmpty: true })
    .pipe(onError('SVG SPRITE'))
    .pipe(
      svgSprite({
        shape: {
          transform: [],
        },
        svg: {
          xmlDeclaration: false,
          doctypeDeclaration: false,
        },
        mode: {
          symbol: {
            dest: '.',
            sprite: 'sprite.svg',
            example: false,
          },
        },
      })
    )
    .pipe(dest(paths.svg.dest));
}

const build = series(
  cleanDist,
  parallel(html, styles, vendorCss, scripts, images, fonts, favicon),
  sprite
);

function watcher() {
  watch(paths.html.watch, html);
  watch(paths.styles.watch, styles);
  watch(paths.vendorCss.watch, vendorCss);
  watch(paths.scripts.watch, scripts);
  watch(paths.images.watch, images);
  watch(paths.fonts.watch, fonts);
  watch(paths.favicon.watch, favicon);
  watch(paths.svg.watch, sprite);
}

exports.clean = cleanDist;
exports.sprite = sprite;
exports.build = build;
exports.default = build;
exports.watch = series(build, watcher);