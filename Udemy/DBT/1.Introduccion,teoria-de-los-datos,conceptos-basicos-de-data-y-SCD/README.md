# The Complete dbt (Data Build Tool) Bootcamp: Zero to Hero - Introducción

## Jerarquía de necesidades aplicada a datos

La **Pirámide de Maslow**, que organiza las necesidades humanas desde las más básicas (fisiológicas) hasta las más avanzadas (autorrealización), puede ser reinterpretada en el contexto de **datos y analítica**.

### Pirámide de necesidades en datos

1. **Recolección de datos**: La base de todo sistema de análisis. Sin datos recopilados de fuentes confiables (sensores, cámaras, aplicaciones, bases de datos, etc.), no es posible construir sistemas de análisis o inteligencia.
2. **Disputa y limpieza de datos**: El siguiente nivel se centra en resolver inconsistencias, errores y garantizar la calidad de los datos. Sin esta etapa, los datos no serían útiles para análisis confiables.
3. **Integración de datos**: Aquí los datos se combinan y preparan para su análisis, asegurando que provengan de diferentes fuentes y formatos, pero estén alineados con un modelo único.
4. **BI y analítica**: Representa la generación de reportes, dashboards y análisis descriptivos basados en datos transformados y preparados.
5. **Inteligencia Artificial y Machine Learning**: La cima de la pirámide, donde los datos se usan para construir sistemas predictivos y automatizar decisiones.

**Nota clave**: Si una capa de la pirámide falla (por ejemplo, datos mal recolectados o sucios), las capas superiores no podrán funcionar correctamente. Esto hace fundamental construir una base sólida.

---

## Modelo de madurez de datos

El **modelo de madurez de datos** sigue un flujo lógico desde la recopilación hasta la acción basada en los datos:

1. **Recolección de datos**:

   - Implica la extracción de datos desde múltiples fuentes como cámaras, sensores, logs de aplicaciones, APIs, entre otros.
   - Aquí entra en juego el concepto de los **3 Vs del Big Data**:
     - **Variedad**: Diversidad en los formatos y tipos de datos (estructurados, no estructurados, semiestructurados).
     - **Velocidad**: Ritmo al que los datos se generan y necesitan ser procesados.
     - **Volumen**: Cantidad masiva de datos generados.
   - Diseñar arquitecturas que consideren estos factores es esencial para garantizar sistemas escalables y confiables.

2. **Zona Staging**:

   - En esta etapa, los datos pasan de su formato crudo u operativo a uno más estructurado y organizado para su análisis.
   - **Enfoque en calidad**:
     - Filtrar valores duplicados, errores, datos faltantes.
     - Validar formatos y asegurarse de que los datos sean consistentes.

3. **Integración de datos**:
   - Transformar y consolidar los datos para análisis y modelos.
   - Se pueden cargar los datos de dos maneras:
     - **Refresh completo**: Reescribir completamente los datos (sobrescribir).
     - **Actualización incremental**: Sólo se aplican los cambios recientes, conservando datos históricos.

---

## ETL vs ELT

### **ETL (Extract, Transform, Load)**

- Modelo clásico donde los datos se transforman antes de cargarlos en el sistema de almacenamiento.
- Diseñado para sistemas donde el almacenamiento y la computación eran caros, obligando a ser selectivo en las transformaciones.
- Adecuado para entornos on-premise y sistemas tradicionales de bases de datos.

### **ELT (Extract, Load, Transform)**

- Modelo moderno donde los datos se cargan primero en su forma **raw** (sin procesar) en un sistema de almacenamiento y luego se transforman dentro de ese mismo sistema.
- Ventajas:
  - Aprovecha la capacidad y escalabilidad de los almacenes de datos modernos en la nube (por ejemplo, Snowflake, BigQuery, Redshift).
  - Permite mantener múltiples capas de datos:
    - **Raw data**: Datos originales sin procesar.
    - **Transform data**: Datos limpios y preparados para análisis.
  - Es más eficiente en costo gracias a los precios más accesibles de almacenamiento en la nube.

### Ejemplo visual de ETL vs ELT

```plaintext
ETL:
1. Extraer → Transformar (fuera del almacén) → Cargar (en el almacén)

ELT:
1. Extraer → Cargar (en el almacén) → Transformar (dentro del almacén)
```

---

### ¿Por qué es importante dbt en este modelo?

dbt (Data Build Tool) es una herramienta clave para la implementación de **ELT**, ya que:

- Permite transformar datos directamente en los almacenes de datos (por ejemplo, Redshift, Snowflake, BigQuery).
- Usa SQL como lenguaje principal, lo que lo hace accesible para muchos equipos.
- Integra procesos como versionado de modelos, pruebas de datos y documentación automatizada.

