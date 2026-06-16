import json, re, unicodedata

words = json.load(open("transcript.json", encoding="utf-8"))
DURCAP = 55.84

# (idxStart, idxEnd, texto limpio). CAPS = enfasis (naranja). digitos = num (ambar).
GROUPS = [
    (0, 6, "Mira, antes de meter un dólar"),
    (7, 11, "en un negocio de reventa"),
    (13, 16, "copié los precios de"),
    (17, 20, "83 competidores"),
    (21, 23, "en Facebook Marketplace"),
    (24, 28, "escribí el programa entero"),
    (30, 33, "scrapeó Marketplace y trajo"),
    (34, 37, "648 publicaciones"),
    (41, 47, "con precios, productos, vendedores"),
    (49, 55, "todo a un Excel automático"),
    (56, 57, "¿Para qué?"),
    (60, 66, "para ver cómo está"),
    (66, 69, "el mercado hoy"),
    (70, 72, "el 90%"),
    (73, 79, "vende exactamente lo mismo"),
    (80, 81, "cargadores, audífonos"),
    (82, 84, "un mercado saturado"),
    (85, 90, "donde pelean por precio"),
    (91, 95, "pero mi código calculó"),
    (96, 98, "la ganancia real"),
    (99, 103, "contra el costo al mayor"),
    (104, 106, "y mira el resultado"),
    (107, 112, "el power bank deja 94%"),
    (115, 119, "la freidora de aire deja"),
    (120, 124, "45% de retorno"),
    (125, 130, "smartwatch y teléfonos"),
    (131, 133, "todos dan PÉRDIDA"),
    (134, 140, "comprando al mayor en Caracas"),
    (141, 143, "y revendiendo"),
    (145, 150, "la gente invierte justo"),
    (151, 155, "en lo que más PIERDE"),
    (156, 162, "con código analizas el mercado"),
    (163, 167, "antes de arriesgar tu plata"),
    (171, 175, "si quieres, SÍGUEME"),
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
    start = words[a]["start"]; end = words[b]["end"]
    toks = text.split(); n = len(toks); span = max(end - start, 0.001)
    wl = [{"text": t, "t": round(start + i * span / n, 3), "type": wtype(t)} for i, t in enumerate(toks)]
    out.append({"start": round(start, 3), "end": round(min(end + 0.12, DURCAP), 3), "words": wl})

for i in range(len(out) - 1):
    cap = out[i + 1]["start"] - 0.02
    if cap > out[i]["start"] + 0.1:
        out[i]["end"] = min(out[i]["end"], cap)

open("captions-data.js", "w", encoding="utf-8").write("window.__CAPTIONS = " + json.dumps(out, ensure_ascii=False) + ";\n")
print(f"{len(out)} grupos, fin {out[-1]['end']}s")
