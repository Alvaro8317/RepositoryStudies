# Práctica: Glue Data Quality

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Contexto

**Glue Data Quality** es una función de AWS Glue que ayuda a mejorar la **integridad y fiabilidad** de
los datos dentro de un ETL Job. Permite:

- Definir un conjunto de **reglas de calidad** personalizadas y específicas para el propio dataset.
- Usar **algoritmos de Machine Learning** para identificar patrones inusuales en los datos (enfoque de
  **detección de anomalías**), como alternativa al enfoque tradicional basado en reglas — útil para
  detectar errores que se hayan pasado por alto al definir las reglas manualmente.

Se puede aplicar tanto a **datos en reposo** (ej. un archivo en un bucket S3) como a **datos en
tránsito** dentro de un pipeline ETL.

## Añadir el nodo de Data Quality

Se parte del ETL Job sencillo creado anteriormente (fuente S3 → destino S3):

1. Añadir un nuevo nodo y buscar **Data Quality**: aparece la opción **Evaluate Data Quality**
   ("evaluar la calidad e integridad de los datos"). Se selecciona.
2. Conectar la **fuente de datos** a este nuevo nodo (puede desconectarse temporalmente del nodo
   destino para configurarlo antes de reconectarlo).
3. Al añadirlo, aparece un aviso de que no hay reglas configuradas todavía.

## Editor de reglas

Existen dos enfoques disponibles:

- **Rule editor** (editor de conjunto de reglas): enfoque tradicional, donde se definen condiciones
  explícitas.
- **Anomaly detection**: escanea automáticamente los datos y genera observaciones sobre patrones
  inusuales, sin necesidad de definir reglas manualmente.

En esta práctica se usa el **Rule editor**.

### Ejemplo: regla sobre número de columnas

- Se puede definir, por ejemplo: `ColumnCount > 10`.
- El editor ofrece un **asistente de reglas** (helper) para construir la condición sin escribirla a
  mano, junto con una **vista previa** que muestra si la regla pasaría o fallaría contra los datos
  reales.
- En la vista previa se observa que el dataset tiene realmente **7 columnas**, por lo que la regla
  `ColumnCount > 10` falla.
- Se corrige la regla a `ColumnCount == 7`, que sí es coherente con la fuente de datos, y al recargar
  la vista previa la regla **pasa**.

### Ejemplo: regla sobre tipo de dato de una columna

- Se añade una segunda regla para comprobar el **tipo de dato** de una columna.
- Las reglas también admiten condiciones más **dinámicas** (por ejemplo, comparar contra la media de
  los últimos N valores), no solo valores fijos como en los ejemplos anteriores. También es posible
  escribir las condiciones directamente como código, o comprobar la existencia de columnas.
- Al probar con una columna que **no existe** en el dataset (ej. `column1`), la regla falla.
- Al probar con una columna real (ej. `name`) pero comprobando que su tipo sea **fecha** (cuando en
  realidad no lo es), la regla también falla: la vista previa muestra que **0% de las filas** superan
  el umbral esperado.

> ⚠️ El editor de reglas permite combinar reglas simples (recuento de columnas, tipos de dato) con
> reglas dinámicas y con código propio, dando bastante flexibilidad para adaptar las comprobaciones al
> dataset real.

## Opciones de salida (output)

Tras definir las reglas, el nodo de Data Quality ofrece varias opciones sobre qué hacer con el
resultado:

- **Original data output**: además del resultado de calidad, también se puede emitir el dato original
  sin modificar.
- **Data quality results output**: emitir los resultados de la evaluación de calidad como salida propia
  — por ejemplo, cargándolos en otro bucket S3 distinto del destino de los datos, para poder analizarlos
  por separado.

## Acción ante un fallo de las reglas

En el nodo **fuente** (o principal) del job se puede configurar qué ocurre si el conjunto de reglas
**falla**:

- **Fail job without loading target data**: si alguna regla falla, el job se detiene y **no** carga los
  datos en el destino.
  - Esto ahorra capacidad de cómputo al no continuar con una carga que no cumple los estándares de
    calidad esperados.
  - Este comportamiento se puede integrar más adelante en un **Workflow** de Glue, de forma que el fallo
    del job dispare otra acción (por ejemplo, una notificación o un proceso de corrección).

## Conclusión

Glue Data Quality permite garantizar, dentro del propio ETL Job, que los datos cumplen unas condiciones
mínimas antes de cargarse en el destino, combinando reglas explícitas (rule editor) con detección de
anomalías basada en ML, y decidiendo de forma flexible qué hacer con los resultados y con los fallos.
