# CCDV-F — Apuntes de estudio para Claude Certified Developer Foundations

Este repositorio contiene los apuntes de Alvaro para preparar la certificación **Claude Certified
Developer Foundations (CCDV-F)** de Anthropic, basados en cursos de Udemy.

## Curso actual y curso legacy

- **Curso actual**: **"Claude Certified Developer - Foundations (CCDV-F)-Exam Prep"**. Todos los
  apuntes nuevos se escriben para este curso, en carpetas de módulo numeradas en la raíz del repo.
- **Curso legacy**: los apuntes del primer curso que Alvaro tomó viven en `legacy/` (módulos
  `1-introduction/` a `9-tools-and-mcps/`, incluido el proyecto de práctica `practice-sortly/`).
  Alvaro lo abandonó porque las prácticas eran aburridas y poco claras, y la teoría se hacía pesada.
  Esos apuntes se conservan como referencia, pero **no se agregan apuntes nuevos en `legacy/`** ni
  se renumeran; la numeración de módulos de la raíz arranca de nuevo en `1-`.

## Rol de Claude en este repo

Claude actúa como asistente para **transformar transcripciones de clases del curso en apuntes en
Markdown**. El flujo de trabajo es:

1. El usuario indica en qué carpeta (módulo) deben ir los apuntes de la próxima clase.
2. El usuario pega la transcripción de la clase (texto crudo, puede venir con muletillas, repeticiones, etc.).
3. Claude debe:
   - Capturar **lo más importante** de la transcripción: conceptos clave, definiciones, comparativas,
     pasos de práctica, ejemplos de código/prompts cuando ayuden a ilustrar un concepto, tablas
     Markdown cuando ayuden a resumir, advertencias/notas importantes (usar `>` con ⚠️ cuando
     aplique).
   - Redactar el apunte en **español**, con un tono consistente y nivel de detalle uniforme a lo
     largo del repositorio (ver ejemplos existentes en el módulo correspondiente una vez existan).
   - Usar un **español latinoamericano con giros de Colombia/México**, con tuteo ("tú puedes",
     "fíjate", "mira", "aquí"), y **no rioplatense (argentino/uruguayo)**: evitar el voseo ("vos",
     "podés", "querés", "fijate", "mirá", "hacé") y regionalismos como "acá", "calzar" (usar
     "encajar"), "parado en" (usar "ubicado en") o "tira un error" (usar "arroja un error"). Aplica
     sobre todo a los apuntes, pero también a las respuestas en la conversación.
   - Proponer **2-3 nombres de archivo candidatos** que respeten la nomenclatura del proyecto (ver
     sección siguiente) para que el usuario elija antes de escribir el archivo definitivo.
   - Escribir el apunte **directamente en la ruta final** (`<carpeta>/<numero>-<slug-elegido>.md`) una
     vez el usuario elige el nombre — no redactarlo primero en un scratchpad/tmp y copiarlo después.
     Si el usuario decide renombrar el archivo más adelante, basta con hacer `mv`/renombrar, no hace
     falta reescribir el contenido.
4. Claude NO debe archivar por su cuenta transcripciones futuras sin que el usuario indique
   primero la carpeta destino.

### Transcripción: cuidado con errores de dictado y términos en inglés

Las transcripciones vienen de audio a texto y pueden contener **errores de reconocimiento de voz**,
especialmente sobre términos técnicos en inglés que el motor de transcripción "traduce" o distorsiona
fonéticamente. Antes de redactar el apunte, Claude debe interpretar el contexto y corregir estos casos:

- Los **términos y nombres propios de productos/conceptos de Anthropic y de la industria de LLMs
  deben quedarse en inglés**, tal como aparecen en la documentación oficial (ej. `prompt`, `prompt
  caching`, `system prompt`, `tool use`, `function calling`, `context window`, `embeddings`, `RAG`,
  `fine-tuning`, `temperature`, `token`, `Model Context Protocol (MCP)`, `subagent`, `hooks`,
  `guardrails`, `jailbreak`, `red teaming`, `few-shot`, `chain-of-thought`, nombres de modelos como
  `Claude Opus`, `Claude Sonnet`, `Claude Haiku`) — no traducirlos al español aunque la transcripción
  los haya traducido o distorsionado.
