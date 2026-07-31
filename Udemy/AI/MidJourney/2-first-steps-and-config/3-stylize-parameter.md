# El parámetro `--stylize` (`--s`)

> Curso: Midjourney (Udemy)

## Qué es `--stylize`

`--stylize` (abreviado `--s`) es un comando que controla cuánta **estética artística** añade
Midjourney automáticamente a una imagen, más allá de lo que se pidió explícitamente en el prompt. En
otras palabras, determina cuánta libertad creativa extra toma la IA sobre el resultado.

```text
--s <valor>
```

Se escribe con doble guion medio, igual que `--ar`.

## Rango de valores

Es un valor numérico entre **0 y 1000**.

| Rango                 | Comportamiento                                                                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **0 – 100** (bajo)    | Midjourney sigue el prompt de forma más precisa y fiel, con menos adornos, efectos o composiciones inesperadas                             |
| **250 – 500** (medio) | Equilibrio entre fidelidad al prompt y belleza/creatividad añadida                                                                         |
| **750 – 1000** (alto) | Midjourney toma más libertad creativa: imágenes más artísticas, complejas o visualmente impactantes, aunque a veces menos fieles al prompt |

## Ejemplo comparativo

Prompt base: `un lobo blanco sobre una roca, fondo de bosque, estilo realista --ar 16:9`

| Comando    | Resultado                                                                                                                                                                                                                                                                             |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--s 50`   | Imagen limpia, enfocada en mostrar exactamente lo que pide el prompt: posición clara, sin elementos decorativos excesivos, fondo sencillo, proporciones naturales. Ideal para proyectos técnicos, precisión en diseño y fotorrealismo                                                 |
| `--s 1000` | Imagen mucho más artística y expresiva: colores más intensos, texturas más elaboradas, poses más dramáticas, posibles elementos adicionales (luces místicas, niebla brillante, composición cinematográfica). Ideal para arte conceptual, portadas, posters e imágenes inspiracionales |

> En la interfaz, se puede reutilizar un prompt ya usado (propio o de la comunidad) haciendo clic sobre
> él para copiarlo al campo de generación, sin necesidad de reescribirlo, y así comparar variaciones
> cambiando solo el `--s`.

## Cuándo usar cada rango

- **Máxima fidelidad al prompt** → `--s` entre 0 y 100.
- **Equilibrio entre claridad y belleza** → `--s` entre 250 y 500.
- **Impacto visual y estilo artístico libre** → `--s` entre 750 y 1000.

## Ejercicio propuesto

Con el prompt `un paisaje montañoso con niebla suave al amanecer, estilo fotográfico --ar 16:9`,
generar tres variaciones cambiando solo el valor de `--s`: **50, 500 y 1000**. Comparar qué cambia en
la composición, cuál resulta más realista y cuál más atractiva visualmente.

## Conclusión

`--stylize` es una herramienta poderosa para modular la estética visual de las imágenes y adaptar los
resultados a necesidades comerciales:

- Precisión (ej. catálogo de productos) → valor bajo.
- Contenido editorial → valor medio/equilibrado.
- Impacto visual (ej. portadas, posters, arte conceptual) → valor alto.

Es especialmente útil para desarrollar un estilo propio o generar variaciones de un mismo resultado
sin cambiar el prompt original.
