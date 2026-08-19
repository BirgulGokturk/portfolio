/**
 * Tailwind CSS'i derleyip index.html icine satir ici gomer.
 *
 * Neden: cdn.tailwindcss.com surumu 126 KB'lik bir betik indirip tarayicida
 * CSS uretiyordu ve sayfanin ilk boyamasini ~830 ms geciktiriyordu. Derlenmis
 * CSS ~20 KB ve dogrudan HTML icinde geldigi icin ek istek/bekleme yok.
 *
 * Kullanim:  npm run build      (index.html'e yeni class ekledikten sonra calistir)
 */
import { execFileSync } from 'node:child_process';
import { readFileSync, writeFileSync, mkdirSync, rmSync } from 'node:fs';
import { createRequire } from 'node:module';

const HTML = 'index.html';
const START = '<!-- TW:START -->';
const END = '<!-- TW:END -->';

let html = readFileSync(HTML, 'utf8');
const a = html.indexOf(START);
const b = html.indexOf(END);
if (a === -1 || b === -1) throw new Error(`${HTML} icinde ${START} / ${END} isaretleri yok`);

// 1) Onceki derlenmis CSS'i temizle ki Tailwind onu tararken yanlis
//    class adaylari toplamasin.
html = html.slice(0, a + START.length) + '\n    ' + html.slice(b);
writeFileSync(HTML, html);

// 2) Tailwind CLI'yi calistir.
mkdirSync('build', { recursive: true });
// (Windows'ta .cmd sarmalayicisi yerine CLI'nin JS dosyasi dogrudan calistirilir.)
const cli = createRequire(import.meta.url).resolve('tailwindcss/lib/cli.js');
execFileSync(
    process.execPath,
    [cli, '-c', 'tailwind.config.js', '-i', 'src/input.css', '-o', 'build/tailwind.css', '--minify'],
    { stdio: 'inherit' }
);

// 3) Uretilen CSS'i isaretlerin arasina goem.
const css = readFileSync('build/tailwind.css', 'utf8').trim();
html = readFileSync(HTML, 'utf8');
const i = html.indexOf(START);
const j = html.indexOf(END);
html = html.slice(0, i + START.length) + '\n    <style>' + css + '</style>\n    ' + html.slice(j);
writeFileSync(HTML, html);

rmSync('build', { recursive: true, force: true });
console.log(`Tailwind gomuldu: ${(css.length / 1024).toFixed(1)} KB CSS -> ${HTML}`);
