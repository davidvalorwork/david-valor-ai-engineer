# Estrategia de Videos — David Valor (@davidvalor7)

> **Documento maestro.** Léelo antes de producir cualquier video nuevo. Define el objetivo, la marca, las reglas de producción, las mejoras obligatorias y el banco de guiones. Es el "norte" para que cada video sume a una línea clara.

_Última actualización: 2026-06-15_

---

## 1. Objetivo (la línea clara)

Construir la marca personal de **David Valor — AI Engineer & Full-Stack Developer** con shorts verticales, para:

1. **Atraer clientes freelance** (negocios + emprendedores que pagan por software/IA/automatización).
2. Crecer audiencia de **devs + emprendedores** que confíen en él como "el ingeniero que sí entrega".

**Posicionamiento (de su CV/perfil):** _"ingeniero que se especializa en IA, no prompt-engineer aprendiendo a programar"_. Lema: **"sistemas que se envían a producción, no demos"**. Diferencial: domina backend + criterio de producto + **control de costos LLM**. (Ver `01-perfil-y-cv/` y `02-freelance/`.)

**Regla de oro:** la controversia/curiosidad es el **gancho**, no el contenido. Después del gancho, **sustancia técnica real enmarcada en el dolor del cliente** → así convierte, no solo entretiene.

---

## 2. Estado de la cuenta + diagnóstico (2026-06-15)

| Métrica | Valor |
|---|---|
| Seguidores | 1.032 |
| Videos publicados | 302 |
| Likes totales | 26.600 (~88/video) |
| Sigue a | 9.640 |

**Diagnóstico:** el problema NO es producción (302 videos), es **conversión y retención**. Volumen alto, enganche bajo.
- ❌ **Dejar de seguir masivo** (ratio 9.640→1.032 huele a spam, resta credibilidad ante clientes).
- ❌ **Cuenta mezcla públicos** → seguidores no convierten. Definir 1 nicho/serie y ser consistente.
- ✅ Tiene disciplina de publicar → si arreglamos hook/retención, escala rápido.

---

## 3. Estrategia viral (TikTok 2026 — lo que pesa)

- **Hook en <3s.** 63% de los top dan valor de inmediato. Nada de "hola, hoy les traigo…".
- **Retención objetivo ~70%** (subió de ~50% en 2024). <40% = sin empuje del algoritmo.
- **Watch time + completion = 40-50%** del ranking. **Shares y saves > likes.**
- **Primer frame:** texto grande + afirmación audaz (85% ve sin sonido).
- **Audio en tendencia** a bajo volumen = empuje gratis.
- **Primeros 60 min** tras publicar deciden el alcance → responder comentarios rápido.
- **Cadencia 3-5/semana** constante.
- **CTA con pregunta** para disparar comentarios (comentarios = alcance).
- **Plataforma #1 real para clientes = LinkedIn**; TikTok/Reels/Shorts = alcance. Repurposear el mismo short a las dos.

---

## 4. Marca visual (especificación fija de cada video)

- **Formato:** vertical 1080×1920, 9:16. Subtítulos quemados siempre.
- **Color de marca:** **naranja SIP** → primario `#ea5536`, acento vivo `#f96a17`. (Ámbar `#ffd166` solo para cifras en captions.) Fondo oscuro `#0c0a09`.
- **Tipografía:** Inter (800-900 títulos / 700 captions). Mono: JetBrains Mono.
- **Cámara (OBS):** facecam circular con **aro naranja** arriba; pantalla abajo. Webcam Fantech C30 = **2560×1440 MJPEG @30fps** (tope de hardware = 30). Assets del OBS en `C:\Users\David\obs-assets\`.
- **Outro fijo:** animación "Sígueme" reutilizable en naranja → `guion-03/compositions/follow-outro.html` (avatar DV, @davidvalor7, botón "+ Seguir", tagline "AI Engineer · sistemas, no demos").

---

## 5. Pipeline de producción (cómo se edita cada video)

Proyecto por video en `videos-proyecto/guion-NN/`. Pasos:

1. **Recortar silencios + tartamudeos + relleno**
   - Usar **`ffmpeg silencedetect`** (NO huecos del ASR — dan falsos negativos). `noise=-30dB:d=0.35`, dejar 0.07s de respiro.
   - Cortes manuales (tiempo original) para tartamudeos/repeticiones y frases de relleno.
   - Concat con `filter_complex` (trim/atrim) → `source-tight.mp4`.
2. **Transcribir el recortado**: `python ../_assets/transcribe.py` → usa **`small` instalado localmente** en `_assets/models/faster-whisper-small/` (descargado a mano; el `.bin` está gitignored). Da texto correcto en español → con `auto-captions.py` los subtítulos salen **automáticos y casi perfectos, sin corrección = sin gasto de tokens**. (Respaldo a `base` si la carpeta del modelo no existe.)
3. **Subtítulos karaoke AUTOMÁTICOS** (ECO DE TOKENS): `python _assets/auto-captions.py --dur <N> --emph RAG,wrapper` → `captions-data.js`. Auto-agrupa (2-4 palabras, uno visible a la vez, cifras ámbar, clave naranja `#f96a17`) **sin autoría manual**. Solo corregir 1-2 palabras si el ASR falló en algo clave. (Ver `CATALOGO-EDICION.md` §7.)
4. **SFX** (`sfx/`): `pop` en cifras/keywords, `ding` en datos fuertes, `whoosh` en la transición al outro. Volumen 0.5-0.6.
5. **Fichas/overlays** (opcional): tarjetas de producto/dato debajo de la cámara cuando se mencionan (`products/`).
6. **Composición** `index.html` (HyperFrames): video + audio + SFX + captions + fichas + outro. `design.md` define la marca.
7. **Validar y renderizar:** `npx hyperframes lint && validate`, luego `render --output "Titulo #hashtags.mp4"`.
8. **Verificar** con frames extraídos (ffmpeg) antes de dar por bueno.

