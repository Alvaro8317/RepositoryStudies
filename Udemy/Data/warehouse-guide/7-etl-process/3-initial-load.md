# Carga Inicial (Initial Load)

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

La `Initial Load` tiene dos pasos: primero extraer todos los datos iniciales desde el sistema fuente
hacia `Staging`, y después cargar esos datos (ya transformados) desde `Staging` hacia `Core`.

## Paso 1: extracción desde el sistema fuente

Este primer paso —extraer **todos** los datos iniciales del sistema de origen— suele producirse tras
varias conversaciones con dos grupos:

- **Usuarios de negocio**: quienes usan y elaboran los reportes, y saben qué datos necesitan.
- **Responsables de IT**: quienes administran los sistemas fuente / bases de datos, y conocen el
  detalle técnico y la estructura de esos datos.

Con ambos grupos se discute qué datos se pueden extraer, cómo están estructurados, y qué datos
necesitan realmente los usuarios de negocio.

### Elegir el momento adecuado

Una vez decidido qué datos se necesitan, también hay que acordar **cuándo** ejecutar la carga
inicial.

> ⚠️ La carga inicial, al traer todos los datos de una sola vez, es la que más tiempo toma y la que
> supone mayor carga para los sistemas fuente.

Por tratarse de sistemas productivos, este momento debe acordarse con los responsables del sistema
fuente para no ralentizarlos innecesariamente. Normalmente se elige un momento en el que el negocio no
está operando (de noche), o si la carga toma más tiempo, incluso un fin de semana (domingo).

Antes de la carga real conviene hacer **extracciones de prueba más pequeñas**, para estimar cuánto
tiempo tomará la carga completa (por ejemplo, poder decir "probablemente tome tres horas") y así
poder acordar con los responsables una buena ventana de tiempo durante la semana.

Esta es la etapa más crítica de la extracción de datos del sistema fuente.

## Paso 2: carga inicial a la capa Core

Una vez que los datos están en `Staging`, también hay una carga inicial hacia la capa `Core`, donde
se aplican todas las transformaciones. Este paso ocurre **después** de haber diseñado, planificado y
probado todos los pasos de transformación en la herramienta `ETL`. En este segundo paso, básicamente
se copian todos los datos de `Staging` a `Core` (ya transformados).

## Próximas clases

Entender cómo funciona el segundo tipo de carga: la `Delta Load`, donde solo se cargan los datos
nuevos desde la última ejecución.
