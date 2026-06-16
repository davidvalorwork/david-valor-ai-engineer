#!/usr/bin/env python3
"""
Transcriptor canonico (ECO DE TOKENS). Modelo por defecto: small (mejor español -> sin correccion).
Lee el video recortado y escribe transcript.json con tiempos por palabra.

Uso:
  python ../_assets/transcribe.py                      # source-tight.mp4 -> transcript.json
  python ../_assets/transcribe.py otro.mp4 --model base
"""
import json, os, argparse
from faster_whisper import WhisperModel

# modelo small instalado localmente (descargado a mano) -> texto correcto sin correccion
SMALL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models", "faster-whisper-small")
DEFAULT = SMALL if os.path.isfile(os.path.join(SMALL, "model.bin")) else "base"

ap = argparse.ArgumentParser()
ap.add_argument("src", nargs="?", default="source-tight.mp4")
ap.add_argument("--out", default="transcript.json")
ap.add_argument("--model", default=DEFAULT)   # default: small local si existe, si no base
ap.add_argument("--lang", default="es")
a = ap.parse_args()

m = WhisperModel(a.model, device="cpu", compute_type="int8")
segs, _ = m.transcribe(a.src, language=a.lang, word_timestamps=True, vad_filter=False)

ws = []
for s in segs:
    for w in (s.words or []):
        t = w.word.strip()
        if t:
            ws.append({"text": t, "start": round(w.start, 3), "end": round(w.end, 3)})

json.dump(ws, open(a.out, "w", encoding="utf-8"), ensure_ascii=False)
print(f"{len(ws)} palabras -> {a.out} (modelo {a.model}, fin {ws[-1]['end'] if ws else 0}s)")
