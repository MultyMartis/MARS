import fs from 'fs';
import path from 'path';

const root = process.argv[2] || path.resolve('workspaces/homegateway-v4-ai/v1');
const gulpPath = path.join(root, 'gulpfile.js');
let gulp = fs.readFileSync(gulpPath, 'utf8');

if (gulp.includes('fontawesome')) {
  console.log('gulpfile already has fontawesome task');
  process.exit(0);
}

const faSrc =
  "path.resolve(__dirname, '../../shared/assets/icon-libraries/Font Awesome Pro 5.15.4')";

const insertPaths = `  fontawesome: {
    css: ${faSrc.replace('path.resolve', 'path.join')} + '/css/all.min.css',
    webfonts: ${faSrc} + '/webfonts/*',
    dest: 'dist/assets/vendor/fontawesome/',
  },`;

// Fix - use proper path join in gulpfile as string
const pathsBlock = `  fontawesome: {
    srcCss: path.join(__dirname, '../../shared/assets/icon-libraries/Font Awesome Pro 5.15.4/css/all.min.css'),
    srcWebfonts: path.join(__dirname, '../../shared/assets/icon-libraries/Font Awesome Pro 5.15.4/webfonts/**/*'),
    dest: 'dist/assets/vendor/fontawesome/',
  },`;

if (!gulp.includes('fontawesome:')) {
  gulp = gulp.replace(
    `  fonts: {
    src: 'src/fonts/**/*.{woff,woff2}',
    watch: 'src/fonts/**/*.{woff,woff2}',
    dest: 'dist/assets/fonts/',
  },
};`,
    `  fonts: {
    src: 'src/fonts/**/*.{woff,woff2}',
    watch: 'src/fonts/**/*.{woff,woff2}',
    dest: 'dist/assets/fonts/',
  },
  fontawesome: {
    srcCss: path.join(__dirname, '../../shared/assets/icon-libraries/Font Awesome Pro 5.15.4/css/all.min.css'),
    srcWebfonts: path.join(__dirname, '../../shared/assets/icon-libraries/Font Awesome Pro 5.15.4/webfonts/**/*'),
    dest: 'dist/assets/vendor/fontawesome/',
  },
};`
  );
}

if (!gulp.includes("const path = require('path')")) {
  gulp = gulp.replace(
    "const { src, dest, watch, series, parallel } = require('gulp');",
    "const path = require('path');\nconst { src, dest, watch, series, parallel } = require('gulp');"
  );
}

if (!gulp.includes('function fontawesome')) {
  gulp = gulp.replace(
    'function fonts() {',
    `function fontawesome() {
  const cssOut = path.join(paths.fontawesome.dest, 'css');
  const cssCopy = src(paths.fontawesome.srcCss, { allowEmpty: false }).pipe(dest(cssOut));
  const wfCopy = src(paths.fontawesome.srcWebfonts, { buffer: true, encoding: false, allowEmpty: true }).pipe(
    dest(path.join(paths.fontawesome.dest, 'webfonts'))
  );
  return Promise.all([new Promise((res, rej) => cssCopy.on('end', res).on('error', rej)), new Promise((res, rej) => wfCopy.on('end', res).on('error', rej))]);
}

function fonts() {`
  );

  gulp = gulp.replace(
    'const build = series(cleanDist, parallel(html, styles, scripts, images, fonts));',
    'const build = series(cleanDist, parallel(html, styles, scripts, images, fonts, fontawesome));'
  );
}

fs.writeFileSync(gulpPath, gulp, 'utf8');
console.log('patched gulpfile.js');
