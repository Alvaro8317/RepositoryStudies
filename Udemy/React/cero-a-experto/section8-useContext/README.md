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
