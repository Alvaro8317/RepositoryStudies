# Modos Standard vs. RAW

> Curso: Midjourney (Udemy)

## Qué son

Midjourney versión 7 permite elegir entre dos **modos de interpretación** del prompt. Ambos modos
funcionan con la misma base del modelo (v7), pero producen resultados visualmente distintos.

| Modo | Comportamiento |
|---|---|
| **Standard** (por defecto) | Añade un toque estilizado: composición estética, efectos visuales, belleza implícita |
| **RAW** | Interpreta el prompt de forma más literal y precisa, sin forzar una estética prediseñada — reacciona exactamente a lo escrito. Ideal para control técnico |

## Formas de activarlo

1. **Desde el menú de Settings de la web** (ver [[6-web-settings-menu]]): selector **Model** con las
   opciones Standard / Raw. La configuración elegida se mantiene entre generaciones hasta cambiarla o
   resetearla.
2. **Con el comando `--style`** (no confundir con `--stylize` / `--s`, que es un parámetro distinto):

```text
--style raw
--style standard
```

Si no se especifica `--style`, el valor por defecto es `standard`.

## Ejemplo comparativo

Prompt base: `una bicicleta roja en la calle, bajo la lluvia --ar 16:9`

| Modo | Resultado |
|---|---|
| **Standard** | Composición estilizada, con reflejos, luces suaves, estética de fotografía artística. Colores más sobresaturados. Pueden aparecer elementos decorativos como charcos reflectantes o iluminación de neón |
| **RAW** | Imagen más sencilla, directa y fiel a la escena: fondo más realista y menos embellecido, mejor interpretación literal del color, el clima y el objeto principal (en este caso, la bicicleta) |

> ⚠️ Cada generación produce imágenes distintas aunque se use exactamente el mismo prompt — los
> modelos de IA no repiten el mismo resultado. La comparación entre Standard y RAW debe hacerse
> generando el mismo prompt en ambos modos y observando la tendencia general, no una imagen puntual.

## Cuándo usar cada modo

- **Standard** → cuando se busca impacto visual inmediato: arte conceptual, portadas, posters,
  imágenes emocionales o estilizadas.
- **RAW** → cuando se necesita precisión y control detallado: diseño de producto, ilustraciones
  técnicas, interpretaciones fieles de prompts complejos, arquitectura, diagramas o contenido
  educativo.

## Ejercicio propuesto

Con el prompt `una sala de estar moderna, con sofá gris, pared blanca y una planta de interior junto a
las ventanas --ar 4:3`, generar la imagen una vez en modo **Standard** y otra en modo **RAW**
(reutilizando el mismo prompt) y comparar: cuál tiene más detalles realistas, cuál es más estética,
cuál se parece más a lo escrito.

## Conclusión

La elección entre Standard y RAW depende del objetivo visual y del nivel de control necesario: arte
bello y estilizado → Standard; precisión, realismo y fidelidad → RAW. La mejor forma de dominar ambos
es probar el mismo prompt en los dos modos y comparar los resultados.
