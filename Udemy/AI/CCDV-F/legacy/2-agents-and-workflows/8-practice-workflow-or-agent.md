# Practice: Workflow or Agent (Lab 1) — Proyecto "Sortly"

> Curso: Claude Certified Developer Foundations (CCDV-F)

## Introducción

Con el entorno del [lab 0](./7-practice-lab-setup.md) ya funcionando, este lab retoma la
pregunta de [[1-workflow-or-agent]] — ¿decides tú los pasos, o los decide Claude? — pero
esta vez sobre la carpeta real de Asha. Son tres demos en
[`practice-sortly/demos/`](./practice-sortly/demos/): un pipeline rígido, el mismo
trabajo entregado a un agent, y un demo final que no ejecuta nada, solo enseña **cómo
elegir**.

## 1. Demo 1 — El pipeline rígido (workflow)

`practice-sortly/demos/p1_pipeline_rigid.py` resetea `workspace/` desde
`workspace_seed/` y después ordena por **reglas fijas de keyword matching** sobre el
nombre del archivo — nunca abre un archivo, solo mira el nombre:

```python
RULES = [
    ("finance", ["bill", "receipt", "statement", "form16", "insurance"]),
    ("work",    ["meeting", "sprint", "resume"]),
    ("personal",["grocery", "wedding", "trek"]),
]
```

```bash
python demos/p1_pipeline_rigid.py
```

Resultado esperado: **12 archivos ordenados, 2 `UNKNOWN`** (`untitled_1.txt` y
`screenshot_error_2026_08_11.txt` — ningún keyword de la lista los toca), **cero llamadas
a la API, cero costo**. Es puro Python: determinístico, rápido y auditable, pero ciego a
cualquier archivo que nadie anticipó.

> ⚠️ En la grabación el instructor ve **3** desconocidos en vez de 2, y lo atribuye a un
> `desktop.ini` que Google Drive agrega porque tenía la carpeta sincronizada. Es un
> artefacto de su máquina, no del proyecto: `workspace_seed/` tiene exactamente 14
> archivos reales, y el resultado esperado según `LAB-1-Workflow-or-Agent.md` es 12/2, no
> 12/3.

## 2. Demo 2 — El mismo trabajo, entregado a un agent

`practice-sortly/demos/p1_pipeline_with_model.py` resetea la carpeta otra vez y le pasa
el mismo problema a Claude, pero como **goal**, no como procedimiento — describe qué
lograr, no cómo:

```python
SYSTEM = """You are Sortly, a tidy-up assistant for Asha's downloads folder in Pune.

Your job: put every loose file into exactly one of these folders -
finance, work, personal, misc.

How to work:
- Call list_files first to see what is there.
- If a filename does not make the contents obvious, call read_file_head
  before deciding. Do not guess from the name alone.
- Then call move_file once per file.
- Use misc only when a file truly fits nothing else.
...
"""
```

Corre a través de `run_agent()` (`practice-sortly/core/agent.py` — el loop escrito a
mano que se presenta formalmente recién en el lab 2, pero este demo ya lo usa) con las
mismas cinco tools del lab 0.

```bash
python demos/p1_pipeline_with_model.py
```

Lo que hay que mirar en la traza: para `untitled_1.txt` y `screenshot_error_...` aparece
primero un `read_file_head` y después un `move_file` — esa lectura es exactamente la
decisión que el pipeline rígido no podía tomar. Al final, el demo compara turnos y tokens
gastados contra los "0 llamadas, Rs 0" del demo 1: ninguna de las dos formas es gratis,
cada una cobra en una moneda distinta.

> 📌 Si corres esto con `uv run` en vez de `python`, `uv` revisa y reinstala
> dependencias antes de cada corrida — por eso el instructor lo canceló y volvió a
> `python demos/...` directo, que no repite ese chequeo.

## 3. Demo 3 — Eligiendo la forma deliberadamente

`practice-sortly/demos/p1_choose_the_shape.py` **no llama a la API ni mueve un solo
archivo** — es Python plano que imprime la regla para decidir, aplicable a cualquier
tarea nueva, no solo a la carpeta de Asha.

Seis preguntas de sí/no:

| Pregunta                                           | Sí →     | No →     |
| -------------------------------------------------- | -------- | -------- |
| ¿Los pasos se conocen antes de correr?             | workflow | agent    |
| ¿El orden de los pasos es fijo?                    | workflow | agent    |
| ¿El conjunto de inputs posibles está acotado?      | workflow | agent    |
| ¿Cada corrida debe ser idéntica y auditable?       | workflow | agent    |
| ¿El siguiente paso depende de lo que se encuentra? | agent    | workflow |
| ¿El input es lenguaje natural abierto?             | agent    | workflow |

Y seis casos resueltos, entre ellos las dos trampas que el demo marca explícitamente:

- **"Redimensionar cada imagen de una carpeta a 800px de ancho" → workflow.** Mucha
  gente dice *agent* aquí porque acaba de ver a un agent hacer algo inteligente — pero es
  una transformación puramente determinística, sin juicio de por medio.
- **"Leer una queja entrante y enrutarla al equipo correcto" → agent.** Otros dicen
  *workflow*, porque el demo 1 hizo ver a los workflows como baratos y seguros — pero aquí
  no se pueden escribir las reglas de enrutamiento de antemano para un texto que todavía
  no se leyó.

```bash
python demos/p1_choose_the_shape.py
```

> ⚠️ La trampa que nombra el propio demo: envolver una tarea fija de tres pasos en un
> agent loop compra no-determinismo, latencia y costo, y no le da nada al usuario. La
> trampa inversa también es real: forzar un trabajo abierto dentro de reglas fijas es
> exactamente la columna `UNKNOWN` del demo 1.

## Puntos clave

1. 12 de 14 archivos ordenados gratis es un **buen** resultado — el workflow no es el
   villano de este lab.
2. La ventaja del agent aparece justo en los archivos que las reglas no podían resolver,
   pero cobra tokens sobre los 14 archivos, no solo sobre esos dos.
3. La regla de decisión: pasos conocidos + orden fijo + input acotado → workflow;
   siguiente paso depende de lo que se encuentra, o input es lenguaje natural abierto →
   agent.
4. Muchos sistemas reales son un workflow con un paso de agent adentro, no una cosa o la
   otra.
