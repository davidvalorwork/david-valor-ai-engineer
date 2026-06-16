# Catálogo de Edición — David Valor

> Librería de **sonidos virales (royalty-free)** + **ediciones reproducibles** para los shorts. Copia los snippets en el `index.html` de cada video. Complementa a `ESTRATEGIA-VIDEOS.md`.

_Última actualización: 2026-06-15_

---

## 1. Librería de SFX

Dos packs, ambos seguros para monetización:
- **`_assets/sfx/`** — 12 sonidos **sintetizados** (ffmpeg, 100% libres), equivalentes a los virales.
- **`_assets/sfx-mixkit/`** — 8 sonidos **reales descargados de Mixkit** (licencia libre, uso comercial, sin atribución): `whoosh, swoosh, pop, click, impact (boom), transition, bell (ding), wrong (error)`. Suenan más "profesionales"; úsalos primero.

Tabla de uso (aplica a ambos packs):

| Archivo | Tipo viral | Cuándo usarlo |
|---|---|---|
| `whoosh.wav` | Whoosh | Transición entre escenas/ideas (suave) |
| `swoosh.wav` | Swoosh rápido | Corte rápido, entrada de texto |
| `boom.wav` | Boom (estilo "vine boom") | **Énfasis** en una afirmación fuerte / palabra clave |
| `riser.wav` | Flash riser / build | Subida 1s **antes de revelar** un dato o el giro |
| `bass-drop.wav` | Bass drop | Impacto en la **revelación** del dato fuerte |
| `pop.wav` | Pop | Aparición de texto/elemento pequeño |
| `click.wav` | Tick UI | Micro-acentos, conteos |
| `ding.wav` | Ding | **Dato positivo** (ROI, ✓) |
| `caching.wav` | Ca-ching | Dinero / ganancia / "+94%" |
| `error.wav` | Buzz | **Dato negativo** ("pérdida", ❌) |
| `glitch.wav` | Glitch/zap | Transición glitch, cambio brusco |
| `shutter.wav` | Cámara | "Captura" de pantalla / snap |

**Cómo insertarlos** (HyperFrames `index.html`, un `<audio>` por golpe, cada uno con `id`, en pistas que no se solapen):
```html
<audio id="sx1" src="../_assets/sfx/boom.wav"  data-start="3.0"  data-duration="0.6" data-track-index="3" data-volume="0.6"></audio>
<audio id="sx2" src="../_assets/sfx/ding.wav"  data-start="36.7" data-duration="0.55" data-track-index="4" data-volume="0.5"></audio>
```
> Voz humana en pista 2; SFX en 3-5; música/trending la añade TikTok al subir (ver §5). Volúmenes 0.4-0.6 para no tapar la voz.

---

## 2. Ediciones reproducibles (recetas copy-paste)

Todas deterministas y seekables (válidas para el render de HyperFrames). El video va en `#vid`; los overlays en sus propios elementos controlados por la timeline `root`.

### 2.1 Hook overlay (texto gigante 0-3s, para muteados)
```html
<div id="hook" style="position:absolute;left:60px;right:60px;top:1050px;z-index:7;text-align:center;
  font:900 96px Inter;color:#fff;text-shadow:0 6px 24px #000;">ESPIÉ A 83 COMPETIDORES</div>
```
```js
tl.fromTo("#hook",{opacity:0,scale:0.7},{opacity:1,scale:1,duration:0.3,ease:"back.out(2)"},0.1);
tl.to("#hook",{opacity:0,duration:0.2},2.8); tl.set("#hook",{visibility:"hidden"},3.0);
```
SFX: `boom.wav` en 0.15.

### 2.2 Zoom punch-in (golpe en palabra clave)
```js
// pulso de zoom sobre el video en el momento del dato
tl.to("#vid",{scale:1.08,duration:0.12,ease:"power2.out"},36.7)
  .to("#vid",{scale:1.0,duration:0.5,ease:"power2.inOut"},36.85);
```
SFX: `ding.wav` o `caching.wav`. (Requiere `#vid{transform-origin:center}`.)

