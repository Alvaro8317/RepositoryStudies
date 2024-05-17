# Introducción a HTML

## ¿Qué es HTML?

Todo es HTML en la web, significa HyperText Markup Language, donde la versión actual es la versión 5. Es fácil de aprender siempre que se practique, cuenta con las siguientes etiquetas:

- Etiqueta p
- Etiqueta html
- Etiqueta head -> Se deja la información meta como el lenguaje, título, descripción, enlace a CSS, etc.
- Etiqueta body -> Se deja todo lo visible al usuario

El index.html es el nombre exclusivo, es el punto de entrada a la página web

## Textos en HTML

Existen etiquetas como p para párrafos, h1 hasta el h6 que se usan para títulos. Entre más alto es el número del heading menor es su importancia en el contenido.

De las mejores prácticas es que solo haya un h1 por página. Para que se tenga un buen SEO se debe de tener un buen contenido, que tiene una descripción que cumple con lo que se puede buscar.

## Imagenes en HTML

Las imagenes son importantes para el diseño, se usa < img > que es la más común pero también se puede usar < figure > que soporta múltiples imágenes y también las imágenes se pueden añadir por medio de CSS. Las imagenes se agregan en base a los atributos HTML. Img es una etiqueta que tiene la posibilidad de ser auto cerrable con />

### Ejemplo

```html
<p> Desarrollador fullstack <p>
<img src="imagen.jpg" alt="Texto alternativo para accesabilidad" width=200 height=300/>
<!-- Alternativa -->
<img 
  src="imagen.jpg" 
  alt="Texto alternativo para accesabilidad" 
  width=200 
  height=300/>
```

Para este ejemplo, src se deja la ubicación de la imagen que es relativa, el alt es para cuando no se carga la imagen. El ancho y la altura se recomienda mejor dejar en CSS.

## Enlaces en HTML

Los enlaces se usan para redireccionar al usuario de una página a otra, esto se hace con la etiqueta de < a >, es una combinación entre enlace y parrafo. Cualquier elemento puede ser un enlace, como una imagen, un vídeo, etc.

## Estructurar el HTML

El sitio web debería de tener una estructura valida, esto hará que sea más facil leerlo y que tenga mejor SEO, esta estructuración está compuesta por:
```html
<header> <!-- Parte superior de un sitio web -->
<nav> <!-- Grupo de enlaces o navegación -->
<main> <!-- Contenido principal del HTML, solo 1 por archivo -->
<section> <!-- Se usa cuando el primer hijo es un heading como h1, h2, etc. e introduce una nueva sección -->
<aside> <!-- El contenido que acompaña el contenido principal -->
<div> <!-- Cuando no aplica a ninguno de los anteriores -->
<footer> <!-- Parte inferior de un sitio web -->
```
