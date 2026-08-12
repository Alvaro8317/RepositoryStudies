# DynamoDB Accelerator (DAX)

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

**DAX** es un servicio de **caché en memoria** para tablas de DynamoDB, diseñado para aumentar el
rendimiento reduciendo la latencia de lectura — hasta niveles de **milisegundos de un solo dígito**.
En comparación con leer directamente de DynamoDB, DAX puede mejorar el rendimiento de lectura hasta
**10 veces**.

## Funcionamiento

- DAX requiere crear y configurar un **clúster DAX**: un conjunto de nodos, donde uno actúa como
  **nodo primario**. Se pueden añadir nodos adicionales para escalar el clúster y mejorar la
  capacidad de caché.
- Las aplicaciones **no se comunican directamente con la tabla**, sino con un **endpoint asociado al
  clúster DAX**. Esto es lo que permite que las lecturas sean más rápidas: los datos se recuperan de
  la caché en memoria en lugar de la tabla.

> ⚠️ Si el volumen de solicitudes supera la capacidad de procesamiento del clúster, DAX aplica
> **throttling**: rechaza temporalmente las solicitudes adicionales y devuelve una excepción de
> estrangulamiento al cliente. Conviene implementar lógica de reintento para manejar estos casos.

## Operaciones de lectura

Cuando una aplicación solicita datos, DAX consulta primero su propia caché:

- **Cache hit** — el elemento está en la caché: DAX devuelve los datos inmediatamente a la aplicación.
- **Cache miss** — el elemento no está en la caché: DAX obtiene los datos directamente de la tabla de
  DynamoDB, los devuelve a la aplicación y **actualiza la caché** para futuras lecturas.

De esta forma, se espera que los datos accedidos con frecuencia terminen disponibles en la caché.

APIs de lectura soportadas por DAX: **GetItem**, **BatchGetItem**, **Query** y **Scan**.

## Operaciones de escritura

Las escrituras (**PutItem**, **UpdateItem**, **DeleteItem**, etc.) se realizan directamente sobre la
tabla de DynamoDB. Los cambios se reflejan después en el clúster DAX, para mantener la caché
**coherente** con los datos de la tabla.

## Cuándo usarlo

DAX es útil para aplicaciones que requieren **alto rendimiento y baja latencia** en operaciones de
lectura sobre DynamoDB, cacheando los datos a los que se accede con frecuencia para minimizar los
tiempos de respuesta.