**Reutilizables:** pack de SFX en `_assets/sfx/` (12 sonidos virales royalty-free); `guion-03/compositions/follow-outro.html` (outro naranja), `design.md`, y los scripts `build-tight.py` / `build-captions.py` / `transcribe-tight.py`.

**Catálogo de edición:** ver **`CATALOGO-EDICION.md`** — librería de SFX + recetas copy-paste de ediciones reproducibles (hook overlay, zoom punch, shake, flash cut, riser→drop, etc.) y el preset de qué sonido/efecto va en cada beat. **Aplicarlo en cada video.**

**Git:** los `.mp4` están en `.gitignore` (pesados); todo lo demás (scripts, html, captions, sfx, png) sí se versiona.

---

## 6. ✅ Mejoras OBLIGATORIAS para el próximo video

Aplicar TODAS (salieron de la auditoría del #3):

1. **Hook <3s con el payoff adelantado** + **overlay de texto grande** en el primer frame (para muteados). Ej: `ESPIÉ A 83 COMPETIDORES… CON UN ROBOT`.
2. **Duración ~40-45s** (cortar setup y frases de transición; ir al grano).
3. **Audio en tendencia** de fondo a bajo volumen.
4. **Destacar los números/datos** en pantalla (zoom/overlay a "94%", tablas) en vez de mostrar la terminal completa y cargada.
5. **CTA con pregunta** al final para comentarios. Ej: "¿Qué producto venderías tú? 👇".
6. **Decir nombre "David Valor"** al inicio y al cierre (autoridad).
7. **Un solo nicho/serie** y consistencia.
8. Grabar tranquilo pero **sin pausas largas** (se cortan, pero menos = menos edición).

---

## 7. Auditoría de referencia — Video #3 ("robot espía 83 competidores")

Marcó **~6/10**. Producción sólida, flojo donde más importa.

| Dimensión | Nota |
|---|---|
| Hook 0-3s | 🟡 arranque lento (payoff a los 4-5s) |
| Texto-gancho visual 0-3s | 🔴 falta título fijo |
| Duración (59s) | 🟡 largo |
| Subtítulos | 🟢 |
| Ritmo/cortes | 🟢 (−62s de pausas) |
| Valor + ejemplo | 🟢 datos reales + fichas |
| Audio trending | 🔴 no tiene |
| CTA comentarios | 🟡 falta pregunta |
| B-roll | 🟡 terminal confusa |
| Nicho consistente | 🔴 |

Retención estimada ~45-55% (bajo la barra viral de 70%).

---

## 8. Banco de guiones / ideas

**Plantilla de guion (estructura ganadora):**
`Hook payoff (<3s) → qué es/problema (claro) → ejemplo VISIBLE en vivo → dato/giro → autoridad ("yo construyo esto") → CTA con pregunta + Sígueme`. Decir "David Valor" al inicio y cierre.

| # | Idea | Estado | Ángulo |
|---|---|---|---|
| 1 | "Pagas $200/mes por un wrapper" | ✅ producido (teal, B-roll flojo) | Apps de IA = `fetch` a OpenAI con etiqueta cara |
| 2 | Cal AI ($30M, ChatGPT disfrazado) | guion listo, sin grabar | Wrapper viral 2026; demo foto-comida en ChatGPT gratis |
| 3 | "Robot espía 83 competidores" (scraper) | ✅ producido (naranja, fichas) | Su repo real `marketplace-scraper-venezuela`; datos > corazonadas |
| — | "Reconstruyo en un finde la app que pagas" | idea | Demo en vivo replicando una app de pago |
| — | "Tu factura de IA se dispara por esto" | idea | Control de costo/token (su diferencial) → cliente |
| — | "Le puse precio a TODO el mercado con código" | idea | Otra cara del scraper: inteligencia de precios como servicio vendible |

**Reglas de seguridad del contenido:** hechos verificables (no inventar cifras); enmarcar como "te cobran por algo gratis" (no "fraude" a empresa con nombre = riesgo legal); para el scraper, enmarcar como "investigación de mercado" y no mostrar cookies/sesión.

---

## 9. Próximos pasos sugeridos
1. Re-editar el #3 con las mejoras de la sección 6 (overlay de hook, recorte a ~45s, CTA-pregunta, zoom a datos).
2. Producir el #2 (Cal AI) ya con todas las mejoras.
3. Repurposear cada short a LinkedIn (donde están los clientes).
4. Dejar de seguir masivo y limpiar el ratio.
