# Direccionar el estilo visual

> Curso: Midjourney (Udemy)

## Qué es el estilo visual

El **estilo visual** es la forma en que se representa una imagen: puede parecer una pintura, una
fotografía realista, un dibujo infantil, un render de videojuego, etc.

Para controlar este aspecto **no se necesitan comandos especiales** (como `--ar`). Basta con usar las
palabras correctas dentro del prompt, por ejemplo: `realista`, `fotorrealista`, `estilo anime`,
`render 3D`, `acuarela`, `pintura al óleo`.

## Cómo influye el estilo en el resultado

El estilo visual define:

- El tipo de trazos, detalles o texturas de la imagen.
- La atmósfera (más artística, técnica, cómica o realista).
- El público objetivo (ej. ilustraciones infantiles vs. fotografía editorial).

## Estructura recomendada del prompt

```text
sujeto o escena, adjetivos descriptivos, estilo (tipo de arte o medio)
```

> Se recomienda separar las keywords por comas en vez de escribir un párrafo descriptivo — Midjourney
> funciona mejor con palabras clave.

## Ejemplos probados

| Prompt                                                                                                     | Aspect ratio            | Estilo obtenido                                                                            |
| ---------------------------------------------------------------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------ |
| Retrato de astronauta, fondo oscuro con estrellas, estilo pintura al óleo                                  | (cuadrado, por defecto) | Retrato tipo pintura al óleo                                                               |
| Retrato de hombre mayor con barba, fondo gris, luz suave, estilo realista                                  | `--ar 3:4`              | Realista, aunque no siempre resulta 100% fotográfico — a veces se acerca más a una pintura |
| Paisaje urbano al atardecer, luces encendidas, fotografía con cámara Canon EOS 60D, lente de 50mm, ISO 100 | `--ar 16:9`             | Fotorrealista — mencionar cámara, lente e ISO ayuda a forzar el fotorrealismo              |
| Gato astronauta en el espacio, expresión feliz, fondo de estrellas, estilo cartoon colorido                | `--ar 1:1`              | Estilo cartoon                                                                             |
| Niña corriendo bajo la lluvia con paraguas rojo, estilo acuarela, fondo urbano desenfocado                 | `--ar 3:4`              | Acuarela: pinceladas suaves, tonos pastel, bordes diluidos, como ilustración hecha a mano  |

> ⚠️ Un estilo no siempre se logra a la primera. Cuantas más palabras relevantes se agreguen al prompt
> (ej. marca de cámara, lente, ISO para fotorrealismo), más se empuja a Midjourney hacia el resultado
> esperado.

## Otros estilos que se pueden dirigir con keywords

- **Render 3D de videojuego** → añadir `estilo render 3D de videojuego`.
- **Pintura digital** → añadir `estilo pintura digital épica, luz dramática, colores fríos, tipo de cámara`.

## Ejercicio propuesto

Tomar un prompt básico y genérico:

```text
Una taza de café sobre una mesa de madera
```

Generar **tres versiones** del mismo prompt agregando distintos estilos, por ejemplo:

1. `..., fotografía de producto`
2. `..., estilo cartoon kawaii`
3. `..., estilo Studio Ghibli` o `..., pintura al óleo clásica`

Comparar los resultados para comprobar cómo cambia la salida según las palabras de estilo usadas.

## Conclusión

Controlar el estilo visual en Midjourney es clave para conseguir resultados coherentes y
profesionales. La clave está en usar descripciones claras del medio artístico o estilo fotográfico
deseado, y experimentar para ver cómo reacciona el modelo.