**Beneficios de usar dbt**:

- Simplifica el flujo de trabajo ELT.
- Automatiza las transformaciones repetitivas.
- Mejora la trazabilidad de los cambios en los datos.

## Data Warehouses, Data Lakes y Lakehouses

## **Data Warehouse (DW)**

Los **Data Warehouses (DW)** existen desde los años 60 y su principal objetivo es servir como tecnología para el análisis de datos y la generación de informes.

### Características principales

- **Estructura y optimización**:
  - Diseñado para análisis de alto rendimiento sobre datos estructurados.
  - Permite crear dimensiones e integraciones que ayudan a responder preguntas de negocio complejas.
- **SQL como lenguaje central**:
  - Los Data Warehouses suelen funcionar mediante SQL, ofreciendo consultas rápidas y eficientes.
- **Almacenamiento y limpieza de datos**:
  - Es fundamental mantener los datos estructurados y limpios para evitar retrasos en el análisis.

### Evolución tecnológica

- **On-premise (local)**:

  - Proveedores como IBM y Oracle lideraban el mercado, con sistemas controlados internamente (hardware, software).
  - Ventajas:
    - Control completo del ecosistema (CPU, memoria, almacenamiento).
  - Desventajas:
    - Altos costos operativos (licencias, mantenimiento, electricidad).
    - Escalabilidad limitada (requiere compra de nuevos servidores y licencias).

- **Cloud-based**:
  - Proveedores como AWS (Redshift), Snowflake y Google BigQuery han revolucionado los DW con soluciones en la nube.
  - Ventajas:
    - Escalabilidad elástica: agregar o eliminar nodos según la demanda.
    - Reducción de costos en infraestructura y personal.

---

## **Tablas externas y Cloud Data Warehouses**

Un problema recurrente en los Data Warehouses, ya sean locales o en la nube, es el **costo fijo de los nodos de cómputo**, independientemente de si están en uso.

### Solución: Tablas externas

- Permiten desacoplar la **capa de cómputo** de la **capa de almacenamiento**.
- Ejemplo:
  - Utilizar **Amazon S3**, Hadoop, o Azure Blob Storage para almacenar datos sin necesidad de mantener recursos computacionales activos constantemente.
- Beneficios:
  - Reducción de costos: paga solo por el almacenamiento y cómputo según su uso.
  - Escalabilidad independiente para almacenamiento y procesamiento.

---

## **Data Lake**

Un **Data Lake** es un sistema de almacenamiento que permite guardar datos en cualquier formato: estructurado, semiestructurado y no estructurado.

### Características principales de data lake

- **Flexibilidad de formatos**:
  - Acepta datos en crudo, imágenes, videos, archivos de texto, etc.
- **Económico y escalable**:
  - Servicios como **Amazon S3** o **Hadoop** son ejemplos de Data Lakes ideales para almacenar grandes volúmenes de datos a bajo costo.
- **Sin cómputo integrado**:
  - Almacenan los datos de forma pasiva; el procesamiento ocurre en otras herramientas (como Databricks o Spark).

### Limitaciones

- Los Data Lakes no están optimizados para consultas estructuradas ni para trabajar con datos transaccionales.

---

## **Lakehouse**

El concepto de **Lakehouse** surge para combinar lo mejor de los Data Lakes y los Data Warehouses.

### Ventajas principales

1. **SQL para datos estructurados y no estructurados**:
   - Los Lakehouses permiten realizar consultas SQL sobre datos que tradicionalmente no serían soportados en un DW.
2. **Modelo ACID**:
   - Ofrecen soporte para transacciones, garantizando integridad en operaciones con datos estructurados y no estructurados.
3. **Unificación de datos**:
   - Almacenan y procesan datos de diferentes tipos en un único sistema (estructurados, no estructurados, semiestructurados).
4. **Integración nativa con herramientas modernas**:
   - Proveedores como **Databricks** y **Snowflake** implementan el modelo Lakehouse por defecto, con soporte para almacenamiento en la nube (por ejemplo, S3).

---

### Comparación rápida

| **Característica**       | **Data Warehouse**                    | **Data Lake**                    | **Lakehouse**                        |
| ------------------------ | ------------------------------------- | -------------------------------- | ------------------------------------ |
| **Tipos de datos**       | Estructurados                         | Estructurados y no estructurados | Estructurados y no estructurados     |
| **Optimización**         | Consultas SQL rápidas                 | Almacenamiento masivo y flexible | Consultas SQL rápidas + Flexibilidad |
| **Transacciones (ACID)** | Sí                                    | No                               | Sí                                   |
| **Escalabilidad**        | Limitada (on-premise) / Media (cloud) | Alta                             | Alta                                 |
| **Costo**                | Elevado en sistemas tradicionales     | Bajo                             | Intermedio                           |

