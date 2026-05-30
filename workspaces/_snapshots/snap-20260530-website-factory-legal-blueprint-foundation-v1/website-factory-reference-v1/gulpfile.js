const gulp = require('gulp');
const fileinclude = require('gulp-file-include');
const plumber = require('gulp-plumber');
const sass = require('gulp-sass')(require('sass'));

const paths = {
  pages: 'src/pages/**/*.html',
  scssEntry: 'src/scss/main.scss',
  js: [
    'src/js/core/lifecycle.js',
    'src/js/core/modal.js',
    'src/js/core/form.js',
    'src/js/sections/sticky_cta.js',
    'src/js/main.js'
  ]
};

function html() {
  return gulp
    .src(paths.pages)
    .pipe(plumber())
    .pipe(
      fileinclude({
        prefix: '@@',
        basepath: '@file'
      })
    )
    .pipe(gulp.dest('dist'));
}

function styles() {
  return gulp
    .src(paths.scssEntry)
    .pipe(plumber())
    .pipe(sass({ outputStyle: 'expanded' }).on('error', sass.logError))
    .pipe(gulp.dest('dist/css'));
}

function scripts() {
  return gulp.src(paths.js, { base: 'src' }).pipe(plumber()).pipe(gulp.dest('dist'));
}

const build = gulp.parallel(html, styles, scripts);

function watchFiles() {
  gulp.watch('src/pages/**/*.html', html);
  gulp.watch('src/partials/**/*.html', html);
  gulp.watch('src/scss/**/*.scss', styles);
  gulp.watch('src/js/**/*.js', scripts);
}

exports.html = html;
exports.styles = styles;
exports.scripts = scripts;
exports.build = build;
exports.watch = gulp.series(build, watchFiles);
exports.default = build;
