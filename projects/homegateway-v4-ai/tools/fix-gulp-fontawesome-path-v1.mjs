import fs from 'fs';
import path from 'path';

const root = process.argv[2] || path.resolve('workspaces/homegateway-v4-ai/v1');
const gulpPath = path.join(root, 'gulpfile.js');
let g = fs.readFileSync(gulpPath, 'utf8');

g = g.replaceAll(
  "path.join(__dirname, '../../shared/assets/icon-libraries/Font Awesome Pro 5.15.4",
  "path.join(__dirname, '../../../shared/assets/icon-libraries/Font Awesome Pro 5.15.4"
);

g = g.replace(
  /function fontawesome\(\) \{[\s\S]*?\}\n\nfunction fonts/,
  `function fontawesomeCss() {
  return src(paths.fontawesome.srcCss, { allowEmpty: false }).pipe(
    dest(path.join(paths.fontawesome.dest, 'css'))
  );
}

function fontawesomeWebfonts() {
  return src(paths.fontawesome.srcWebfonts, { buffer: true, encoding: false, allowEmpty: true }).pipe(
    dest(path.join(paths.fontawesome.dest, 'webfonts'))
  );
}

function fonts`
);

g = g.replace(
  'parallel(html, styles, scripts, images, fonts, fontawesome)',
  'parallel(html, styles, scripts, images, fonts, fontawesomeCss, fontawesomeWebfonts)'
);

fs.writeFileSync(gulpPath, g);
console.log('gulpfile fixed');