### 2.3 Camera shake (en boom/impacto)
```js
var SH=37.0; [0,0.05,0.1,0.15].forEach(function(o,i){
  tl.to("#vid",{x:(i%2?12:-12),y:(i%2?-8:8),duration:0.05},SH+o);
}); tl.to("#vid",{x:0,y:0,duration:0.05},SH+0.2);
```
SFX: `boom.wav` en SH.

### 2.4 Flash cut (corte con destello blanco)
```html
<div id="flash" style="position:absolute;inset:0;background:#fff;z-index:8;opacity:0"></div>
```
```js
tl.to("#flash",{opacity:0.9,duration:0.06},T).to("#flash",{opacity:0,duration:0.16},T+0.06);
```
SFX: `swoosh.wav` o `glitch.wav`.

### 2.5 Speed ramp (acelerar relleno) — a nivel de fuente, ffmpeg
```bash
# acelerar un tramo X2 (video y audio) antes de componer
ffmpeg -i in.mp4 -filter_complex "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]" -map "[v]" -map "[a]" out.mp4
```

### 2.6 Number pop / contador (revelar cifra)
```js
tl.fromTo("#dato",{opacity:0,scale:0.5,y:30},{opacity:1,scale:1,y:0,duration:0.35,ease:"back.out(2)"},T);
```
SFX: `riser.wav` (en T-1.0, build) → `bass-drop.wav` (en T, impacto).

### 2.7 Subtítulos karaoke — ya estandarizado
`build-captions.py` → `captions-data.js`. Grupos 2-4 palabras, uno visible a la vez, cifras ámbar `#ffd166`, clave naranja `#f96a17`. (Reutilizar de `guion-03/`.)

### 2.8 Fichas de dato/producto (pop bajo la cámara) — ya estandarizado
PNG en `products/`, animación pop in/out. (Reutilizar de `guion-03/`.)

