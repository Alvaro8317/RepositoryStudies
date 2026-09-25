# Practice: Lab Setup — Proyecto "Sortly"

> Curso: Claude Certified Developer Foundations (CCDV-F)

## Introducción: el primer hands-on lab

Este es el primer hands-on lab del curso, y cubre en la práctica los conceptos del
domain 1 (agents y workflows) — 14.7% del examen. Este lab en particular es solo el
setup del entorno — antes de tocar código de agents, hay que dejar el proyecto
corriendo. El código de referencia vive en
[`practice-sortly/`](./practice-sortly/), junto a este apunte.

> ⚠️ La transcripción original de la clase dice "Shortly", pero el proyecto real se
> llama **Sortly** (`practice-sortly/pyproject.toml:2` — `name = "sortly"`).

## 1. La historia: el proyecto Sortly

Asha Kulkarni es backend developer en Kothrud, Pune. Su carpeta de Downloads tiene 14
archivos sueltos: dos facturas de luz, un recibo de alquiler, un Form 16, un extracto de
un SIP, notas de sprint, una lista de compras, una invitación de boda, un archivo
llamado `untitled_1.txt`, y dos copias de su currículum que no son idénticas. Sortly
ordena esa carpeta.

A lo largo de 6 labs (18 demos en total) se ordena de seis formas distintas, y cada una
enseña un concepto del domain 1:

| Lab | La idea central                                                         | Tool usada                              |
| --- | ----------------------------------------------------------------------- | --------------------------------------- |
| 0   | Levantar el entorno y conocer la carpeta                                | Messages API                            |
| 1   | Un workflow no decide nada en runtime; un agent decide todo             | Python plano, luego Messages API        |
| 2   | Un agent loop es un `while`, y el SDK lo escribe por ti                 | Messages API, luego Agent SDK           |
| 3   | Devolver la conclusión, no la evidencia                                 | Messages API                            |
| 4   | Un prompt persuade; un hook obliga                                      | Messages API, luego hooks del Agent SDK |
| 5   | Qué sobrevive entre corridas, y qué no debería sobrevivir dentro de una | Messages API + Python plano             |

## 2. Estructura del proyecto (`practice-sortly/`)

```text
practice-sortly/
├── pyproject.toml          nombre del proyecto: "sortly", requiere Python >=3.10
├── .env                    ANTHROPIC_API_KEY (excluido por .gitignore)
├── check_setup.py          el script de este lab — correr primero
├── reset_workspace.py      restaura la carpeta desordenada
├── workspace_seed/         14 archivos reales, NUNCA se modifican
├── workspace/              se crea en runtime; se destruye libremente
├── core/                   utilidades compartidas, agregadas lab por lab
│   ├── banner.py             las tarjetas concept / step / takeaway de cada demo
│   ├── _shared.py            modelos pineados, cliente, carga de .env, paths
│   ├── tools.py               las cinco tools que usa todo agent del curso
│   ├── agent.py               (Lab 2) el loop escrito a mano
│   ├── sdk_tools.py           (Lab 2) las mismas tools, para el Agent SDK
│   ├── subagents.py           (Lab 3) el subagent clasificador
│   ├── hooks.py               (Lab 4) el guard, para ambos harnesses
│   └── memory.py              (Lab 5) persistencia + pruning del transcript
├── demos/                  15 scripts, prefijados por lab (p1_..., p2_..., ...)
└── labs/                   los seis archivos Markdown con la guía de cada lab
```

> 📌 `workspace_seed/` es la copia pristina — nunca se toca. `workspace/` es la carpeta
> desordenada sobre la que corren los demos, y `reset_workspace.py` la reconstruye
> copiando desde `workspace_seed/` cada vez que hace falta (`practice-sortly/core/_shared.py:76-84`).
> Ningún demo necesita que corras el reset antes: cada uno reconstruye `workspace/` como
> su primer paso.

### Las cinco tools (`practice-sortly/core/tools.py`)

Todos los agents del curso usan las mismas cinco tools:

