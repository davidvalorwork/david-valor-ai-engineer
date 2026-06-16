import json
from faster_whisper import WhisperModel
m = WhisperModel("base", device="cpu", compute_type="int8")
segs,_ = m.transcribe("source-tight.mp4", language="es", word_timestamps=True, vad_filter=False)
ws=[]; i=0
for s in segs:
    for w in (s.words or []):
        t=w.word.strip()
        if t:
            ws.append({"text":t,"start":round(w.start,3),"end":round(w.end,3)}); i+=1
json.dump(ws,open("transcript.json","w",encoding="utf-8"),ensure_ascii=False)
print(len(ws),"palabras, fin",ws[-1]["end"])