- Si Claude detecta una palabra o frase que suena a una mala transcripción de un término técnico en
  inglés (fonéticamente parecida, fuera de contexto, etc.), debe usar el término correcto en inglés y,
  si hay ambigüedad real sobre a qué concepto se refería, preguntar al usuario antes de asumir.

## Convención de nombres de archivo

Cada carpeta de módulo numerada (`1-`, `2-`, `3-`...) contiene archivos Markdown numerados
secuencialmente dentro de esa misma carpeta, empezando en `1-`:

```text
<numero>-<slug-descriptivo-en-ingles>.md
```

Ejemplo ilustrativo del patrón (los nombres reales dependerán del contenido de cada clase):

- `1-introduction-to-claude.md`
- `2-prompt-engineering-basics.md`
- `3-tool-use.md`
- `4-practice-tool-use.md`

Reglas:

- El número siempre va primero, seguido de un guion.
- El slug es corto, en minúsculas, palabras separadas por guiones, y **siempre en inglés**
  (aunque el contenido del apunte se redacte en español).
- Los archivos de práctica/laboratorio suelen llevar el prefijo `practice-` (ej. `4-practice-tool-use.md`).
- La numeración es **por carpeta**, no global — cada módulo reinicia en `1-`.
- No renombrar ni renumerar archivos ya existentes al añadir uno nuevo; el nuevo archivo simplemente
  continúa la secuencia del folder correspondiente.

## Estructura del repositorio

> ⚠️ Las carpetas de módulos del curso actual se van creando a medida que el usuario indica en qué
> carpeta van los apuntes de cada clase: Claude crea la carpeta numerada correspondiente
> (`1-<slug>/`, `2-<slug>/`, ...) siguiendo el temario real del curso — no asumir de antemano qué
> módulos existen. Antes de confiar en cualquier árbol de carpetas que se documente aquí, verificar
> con `ls` en vez de asumir que está al día.

```text
CCDV-F/
├── legacy/          apuntes del curso anterior (solo referencia, no se agregan apuntes)
└── (carpetas de módulos del curso actual, numeradas secuencialmente según su temario)
```

### Formato de cada apunte

Cada archivo `.md` sigue esta estructura:

- Título `#` con el nombre del tema/concepto.
- Línea de contexto: `> Curso: Claude Certified Developer - Foundations (CCDV-F)-Exam Prep`
  (los apuntes de `legacy/` conservan la línea anterior,
  `> Curso: Claude Certified Developer Foundations (CCDV-F)`, y no se modifican).
- Secciones con `##`/`###` por subtema.
- Tablas Markdown para comparativas o resúmenes de conceptos.
- Bloques de código para ejemplos de prompts, snippets de la API, configuración de herramientas, etc.
- Notas de advertencia con `> ⚠️ ...` cuando algo es un detalle importante o contraintuitivo.

### Formateo automático

Este repositorio usa **markdownlint-cli2** para formatear Markdown automáticamente:

- `package.json` declara `markdownlint-cli2` como devDependency (`npm install` para instalarlo
  en `node_modules/`, ignorado por git).
- `.markdownlint-cli2.jsonc` configura las reglas. Se desactivan dos reglas por decisión de
  estilo del repo, no por descuido:
  - `MD013` (line-length): los apuntes tienen párrafos largos en español, no se fuerza wrap.
  - `MD028` (no-blanks-blockquote): el formato del repo encadena varios recuadros
    `> ⚠️/🎯/📌/💡` independientes separados por una línea en blanco; no son un único blockquote.
- `.claude/settings.json` define un hook `PostToolUse` que corre
  `markdownlint-cli2 --fix` sobre cualquier `.md` que Claude escriba o edite (`Write`/`Edit`),
  incluyendo el realineado de tablas (`MD060`, estilo `aligned`).
- `npm run lint:md` / `npm run lint:md:fix` corren el lint manualmente sobre todo el repo.

> ⚠️ El auto-fix de `MD060` para tablas con emoji (ancho visual doble) puede no resolverse solo
> con `--fix` — si markdownlint sigue marcando una tabla como desalineada tras el hook, hay que
> repadear las celdas a mano (o con un script que use `string-width`, como en el commit que
> introdujo esta configuración) en vez de forzar el commit con el aviso activo.