| Tool             | Qué hace                                                        |
| ---------------- | --------------------------------------------------------------- |
| `list_files`     | lista los archivos sueltos y sin ordenar                        |
| `read_file_head` | lee las primeras líneas de un archivo                           |
| `move_file`      | mueve un archivo a `finance`, `work`, `personal` o `misc`       |
| `rename_file`    | le da a un archivo un nombre más claro                          |
| `delete_file`    | borra un archivo de forma permanente — el lab 4 gira sobre esta |

## 3. Setup del entorno (lab 0)

Con el entorno de Python activado (`uv venv` + activar el `.venv`), ubicado dentro de
`practice-sortly/`:

```bash
uv venv
.venv\Scripts\activate          # WSL/macOS/Linux: source .venv/bin/activate
uv pip install anthropic claude-agent-sdk
```

`anthropic` es el cliente de la Messages API (se usa desde el lab 1). `claude-agent-sdk`
hace falta en los labs 2 y 4, y trae empaquetado el Claude Code CLI — instalar los dos
de una vez evita que un lab posterior se frene por una descarga.

> ⚠️ El `pyproject.toml` del proyecto solo pide **Python 3.10 o más nuevo**
> (`requires-python = ">=3.10"`) y ni siquiera lista `claude-agent-sdk` como dependencia
> fija — queda comentado para agregarlo con `uv add claude-agent-sdk` cuando se llega al
> lab 2. Que el instructor haya fijado 3.12 a mano fue una decisión suya por experiencia
> propia, no un requisito del código.

> ⚠️ Node.js también hace falta para el Agent SDK (labs 2 y 4) — sin él, el SDK instala
> bien pero falla en runtime con un *spawn error* que ni siquiera menciona a Node.
> Conviene confirmar con `node --version` antes de llegar a esos labs.

Confirmar que ambos paquetes quedaron instalados:

```bash
python -c "import anthropic, claude_agent_sdk; print('both installed')"
```

Si arroja `ModuleNotFoundError`, el entorno no está activado.

## 4. Verificar el setup (`check_setup.py`)

`practice-sortly/check_setup.py` hace **cinco** chequeos (no fue una tarjeta de
concepto — es puro plumbing para no depurar el entorno en medio de una lección):

1. Versión de Python.
2. Archivos en `workspace_seed/` — espera exactamente **14**.
3. Los model IDs que el proyecto tiene pineados:
   - `MODEL = "claude-sonnet-5"` (modelo principal de los demos).
   - `FAST_MODEL = "claude-haiku-4-5-20251001"` (más barato, usado por el subagent del
     lab 3).
4. Que `.env` se haya leído y que `ANTHROPIC_API_KEY` esté presente.
5. Una llamada real a la API, pidiéndole al modelo que responda exactamente
   `sortly ready`.

```bash
python check_setup.py
```

> 📌 Los dos model IDs se ven distintos a propósito
> (`practice-sortly/core/_shared.py:55-63`): `claude-sonnet-5` es de la generación 4.6
> en adelante, donde el ID sin fecha **es** el snapshot pineado. `claude-haiku-4-5` sin
> fecha, en cambio, es un alias de conveniencia que sí se mueve — por eso ese va con
> fecha (`-20251001`). Nunca usar un alias que se mueve en código que se va a shippear.

> ⚠️ Si el conteo de `workspace_seed/` no da 14 en Windows, revisa si hay un archivo
> oculto del sistema como `desktop.ini` antes de asumir que hay un bug — el proyecto en
> sí espera exactamente 14, ni uno más.

## Puntos clave

1. El objetivo de Sortly es usar un agent para ordenar automáticamente una carpeta
   desordenada de archivos reales, a lo largo de 6 labs y 18 demos.
2. `workspace_seed/` es la copia pristina que nunca se toca; `workspace/` es la que se
   destruye y reconstruye en cada demo.
3. Las cinco tools (`list_files`, `read_file_head`, `move_file`, `rename_file`,
   `delete_file`) son las mismas para todos los agents del curso — viven en
   `core/tools.py`.
4. `check_setup.py` corre cinco chequeos: Python, seed files, model IDs pineados,
   credenciales, y una llamada real a la API — antes de arrancar cualquier lab.
5. Fijar el model ID exacto (sin alias que se mueva) es la misma disciplina que se repite
   en todo el curso, no una particularidad de este setup.
