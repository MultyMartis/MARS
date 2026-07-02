import fs from 'node:fs';
const p = 'src/pages/uslugi-v2.html';
let s = fs.readFileSync(p, 'utf8');
const pairs = [
  ['>Эмоциональное выгорание</span>', '/uslugi/psihicheskoe-zdorovie/ptrs/', '/uslugi/psihicheskoe-zdorovie/emocionalnoe-vygoranie/'],
  ['>Тревожные расстройства</span>', '/uslugi/psihicheskoe-zdorovie/ptrs/', '/uslugi/psihicheskoe-zdorovie/trevozhnye-rasstroystva/'],
  ['>Расстройства сна</span>', '/uslugi/psihicheskoe-zdorovie/ptrs/', '/uslugi/psihicheskoe-zdorovie/rasstroystva-sna/'],
  ['>Травма</span>', '/uslugi/psihicheskoe-zdorovie/ptrs/', '/uslugi/psihicheskoe-zdorovie/travma/'],
  ['>Нервная булимия</span>', '/uslugi/rasstroystva-pischevogo-povedeniya/"', '/uslugi/rasstroystva-pischevogo-povedeniya/nervnaya-bulimiya/"'],
  ['>Компульсивное переедание</span>', '/uslugi/rasstroystva-pischevogo-povedeniya/"', '/uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie/"'],
];
for (const [label, wrong, right] of pairs) {
  const idx = s.indexOf(label);
  if (idx === -1) continue;
  const slice = s.slice(idx, idx + 800);
  const hrefIdx = slice.indexOf(wrong);
  if (hrefIdx !== -1) {
    const abs = idx + hrefIdx;
    s = s.slice(0, abs) + right + s.slice(abs + wrong.length);
  }
}
fs.writeFileSync(p, s);
console.log('patched');
