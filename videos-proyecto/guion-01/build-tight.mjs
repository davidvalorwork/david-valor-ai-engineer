// Calcula segmentos a conservar quitando silencios muertos y genera filtergraph ffmpeg.
import { writeFileSync } from "node:fs";

const END = 52.383333;
const MIN_CUT = 0.5;  // solo cortar silencios >= 0.5s
const PAD = 0.07;     // dejar respiro a cada lado
const EDGE = 0.08;    // recorte de entrada/salida

const silences = [
  [0, 1.084375], [4.238792, 4.683813], [6.130417, 7.231583],
  [11.308083, 12.246729], [12.545375, 13.347896], [14.268958, 15.039021],
  [15.4085, 16.329438], [16.714375, 17.853896], [18.901229, 19.342146],
  [19.351083, 19.762375], [26.094437, 28.033854], [28.617104, 29.632979],
  [32.201563, 33.749896], [36.154312, 36.641979], [40.800125, 41.241854],
  [41.242104, 41.649646], [42.047479, 43.443417], [44.424958, 45.796021],
  [47.373, 48.116146], [48.503625, 49.013375], [49.677208, 50.251],
  [51.5715, 52.352],
];

const cuts = [];
silences.forEach(([s, e], i) => {
  if (i === 0 && s <= 0.01) cuts.push([0, Math.max(0, e - EDGE)]);
  else if (e >= END - 0.05) cuts.push([s + EDGE, END]);
  else if (e - s >= MIN_CUT) cuts.push([s + PAD, e - PAD]);
});

// keep = complemento de cuts sobre [0, END]
const keeps = [];
let cursor = 0;
for (const [cs, ce] of cuts) {
  if (cs > cursor) keeps.push([cursor, cs]);
  cursor = Math.max(cursor, ce);
}
if (cursor < END) keeps.push([cursor, END]);
const kept = keeps.filter(([a, b]) => b - a > 0.03);

// filtergraph
let fg = "";
kept.forEach(([a, b], i) => {
  fg += `[0:v]trim=start=${a.toFixed(3)}:end=${b.toFixed(3)},setpts=PTS-STARTPTS[v${i}];\n`;
  fg += `[0:a]atrim=start=${a.toFixed(3)}:end=${b.toFixed(3)},asetpts=PTS-STARTPTS[a${i}];\n`;
});
fg += kept.map((_, i) => `[v${i}][a${i}]`).join("") + `concat=n=${kept.length}:v=1:a=1[v][a]`;
writeFileSync("filter.txt", fg);

const total = kept.reduce((s, [a, b]) => s + (b - a), 0);
console.log(`Segmentos conservados: ${kept.length}`);
console.log(`Duracion final estimada: ${total.toFixed(2)}s (de ${END}s, -${(END - total).toFixed(2)}s)`);
