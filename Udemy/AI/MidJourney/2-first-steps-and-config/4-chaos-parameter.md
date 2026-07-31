# El parámetro `--chaos` (`--c`)

> Curso: Midjourney (Udemy)

## Qué es `--chaos`

`--chaos` (abreviado `--c`) controla cuánta **variabilidad o aleatoriedad** aplica Midjourney al
generar el conjunto de imágenes (las 4 variaciones de un mismo prompt).

```text
--c <valor>
```

- Con **caos bajo**, las imágenes generadas son similares entre sí.
- Con **caos alto**, los resultados son muy distintos entre sí, incluso usando el mismo prompt.

Se escribe con doble guion medio, igual que `--ar` y `--s`, y admite tanto `--chaos` como `--c`.

## Rango de valores

Es un valor numérico entre **0 y 100**.

| Rango               | Comportamiento                                                        |
| ------------------- | --------------------------------------------------------------------- |
| **0 – 20** (bajo)   | Resultados consistentes, con variaciones sutiles entre las 4 imágenes |
| **30 – 60** (medio) | Variaciones perceptibles, pero aún conectadas al patrón base          |
| **70 – 100** (alto) | Resultados inesperados, creativos y muy variados entre sí             |

## Ejemplo comparativo

Prompt base: `un guerrero medieval con espada de fuego, fondo de castillo en ruinas --ar 3:4`

| Comando  | Resultado                                                                                                                                                                                                       |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--c 10` | Las 4 imágenes tienen poses, armaduras y fondos similares; solo pequeños cambios en detalles como la dirección de la luz o el estilo del fuego                                                                  |
| `--c 90` | Las 4 imágenes son muy diferentes entre sí: una puede ser caricaturesca, otra estilo videojuego, otra con fondo nevado, otra en un paisaje apocalíptico. Mismo prompt, interpretaciones completamente distintas |

> Para reutilizar el mismo prompt con otro valor de `--chaos` sin reescribirlo, se puede pasar el
> cursor sobre una imagen ya generada y usar la opción **Use** (aparece junto a **Re-run** y otras
> opciones), que copia el prompt y sus parámetros al campo de generación para editarlos.

## Cuándo usar cada rango

- **Coherencia para un producto o diseño preciso** → `--c` entre 0 y 20.
- **Experimentar distintas ideas desde un mismo prompt** → `--c` entre 60 y 80.
- **Creatividad libre y resultados impredecibles** → `--c` entre 90 y 100.

## Ejercicio propuesto

Con el prompt `una nave espacial aterrizando en un planeta alienígena, estilo ciencia ficción --ar
16:9`, generar tres variaciones cambiando solo el valor de `--c`: **10, 50 y 90/100**. Observar qué
tanto cambian los colores, el estilo y el escenario, y cuál resulta más exploratorio.

## Conclusión

`--chaos` es el aliado para explorar, romper patrones y desbloquear creatividad, o simplemente dejar
que Midjourney sorprenda:

- Caos bajo → precisión.
- Caos alto → experimentación.

Es especialmente útil en etapas tempranas de diseño o brainstorming visual.
