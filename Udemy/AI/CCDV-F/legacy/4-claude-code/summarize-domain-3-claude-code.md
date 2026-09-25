# Domain 3: Claude Code

> Curso: Claude Certified Developer Foundations (CCDV-F)

Resumen del PDF oficial de **Domain 3: Claude Code**. Cubre dos lecciones: los building
blocks de Claude Code (qué es, Rules, Skills, Commands, Agents y Agent Memory) y cómo se
ejecuta en la práctica (`/init`, la jerarquía de `CLAUDE.md`, `settings.json`, gestión de
sesiones y los modos de ejecución).

## 1. Claude Code — The Building Blocks

### ¿Qué es Claude Code?

Claude Code es **Claude trabajando dentro de tu código base** — en terminal, desktop app
o IDE — y no en una ventana de chat aparte. Desde ahí puede leer tus archivos, ejecutar
comandos, editar código y corregir sus propios errores directamente sobre el proyecto.

> 🎯 Es un dominio pequeño en el examen — se trata de conocer las piezas que configuras y
> cómo las ejecutas, no de teoría profunda.

### Rules — instrucciones que cargan cuando hacen falta

Las **rules** viven en `.claude/rules/` como archivos separados (ej. `database.md`,
`frontend.md`, `testing.md`). En vez de un único archivo de instrucciones gigante que
siempre ocupa memoria, cada rule carga **solo cuando se tocan los archivos que le
corresponden** — editar un archivo de base de datos carga la rule de `database.md`;
editar el frontend no la carga.

> 📌 Rules = tus instrucciones de proyecto, divididas en piezas enfocadas que cargan solo
> cuando son relevantes. Mantiene el contexto limpio — la misma lección del Domain 1
> sobre evitar el bloat.

### Skills — conocimiento reutilizable para una tarea

Una **skill** es una carpeta de instrucciones que Claude puede invocar para **una clase de
tarea concreta** (ej. "cómo redactar un post de blog", "cómo debuggear nuestros deploys").
Se define en un archivo `SKILL.md` con frontmatter YAML (`name`, `description`) y el
contenido en Markdown:

```yaml
---
name: blog-post
description: draft a post
---
# How to draft a blog post for this site…
```

Hay dos formas de dispararla:

- Escribiendo el comando explícito: `/blog-post`.
- Dejando que Claude detecte una tarea que coincide con la descripción de la skill.

> 💡 Las skills cargan solo cuando se disparan — así no saturan cada conversación con
> instrucciones que no aplican.

### Commands — built-in y custom

Los **slash commands** son atajos que escribes para controlar la sesión sin salir del
terminal.

| Tipo                                                        | Comando    | Qué hace              |
| ----------------------------------------------------------- | ---------- | --------------------- |
| **Built-in** (vienen con Claude Code)                       | `/init`    | configura un proyecto |
|                                                             | `/clear`   | reinicia la sesión    |
|                                                             | `/compact` | reduce el historial   |
| **Custom** (los tuyos — un archivo se convierte en comando) | `/deploy`  | tus pasos de deploy   |
|                                                             | `/standup` | tu resumen diario     |

Ambos tipos controlan la sesión sin salir del terminal; los commands son el siguiente
componente central después de rules y skills.

### Agents — especialistas para subtareas

Un **agent** dentro de Claude Code recibe un trabajo enfocado y lo ejecuta con su propio
contexto limpio, separado de la sesión principal:

```text
Claude Code (main session)
  ├─ 🔍 Review agent        — own clean context
  ├─ 🧪 Test-writing agent  — own clean context
  └─ 📦 Refactor agent      — own clean context
```

Es exactamente la idea de **subagent** del Domain 1 — un helper enfocado con su propio
contexto limpio hace un solo trabajo y reporta de vuelta. Esto mantiene el contexto
principal sin saturar y habilita trabajo en paralelo.

### Agent Memory — lo que Claude recuerda

Hay dos tipos de memoria, según quién la escribe:

|                  | `CLAUDE.md`                            | Auto memory                                                                       |
| ---------------- | -------------------------------------- | --------------------------------------------------------------------------------- |
| Quién la escribe | **TÚ** la escribes                     | Claude la **APRENDE**                                                             |
| Qué contiene     | Las reglas que anotas para el proyecto | Patrones que Claude detecta solo: tu build command, tu estilo de código preferido |

Las rules (sección anterior) son simplemente `CLAUDE.md` partido en piezas — pertenecen a
la misma familia de mecanismo.

> 💡 Uno es explícito y escrito por ti; el otro es aprendido. Juntos, Claude no empieza de
> cero en cada sesión.

## 2. Claude Code — Running It

### Starting a project — `/init`

Un solo comando escanea todo tu repositorio y escribe tu primer `CLAUDE.md`:

```text
/init  →  escanea tu repositorio (todos los archivos)  →  escribe un CLAUDE.md inicial
```

