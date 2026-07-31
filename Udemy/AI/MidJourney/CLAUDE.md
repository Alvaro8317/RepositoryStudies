# MidJourney — Apuntes de estudio del curso de Udemy

Este repositorio contiene los apuntes de Alvaro del curso de Udemy sobre **Midjourney** (generación
de imágenes y video con IA): conceptos clave, configuración, uso en Discord, técnicas de prompting y
novedades de la versión 7.

## Rol de Claude en este repo

Claude actúa como asistente para **transformar transcripciones de clases del curso en apuntes en
Markdown**. El flujo de trabajo es:

1. El usuario indica en qué carpeta (sección) deben ir los apuntes de la próxima clase.
2. El usuario pega la transcripción de la clase (texto crudo, puede venir con muletillas, repeticiones, etc.).
3. Claude debe:
   - Capturar **lo más importante** de la transcripción: conceptos clave, definiciones, comandos y
     parámetros de Midjourney, pasos de práctica, tablas cuando ayuden a resumir, advertencias/notas
     importantes (usar `>` con ⚠️ cuando aplique).
   - Redactar el apunte en **español**, con estructura clara y nivel de detalle consistente con los
     archivos ya existentes en la carpeta correspondiente (ver ejemplos en carpetas ya pobladas).
   - Proponer **2-3 nombres de archivo candidatos** que respeten la nomenclatura del proyecto (ver
     sección siguiente) para que el usuario elija antes de escribir el archivo definitivo.
4. Claude NO debe archivar por su cuenta transcripciones futuras sin que el usuario indique
   primero la carpeta destino.

### Transcripción: cuidado con errores de dictado y términos en inglés

Las transcripciones vienen de audio a texto y pueden contener **errores de reconocimiento de voz**,
especialmente sobre términos técnicos/comandos de Midjourney y Discord en inglés que el motor de
transcripción "traduce" o distorsiona fonéticamente. Antes de redactar el apunte, Claude debe
interpretar el contexto y corregir estos casos:

- Los **comandos, parámetros y nombres propios de Midjourney/Discord deben quedarse en inglés**, tal
  como aparecen en la documentación oficial (ej. `/imagine`, `--ar`, `--chaos`, `--stylize`, `--v`,
  `--niji`, `seed`, `upscale`, `variations`, `prompt`, `remix mode`, `Discord server`, `channel`,
  `slash command`) — no traducirlos al español aunque la transcripción los haya traducido o
  distorsionado.
- Si Claude detecta una palabra o frase que suena a una mala transcripción de un término/comando en
  inglés (fonéticamente parecida, fuera de contexto, ej. "estilizar" en vez de `--stylize`, "caos" en
  vez de `--chaos`), debe usar el término correcto en inglés y, si hay ambigüedad real sobre a qué
  comando/parámetro se refería, preguntar al usuario antes de asumir.

## Convención de nombres de archivo

Cada carpeta de sección numerada (`1-`, `2-`, `3-`...) contiene archivos Markdown numerados
secuencialmente dentro de esa misma carpeta, empezando en `1-`:

```text
<numero>-<slug-descriptivo-corto>.md
```

Reglas:

- El número siempre va primero, seguido de un guion.
- El slug es corto, en minúsculas, **siempre en inglés**, palabras separadas por guiones (el
  contenido del apunte sí va en español, solo el nombre de archivo va en inglés).
- Los archivos de práctica/ejercicios suelen llevar el prefijo `practice-` (ej.
  `3-practice-prompts.md`).
- La numeración es **por carpeta**, no global — cada sección reinicia en `1-`.
- No renombrar ni renumerar archivos ya existentes al añadir uno nuevo; el nuevo archivo simplemente
  continúa la secuencia del folder correspondiente.

## Estructura del repositorio

```text
MidJourney/
├── 1-introduction/                        # Introducción y conceptos clave de Midjourney
├── 2-first-steps-and-config/              # Fundamentos prácticos: primeros pasos y configuración
├── 3-intermediate-techniques/             # Técnicas intermedias para mejorar resultados visuales
├── 4-discord-bots-channels-commands/      # Uso de bots, canales y comandos en Discord
├── 5-creative-exercises-and-prompts/      # Ejercicios creativos y prompts profesionales
├── 6-advanced-styles-parameters-control/  # Estilos, parámetros y control total de las imágenes
├── 7-v7-updates/                          # Novedades de Midjourney V7
└── 8-video-creation-with-ai/              # Creación de videos con IA, animaciones y técnicas visuales
```

### Formato de cada apunte

Cada archivo `.md` sigue esta estructura:

- Título `#` con el nombre del tema/clase.
- Línea de contexto: `> Curso: Midjourney (Udemy)`
- Secciones con `##`/`###` por subtema.
- Tablas Markdown para comparativas o resúmenes de parámetros/comandos.
- Notas de advertencia con `> ⚠️ ...` cuando algo es un detalle importante o contraintuitivo.
