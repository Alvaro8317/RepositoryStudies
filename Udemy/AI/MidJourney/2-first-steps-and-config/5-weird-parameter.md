# El parámetro `--weird` (`--w`)

> Curso: Midjourney (Udemy)

## Qué es `--weird`

`--weird` (abreviado `--w`) le indica a Midjourney que rompa los patrones normales, permitiendo
interpretaciones más abstractas, inusuales o surrealistas del prompt. No significa "mal hecho", sino
imágenes más complejas, impredecibles y creativas que se alejan del estándar visual.

Activa el "modo extraño" del modelo. Es ideal para arte experimental, conceptos originales, ideas
inusuales o inspiración visual no convencional.

```text
--w <valor>
```

Se escribe con doble guion medio, igual que `--ar`, `--s` y `--c`, y admite tanto `--weird` como `--w`.

> Es similar al comando `--chaos`, pero mientras `--chaos` controla la **variación entre las 4
> imágenes** generadas, `--weird` controla qué tan **rara/abstracta** es cada imagen respecto al
> estándar visual esperado.

## Rango de valores

Es un valor numérico entre **0 y 3000**.

| Rango                  | Comportamiento                                               |
| ---------------------- | ------------------------------------------------------------ |
| **0 – 300** (bajo)     | Resultado algo fuera de lo común, pero aún reconocible       |
| **500 – 1000** (medio) | Interpretaciones más creativas y visuales, no convencionales |
| **1000 – 3000** (alto) | Resultados muy extraños, abstractos o conceptuales           |

## Ejemplo comparativo

Prompt base: `una mariposa sobre un campo de flores, luz cálida de atardecer --ar 3:2`

| Comando    | Resultado                                                                                                                                                                                                                  |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--w 250`  | Composición fiel al prompt, con ligero aire artístico: patrones inusuales en las alas, posible combinación de especies o una flor fuera de escala. Ideal si se quiere un ligero toque artístico sin volverse muy abstracto |
| `--w 1500` | La mariposa puede parecer una criatura híbrida, colores imposibles, flores fusionadas con estructuras mecánicas o elementos de otro mundo                                                                                  |
| `--w 3000` | Imagen completamente surrealista: iluminación y composición muy alejadas del prompt original                                                                                                                               |

## Cuándo usar cada rango

- **Ideas originales para arte conceptual e ilustración** → `--w` entre 500 y 1000.
- **Ideas visuales totalmente abstractas / surrealismo** → `--w` mayor a 2000.
- **Romper la estética convencional sin cambiar el prompt** → `--w` muy alto, cercano a 3000.

## Combinar `--weird` con `--stylize`

Se puede combinar con `--s` para reforzar el efecto, por ejemplo `--w 1000 --s 750`.

## Ejercicio propuesto

Con el prompt `diseño conceptual de criatura marina del futuro --ar 1:1`, generar variaciones probando
`--w 1000`, `--w 2000` y `--w 3000`, y comparar las diferencias.

## Comando `Run`

Además de **Use** (que copia el prompt y sus parámetros al campo de generación), existe la opción
**Run**, disponible al pasar el cursor sobre una imagen ya generada. Regenera nuevamente 4 imágenes
nuevas basadas en ese mismo prompt tal como está, sin necesidad de reescribirlo ni pasarlo al campo de
edición.

## Conclusión

`--weird` es una herramienta poderosa para artistas, diseñadores e instructores que quieren salir de
lo predecible y explorar el lado más creativo y experimental de Midjourney. Es especialmente útil
cuando los resultados empiezan a verse "muy normales" o en prompts repetidos, para obtener resultados
frescos sin cambiar todo el texto.
