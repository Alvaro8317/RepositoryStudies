# Introducción a CSS

CSS permite darle la apariencia a la página HTML, CSS cuenta con una anatomia donde:

```css
/* 
p -> Selector de CSS 
{} -> Llaves de CSS que contienen los estilos que se le aplicarán al selector
color: blue -> Propiedad y valor, juntos con una declaración
Las propiedades que tienen de tamaños, tienen UNIDADES DE MEDIDA
*/
p {
  /*  */
  color: blue;
  font-size: 20px;
}
```

## Unidades de medida

Algunas propiedades que aceptan unidades de medida son como padding, margin, width, height, etc. Existen uniades fijas como pixeles o centímetros, y relativas que toman su valor dependiendo del valor definido por otra propiedad.

## Aplicando los estilos

Se pueden aplicar los estilos en la etiqueta style, inline o en un archivo css lo cuál es la mejor práctica ya que aquí se pueden aplicar los estilos para diferentes archivos.

## Colores en CSS

Se pueden definir en base al nombre, en base al valor hexadecimal, RGB y HSL. En cuando al valor, existen una serie de colores y nombres que CSS soporta como black, blue, etc. Aunque no se recomiendan. Se puede añadir transparencia con RGBA y HSLA y recientemente es posible hacerlo por medio de RGB y HSL. Todas las opciones anteiores tienen mucho soporte en todos los navegadores.

## Span

Es la etiqueta ideal para modificar elementos via CSS como Tienda **Muebles** donde Muebles puede ir dentro de un span

## Especificidad

Con la especificidad se puede saber que valores serán tomados en cuenta por el navegador, CSS se escribe en cascada, si buen un selector que aparece después de otro tiene más peso y es tomado en cuenta, hay otras consideraciones como el nivel de especificididad.
Utilizar clases y IDS dan especificidad más alta, se recomienda evitar crear selectores muy complicados para evitar un dificil mantenimiento.

### Classes y IDs

Estos son conceptos relevantes para la especificidad, ambos se definen en el HTML. El class tiene como característica que soporta 1 o más, es decir, se pueden reutilizar. Los IDs solo se pueden asignar uno por elemento HTML y máximo uno por documento. Una etiqueta no debería de tener dos ids, pero si podría tener dos clases. Para el nombramiento de las clases o ids se recomienda usar - para separar varias palabras, ejemplo: nav-principal

## Aplicando estilos en CSS

Se pueden aplicar estilos en base a **modulos, BEM o SMACSS**

### Modulos

Se le aplica el nombre a una clase y desde la clase, se acceden a los elementos que hay dentro. Esto ayuda a mantener el estilo encapsulado dentro del módulo específico, lo que evita conflictos con otros estilos en la página. Ejemplo:

```css
.myClass {
  background-color: #000;
}
.myClass a {
  color: blue;
}
```

### BEM (Block, Element, Modifier)

BEM es una metodología de nombrado que facilita la lectura y el mantenimiento del código CSS. Se basa en la idea de dividir la interfaz en bloques independientes. Un bloque puede tener elementos y modificadores.

- **Bloque**: Representa un componente independiente.
- **Elemento**: Representa una parte del bloque que cumple una función.
- **Modificador**: Representa una variación del bloque o del elemento.

```html
<button class="button button--primary">
  <span class="button__icon">🔍</span>
  Search
</button>
```

```css
/* Bloque */
.button {
  background-color: #000;
  color: #fff;
}

/* Elemento */
.button__icon {
  margin-right: 8px;
}

/* Modificador */
.button--primary {
  background-color: blue;
}
```

### SMACSS (Scalable and Modular Architecture for CSS)

SMACSS es una metodología que propone una forma de organizar el CSS en categorías para hacer el código más modular y escalable. Las categorías incluyen:

Base: Estilos predeterminados para elementos HTML.
Layout: Estilos para la estructura de la página.
Module: Estilos para componentes reutilizables.
State: Estilos para representar diferentes estados de los elementos.
Theme: Estilos temáticos o de apariencia.

```html
<div class="l-header">Header</div>
<div class="m-card">Card content</div>
<div class="m-card is-hidden">Hidden Card content</div>
<div class="t-dark">
  <div class="m-card">Dark themed card content</div>
</div>
```

```css
/* Base */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

/* Layout */
.l-header {
  background-color: #333;
  color: #fff;
  padding: 20px;
}

/* Module */
.m-card {
  background-color: #fff;
  border: 1px solid #ddd;
  padding: 20px;
  margin: 20px;
}

/* State */
.is-hidden {
  display: none;
}

/* Theme */
.t-dark .m-card {
  background-color: #333;
  color: #fff;
}
```

## Box Model CSS

En CSS todo es una caja, pero como sea esa caja y qué medidas tenga depende de 4 cosas:

1. Contenido
2. Padding
3. Borde
4. Margin

Para aplicar el box model correctamente, se debe de tener en cuenta la propiedad de box-sizing, porque por defecto, esta es content-box, es decir, si se tiene un width de 200 px y un padding de 25 px se sumarán estos, muchas veces lo que se espera es que la caja no supere el tamaño del width, entonces al dejar box-sizing: border-box, se ajustará el contenido + padding + borde + margin al tamaño de la caja definido por width. Cabe recordar que el padding le añade contenido por defecto a todos los lados, entonces padding 100px añadirá 100 a los 4 lados. Se recomienda que se tenga este snippet a todo CSS para evitar preocupaciones inesperadas:

```css
html {
  box-sizing: border-box;
}

*,
*:before,
*:after {
  box-sizing: inherit;
}
```

## Display en CSS

Todos los elementos en HTML tienen un display por defecto y algunos elementos comparten un display mientras que otros pueden variar, es decir, un div puede tener un display pero una etiqueta adentro puede tener otro display, existen estos display:

- Block -> Significa que un elemento se colocará por debajo del otro sin importar su tamaño o que tanto contenido tiene
- Inline -> Significa que se posicionará a la derecha una vez que haya tomado el espacio que requiere. No permite ajustar width, height, etc.
- inline-block -> Permite darle un width, height, margin a un elemento inline

Cada elemento ya tiene un display por defecto. Otros display son flex y grid pero se verán más adelante.
