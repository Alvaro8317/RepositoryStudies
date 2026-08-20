# Redshift: redimensionamiento de clusters

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Node slices

Antes de hablar del redimensionamiento, hay que entender cómo se compone un **nodo de
computación**: siempre se divide en varias **"rebanadas" (node slices)**.

- Cada **slice** tiene asignada una parte de la **memoria** y del **espacio en disco** del nodo.
- El **nodo líder** gestiona la **distribución de los datos** y la **asignación de la carga de
  trabajo** entre esas slices.
- Esto permite que el trabajo se procese **en paralelo**: las consultas se ejecutan de forma
  paralela y eficiente entre las slices del nodo.

## Redimensionamiento: cuándo y por qué

A veces es necesario **escalar el cluster**, ya sea:

- Aumentando (o reduciendo) el **número de nodos**.
- Cambiando el **tipo de nodo**.

Para ello existen dos métodos: **elastic resize** y **classic resize**.

## Elastic resize

- Es el método **recomendado** — debe usarse siempre que sea posible.
- **Redistribuye las slices de datos** entre los nodos.
- Permite ajustar **dinámicamente** el número de nodos de computación **sin interrupción**: no
  requiere reiniciar el cluster.
- Es **rápido**: tarda de media unos **10 minutos**, mucho más rápido que el classic resize.
- Durante la operación, algunas **consultas en ejecución pueden completarse con éxito**, pero
  **otras pueden eliminarse (drop)** como parte de la operación.
- También permite **cambiar el tipo de nodo** (ej. de `dc2.large` a `dc2.8xlarge`):
  - En ese caso se crea una **snapshot**.
  - Los datos se **redistribuyen** desde el cluster de origen a un nuevo cluster **aprovisionado
    con el nuevo tipo de nodo**.
  - Las **consultas en ejecución se eliminan (drop)** al finalizar, mientras el redimensionamiento
    se completa rápidamente.
- Tiene **limitaciones**: no se puede añadir una cantidad ilimitada de nodos adicionales, ni todos
  los tipos/cantidades de nodo son compatibles con elastic resize.

## Classic resize

- Se usa cuando **elastic resize no es posible** por sus limitaciones (ej. el número de nodos o el
  tipo de nodo destino no son compatibles con elastic resize — por ejemplo, cambiar el recuento de
  nodos a un número muy alto).
- **Tarda más tiempo** que elastic resize.

## Resumen: elastic vs. classic resize

| Característica | Elastic resize | Classic resize |
| -------------------------- | --------------------------------------------------- | ----------------------------------------------------- |
| **Método recomendado** | Sí | Solo cuando elastic resize no es posible |
| **Duración** | Rápido (~10 minutos de media) | Más lento |
| **Interrupción** | Sin interrupción, dinámico | Requiere más tiempo/complejidad |
| **Limitaciones** | Sí — número/tipo de nodo limitado | Sin esas limitaciones |
| **Cambio de tipo de nodo** | Soportado (vía snapshot + redistribución de datos) | Soportado |
