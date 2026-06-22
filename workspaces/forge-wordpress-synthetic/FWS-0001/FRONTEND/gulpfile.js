const { src, dest, watch, series, parallel } = require('gulp');
const fileInclude = require('gulp-file-include');
const sass = require('gulp-sass')(require('sass'));
const postcss = require('gulp-postcss');
const autoprefixer = require('autoprefixer');
const cssnano = require('cssnano');
const plumber = require('gulp-plumber');
const terser = require('gulp-terser');
const { deleteAsync } = require('del');
const yargs = require('yargs');
const isProd = !!yargs.argv.prod;

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
};

function onError(title) {
  return plumber({
    errorHandler(err) {
      console.error(`[${title}]`, err.message);
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
      })
    )
    .pipe(dest(paths.html.dest));
}

function styles() {
  const plugins = [autoprefixer()];
  if (isProd) plugins.push(cssnano());
  return src(paths.styles.src)
    .pipe(onError('SCSS'))
    .pipe(sass({ outputStyle: isProd ? 'compressed' : 'expanded' }))
    .pipe(postcss(plugins))
    .pipe(dest(paths.styles.dest));
}

function scripts() {
  let stream = src(paths.scripts.src).pipe(onError('JS')).pipe(dest(paths.scripts.dest));
  if (isProd) {
    stream = stream.pipe(terser()).pipe(dest(paths.scripts.dest));
  }
  return stream;
}

const build = series(cleanDist, parallel(html, styles, scripts));

function watcher() {
  watch(paths.html.watch, html);
  watch(paths.styles.watch, styles);
  watch(paths.scripts.watch, scripts);
}

exports.build = build;
exports.watch = series(build, watcher);
exports.default = build;
