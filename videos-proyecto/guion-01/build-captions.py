# Construye captions-data.js con texto corregido anclado a los tiempos reales del transcript.
import json, re

words = json.load(open("transcript.json", encoding="utf-8"))

# (idxStart, idxEnd, texto corregido).  CAPS = enfasis (cyan).  digitos = numero (amarillo).
GROUPS = [
    (0, 1, "Mira, escucha"),
    (2, 7, "te ha estado cobrando"),
    (8, 11, "200 dólares al mes"),
    (12, 15, "y por dentro es"),
    (16, 19, "solo un llamado a una API"),
    (20, 22, "te lo pruebo"),
    (23, 27, "mira, le puse un proxy"),
    (28, 32, "y capturé sus peticiones"),
    (33, 36, "¿y sabes cuál es"),
    (37, 38, "el producto?"),
    (39, 43, "un PROMPT y un FETCH"),
    (44, 46, "o sea, sin RAG"),
    (47, 48, "sin evals"),
    (49, 53, "sin control de costo"),
    (54, 56, "o sea, el problema"),
    (57, 61, "no es que sea simple"),
    (62, 65, "es que sin un"),
    (66, 67, "EVAL HARNESS"),
    (68, 74, "el día en que el modelo"),
    (75, 77, "ALUCINE"),
    (78, 83, "te enteras por un cliente"),
    (84, 86, "no por un test"),
    (87, 89, "y sin cacheo"),
    (90, 93, "tu factura de TOKENS"),
    (94, 96, "se dispara"),
    (97, 99, "y nadie lo nota"),
    (100, 103, "eso yo lo monto"),
    (104, 107, "un fin de semana"),
    (113, 115, "pero con tests"),
    (116, 119, "con tope de costos"),
    (120, 121, "por token"),
    (122, 125, "y el código es TUYO"),
    (126, 129, "no tienes que pagar"),
    (130, 131, "esas mensualidades"),
    (132, 136, "y suscripción de por vida"),
    (137, 141, "así que si estás pagando"),
    (142, 145, "un WRAPPER sin verlo"),
    (146, 150, "te acabo de ahorrar PLATA"),
    (151, 154, "SÍGUEME y te enseño"),
    (155, 159, "cómo se hace de verdad"),
]

def wtype(tok):
    core = re.sub(r"[^0-9A-Za-zÁÉÍÓÚÜÑáéíóúüñ]", "", tok)
    if any(c.isdigit() for c in core):
        return "num"
    if len(core) >= 2 and core == core.upper() and any(c.isalpha() for c in core):
        return "emph"
    return "norm"

out = []
for (a, b, text) in GROUPS:
    start = words[a]["start"]
    end = words[b]["end"]
    toks = text.split()
    n = len(toks)
    span = max(end - start, 0.001)
    wl = []
    for i, tok in enumerate(toks):
        wl.append({"text": tok, "t": round(start + i * span / n, 3), "type": wtype(tok)})
    out.append({"start": round(start, 3), "end": round(min(end + 0.15, 37.84), 3), "words": wl})

# un grupo visible a la vez: recortar fin al inicio del siguiente
for i in range(len(out) - 1):
    cap = out[i + 1]["start"] - 0.02
    if cap > out[i]["start"] + 0.1:
        out[i]["end"] = min(out[i]["end"], cap)

with open("captions-data.js", "w", encoding="utf-8") as f:
    f.write("window.__CAPTIONS = " + json.dumps(out, ensure_ascii=False) + ";\n")

print(f"{len(out)} grupos, fin ultimo grupo {out[-1]['end']}s")