## El Stack de Datos Moderno

El stack de datos moderno ha evolucionado significativamente gracias a la reducción de costos en almacenamiento, computación y transmisión de datos. Este cambio ha permitido la creación de herramientas como **DBT** y nuevas arquitecturas escalables que transforman cómo gestionamos y procesamos la información.

---

### **Evolución del Stack de Datos**

#### **1. El inicio: SMP Data Warehouses (Shared Memory Processing)**

En los primeros sistemas, los **SMP Data Warehouses** funcionaban en un único servidor que compartía recursos como CPU, memoria y almacenamiento.

##### **Ventajas:**

- Todo ocurre dentro de una sola máquina, lo que reduce latencia y tiempos de procesamiento.

##### **Desventajas:**

- **Escalabilidad limitada:** Solo soportan escalamiento vertical (ampliar recursos en una sola máquina).
- **Dependencia del hardware:** El almacenamiento y cómputo estaban acoplados, lo que exigía mantener constantes respaldos para evitar pérdidas.
- **Sin balanceo de carga:** No existían tecnologías para repartir tareas entre diferentes máquinas (no había escalabilidad horizontal).

#### **2. MPP Cloud Data Warehouses (Massively Parallel Processing)**

Con la llegada de **BigQuery, Snowflake, Redshift** y **Synapse Analytics**, los Data Warehouses adoptaron una arquitectura **MPP**.

##### **Características clave:**

- **Nodos distribuidos:**
  - Existe un nodo maestro que orquesta las tareas y múltiples nodos de cómputo independientes, cada uno con su propio sistema operativo.
- **Escalabilidad horizontal:**
  - Agregar o quitar nodos según las necesidades de cómputo, lo que permite manejar flujos de trabajo más grandes.
- **Desacoplamiento de almacenamiento y cómputo:**
  - El almacenamiento puede ser compartido entre nodos o externo (por ejemplo, en Amazon S3).

##### **Ventajas sobre SMP:**

- Escalabilidad horizontal casi ilimitada.
- Reducción de costos al usar recursos de cómputo solo cuando se necesitan.

---

### **Bases de Datos Columnares: Un cambio fundamental**

Anteriormente, las bases de datos estaban **orientadas a filas**, optimizadas para operaciones transaccionales (OLTP). Sin embargo, con el crecimiento de los análisis de datos (OLAP), surgieron las bases **orientadas a columnas**.

#### **Beneficios de las bases columnares:**

1. **Menor uso de I/O (entrada/salida):**
   - Solo se leen las columnas necesarias para una consulta, no toda la fila.
2. **Compresión eficiente:**
   - Las columnas de un mismo tipo de dato pueden comprimirse mejor que filas con datos variados.
3. **Mejor rendimiento para análisis:**
   - Ideales para agregaciones, cálculos y consultas de grandes volúmenes de datos.

#### **Ejemplos de bases columnares:**

- Amazon Redshift
- Google BigQuery
- Apache Parquet y ORC

---

### **Desacoplamiento del Cómputo y Almacenamiento**

Uno de los avances más importantes del stack moderno fue separar el cómputo del almacenamiento.

#### **Ventajas del desacoplamiento:**

- **Flexibilidad:**
  - Escalar únicamente el cómputo o el almacenamiento según sea necesario.
- **Optimización de costos:**
  - Usar cómputo solo para cargas de trabajo específicas (pago por uso).

Por ejemplo, **Amazon S3** puede almacenar grandes volúmenes de datos sin necesidad de mantener nodos de cómputo activos todo el tiempo.

---

### **El Stack Moderno de Datos en la Era de la IA**

En la actualidad, el stack de datos es más **horizontal e integrado** que vertical, diseñado para soportar arquitecturas escalables y ágiles, con un flujo claro desde la fuente de datos hasta las herramientas de consumo.

#### **Componentes principales del Stack Moderno:**

1. **Data Sources:**
   - Fuentes de datos: APIs, sensores, bases de datos transaccionales, archivos, LinkedIn, etc.
2. **Extract / Load (EL):**
   - Extraer y cargar datos en bruto desde las fuentes al sistema central.
3. **Transformación (T):**
   - Limpiar, modelar y transformar datos usando herramientas como **DBT**.
4. **Data Warehouse:**
   - Centralizar los datos estructurados en un almacén optimizado (Snowflake, BigQuery, Redshift).
5. **Data Science:**
   - Aplicar análisis avanzados, modelado predictivo e IA.
