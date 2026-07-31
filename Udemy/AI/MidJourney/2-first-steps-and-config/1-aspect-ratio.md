# Aspect ratio (relación de aspecto)

> Curso: Midjourney (Udemy)

## Qué es el aspect ratio

El **aspect ratio** (relación de aspecto) es la proporción entre el ancho y el alto de una imagen. Se
expresa como una relación en **unidades**, no en píxeles, por ejemplo `3:2` o `16:9`.

> ⚠️ No confundir aspect ratio con **resolución**. La resolución se expresa en píxeles (ej. Full HD =
> 1920 x 1080). El aspect ratio es la proporción entre ancho y alto (ej. `16:9`), independientemente
> de la resolución final de la imagen.

El valor a la izquierda de los dos puntos es la proporción del **ancho** y el valor a la derecha es la
proporción del **alto**. Por ejemplo, en `16:9`, 16 es el ancho y 9 es el alto.

## Comportamiento por defecto

Sin indicar ningún parámetro, Midjourney genera imágenes **cuadradas** (mismo ancho que alto). Para
cambiar esto es necesario usar un comando.

## El comando `--ar`

Los comandos en Midjourney se escriben con doble guion medio (`--`) seguido del nombre del parámetro.
Para cambiar el aspect ratio se usa:

```text
--ar <ancho>:<alto>
```

`ar` es el diminutivo de *aspect ratio*.

### Ejemplos de prompts probados

| Prompt (keywords)                                                              | Comando    | Resultado                                        |
| ------------------------------------------------------------------------------ | ---------- | ------------------------------------------------ |
| robot niño, luces de neón, estilo dibujo animado, colores pastel, fondo blanco | `--ar 4:3` | Imagen más ancha que alta                        |
| retrato fotográfico, mujer elegante, luz natural, fondo borroso                | `--ar 5:3` | Imagen aún más ancha (formato horizontal amplio) |
| (mismo tipo de prompt)                                                         | `--ar 3:5` | Imagen más alta que ancha (vertical)             |

> El prompt en Midjourney funciona mejor como una lista de **keywords separadas por comas**, no como
> un párrafo descriptivo (ej. `robot niño, luces de neón, estilo dibujo animado, colores pastel,
> fondo blanco`).

### Formatos verticales

Un aspect ratio vertical (ej. `--ar 3:5`) es útil para contenido tipo Reels, TikTok, Shorts o Stories,
donde se necesita una imagen más alta que ancha.

> El aspect ratio también se puede ajustar desde la interfaz gráfica (sin escribir el comando), pero
> es importante aprender el comando `--ar` porque se usa constantemente al escribir prompts.

## Idioma del prompt

El prompt se puede escribir tanto en español como en inglés — Midjourney genera la imagen igual en
ambos casos (ej. `Epic dragonfly over castle, cinematic lighting and storm clouds`).
