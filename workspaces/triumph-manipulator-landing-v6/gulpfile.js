const { src, dest, watch, series, parallel } = require('gulp');
const { Transform } = require('stream');
const path = require('path');
const fileInclude = require('gulp-file-include');
const sass = require('gulp-sass')(require('sass'));
const postcss = require('gulp-postcss');
const autoprefixer = require('autoprefixer');
const cssnano = require('cssnano');
const rename = require('gulp-rename');
const terser = require('gulp-terser');
const plumber = require('gulp-plumber');
const { deleteAsync } = require('del');
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
  scripts: {
    src: 'src/js/**/*.js',
    watch: 'src/js/**/*.js',
    dest: 'dist/assets/js/',
  },
  images: {
    src: 'src/img/**/*.{jpg,jpeg,png,gif,svg,webp,avif}',
    watch: 'src/img/**/*.{jpg,jpeg,png,gif,svg,webp,avif}',
    dest: 'dist/assets/img/',
  },
  favicon: {
    src: 'src/favicon/**/*.*',
    watch: 'src/favicon/**/*.*',
    dest: 'dist/assets/favicon/',
  },
  vendorFontawesome: {
    src: 'src/assets/vendor/fontawesome/**/*.{css,woff,woff2}',
    watch: 'src/assets/vendor/fontawesome/**/*.{css,woff,woff2}',
    dest: 'dist/assets/vendor/fontawesome/',
  },
  fonts: {
    src: 'src/fonts/**/*.{woff,woff2}',
    watch: 'src/fonts/**/*.{woff,woff2}',
    dest: 'dist/assets/fonts/',
  },
  backend: {
    src: 'backend/**/*.php',
    watch: 'backend/**/*.php',
    dest: 'dist/',
  },
};

function onError(title) {
  return plumber({
    errorHandler: function (err) {
      const msg = (err && err.message) || (err && err.toString && err.toString()) || 'Unknown error';
      console.error(`[${title}]`, msg);
      this.emit('end');
    },
  });
}

async function cleanDist() {
  // Delete dist contents, not the folder — avoids EBUSY on Windows when dist/index.html
  // is open in a browser or editor (rmdir on dist itself fails while a file is locked).
  await deleteAsync([`${paths.dist}/**/*`], { force: true });
}

function assetPrefixForHtmlRelative(relativePath) {
  const dir = path.dirname(relativePath);
  const depth = dir === '.' ? 0 : dir.split(path.sep).filter(Boolean).length;
  return depth === 0 ? 'assets/' : `${'../'.repeat(depth)}assets/`;
}

function rewriteHtmlAssetPaths() {
  return new Transform({
    objectMode: true,
    transform(file, _enc, cb) {
      if (file.isBuffer()) {
        const prefix = assetPrefixForHtmlRelative(file.relative);
        const html = file.contents.toString().replace(/\/assets\//g, prefix);
        file.contents = Buffer.from(html);
      }
      cb(null, file);
    },
  });
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
    .pipe(rewriteHtmlAssetPaths())
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
  return src(paths.scripts.src, { sourcemaps: true, allowEmpty: true })
    .pipe(onError('JS'))
    .pipe(dest(paths.scripts.dest))
    .pipe(terser())
    .pipe(rename({ suffix: '.min' }))
    .pipe(dest(paths.scripts.dest));
}

function images() {
  return src(paths.images.src, { buffer: true, encoding: false, allowEmpty: true }).pipe(dest(paths.images.dest));
}

function favicon() {
  return src(paths.favicon.src, { buffer: true, encoding: false, allowEmpty: true }).pipe(dest(paths.favicon.dest));
}

function vendorFontawesome() {
  return src(paths.vendorFontawesome.src, { buffer: true, encoding: false, allowEmpty: true }).pipe(
    dest(paths.vendorFontawesome.dest)
  );
}

function fonts() {
  return src(paths.fonts.src, { buffer: true, encoding: false, allowEmpty: true }).pipe(dest(paths.fonts.dest));
}

function backend() {
  return src([paths.backend.src, '!backend/api/forms/send.php'], { base: 'backend', allowEmpty: true }).pipe(
    dest(path.join(paths.dist, 'backend'))
  );
}

const build = series(cleanDist, parallel(html, styles, scripts, images, favicon, vendorFontawesome, fonts, backend));

function watcher() {
  watch(paths.html.watch, html);
  watch(paths.styles.watch, styles);
  watch(paths.scripts.watch, scripts);
  watch(paths.images.watch, images);
  watch(paths.favicon.watch, favicon);
  watch(paths.vendorFontawesome.watch, vendorFontawesome);
  watch(paths.fonts.watch, fonts);
  watch(paths.backend.watch, backend);
}

exports.clean = cleanDist;
exports.build = build;
exports.default = build;
exports.watch = series(build, watcher);
