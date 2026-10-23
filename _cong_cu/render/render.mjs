// usage: node render.mjs in.drawio out.svg out.png [scale]
// d2s.js: bundle esbuild của entry.mjs (npm @markdown-viewer/drawio2svg), đặt cạnh file này.
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs';
const [,, inp, outSvg, outPng, sc] = process.argv;
const b = await chromium.launch(); const p = await b.newPage({deviceScaleFactor: Number(sc||1.5)});
await p.setContent('<html><body style="margin:0;background:#fff"></body></html>');
await p.addScriptTag({path: new URL('./d2s.js', import.meta.url).pathname});
const svg = await p.evaluate(x => window.d2s(x), fs.readFileSync(inp,'utf-8'));
fs.writeFileSync(outSvg, svg);
await p.setContent('<html><body style="margin:0;background:#fff">'+svg+'</body></html>');
const el = await p.$('svg'); await el.screenshot({path: outPng});
await b.close();