6. **BI Tools:**
   - Herramientas de análisis y visualización como Tableau, Power BI o Looker.
7. **Reverse ETL:**
   - Llevar datos transformados de vuelta a herramientas operativas (por ejemplo, CRMs como Salesforce).
8. **Destinations:**
   - Lugares donde los datos finales se consumen: dashboards, informes, aplicaciones, etc.

---

### **Impacto del Stack Moderno**

El stack moderno ha permitido:

- Democratizar el acceso a datos y análisis mediante herramientas fáciles de usar.
- Escalar sistemas de datos para soportar cargas masivas de trabajo, especialmente en la era de la inteligencia artificial.
- Reducir costos de almacenamiento y cómputo, mientras se aumenta la flexibilidad operativa.

## Slowly changing dimensions

Las **Slowly Changing Dimensions (SCD)** son una técnica utilizada en el modelado de datos dentro de un **Data Warehouse** para manejar cómo se almacenan y gestionan los cambios en los datos dimensionales a lo largo del tiempo. Estos datos dimensionales suelen describir atributos de las entidades de un negocio, como clientes, productos, o ubicaciones, y aunque generalmente no cambian con frecuencia, sí pueden actualizarse ocasionalmente.

---

### **Ejemplo típico**

Un cliente puede cambiar de dirección, o un producto puede tener un nuevo nombre. La pregunta es: ¿cómo se gestionan estos cambios en el Data Warehouse para preservar la integridad histórica y permitir análisis tanto históricos como actuales?

---

### **Tipos de Slowly Changing Dimensions**

Existen varios métodos para manejar estos cambios, conocidos como **tipos de SCD**. Los más comunes son:

#### **SCD Tipo 0: Sin cambios**

- La dimensión no permite cambios.
- Se usa cuando la información debe permanecer constante, como un identificador único.

#### **SCD Tipo 1: Sobrescribir el valor anterior**

- Se actualiza el registro con el nuevo valor, sin guardar el histórico.
- **Ventaja:** Simplicidad en el diseño y menor uso de almacenamiento.
- **Desventaja:** Se pierde el historial de los cambios.

**Ejemplo:**  
Si la dirección de un cliente cambia de "Calle 1" a "Calle 2", simplemente se actualiza el registro con "Calle 2".

---

#### **SCD Tipo 2: Crear un nuevo registro para cada cambio**

- Se guarda el histórico creando un nuevo registro por cada cambio en el atributo.
- Incluye columnas adicionales, como:
  - Fecha de inicio y fin del registro.
  - Indicador de si el registro está activo.

**Ventaja:**  
Permite rastrear todos los cambios históricos.

**Desventaja:**  
Mayor complejidad y uso de almacenamiento.

**Ejemplo:**

| ID Cliente | Dirección | Fecha Inicio | Fecha Fin  | Activo |
| ---------- | --------- | ------------ | ---------- | ------ |
| 1          | Calle 1   | 01/01/2020   | 31/12/2021 | No     |
| 1          | Calle 2   | 01/01/2022   | NULL       | Sí     |

---

#### **SCD Tipo 3: Añadir columnas para cambios históricos limitados**

- Se añaden columnas adicionales para registrar un número fijo de versiones del atributo.
- **Ventaja:** Menos consumo de almacenamiento comparado con el SCD Tipo 2.
- **Desventaja:** Limitado al número de versiones configuradas (no guarda un historial completo).

**Ejemplo:**

| ID Cliente | Dirección Actual | Dirección Anterior | Fecha Cambio |
| ---------- | ---------------- | ------------------ | ------------ |
| 1          | Calle 2          | Calle 1            | 01/01/2022   |

---

#### **Otros tipos menos comunes**

- **SCD Tipo 4:** Se utiliza una tabla histórica separada para almacenar los cambios, manteniendo la tabla principal más sencilla.
- **SCD Tipo 6:** Es una combinación de los tipos 1, 2 y 3, permitiendo almacenar valores actuales, históricos y cambios recientes en la misma tabla.

---

### **¿Cuándo utilizar cada tipo?**

- **Tipo 1:** Cuando el historial no es relevante o cuando solo interesa el valor actual.
- **Tipo 2:** Para análisis históricos detallados.
- **Tipo 3:** Cuando solo necesitas guardar un cambio reciente o los más relevantes.
- **Tipo 4 y 6:** En escenarios más avanzados que combinan flexibilidad y rendimiento.

---

### **Conclusión**

El manejo de Slowly Changing Dimensions permite que un Data Warehouse sea útil para analizar datos históricos, identificar tendencias y mantener consistencia en los reportes. La elección del tipo de SCD depende de los requisitos de negocio, la importancia del historial y las restricciones de almacenamiento.