Es más rápido que escribirlo a mano, y suele ser lo primero que se ejecuta en un
repositorio nuevo. Después de generado, tú lo editas para añadir tus propias reglas.

### La jerarquía de `CLAUDE.md`

Las reglas se apilan de lo **amplio** a lo **específico**, según el nivel de carpeta:

| Nivel                      | Alcance                         |
| -------------------------- | ------------------------------- |
| 🏠 Home folder `CLAUDE.md` | tus propios hábitos             |
| 📁 Project `CLAUDE.md`     | compartido con el equipo        |
| Sub-folder `CLAUDE.md`     | un área específica del proyecto |

> 📚 Se lee **hacia arriba** en el árbol de directorios: la base amplia se lee primero
> (⬇ broad base), y las reglas más específicas se añaden encima (⬆ more specific),
> agregando detalle donde hace falta.

Esto conecta directamente con las ideas de configuración vistas en el Domain 2.

### `settings.json` — un recap rápido

`settings.json` es el panel de control **machine-readable** que ya se vio en el Domain 2:
define qué tools están permitidas y cómo está todo cableado.

```json
// .claude/settings.json
{
  "permissions": {
    "allow": ["Bash", "Read"]
  }
}
```

Se combina (merge) desde varios niveles: primero **user settings**, luego **project
settings** — y los ajustes definidos después sobrescriben a los anteriores.

> ✅ Eso es todo lo que hace falta recordar aquí — el deep dive completo fue en
> "Configuration Management" del Domain 2.

### Gestión de sesiones — guardar, retomar, reiniciar

El trabajo en Claude Code vive como una **sesión** a la que puedes volver:

| Acción            | Qué hace                                    |
| ----------------- | ------------------------------------------- |
| ▶️ **Resume**     | retomar la sesión donde la dejaste          |
| 🌿 **Branch**     | dividir la sesión hacia una nueva dirección |
| ⏮️ **Checkpoint** | volver a un punto anterior de la sesión     |
| 🧹 **/clear**     | reiniciar una sesión saturada               |

`/clear` es la misma regla de higiene de sesión del Domain 2, ahora aplicada directamente
en la herramienta.

> ⚠️ Precaución de examen: los checkpoints **NO son Git** — no pueden deshacer efectos
> secundarios en el mundo real, como una llamada a una API que ya se envió.

### Dos formas de correrlo — Interactive vs Headless

|             | Interactive                               | Headless                                              |
| ----------- | ----------------------------------------- | ----------------------------------------------------- |
| Cómo se usa | Tú escribes, Claude responde, tú observas | Pasas la tarea completa, sin UI, imprime el resultado |
| Comando     | `claude`                                  | `claude -p "…"`                                       |
| Perfil      | Una persona en el terminal                | Un script dentro de un pipeline                       |

Headless mete a Claude Code en pipelines de **CI/CD** — el mismo eco del principio
"stream para humanos, no para máquinas" del Domain 2.

### Output modes — Streaming y Auto-mode

Son dos ejes **independientes**, no alternativas del mismo control:

- **Streaming mode** — cómo fluye el output: `stream-json → event → event`, un feed en
  vivo de eventos pensado para un programa que consume el output paso a paso.
- **Auto-mode** — cómo se manejan los permisos: un segundo modelo revisa cada tool call,
  y las acciones rutinarias se aprueban automáticamente en vez de detenerse a
  preguntarte.

> ⚠️ Ojo con esto: uno controla cómo fluye el **OUTPUT**; el otro controla cómo se
> manejan las **APROBACIONES** — ninguno de los dos controla la ejecución en sí.

## Puntos clave del dominio

- Claude Code es Claude trabajando directamente dentro del código base (terminal,
  desktop o IDE) — no en una ventana de chat.
- **Rules** cargan cuando son relevantes al archivo que se toca; **Skills** cargan cuando
  se disparan (por comando explícito o porque Claude detecta la tarea).
- **Commands** son atajos slash: built-in (`/init`, `/clear`, `/compact`) o custom
  (definidos por ti).
- **Agents** dentro de Claude Code son subagents con contexto limpio para subtareas
  enfocadas; **Agent Memory** combina lo que tú escribes en `CLAUDE.md` con lo que Claude
  aprende automáticamente.
- `/init` genera el primer `CLAUDE.md`; múltiples archivos `CLAUDE.md` se apilan de lo
  amplio (home, project) a lo específico (sub-folder), leyéndose de abajo hacia arriba.
- `settings.json` es el panel de permisos machine-readable, con merge de user settings →
  project settings.
- Las sesiones se guardan, retoman (resume), ramifican (branch) y reinician (`/clear`) —
  pero los checkpoints **no son Git** y no deshacen efectos secundarios reales.
- **Interactive** vs **Headless** es *quién* opera Claude Code (persona vs. pipeline);
  **Streaming** vs **Auto-mode** son ejes independientes que controlan, respectivamente,
  cómo fluye el output y cómo se manejan las aprobaciones — no la ejecución.
