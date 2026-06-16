import json
from faster_whisper import WhisperModel

SRC = "C:/Users/David/Videos/2026-06-15 15-21-37.mp4"

model = WhisperModel("base", device="cpu", compute_type="int8")
segments, info = model.transcribe(SRC, language="es", word_timestamps=True, vad_filter=False)

words = []
i = 0
for seg in segments:
    if not seg.words:
        continue
    for w in seg.words:
        t = w.word.strip()
        if not t:
            continue
        words.append({"id": f"w{i}", "text": t, "start": round(w.start, 3), "end": round(w.end, 3)})
        i += 1

with open("transcript-orig.json", "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=0)
print(f"{len(words)} palabras, dur {words[-1]['end']}s")
