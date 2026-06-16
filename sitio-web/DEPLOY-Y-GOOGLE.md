# Salir en Google como Desarrollador Web — Caracas

Lo técnico ya está hecho (sitio + schema + sitemap + robots, todo con **Caracas**). Falta lo que solo puedes hacer tú: dominio, deploy, y los registros en Google. Pasos con links.

> El sitio está configurado para el subdominio **GRATIS** `davidvalor.vercel.app`. Para que la URL salga exactamente así, al desplegar nombra el proyecto **`davidvalor`** (Vercel arma la URL como `<nombre-proyecto>.vercel.app`). Si Vercel te da otro nombre, dímelo y cambio los 3 archivos.

---

## PASO 1 — Publicar GRATIS en Vercel (10 min, sin pagar nada)
1. Crea cuenta: https://vercel.com/signup (entra con GitHub).
2. https://vercel.com/new → **arrastra la carpeta `sitio-web/`** (o importa el repo de GitHub).
3. En "Project Name" pon **`davidvalor`** → Deploy.
4. Listo: tu sitio queda vivo en **`https://davidvalor.vercel.app`** al instante, gratis, con HTTPS.

**Alternativa gratis — GitHub Pages:**
1. Repo en GitHub con el contenido de `sitio-web/` en la raíz.
2. Settings → Pages → Source: rama `main` → guardar. (La URL será `usuario.github.io/repo` — si la usas, avísame para ajustar las URLs.)

## PASO 1.5 — Dominio propio (OPCIONAL, más adelante, ~$12/año)
Cuando quieras verte más pro: compra `davidvalor.dev` en [Namecheap](https://www.namecheap.com) o [Vercel Domains](https://vercel.com/domains) → en Vercel: Project → Settings → Domains → agregar. (Por ahora **no hace falta**, el `.vercel.app` funciona igual para Google.)

## PASO 2 — Google Search Console (indexar, 10 min)
1. Entra: https://search.google.com/search-console
2. Agregar propiedad → tipo **"Prefijo de URL"** → `https://davidvalor.vercel.app`
3. Verifica (lo más fácil: registro **DNS TXT**, o sube el archivo HTML que te dan a `sitio-web/`).
4. Menú **Sitemaps** → envía `sitemap.xml`.
5. Pega tu URL en "Inspección de URL" → **Solicitar indexación**.

## PASO 3 — Perfil de Empresa de Google (lo que te ubica en Maps, 15 min)
Entra: https://www.google.com/business → **"Administrar ahora"**

Rellena con este borrador:
- **Nombre del negocio:** `David Valor — Desarrollo Web & IA`
- **Categoría principal:** `Diseñador de sitios web`
- **Categorías secundarias:** `Desarrollador de software`, `Servicio de marketing en internet`
- **¿Tienes local que visitan los clientes?** → **NO** → quedas como *negocio de servicio*. Así **ocultas tu dirección** y solo muestras zona.
- **Zona de servicio:** `Caracas`, `Distrito Capital`, y agrega `Venezuela (remoto)`.
- **Teléfono / WhatsApp:** tu número.
- **Sitio web:** `https://davidvalor.vercel.app`
- **Verificación:** elige **video** (graban/grabas tu espacio de trabajo + identidad). Sin esto NO apareces.

**Descripción (pégala):**
> Desarrollador web full‑stack y AI Engineer en Caracas. Construyo apps web y móviles, automatización con IA (chatbots, RAG), integraciones LLM y landing pages optimizadas. Sistemas que se envían a producción, no demos. Atención remota, híbrida o presencial en Caracas y toda Venezuela. Defino alcance y costo antes de empezar, con demos semanales.

**Servicios a cargar:** Desarrollo de páginas web · Desarrollo de aplicaciones · Automatización con IA · Chatbots / RAG · Landing pages · Mantenimiento de sistemas.

## PASO 4 — Reseñas (lo que más sube el ranking local)
Cuando el perfil esté verificado, Google te da un **link de reseña**. Mándalo a exclientes con esto:
> Hola [nombre], acabo de abrir mi perfil de Google como desarrollador. ¿Me dejarías una reseña corta de cómo te fue con el proyecto que hicimos? Te paso el link: [link]. ¡Gracias!

## PASO 5 — LinkedIn (rankea para tu nombre)
- Ubicación: **Caracas, Venezuela**.
- Titular: `Desarrollador Web & AI Engineer · Apps + IA · Caracas`.
- Mismo nombre/zona/contacto que en Google (consistencia = Google los cruza).

---

## Orden de impacto
1. Publicar el sitio gratis (Paso 1) ← primero, para tener URL
2. Perfil de Empresa de Google **verificado** (Paso 3) ← lo que te pone en el mapa
3. Reseñas (Paso 4)
4. Search Console (Paso 2) + LinkedIn (Paso 5)
