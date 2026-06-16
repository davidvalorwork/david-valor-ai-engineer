#!/usr/bin/env python3
"""
Auto-genera captions-data.js desde transcript.json SIN autoria manual.
Agrupa por puntuacion / pausa / max palabras, asigna tiempos reales (karaoke)
y clasifica cifras (num) y MAYUSCULAS/keywords (emph).

Uso:
  python ../_assets/auto-captions.py                 # transcript.json -> captions-data.js
  python ../_assets/auto-captions.py --dur 55.84     # recorta el ultimo grupo al fin del video
  python ../_assets/auto-captions.py --emph RAG,wrapper,API   # palabras extra a resaltar

Token-eficiente: el modelo NO lee el transcript ni escribe grupos; este script hace todo.
Solo corrige texto a mano si el ASR escribio mal alguna palabra clave.
"""
import json, re, sys, argparse, unicodedata

ap = argparse.ArgumentParser()
ap.add_argument("transcript", nargs="?", default="transcript.json")
ap.add_argument("--out", default="captions-data.js")
ap.add_argument("--dur", type=float, default=None, help="duracion del video (clamp del ultimo grupo)")
ap.add_argument("--max", type=int, default=4, help="max palabras por grupo")
ap.add_argument("--gap", type=float, default=0.4, help="pausa que rompe grupo")
ap.add_argument("--emph", default="", help="palabras extra a resaltar, separadas por coma")
a = ap.parse_args()

words = json.load(open(a.transcript, encoding="utf-8"))
EMPH = {w.strip().lower() for w in a.emph.split(",") if w.strip()}

def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", s.lower())

def wtype(tok):
    core = re.sub(r"[^0-9A-Za-zÁÉÍÓÚÜÑáéíóúüñ]", "", tok)
    if any(c.isdigit() for c in core):
        return "num"
    if (len(core) >= 3 and core == core.upper() and any(c.isalpha() for c in core)) or norm(tok) in EMPH:
        return "emph"
    return "norm"

# agrupar
groups, cur = [], []
for i, w in enumerate(words):
    cur.append(w)
    t = w["text"]
    ends = t[-1:] in ".?!:" or t[-1:] == ","
    gap = (words[i + 1]["start"] - w["end"]) if i + 1 < len(words) else 99
    if len(cur) >= a.max or ends or gap > a.gap:
        groups.append(cur); cur = []
if cur:
    groups.append(cur)

DUR = a.dur if a.dur else (words[-1]["end"] + 0.2)
out = []
for g in groups:
    wl = [{"text": w["text"], "t": round(w["start"], 3), "type": wtype(w["text"])} for w in g]
    out.append({"start": round(g[0]["start"], 3), "end": round(min(g[-1]["end"] + 0.12, DUR), 3), "words": wl})

# un grupo visible a la vez
for i in range(len(out) - 1):
    cap = out[i + 1]["start"] - 0.02
    if cap > out[i]["start"] + 0.1:
        out[i]["end"] = min(out[i]["end"], cap)

open(a.out, "w", encoding="utf-8").write("window.__CAPTIONS = " + json.dumps(out, ensure_ascii=False) + ";\n")
print(f"{len(out)} grupos -> {a.out} (fin {out[-1]['end']}s)")