### 2.9 Glitch transition entre ideas
`flash cut` (#2.4) + `glitch.wav` + opcional desplazamiento RGB con 2 copias y `mix-blend-mode`.

---

## 3. Preset de momentos (qué combo en cada beat)

| Beat del video | Edición | SFX |
|---|---|---|
| **Hook (0-3s)** | Hook overlay (2.1) + zoom punch leve | `boom` |
| **Transición de idea** | Flash/glitch cut (2.4) | `whoosh` / `swoosh` |
| **Build a un dato** | (1s antes) nada visual, sube tensión | `riser` |
| **Revelar dato fuerte** | Number pop (2.6) + zoom punch (2.2) | `bass-drop` + `ding`/`caching` |
| **Dato negativo** | Ficha roja (2.8) + shake leve | `error` |
| **Captura de pantalla** | Ficha/zoom a la zona | `shutter` |
| **CTA / outro** | Outro "Sígueme" (naranja) | `whoosh` al entrar |

---

## 4. Ritmo (no abusar)
- **1 SFX cada 3-6s** como máximo; saturar suena amateur.
- Sincroniza el golpe **exacto** con el corte/palabra (usa los tiempos del transcript).
- El `boom` solo en 1-2 momentos pico por video.
- Variedad: no repitas el mismo whoosh 8 veces; alterna whoosh/swoosh/glitch.

---

## 5. ⚠️ Audio en tendencia (lo más importante para el algoritmo)
Los SFX de arriba se **queman** en el render (son la "edición"). Pero el **empuje del algoritmo** viene del **sonido/música en tendencia que se añade NATIVO en TikTok/CapCut al subir**, a volumen bajo (10-20%) por debajo de tu voz.
- Flujo: renderizas el video con voz + SFX → lo subes a TikTok → añades un **sonido trending** del momento desde la app → publicas.
- Revisa los trending semanalmente (rotan). Elige sonidos con uso creciente pero aún no saturados.

---

## 6. Inventario reutilizable (resumen)
- `_assets/sfx/` — 12 SFX (este pack).
- `guion-03/compositions/follow-outro.html` — outro "Sígueme" naranja.
- `guion-03/build-tight.py · build-captions.py · transcribe-tight.py` — scripts del pipeline.
- `design.md` — marca (naranja SIP).

**Fuentes de referencia (sonidos trending):** [Pixabay SFX](https://pixabay.com/sound-effects/), [Freesound (CC0)](https://freesound.org/), CapCut/TikTok librería nativa.

---

## 7. Flujo ECO DE TOKENS (producir cada video barato)

El paso caro en tokens era **autorar los subtítulos a mano** (40-50 grupos). Ya está **automatizado** → cada video nuevo cuesta una fracción.

**Pipeline lean (los scripts hacen el trabajo; el modelo NO lee transcripts ni escribe grupos):**
1. `python build-tight.py` — recorta silencios + tartamudeos (usa `ffmpeg silencedetect`).
2. `python transcribe-tight.py` — transcribe el recortado.
3. `python ../_assets/auto-captions.py --dur <N> --emph RAG,wrapper,API` — **subtítulos automáticos** (`captions-data.js`). **Sin autoría manual.**
4. SFX por preset (§3) + `npx hyperframes render`.

**Reglas para gastar pocos tokens:**
- ❌ NO volcar el transcript completo al chat — los scripts lo procesan en disco.
- ❌ NO autorar grupos a mano — usar `auto-captions.py`. Solo corregir 1-2 palabras si el ASR falló en algo **clave** (edición puntual, no reescribir todo).
- ✅ **Modelo de transcripción:** usar `small`/`medium` con audio limpio → el texto sale correcto → **cero corrección manual** = cero tokens en captions. `base` solo si la descarga del modelo falla (entonces el texto trae errores y sí cuesta corregir).
- ✅ Verificar con **1-2 frames**, no más.
- ✅ Grabar **sin pausas largas ni tartamudeos** → menos cortes que decidir = menos tokens.

> Compromiso: subtítulos 100% automáticos = baratísimos pero copian el texto del ASR tal cual (puede traer errores con `base`). Para texto perfecto sin gastar: graba claro + transcribe con `small`/`medium`.

---

## 8. Dónde sacar sonidos virales SIN riesgo

⚠️ **"Todo el mundo los usa" ≠ "sin copyright".** El vine boom, sonidos meme, snippets de canciones/series → casi todos **tienen dueño**. Se usan sin problema **dentro de TikTok** porque la app tiene licencias. El riesgo aparece si **quemas** un sonido con copyright en el render o lo subes a YouTube monetizado (Content ID).

**Estrategia de dos capas (lo mejor de ambos):**

| Capa | Qué usar | Dónde va |
|---|---|---|
| **SFX de edición** (whoosh, boom, ding…) | `_assets/sfx-mixkit/` o `_assets/sfx/` (libres) | **Quemados en el render** |
| **Música / sonido trending** | El nativo de TikTok/CapCut | **Añadido en la app al subir** (NO en el render) → legal + empuje del algoritmo |

**Fuentes para descargar SFX libres (usables en cualquier lado):**
- **Mixkit** — `https://mixkit.co/free-sound-effects/` → descarga directa por terminal (CDN `assets.mixkit.co/active_storage/sfx/<id>/<id>-preview.mp3`). Licencia libre comercial, sin atribución. **(Es de donde bajé el pack `sfx-mixkit/`.)**
- **Pixabay** — `https://pixabay.com/sound-effects/` → su CDN bloquea curl (403); descarga manual desde la web. CC0.
- **Freesound** — `https://freesound.org/` → requiere cuenta/API; filtra por licencia **CC0**.

**Sonidos virales "originales" (vine boom, memes):** úsalos **solo nativos en TikTok** ("Añadir sonido" / "Usar este sonido"). No los bajes para quemarlos en el render.
