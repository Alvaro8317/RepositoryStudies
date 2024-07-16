# UseContext

Es de las secciones más importantes, a pesar que useContext no es necesaria en todas las aplicaciones es muy recomendable hacer uso porque en una aplicación sin un useContext tocaría pasar la información del componente padre luego al hijo y luego al nieto. Estos componentes hacía abajo puede extenderse, el useContext rompe la referencia y comunicación entre los componentes, useContext dejaría todo lo relevante en un espacio centralizado. useContext no se usará siempre, cuando es una comunicación entre padre e hijo, mejor usar una comunicación directa, pero, cuando se pasa la información por múltiples componentes, lo ideal es hacer uso de useContext

## Temas a ver en la sección

- Context
- Provider
- useContext
- React Router
- Links y NavLinks
- CreateContext
- SPA ( Single Page Application )

El objetivo de la sección es principalmente aprender sobre el Context, el Router es un valor agregado que explotaremos mucho más en próximas secciones, pero al usar un Router, podemos explicar claramente el problema y necesidad del context.

## Context

¿Qué es el context?
Cuando se tiene una app compuesta por múltiples componentes, se pueden pasar props de un componente abuelo a un padre (aquí no se haría nada con esos props) y finalmente se pasaría a los componentes hijos, pero esto podría mejorarse con el context. Porque donde se tuviera el caso que hay dos componentes distintos y se requiere tener una comunicación o pasar props, se puede resolver con un context
En el context se puede tener el contexto del usuario, sesión o similares de los que están activos. Un context es un High Order Component

## Rutas con react

Para desplegar rutas con react se puede usar react-router-dom, importando el BrowserRouter, este es un componente de orden superior (HOC), son solamente componentes creados por uno, pero recibe componentes dentro de este mismo, ejemplo, como un div. Esto da una ventaja que todos los hijos puedan acceder a la información del componente padre.

```html
<div>
  <h1>Esto podría ser un componente</h1>
  <h2>Esto podría ser otro componente</h2>
</div>
```

## Link

React-router-dom cuenta con una característica y es que permite usar Links para las SPA, esta es útil porque si se dejara con etiquetas

```html
<a></a>
```

dentro del código de react, se haría una recarga completa de toda la página web, lo que implicaría que se renderizarian todos los componentes y por ende, react dejaría de ser tan potente por ese lado.
NavLink es un link que se usa para la navegación
