# Menú de Settings (configuraciones) en la web

> Curso: Midjourney (Udemy)

## Contexto

Además de escribir comandos con `--` en el prompt (`--ar`, `--s`, `--c`, `--w`), la interfaz **web**
de Midjourney (a junio de 2025) ofrece un panel visual de configuración con controles deslizantes y
botones, accesible antes de generar una imagen. Permite personalizar cómo la IA interpreta el prompt
sin necesidad de escribir parámetros.

> ⚠️ Este menú de Settings es exclusivo de la interfaz **web**. En Discord el control se hace
> únicamente con comandos de texto (`--ar`, `--s`, `--c`, `--w`, etc.).

## Image Size

Define la relación de aspecto (equivalente a `--ar`). Por defecto está en **Square** (`1:1`, cuadrada).

| Opción | Aspect ratio aproximado | Uso |
|---|---|---|
| **Square** (por defecto) | `1:1` | Formato cuadrado |
| **Portrait** | `3:4` (y variantes: `2:3`, `1:2`, `9:16`) | Imagen vertical — más alta que ancha |
| **Landscape** | `16:9` (y variantes: `4:3`, `3:2`, `2:1`) | Imagen apaisada — más ancha que alta |

Ideal para ajustar el formato según el uso final: redes sociales, ilustración, portada, reel, video
vertical, etc.

## Aesthetics (estética visual)

Contiene tres sliders equivalentes a los comandos ya vistos:

| Slider | Equivale a | Qué controla |
|---|---|---|
| **Stylization** | `--stylize` / `--s` | Cuánto estilo artístico añade Midjourney automáticamente. Valor alto → más estética y libertad creativa. Valor bajo → más fidelidad al prompt. Recomendado: alto para arte, bajo para precisión técnica |
| **Weirdness** | `--weird` / `--w` | Qué tan inusual, abstracta o compleja será la imagen. Nivel bajo → resultados normales. Nivel alto → imágenes experimentales o surrealistas. Útil para diseño conceptual, criaturas extrañas, collages digitales |
| **Variety** | `--chaos` / `--c` | Cuánta diferencia habrá entre las 4 imágenes generadas (diversidad interna). Nivel bajo → imágenes parecidas entre sí. Nivel alto → las 4 muy distintas en color, composición y estilo. Excelente para explorar variaciones desde un solo prompt |

> Al pasar el cursor sobre cada slider aparece un tooltip explicando el parámetro, junto con el
> comando `--` equivalente en la esquina superior derecha.

## Model

Permite elegir entre dos modos de interpretación:

| Modo | Comportamiento |
|---|---|
| **Standard** | Más estilizado, optimizado para belleza visual |
| **Raw** | Interpreta el prompt de forma más literal, menos embellecida — recomendado para imágenes técnicas o científicas |

## Version

Permite elegir con qué versión del modelo trabajar. A junio de 2025 la más reciente es la **versión
7** (recomendada para máximo realismo y detalle), pero se puede volver a versiones anteriores (6.1,
5, 3, 1) o a modelos alternativos como **niji** (especializado en estilo anime, entre otros).

También se puede activar el **modo Draft**: genera más rápido y con menor calidad, consumiendo menos
recursos/tokens.

## Speed

Controla la velocidad de renderizado, y depende del **plan de suscripción** contratado (ver **Manage
Subscriptions**):

| Velocidad | Descripción |
|---|---|
| **Fast** | Generación rápida usando la GPU; disponible desde el plan Basic. Tiene un límite mensual de minutos de generación rápida (visible en Manage Subscriptions) |
| **Turbo** | Genera aún más rápido; requiere un plan con soporte Turbo o una compra adicional |
| **Relax** | Generación sin límite de tiempo pero más lenta; solo disponible en planes **Pro** y **Mega**, no en Basic/Standard |

> ⚠️ Las opciones visibles varían según el plan contratado. Con el plan Basic, por ejemplo, solo
> aparecen Fast y Turbo (no Relax).

## Botón Reset

Al hacer clic en **Reset**, el panel vuelve a su configuración por defecto: Image Size en Square,
Aesthetics reiniciados, Model en Standard y Version en la versión por defecto del sistema (no
necesariamente la última usada).

## Conclusión

El menú de Settings de la web es una alternativa visual, sin necesidad de escribir comandos, para
controlar formato, nivel artístico/técnico, complejidad, creatividad, velocidad y calidad de
renderizado. Los comandos (`--ar`, `--s`, `--c`, `--w`, etc.) siguen funcionando igual y logran el
mismo resultado; el panel es simplemente otra forma de llegar a la misma configuración.
