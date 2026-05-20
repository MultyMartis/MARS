const { src, dest, watch, series, parallel } = require('gulp');
const fileInclude = require('gulp-file-include');
const sass = require('gulp-sass')(require('sass'));
const postcss = require('gulp-postcss');
const autoprefixer = require('autoprefixer');
const cssnano = require('cssnano');
const plumber = require('gulp-plumber');
const rename = require('gulp-rename');
const terser = require('gulp-terser');
const { deleteAsync } = require('del');
const yargs = require('yargs');

const argv = yargs.argv;
const isProd = Boolean(argv.prod);

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
  scripts: {
    src: 'src/js/**/*.js',
    watch: 'src/js/**/*.js',
    dest: 'dist/assets/js/',
  },
  assets: {
    src: [
      'src/assets/**/*.{css,jpg,jpeg,png,gif,svg,webp,avif,ico}',
      '!src/assets/vendor/fontawesome/webfonts/*.svg',
      'src/assets/**/*.woff',
      'src/assets/**/*.woff2',
    ],
    watch: [
      'src/assets/**/*.{css,jpg,jpeg,png,gif,svg,webp,avif,ico}',
      '!src/assets/vendor/fontawesome/webfonts/*.svg',
      'src/assets/**/*.woff',
      'src/assets/**/*.woff2',
    ],
    dest: 'dist/assets/',
  },
};

function onError(title) {
  return plumber({
    errorHandler(error) {
      const message = (error && error.message) || String(error || 'Unknown error');
      console.error(`[${title}]`, message);
      this.emit('end');
    },
  });
}

async function clean() {
  await deleteAsync([paths.dist]);
}

function html() {
  return src(paths.html.pages, { allowEmpty: true })
    .pipe(onError('HTML'))
    .pipe(
      fileInclude({
        prefix: '@@',
        basepath: 'src',
        context: {
          isProd,
        },
      })
    )
    .pipe(dest(paths.html.dest));
}

function styles() {
  const plugins = [autoprefixer()];

  if (isProd) {
    plugins.push(cssnano());
  }

  return src(paths.styles.src, { allowEmpty: true })
    .pipe(onError('SCSS'))
    .pipe(sass({ outputStyle: 'expanded' }))
    .pipe(postcss(plugins))
    .pipe(dest(paths.styles.dest));
}

function scripts() {
  const pipeline = src(paths.scripts.src, { allowEmpty: true })
    .pipe(onError('JS'))
    .pipe(dest(paths.scripts.dest));

  if (!isProd) {
    return pipeline;
  }

  return pipeline
    .pipe(terser())
    .pipe(rename({ suffix: '.min' }))
    .pipe(dest(paths.scripts.dest));
}

function assets() {
  return src(paths.assets.src, { buffer: true, encoding: false, allowEmpty: true })
    .pipe(onError('ASSETS'))
    .pipe(dest(paths.assets.dest));
}

const build = series(clean, parallel(html, styles, scripts, assets));

function watcher() {
  watch(paths.html.watch, html);
  watch(paths.styles.watch, styles);
  watch(paths.scripts.watch, scripts);
  watch(paths.assets.watch, assets);
}

exports.clean = clean;
exports.build = build;
exports.default = build;
exports.watch = series(build, watcher);
