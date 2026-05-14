const { src, dest, watch, series, parallel } = require('gulp');

const fileInclude = require('gulp-file-include');
const sass = require('gulp-sass')(require('sass'));
const postcss = require('gulp-postcss');
const autoprefixer = require('autoprefixer');
const cssnano = require('cssnano');
const sourcemaps = require('gulp-sourcemaps');

const { deleteAsync } = require('del');

const fs = require('fs');
const path = require('path');

const rename = require('gulp-rename');
const terser = require('gulp-terser');

const svgSprite = require('gulp-svg-sprite');

const plumber = require('gulp-plumber');

const yargs = require('yargs');
const argv = yargs.argv;
const isProd = !!argv.prod;

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
    dest: path.join('dist', 'assets', 'vendor', 'fontawesome'),
  },
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

function vendorFontawesome(done) {
  const root = paths.fontawesome.root;
  if (!fs.existsSync(root)) {
    console.warn('[vendorFontawesome] Font Awesome Pro folder missing, skipping:', root);
    done();
    return;
  }
  src(['css/all.min.css', 'webfonts/**/*'], { cwd: root, allowEmpty: true })
    .pipe(onError('FONTAWESOME'))
    .pipe(dest(paths.fontawesome.dest))
    .on('end', done);
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
          id: {
            generator: function (name) {
              const base = String(name || '')
                .replace(/\.svg$/i, '')
                .replace(/\s+/g, '-');
              return 'i-' + base;
            },
          },
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

const SPRITE_MARKER_START = '<!--SVG-SPRITE-START-->';
const SPRITE_MARKER_END = '<!--SVG-SPRITE-END-->';

function injectInlineSprite(done) {
  const distDir = path.join(__dirname, paths.dist);
  const spritePath = path.join(distDir, 'assets', 'img', 'sprite.svg');

  if (!fs.existsSync(spritePath)) {
    console.warn('[injectInlineSprite] sprite.svg missing, skipping');
    return done();
  }

  const spriteRaw = fs.readFileSync(spritePath, 'utf8').trim();
  if (!/^<svg\b[^>]*>/i.test(spriteRaw) || !/<\/svg>\s*$/i.test(spriteRaw)) {
    console.warn('[injectInlineSprite] unexpected sprite.svg format, skipping');
    return done();
  }

  const inner = spriteRaw
    .replace(/^<svg\b[^>]*>/i, '')
    .replace(/<\/svg>\s*$/i, '')
    .trim();

  const spriteBlock =
    SPRITE_MARKER_START +
    '\n' +
    '<div class="svg-sprite" aria-hidden="true">' +
    '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" focusable="false" aria-hidden="true" width="0" height="0" style="position:absolute;width:0;height:0;overflow:hidden">' +
    inner +
    '</svg></div>\n' +
    SPRITE_MARKER_END;

  let htmlCount = 0;
  if (!fs.existsSync(distDir)) {
    return done();
  }

  const files = fs.readdirSync(distDir).filter((f) => f.endsWith('.html'));
  const markerRegion = new RegExp(
    SPRITE_MARKER_START.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') +
      '[\\s\\S]*?' +
      SPRITE_MARKER_END.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'),
    'g'
  );

  for (const file of files) {
    const fp = path.join(distDir, file);
    let html = fs.readFileSync(fp, 'utf8');
    if (!/<body\b/i.test(html)) {
      continue;
    }

    if (html.includes(SPRITE_MARKER_START)) {
      html = html.replace(markerRegion, spriteBlock);
    } else {
      html = html.replace(/<body(\b[^>]*)>/i, '<body$1>\n' + spriteBlock + '\n');
    }

    fs.writeFileSync(fp, html, 'utf8');
    htmlCount += 1;
  }

  if (htmlCount) {
    console.log('[injectInlineSprite] updated', htmlCount, 'HTML file(s)');
  }
  done();
}

const build = series(
  cleanDist,
  parallel(html, styles, vendorCss, vendorFontawesome, scripts, images, fonts, favicon),
  sprite,
  injectInlineSprite
);

function watcher() {
  watch(paths.html.watch, series(html, injectInlineSprite));
  watch(paths.styles.watch, styles);
  watch(paths.vendorCss.watch, vendorCss);
  // Font Awesome copied from repo shared assets (no watch — change rarely).
  watch(paths.scripts.watch, scripts);
  watch(paths.images.watch, images);
  watch(paths.fonts.watch, fonts);
  watch(paths.favicon.watch, favicon);
  watch(paths.svg.watch, series(sprite, injectInlineSprite));
}

exports.clean = cleanDist;
exports.sprite = series(sprite, injectInlineSprite);
exports.build = build;
exports.default = build;
exports.watch = series(build, watcher);