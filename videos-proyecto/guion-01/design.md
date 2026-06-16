# Design System — David Valor (shorts)

Marca para videos cortos verticales de David Valor (AI Engineer). Tono: técnico, directo, con energía. Audiencia: devs + clientes freelance.

## Colors (Palette)

| Rol | Hex |
|---|---|
| Background (base) | `#07110f` |
| Background alt | `#0b1a17` |
| Foreground (texto) | `#ffffff` |
| Texto secundario | `#9fb4ae` |
| Accent primario (teal) | `#00897b` |
| Accent brillante (cyan) | `#26d0ce` |
| Énfasis / dato (amarillo) | `#ffd166` |

Gradiente de marca: teal `#00897b` → cyan `#26d0ce` (45°).

## Typography

- **Display / títulos:** Inter, weight 800–900.
- **Body / captions:** Inter, weight 700.
- **Código / mono:** JetBrains Mono, weight 500.
- Captions en MAYÚSCULAS para impacto.

## Motion

- Energía alta: entradas scale-pop con `back.out(1.7)`, 0.12–0.2s.
- Variar eases (al menos 3 por escena).
- Captions: 2–3 palabras por grupo, una a la vez.

## Corners / Depth

- Esquinas redondeadas: pills totalmente redondeados (999px), tarjetas 24px.
- Profundidad: glows localizados en teal/cyan sobre fondo oscuro. Nada de gradientes lineales a pantalla completa (banding H.264).

## What NOT to Do

- No usar azul genérico `#3b82f6` ni `Roboto`.
- No gradientes lineales full-screen sobre fondo oscuro.
- No captions tapando la cara (círculo arriba) — van en la franja media-baja.
