# Curso de Amazon DynamoDB

## Tipos de Bases de Datos NoSQL 🗂️

### 1. Bases de datos clave-valor 🔑➡️📦

- **Definición:** Almacenan datos como pares clave-valor. Cada clave es única y se utiliza para recuperar el valor asociado. Este modelo es altamente eficiente para búsquedas rápidas y operaciones de lectura/escritura.

- ✅ **Casos de uso:**

  - **Almacenamiento de sesiones:** Las sesiones de usuarios en aplicaciones web suelen almacenarse como pares clave-valor.
  - **Cache de datos:** Redis es muy utilizado como caché para reducir la carga en bases de datos primarias.
  - **Gestión de configuraciones:** DynamoDB es usado para almacenar configuraciones de aplicaciones distribuidas.

- 🛠️ **Ejemplos:**

  - **Redis:** Permite almacenamiento en memoria para operaciones de baja latencia.
  - **Amazon DynamoDB:** Ofrece un servicio gestionado, escalable y de alta disponibilidad.
  - **Riak:** Una base de datos distribuida que se enfoca en alta disponibilidad.

- ⚖️ **Comparativa:**
  - Redis vs DynamoDB: Redis es más rápido para datos en memoria, mientras que DynamoDB ofrece mayor durabilidad y escalabilidad automática.

---

### 2. Bases de datos documentales 📄

- **Definición:** Almacenan datos como documentos JSON, BSON o XML, estructurados o semi-estructurados. Los documentos pueden ser anidados, lo que facilita la representación de datos complejos.

- ✅ **Casos de uso:**

  - **Catálogos de productos:** MongoDB es ideal para almacenar catálogos de productos en e-commerce.
  - **Gestión de contenido:** Couchbase es utilizado para manejar sistemas de gestión de contenido (CMS).
  - **Sistemas de análisis de logs:** CouchDB permite almacenamiento distribuido para logs estructurados.

- 🛠️ **Ejemplos:**

  - **MongoDB:** Soporta consultas complejas y es altamente escalable.
  - **Couchbase:** Mejora el rendimiento gracias a su arquitectura de memoria distribuida.
  - **Apache CouchDB:** Ofrece sincronización offline y replicación.

- ⚖️ **Comparativa:**
  - MongoDB vs Couchbase: MongoDB es más flexible para desarrolladores, mientras que Couchbase ofrece mejor rendimiento para consultas de lectura intensiva.

---

### 3. Bases de datos de grafos 🔗

- **Definición:** Almacenan datos como nodos y relaciones (aristas), lo que permite modelar estructuras altamente conectadas. Son ideales para consultas complejas que requieren explorar relaciones.

- ✅ **Casos de uso:**

  - **Redes sociales:** Neo4j permite modelar relaciones entre usuarios para recomendaciones.
  - **Detección de fraudes:** Identificación de patrones sospechosos en transacciones bancarias.
  - **Sistemas de recomendación:** Grafos para encontrar similitudes y sugerir contenido relevante.

- 🛠️ **Ejemplos:**

  - **Neo4j:** Líder en bases de datos de grafos, soporta consultas Cypher para analizar relaciones complejas.
  - **OrientDB:** Ofrece soporte para modelos multimodales, combinando grafos y documentos.
  - **ArangoDB:** Combina modelo de grafos, documentos y clave-valor en una única base de datos.

- ⚖️ **Comparativa:**
  - Neo4j vs OrientDB: Neo4j ofrece mejor rendimiento para grafos densos, mientras que OrientDB permite flexibilidad al combinar distintos modelos.

---

### 4. Bases de datos de columnas 📚

- **Definición:** Almacenan datos en formato de columnas en lugar de filas, lo que permite una recuperación más rápida para análisis masivos de datos.

- ✅ **Casos de uso:**

  - **Análisis de datos masivos:** Cassandra es utilizado para análisis de big data y gestión de logs.
  - **Motores de recomendaciones:** Escalabilidad horizontal para volúmenes masivos.
  - **Monitorización de IoT:** HBase es ideal para manejar grandes volúmenes de datos de sensores.

- 🛠️ **Ejemplos:**

  - **Apache Cassandra:** Diseñada para alta disponibilidad y escalabilidad horizontal.
  - **Apache HBase:** Proporciona almacenamiento distribuido en columnas sobre Hadoop.
  - **ScyllaDB:** Alternativa de alto rendimiento compatible con Cassandra.

- ⚖️ **Comparativa:**
  - Cassandra vs HBase: Cassandra es más fácil de escalar, mientras que HBase ofrece mayor consistencia en entornos Hadoop.

---

### 5. Bases de datos de objetos 🎯

- **Definición:** Almacenan datos como objetos complejos, siguiendo un modelo similar a la programación orientada a objetos (POO). Son útiles para persistir estructuras de datos complejas.

- ✅ **Casos de uso:**

  - **Persistencia de objetos en POO:** Almacenar objetos Java o C# directamente en bases de datos.
  - **Modelado de datos complejos:** Ideal para aplicaciones que utilizan modelos de datos ricos.
  - **Aplicaciones científicas:** Utilizadas para gestionar simulaciones o datos estructurados.

- 🛠️ **Ejemplos:**

  - **db4o:** Base de datos de objetos para Java y .NET.
  - **ObjectDB:** Ofrece persistencia orientada a objetos para entornos Java.
  - **Versant:** Utilizada para aplicaciones críticas que requieren modelos complejos.

- ⚖️ **Comparativa:**
  - db4o vs ObjectDB: db4o es más ligero y fácil de usar, mientras que ObjectDB ofrece mejores opciones para aplicaciones Java avanzadas.

---

## 📊 Comparativa Global

| Tipo         | Mejores Casos de Uso            | Ejemplos Populares | Ventajas                         | Desventajas                           |
| ------------ | ------------------------------- | ------------------ | -------------------------------- | ------------------------------------- |
| Clave-Valor  | Caché, sesiones, config.        | Redis, DynamoDB    | Alta velocidad y escalabilidad   | Dificultad en consultas complejas     |
| Documentales | CMS, catálogos, logs            | MongoDB, CouchDB   | Flexibilidad en modelado         | Mayor consumo de memoria              |
| Grafos       | Redes sociales, fraude, reco.   | Neo4j, OrientDB    | Relaciones complejas optimizadas | Curva de aprendizaje elevada          |
| Columnas     | Big data, IoT, logs             | Cassandra, HBase   | Escalabilidad horizontal         | Operaciones de escritura más costosas |
| Objetos      | Persistencia POO, modelos ricos | db4o, ObjectDB     | Integración directa POO          | Menor adopción general                |

Aquí tienes los apuntes complementados para **DynamoDB** con ejemplos, casos de uso, mejores prácticas, herramientas del curso y comparativas:

---

## 📚 **DynamoDB: Base de datos NoSQL Serverless**

### ✅ **¿Qué es DynamoDB?**

- DynamoDB es una base de datos **NoSQL serverless** totalmente gestionada por AWS.
- El usuario **no gestiona servidores, backups ni escalabilidad**, ya que AWS se encarga automáticamente de estas tareas.
- Solo es necesario **crear tablas** y optimizar la estructura de datos para maximizar el rendimiento.

---

## 🚀 **Características Clave de DynamoDB**

### 1. **Modelo Clave-Valor y Documentos**

- Almacena datos como **pares clave-valor**.
- Admite **JSON o documentos anidados**, lo que permite almacenar estructuras complejas.

### 2. **Escalabilidad Automática**

- Utiliza **Auto Scaling** para ajustar la capacidad en función de la demanda.
- Puede manejar **millones de solicitudes por segundo** sin afectar el rendimiento.

### 3. **Alta Disponibilidad y Durabilidad**

- Replica automáticamente los datos en **3 zonas de disponibilidad** dentro de una región de AWS.
- Garantiza **99.999%** de disponibilidad.

### 4. **Desempeño Ultra Rápido**

- Utiliza solo **unidades de estado sólido (SSD)** para ofrecer tiempos de respuesta de milisegundos.

### 5. **Integración Nativa con Arquitecturas Event-Driven**

- DynamoDB se integra fácilmente con **Amazon EventBridge, AWS Lambda y Kinesis** para construir arquitecturas basadas en eventos.

---

## 🛠️ **Herramientas Utilizadas en el Curso**

### 1. **AWS CLI** 🌐

- Permite crear, consultar y administrar tablas mediante comandos.
- ✅ **Ejemplo:**

```bash
# Crear una tabla en DynamoDB
aws dynamodb create-table \
  --table-name Usuarios \
  --attribute-definitions AttributeName=ID,AttributeType=S \
  --key-schema AttributeName=ID,KeyType=HASH \
  --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
```

---

### 2. **API Gateway** 🔀

- Expone DynamoDB a través de **endpoints REST** o **HTTP APIs**.
- ✅ **Caso de Uso:**
  - Crear una API para consultar información de un usuario almacenado en DynamoDB.

---

### 3. **AWS Lambda** 🖥️

- Ejecuta funciones sin servidores que interactúan con DynamoDB en respuesta a eventos.
- ✅ **Caso de Uso:**
  - Actualizar registros en DynamoDB cuando un usuario inicia sesión o realiza cambios.
  - Procesar flujos de datos provenientes de Kinesis o EventBridge.

---

### 4. **Python (Boto3)** 🐍

- SDK para interactuar programáticamente con DynamoDB.
- ✅ **Ejemplo:**

```python
import boto3

# Inicializar cliente de DynamoDB
dynamodb = boto3.resource('dynamodb')

# Seleccionar tabla
table = dynamodb.Table('Usuarios')

# Insertar un nuevo ítem
response = table.put_item(
    Item={
        'ID': '123',
        'Nombre': 'Juan',
        'Email': 'juan@example.com'
    }
)
print("Item insertado con éxito:", response)
```

---

## 📦 **Casos de Uso de DynamoDB**

### 🎯 **1. Gestión de Sesiones de Usuarios**

- Almacena sesiones activas de usuarios para aplicaciones web o móviles.
- **Ejemplo:** Gestionar sesiones de autenticación para una app de e-commerce.

---

### 📡 **2. Procesamiento de Eventos en Tiempo Real**

- DynamoDB puede actuar como una fuente de eventos para **AWS Lambda** y **EventBridge**.
- **Ejemplo:** Detectar actualizaciones en datos de pedidos y enviar notificaciones en tiempo real.

---

### 🛍️ **3. Catálogos de Productos para E-commerce**

- Almacena información de productos con atributos como **nombre, precio, stock, etc.**
- **Ejemplo:** Consultar productos en una tienda en línea con baja latencia.

---

### 📊 **4. Registro de Logs y Auditorías**

- Utilizar **Streams de DynamoDB** para registrar cambios en tablas y mantener auditorías.
- **Ejemplo:** Guardar un historial de cambios en la información de clientes.

---

## 🎯 **Buenas Prácticas para DynamoDB**

✅ **1. Uso de Claves Particionadas Eficientes**

- Optimiza el rendimiento distribuyendo las escrituras uniformemente.
- Evita **hot partitions** eligiendo claves de partición únicas.

✅ **2. Uso de Índices Secundarios (GSI y LSI)**

- **GSI (Global Secondary Index):** Permite consultas eficientes usando distintos atributos.
- **LSI (Local Secondary Index):** Optimiza consultas en la misma clave de partición.

✅ **3. Configuración de Auto Scaling**

- Habilitar **Auto Scaling** para ajustar automáticamente la capacidad de lectura/escritura.

✅ **4. Uso de Streams para Arquitecturas Event-Driven**

- Habilitar **DynamoDB Streams** para capturar cambios y procesarlos en tiempo real.

---

## 📊 **Comparativa DynamoDB vs Otras Bases NoSQL**

| Característica          | DynamoDB              | MongoDB                | Cassandra                  |
| ----------------------- | --------------------- | ---------------------- | -------------------------- |
| Modelo                  | Clave-Valor/Documento | Documento              | Columnar                   |
| Escalabilidad           | Automática            | Manual o auto-sharding | Horizontal                 |
| Rendimiento             | Milisegundos          | Depende del tamaño     | Alta latencia en escritura |
| Arquitectura Serverless | Sí                    | No                     | No                         |
| Integración con AWS     | Nativa                | Limitada               | No integrada               |
| Consistencia            | Eventual/Strong       | Eventual               | Eventual                   |

---

Aquí tienes una explicación completa sobre **llaves primarias, llaves de partición y llaves de ordenación** en **DynamoDB**, con ejemplos, casos de uso y buenas prácticas:

---

## 🔑 **1. Llave Primaria (Primary Key)**

### ✅ **Definición de llave primaria**

- La **llave primaria** identifica de manera **única** cada ítem en una tabla de DynamoDB.
- Es un conjunto de atributos que define cómo se almacenan y acceden los datos.
- DynamoDB ofrece dos tipos de llaves primarias:
  - **Llave de Partición (Partition Key)** → Clave simple.
  - **Llave Compuesta (Partition Key + Sort Key)** → Clave compuesta.

---

## 🧩 **2. Llave de Partición (Partition Key)**

### ✅ **Definición de llave de partición**

- También conocida como **Hash Key**, es un atributo único utilizado para distribuir datos en particiones físicas.
- DynamoDB **hash** el valor de la llave de partición para determinar en qué partición se almacena el ítem.
- Los ítems con la misma llave de partición se almacenan en la misma partición.

---

### 📚 **Ejemplo: Llave de Partición Simple**

```bash
# Crear una tabla con llave de partición simple
aws dynamodb create-table \
  --table-name Productos \
  --attribute-definitions AttributeName=ProductoID,AttributeType=S \
  --key-schema AttributeName=ProductoID,KeyType=HASH \
  --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
```

- **ProductoID:** Es la llave de partición y su valor puede ser un `String` (S), `Number` (N) o `Binary` (B).
- Cada ítem en la tabla **Productos** será identificado por su `ProductoID`.

---

### 🛠️ **Caso de Uso: Llave de Partición Simple**

- **Catálogo de Productos:** Una tabla que almacena productos donde `ProductoID` es único.
- **Consulta de datos:** Búsqueda rápida usando el valor de la llave de partición.

```python
import boto3

# Inicializar cliente DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Productos')

# Obtener un producto por su ProductoID
response = table.get_item(Key={'ProductoID': '12345'})
print(response['Item'])
```

---

### ⚡️ **Problema de Hot Partitions**

- Si muchos ítems tienen la misma llave de partición o si algunas llaves son consultadas más frecuentemente, pueden crear **particiones calientes (hot partitions)**.
- Para evitar esto:
  - Distribuye datos uniformemente con claves diversificadas.
  - Usa patrones como **prefijos aleatorios** o **hashes**.

---

## 🧩 **3. Llave de Ordenación (Sort Key)**

### ✅ **Definición**

- También conocida como **Range Key**, es un segundo atributo utilizado para ordenar ítems dentro de la misma llave de partición.
- Los ítems con la misma llave de partición son ordenados por valor de la llave de ordenación.
- Permite consultas eficientes al buscar rangos de valores.

---

### 📚 **Ejemplo: Llave de Partición + Llave de Ordenación**

```bash
# Crear una tabla con llave compuesta
aws dynamodb create-table \
  --table-name Pedidos \
  --attribute-definitions \
    AttributeName=ClienteID,AttributeType=S \
    AttributeName=FechaPedido,AttributeType=S \
  --key-schema \
    AttributeName=ClienteID,KeyType=HASH \
    AttributeName=FechaPedido,KeyType=RANGE \
  --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
```

- **ClienteID:** Llave de partición.
- **FechaPedido:** Llave de ordenación que permite ordenar los pedidos de cada cliente.

---

### 🛠️ **Caso de Uso: Llave de Ordenación**

- **Historial de Pedidos:** Almacenar pedidos de clientes donde `ClienteID` es la llave de partición y `FechaPedido` es la llave de ordenación.
- **Consulta de datos:** Obtener pedidos recientes de un cliente específico.

```python
# Obtener los pedidos más recientes de un cliente
response = table.query(
    KeyConditionExpression='ClienteID = :cliente AND FechaPedido BETWEEN :inicio AND :fin',
    ExpressionAttributeValues={
        ':cliente': 'C123',
        ':inicio': '2023-01-01',
        ':fin': '2023-12-31'
    }
)
for item in response['Items']:
    print(item)
```

---

### 🎯 **Ventajas de Llave Compuesta**

- Permite consultas de rangos eficaces, como:
  - Obtener **los últimos N pedidos** de un cliente.
  - Buscar **eventos** dentro de un rango de fechas.
  - Recuperar **mensajes** ordenados cronológicamente.

---

## ⚡️ **Comparativa: Llave de Partición vs Llave de Ordenación**

| Característica         | Llave de Partición              | Llave de Ordenación                        |
| ---------------------- | ------------------------------- | ------------------------------------------ |
| Función principal      | Distribuir ítems en particiones | Ordenar ítems dentro de la misma partición |
| Tipo                   | Clave única                     | Clave secundaria (opcional)                |
| Operaciones permitidas | Búsqueda directa                | Búsqueda por rango o valores específicos   |
| Escalabilidad          | Alta si es bien distribuida     | No afecta directamente la escalabilidad    |
| Consulta               | get_item                        | query (para rangos)                        |

---

## 🔥 **4. Índices Secundarios para Consultas Alternativas**

Para realizar consultas más avanzadas, puedes utilizar índices secundarios:

### ✅ **Índice Secundario Global (GSI)**

- Permite buscar ítems utilizando atributos distintos a la llave primaria.
- Las consultas no necesitan la llave de partición original.

### ✅ **Índice Secundario Local (LSI)**

- Usa la misma llave de partición pero permite diferentes llaves de ordenación para consultas alternativas.

---

## 🎯 **Buenas Prácticas para Llaves en DynamoDB**

✅ **1. Evita Hot Partitions**

- Usa llaves de partición diversificadas.
- Considera agregar un prefijo aleatorio o timestamp para distribuir mejor los datos.

✅ **2. Usa Llaves Compuestas para Rango de Consultas**

- Utiliza llaves de ordenación si necesitas filtrar datos por fecha, ID, o valores secuenciales.

✅ **3. Habilita Índices Secundarios para Consultas Alternativas**

- Crea GSIs para permitir búsquedas en atributos que no son parte de la llave primaria.

✅ **4. Usa Tipos de Datos Apropiados**

- Claves de partición deben ser cadenas (`String`), números (`Number`), o binarios (`Binary`).

---

## 📚 **¿Qué es una Partición en DynamoDB?**

- Una **partición** es una unidad física de almacenamiento en DynamoDB que almacena una porción de los datos de la tabla.
- Los datos se distribuyen automáticamente en particiones para mantener **escalabilidad** y **rendimiento**.
- **Claves de Partición** determinan cómo los datos se dividen entre particiones.

---

## 🧠 **¿Cómo Funciona el Mapeo a Particiones?**

1. **Hash de la Clave de Partición**

   - DynamoDB aplica una función hash al valor de la clave de partición para calcular un **valor hash**.
   - Este valor hash se utiliza para asignar el ítem a una **partición específica**.

2. **Almacenamiento en Particiones**
   - Los ítems con la **misma clave de partición** se almacenan en la misma partición, pero ordenados por la **llave de ordenación** (si existe).
   - Si la tabla solo tiene una **clave de partición** (sin clave de ordenación), DynamoDB almacena todos los ítems con la misma clave de partición juntos.

---

## 📊 **Ejemplo Visual de Particionamiento**

Imagina que tienes una tabla de **Usuarios** con la siguiente estructura:

- **UsuarioID (Partition Key):** Identificador único del usuario.
- **Nombre:** Nombre del usuario.
- **FechaRegistro:** Fecha en la que el usuario se unió.

```plaintext
+------------+--------+--------------+
| UsuarioID   | Nombre | FechaRegistro|
+------------+--------+--------------+
| U1001      | Juan   | 2023-01-10   |
| U1002      | Maria  | 2023-02-15   |
| U1003      | Pedro  | 2023-03-20   |
| U1004      | Ana    | 2023-04-25   |
+------------+--------+--------------+
```

- DynamoDB aplica un **hash** al valor de `UsuarioID` para determinar a qué partición asignar cada ítem.
- Por ejemplo:
  - `U1001 → Partición 1`
  - `U1002 → Partición 2`
  - `U1003 → Partición 1`
  - `U1004 → Partición 3`

---

## ⚡️ **Capacidad de las Particiones**

Cada partición tiene una capacidad definida en función del modelo de capacidad seleccionado:

### ✅ **Modo de Capacidad Aprovisionada**

- Capacidad de lectura y escritura es **manual**.
- Cada partición puede manejar:
  - **3,000 lecturas fuertes** por segundo.
  - **6,000 lecturas eventual-consistentes** por segundo.
  - **1,000 escrituras por segundo.**

---

### ✅ **Modo de Capacidad Bajo Demanda**

- DynamoDB ajusta automáticamente la capacidad según el tráfico.
- Ideal para cargas impredecibles o poco consistentes.

---

## 🎯 **Cálculo del Número de Particiones**

El número de particiones depende de:

- **Tamaño de los Datos:** 10 GB por partición.
- **Capacidad de Lectura/Escritura:** 3,000 RCUs o 1,000 WCUs por partición.

### 🧠 **Fórmula para Particiones:**

- **Particiones por tamaño:**
  \[
  \text{Número de Particiones} = \frac{\text{Tamaño Total de la Tabla (GB)}}{10}
  \]

- **Particiones por capacidad:**
  \[
  \text{Número de Particiones} = \max \left( \frac{\text{Lecturas por segundo}}{3000}, \frac{\text{Escrituras por segundo}}{1000} \right)
  \]

---

### 📚 **Ejemplo:**

- Tabla con **120 GB** de datos y **2,000 escrituras/segundo.**
- **Particiones por tamaño:**
  \[
  \frac{120}{10} = 12 \text{ particiones.}
  \]
- **Particiones por capacidad:**
  \[
  \frac{2000}{1000} = 2 \text{ particiones.}
  \]

DynamoDB elegirá el valor **mayor**, es decir, **12 particiones.**

---

## ⚡️ **Hot Partitions: Un Problema Común**

### ❗️ **¿Qué es una Hot Partition?**

- Ocurre cuando una partición recibe demasiadas lecturas/escrituras respecto a otras.
- Si una clave de partición es accedida con mucha frecuencia, esta partición puede **saturarse**, afectando el rendimiento de toda la tabla.

---

### 🛑 **Ejemplo de Hot Partition**

- Una tabla de **Pedidos** donde todos los pedidos del día tienen la misma clave de partición (`FechaPedido`).
- Si muchos pedidos llegan en la misma fecha, esta clave de partición sobrecarga una única partición.

---

## 🎯 **Buenas Prácticas para Evitar Hot Partitions**

✅ **1. Diversificación de Claves de Partición**

- Añade prefijos o sufijos aleatorios para distribuir la carga.

```python
# Prefijo aleatorio para la clave de partición
PartitionKey = f"{random.randint(1, 100)}#UsuarioID123"
```

✅ **2. Usa Llaves Compuestas para Segmentar Datos**

- Añadir una **llave de ordenación** para permitir segmentación dentro de la misma partición.

```bash
aws dynamodb create-table \
  --table-name Pedidos \
  --attribute-definitions \
    AttributeName=UsuarioID,AttributeType=S \
    AttributeName=FechaPedido,AttributeType=S \
  --key-schema \
    AttributeName=UsuarioID,KeyType=HASH \
    AttributeName=FechaPedido,KeyType=RANGE \
  --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
```

✅ **3. Uso de TTL para Eliminar Datos Antiguos**

- Habilita **Time to Live (TTL)** para eliminar automáticamente ítems antiguos y reducir la carga.

```bash
aws dynamodb update-time-to-live \
  --table-name Pedidos \
  --time-to-live-specification "Enabled=true, AttributeName=FechaExpiracion"
```

✅ **4. Distribución Uniforme de Cargas de Trabajo**

- Divide datos grandes en múltiples tablas si es necesario.
- Usa estrategias como **Sharding Manual** si esperas un crecimiento constante.

---

## 🔥 **Comparativa: Particiones vs Índices**

| Característica               | Particiones                     | Índices Secundarios (GSI/LSI) |
| ---------------------------- | ------------------------------- | ----------------------------- |
| Función principal            | Distribuir datos                | Consultas alternativas        |
| Capacidad                    | Limitada por tamaño y capacidad | Capacidad independiente       |
| Escalabilidad                | Automática                      | Necesita planificación manual |
| Uso de memoria               | Almacena ítems principales      | Almacena copias parciales     |
| Prevención de Hot Partitions | Diversificación de llaves       | Uso de GSIs para consulta     |

---

aws dynamodb create-table --table-name dynamodb-prueba --key-schema AttributeName=IdStudent,KeyType=HASH --attribute-definitions AttributeName=IdStudent,AttributeType=N
aws dynamodb create-table --table-name dynamodb-prueba --key-schema AttributeName=IdStudent,KeyType=HASH --attribute-definitions AttributeName=IdStudent,AttributeType=N --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
aws dynamodb batch-write-item --request-items file://characters.json

## 🎯 **Objetivo de una Buena Partition Key**

El objetivo principal de una **Partition Key** bien diseñada es:

- **Distribuir datos de manera uniforme** para evitar **Hot Partitions**.
- **Optimizar consultas** para garantizar lecturas y escrituras rápidas.
- **Minimizar latencia** en operaciones de DynamoDB.

---

## 📚 **1. Atributos con Alta Cardinalidad**

### ✅ **¿Qué es la Cardinalidad?**

- La **cardinalidad** se refiere al **número de valores únicos** que puede tener un atributo.
  - **Alta cardinalidad:** Muchos valores únicos → Ideal para clave de partición.
  - **Baja cardinalidad:** Pocos valores repetidos → Mala opción para clave de partición.

---

### 🎯 **Por qué es importante?**

- Una clave de partición con **alta cardinalidad** garantiza que los datos se distribuyan equitativamente entre las particiones.
- Si eliges un atributo con **baja cardinalidad**, algunos valores recibirán mucha más carga, causando **hot partitions**.

---

### 📚 **Ejemplo: Alta vs Baja Cardinalidad**

- **Alta Cardinalidad:** `UsuarioID`, `ProductoID`, `NumeroTransaccion`
- **Baja Cardinalidad:** `Estado`, `TipoProducto`, `Región`

```plaintext
Tabla: Pedidos
+-------------+-------------+------------+
| PedidoID    | Estado      | Fecha      |
+-------------+-------------+------------+
| 10001       | Enviado     | 2023-01-10 |
| 10002       | Pendiente   | 2023-02-05 |
| 10003       | Enviado     | 2023-03-15 |
| 10004       | Cancelado   | 2023-04-25 |
+-------------+-------------+------------+
```

- ✅ **Recomendado:** Usar `PedidoID` o `UsuarioID` como clave de partición.
- ❌ **Evitar:** Usar `Estado`, ya que solo tiene 3 valores (`Enviado`, `Pendiente`, `Cancelado`), causando **particiones calientes.**

---

## 🔗 **2. Uso de Atributos Compuestos para Claves Compuestas**

### ✅ **¿Qué es una Clave Compuesta?**

- Una **clave compuesta** utiliza:
  - **Partition Key:** Para distribuir datos.
  - **Sort Key:** Para ordenar los datos dentro de la misma partición.

---

### 📚 **Ejemplo: Clave Compuesta**

Tabla **Pedidos** donde:

- **Partition Key:** `UsuarioID`
- **Sort Key:** `FechaPedido`

```bash
aws dynamodb create-table \
  --table-name Pedidos \
  --attribute-definitions \
    AttributeName=UsuarioID,AttributeType=S \
    AttributeName=FechaPedido,AttributeType=S \
  --key-schema \
    AttributeName=UsuarioID,KeyType=HASH \
    AttributeName=FechaPedido,KeyType=RANGE \
  --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
```

✅ **Ventajas:**

- Permite consultas eficaces por rango de valores.
- Evita saturar una partición al distribuir datos por múltiples `UsuarioID`.

---

### 📡 **Caso de Uso: Pedidos por Usuario**

```python
import boto3
from boto3.dynamodb.conditions import Key

# Inicializar cliente de DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Pedidos')

# Consultar pedidos de un usuario específico
response = table.query(
    KeyConditionExpression=Key('UsuarioID').eq('U123') & Key('FechaPedido').between('2023-01-01', '2023-12-31')
)
for item in response['Items']:
    print(item)
```

---

## 🧩 **3. Uso de Prefijos y Sufijos para Distribuir Carga**

### ✅ **¿Por qué agregar Prefijos o Sufijos?**

- Ayuda a **distribuir datos** cuando tienes un valor de clave de partición con **alta frecuencia de acceso**.
- El uso de **prefijos aleatorios** o **sufijos** divide los datos en múltiples particiones.

---

### 📚 **Ejemplo: Prefijos Aleatorios**

Si `UsuarioID` es la clave de partición y hay muchos accesos a un solo usuario, puedes usar un **prefijo aleatorio** para balancear la carga:

```python
import random

# Generar clave de partición diversificada
PartitionKey = f"{random.randint(1, 100)}#UsuarioID123"
```

✅ **Ventaja:** Distribuye la carga de acceso uniformemente en 100 particiones diferentes.

---

### 📚 **Ejemplo: Sufijos por Tiempo**

Agregar un **sufijo de fecha** a la clave de partición para dividir datos en intervalos:

```python
# Clave de partición con sufijo temporal
PartitionKey = f"Pedido#2023-01-01"
```

✅ **Ventaja:** Los pedidos se dividen en múltiples claves, facilitando consultas históricas.

---

## ⚡️ **4. Uso de Hash Manual para Diversificación**

Si esperas **alta carga de tráfico** en una clave de partición, puedes agregar un **hash manual** para diversificar.

---

### 📚 **Ejemplo: Hash para PedidoID**

```python
import hashlib

# Generar hash para distribuir carga
PedidoID = '12345'
hash_value = int(hashlib.md5(PedidoID.encode()).hexdigest(), 16) % 10
PartitionKey = f"{hash_value}#PedidoID#{PedidoID}"
```

✅ **Ventaja:** Crea múltiples claves diferentes que distribuyen datos de manera más uniforme.

---

## 🚀 **5. Elección Inteligente de Partition Keys**

### ✅ **Criterios para Elegir una Buena Clave de Partición**

1. **Alta Cardinalidad:** El atributo debe tener valores altamente variados.
   - 🎯 Ejemplo: `UsuarioID`, `PedidoID`, `NumeroTransaccion`
2. **Accesos Uniformes:** Los valores de la clave de partición deben recibir tráfico uniforme.
   - 🚫 Evita usar `Estado` o `TipoProducto`.
3. **Distribución de Datos:** Si esperas acceso masivo en un solo valor, añade prefijos/sufijos.
   - 🎯 Usa valores aleatorios o timestamps.
4. **Considera Consultas Futuras:** Piensa en cómo se consultarán los datos.
   - ✅ Claves compuestas (`UsuarioID` + `FechaPedido`) optimizan búsquedas por rango.

---

## 📊 **Comparativa: Buenas vs Malas Claves de Partición**

| Criterio                     | Buena Clave de Partición                | Mala Clave de Partición        |
| ---------------------------- | --------------------------------------- | ------------------------------ |
| Cardinalidad Alta            | `UsuarioID`, `ProductoID`               | `Estado`, `Región`             |
| Uniformidad de Carga         | Diversificación con prefijos            | Concentración en pocos valores |
| Consultas Eficientes         | Claves compuestas (`UsuarioID + Fecha`) | Atributos repetidos            |
| Prevención de Hot Partitions | Sí                                      | No                             |

## ⚡️ **¿Qué es una Hot Partition?**

Una **Hot Partition** ocurre cuando una sola partición recibe una carga **desproporcionada de tráfico** (lecturas o escrituras) en comparación con otras particiones. Esto provoca:

✅ **Síntomas:**

- Latencia elevada en las consultas.
- Errores de `ProvisionedThroughputExceededException`.
- Pérdida de rendimiento en toda la tabla.

✅ **Causa Principal:**

- Claves de partición que **no distribuyen datos uniformemente**, lo que lleva a que una o pocas particiones manejen la mayoría del tráfico.

---

## 📚 **¿Cómo Funcionan las Particiones en DynamoDB?**

1. **Claves de Partición:** DynamoDB aplica una función **hash** a la clave de partición para determinar la partición donde se almacenará el ítem.
2. **Distribución de Datos:** Los datos se dividen en particiones físicas de hasta **10 GB** de tamaño o **3,000 RCUs (Read Capacity Units)** o **1,000 WCUs (Write Capacity Units)**.
3. **Carga Desbalanceada:** Si una clave de partición es consultada o escrita con frecuencia, puede **sobrecargar** la partición correspondiente.

---

## 🔥 **Ejemplo Visual de Hot Partition**

Imagina que tienes una tabla de **Pedidos** con esta estructura:

- **Partition Key:** `FechaPedido`
- **Sort Key:** `PedidoID`

```plaintext
+--------------+-----------+---------+
| FechaPedido  | PedidoID  | Cliente |
+--------------+-----------+---------+
| 2023-03-10   | P001      | Juan    |
| 2023-03-10   | P002      | Ana     |
| 2023-03-10   | P003      | Pedro   |
| 2023-03-10   | P004      | Maria   |
+--------------+-----------+---------+
```

⚡️ **Problema:**

- Si todos los pedidos del día **2023-03-10** usan la misma clave de partición (`FechaPedido`), esta partición recibe toda la carga, causando una **hot partition**.

---

## ⚡️ **Causas Comunes de Hot Partitions**

### ❗️ **1. Baja Cardinalidad de la Clave de Partición**

- Si un atributo tiene **pocos valores únicos**, todas las consultas recaen en unas pocas particiones.
- **Ejemplo:** Usar `EstadoPedido` (`Enviado`, `Pendiente`, `Cancelado`) como clave de partición.

---

### ❗️ **2. Consultas Frecuentes a una Sola Partición**

- Si una clave de partición es consultada o actualizada masivamente, sobrecarga una única partición.
- **Ejemplo:** Consultar repetidamente datos de un solo cliente (`UsuarioID`).

---

### ❗️ **3. Escrituras o Lecturas Masivas en un Intervalo Corto**

- Cargas de datos masivas o procesos ETL que insertan o leen datos rápidamente pueden saturar particiones.
- **Ejemplo:** Insertar millones de registros con la misma `FechaPedido`.

---

### ❗️ **4. Uso de Timestamp como Clave de Partición**

- Si utilizas **fechas/timestamps** como clave de partición, es probable que ciertos períodos tengan más actividad que otros.
- **Ejemplo:** Consultas de logs para un solo día o una hora específica.

---

## 📊 **Impacto de Hot Partitions**

- 🔴 **Latencia Elevada:** Afecta el tiempo de respuesta para consultas y escrituras.
- 🔴 **Errores de Throughput:** Si superas la capacidad de la partición, obtendrás `ProvisionedThroughputExceededException`.
- 🔴 **Degradación del Rendimiento Global:** Afecta a toda la tabla, incluso si otras particiones están infrautilizadas.

---

## 🛠️ **Cómo Detectar Hot Partitions**

### 📡 **1. Usar Amazon CloudWatch**

- Monitorea métricas de DynamoDB, como:
  - `ConsumedReadCapacityUnits` (RCUs consumidos)
  - `ConsumedWriteCapacityUnits` (WCUs consumidos)
  - `ThrottledRequests` (solicitudes limitadas)

---

### 📚 **2. Habilitar DynamoDB Streams**

- Usa **Streams** para analizar cambios y detectar cuándo una clave de partición está siendo actualizada o consultada frecuentemente.

---

## 🚀 **Estrategias para Prevenir Hot Partitions**

---

### ✅ **1. Usar Atributos con Alta Cardinalidad**

- Elige claves de partición con **muchos valores únicos** para distribuir los datos.
- **Ejemplo:** Usar `UsuarioID` en lugar de `EstadoPedido`.

```plaintext
+----------+------------+
| UsuarioID | FechaPedido|
+----------+------------+
| U123      | 2023-03-10 |
| U456      | 2023-03-10 |
| U789      | 2023-03-10 |
+----------+------------+
```

---

### ✅ **2. Uso de Prefijos Aleatorios**

- Añadir **prefijos aleatorios** para diversificar claves de partición.
- **Ejemplo:**

```python
import random

# Generar clave diversificada
PartitionKey = f"{random.randint(1, 100)}#PedidoID#12345"
```

✅ **Ventaja:** Los datos se distribuyen en múltiples particiones en lugar de una sola.

---

### ✅ **3. Hash Manual para Claves de Partición**

- Usa un **hash manual** para crear múltiples versiones de la clave de partición.

```python
import hashlib

# Hash para distribuir carga
UsuarioID = 'U12345'
hash_value = int(hashlib.md5(UsuarioID.encode()).hexdigest(), 16) % 10
PartitionKey = f"{hash_value}#UsuarioID#{UsuarioID}"
```

✅ **Ventaja:** Distribuye automáticamente datos de manera uniforme.

---

### ✅ **4. Uso de Claves Compuestas (Partition + Sort Key)**

- Usa una **clave compuesta** para segmentar datos y evitar sobrecargas.
- **Ejemplo:** `UsuarioID` como clave de partición y `FechaPedido` como clave de ordenación.

```bash
aws dynamodb create-table \
  --table-name Pedidos \
  --attribute-definitions \
    AttributeName=UsuarioID,AttributeType=S \
    AttributeName=FechaPedido,AttributeType=S \
  --key-schema \
    AttributeName=UsuarioID,KeyType=HASH \
    AttributeName=FechaPedido,KeyType=RANGE \
  --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
```

---

### ✅ **5. Uso de TTL para Reducir Carga de Particiones Antiguas**

- Habilita **Time to Live (TTL)** para eliminar ítems antiguos y liberar espacio en particiones congestionadas.

```bash
aws dynamodb update-time-to-live \
  --table-name Pedidos \
  --time-to-live-specification "Enabled=true, AttributeName=FechaExpiracion"
```

---

### ✅ **6. Sharding Manual para Distribuir Datos**

- Divide los datos manualmente en múltiples tablas si esperas una **alta carga de tráfico**.
- **Ejemplo:** Crear tablas separadas para diferentes rangos de fechas (`Pedidos_2023`, `Pedidos_2024`).

---

## 🎯 **Consejos adicionales**

✅ **1. Analiza tus Patrones de Acceso**

- Estudia cómo se consultan y actualizan los datos para optimizar la distribución.

✅ **2. Agrega Entropía a las Claves de Partición**

- Usa valores aleatorios o hash para evitar valores repetidos.

✅ **3. Monitorea Capacidad y Latencia con CloudWatch**

- Detecta patrones de tráfico anómalos.

✅ **4. Evita Consultas en Masa en la Misma Partición**

- Distribuye grandes operaciones entre múltiples particiones.

✅ **5. Usa Claves Compuestas si es Necesario**

- Optimiza consultas por rangos para evitar acceder a la misma partición.

---

## 📊 **Comparativa: Buenas vs Malas Prácticas para Particiones**

| Práctica                    | Efecto en Particiones   | Resultado         |
| --------------------------- | ----------------------- | ----------------- |
| Alta cardinalidad           | Carga distribuida       | Óptimo            |
| Clave de baja cardinalidad  | Hot Partitions          | Mala distribución |
| Prefijos/Sufijos aleatorios | Particiones balanceadas | Mayor rendimiento |
| Timestamp como clave        | Partición sobrecargada  | Latencia elevada  |
| Uso de claves compuestas    | Segmentación optimizada | Consultas rápidas |

## 📚 **¿Qué es un Índice Secundario Local (LSI)?**

Un **Índice Secundario Local (Local Secondary Index, LSI)** permite crear consultas alternativas sobre una tabla en DynamoDB utilizando una **clave de ordenación (sort key) diferente** de la tabla principal, manteniendo la misma **clave de partición (partition key)**.

✅ **Características Clave:**

- Solo se puede crear **al momento de crear la tabla**.
- Usa la **misma clave de partición** que la tabla base.
- Puede tener **diferentes claves de ordenación** para permitir consultas por distintos atributos.
- **Máximo 5 LSIs** por tabla.

---

## 🎯 **Diferencia Entre LSI y GSI**

| Característica      | LSI (Índice Secundario Local) | GSI (Índice Secundario Global)    |
| ------------------- | ----------------------------- | --------------------------------- |
| Clave de Partición  | Igual a la tabla base         | Puede ser diferente               |
| Clave de Ordenación | Diferente                     | Diferente                         |
| Creación            | Solo al crear la tabla        | Puede crearse/modificarse después |
| Consistencia        | Consistencia fuerte posible   | Solo eventual                     |
| Máximo por tabla    | 5 índices                     | 20 índices                        |

---

## 🧠 **¿Cuándo Usar LSI?**

- Cuando necesitas consultar **múltiples atributos** relacionados con la misma clave de partición.
- Para realizar **consultas por rango** sobre distintos atributos sin modificar la clave principal.
- Ideal para **consultar historiales** o **datos ordenados cronológicamente**.

---

## 📚 **Ejemplo Práctico de LSI**

### 🎨 **Caso de Uso: Historial de Pedidos de un Usuario**

- **Tabla:** `Pedidos`
- **Clave de Partición:** `UsuarioID` (STRING)
- **Clave de Ordenación Principal:** `PedidoID` (STRING)

Queremos poder:

- Consultar pedidos de un usuario **por estado** (`EstadoPedido`).
- Consultar pedidos por **fecha de creación** (`FechaPedido`).

---

### ✅ **1. Crear la Tabla con un LSI**

```bash
aws dynamodb create-table \
  --table-name Pedidos \
  --attribute-definitions \
    AttributeName=UsuarioID,AttributeType=S \
    AttributeName=PedidoID,AttributeType=S \
    AttributeName=EstadoPedido,AttributeType=S \
  --key-schema \
    AttributeName=UsuarioID,KeyType=HASH \
    AttributeName=PedidoID,KeyType=RANGE \
  --local-secondary-indexes \
    "[
      {
        \"IndexName\": \"EstadoPedidoIndex\",
        \"KeySchema\": [
          {\"AttributeName\": \"UsuarioID\", \"KeyType\": \"HASH\"},
          {\"AttributeName\": \"EstadoPedido\", \"KeyType\": \"RANGE\"}
        ],
        \"Projection\": {\"ProjectionType\": \"ALL\"}
      }
    ]" \
  --billing-mode PAY_PER_REQUEST
```

---

### 📚 **2. Explicación del Comando**

- **`--attribute-definitions`**: Define los atributos usados en la tabla y los índices.
- **`--key-schema`**: Define la clave primaria de la tabla (`UsuarioID` y `PedidoID`).
- **`--local-secondary-indexes`**: Define el LSI.
  - `IndexName`: Nombre del índice (`EstadoPedidoIndex`).
  - `KeySchema`: Usa la misma `UsuarioID` pero cambia la sort key a `EstadoPedido`.
  - `ProjectionType`: `ALL` incluye todos los atributos del ítem.

---

## 🔎 **3. Consultar Usando el LSI**

Ahora puedes consultar pedidos de un usuario filtrados por `EstadoPedido`.

---

### ✅ **Ejemplo 1: Consultar Pedidos por Estado**

```bash
aws dynamodb query \
  --table-name Pedidos \
  --index-name EstadoPedidoIndex \
  --key-condition-expression "UsuarioID = :id AND EstadoPedido = :estado" \
  --expression-attribute-values file://values.json
```

**Archivo `values.json`:**

```json
{
  ":id": { "S": "U123" },
  ":estado": { "S": "Enviado" }
}
```

---

### ✅ **Ejemplo 2: Consultar Pedidos Ordenados por Fecha**

Si necesitas consultar pedidos **ordenados por `FechaPedido`**, puedes agregar otro LSI.

```bash
aws dynamodb create-table \
  --table-name Pedidos \
  --attribute-definitions \
    AttributeName=UsuarioID,AttributeType=S \
    AttributeName=PedidoID,AttributeType=S \
    AttributeName=FechaPedido,AttributeType=S \
  --key-schema \
    AttributeName=UsuarioID,KeyType=HASH \
    AttributeName=PedidoID,KeyType=RANGE \
  --local-secondary-indexes \
    "[
      {
        \"IndexName\": \"FechaPedidoIndex\",
        \"KeySchema\": [
          {\"AttributeName\": \"UsuarioID\", \"KeyType\": \"HASH\"},
          {\"AttributeName\": \"FechaPedido\", \"KeyType\": \"RANGE\"}
        ],
        \"Projection\": {\"ProjectionType\": \"ALL\"}
      }
    ]" \
  --billing-mode PAY_PER_REQUEST
```

---

## 🧩 **Tipos de Proyecciones en LSI**

Cuando defines un LSI, puedes elegir qué atributos incluir en el índice:

✅ **1. ALL (Todos los Atributos)**

- Incluye todos los atributos del ítem.
- Usa más espacio, pero permite consultas más completas.

✅ **2. KEYS_ONLY (Solo Claves)**

- Solo almacena la clave primaria y clave de ordenación.
- Más eficiente en espacio, pero requiere consultas adicionales.

✅ **3. INCLUDE (Atributos Seleccionados)**

- Incluye atributos específicos además de la clave.

---

## ⚡️ **Limitaciones de LSI**

❗️ **1. Máximo 5 LSIs por Tabla**

- Si necesitas más de 5 índices, considera usar **GSIs**.

❗️ **2. No Se Puede Modificar Después**

- Los LSIs solo pueden ser creados durante la **creación de la tabla**. Si necesitas cambios:
  - **Solución:** Crear una nueva tabla y migrar los datos.

❗️ **3. Tamaño Máximo de Partición**

- El tamaño de cada partición no puede exceder **10 GB**.
- Si usas LSIs, asegúrate de que los datos estén bien distribuidos.

---

## 🎯 **Comparativa: LSI vs GSI**

| Característica      | LSI                            | GSI                           |
| ------------------- | ------------------------------ | ----------------------------- |
| Clave de Partición  | Igual a la tabla base          | Puede ser diferente           |
| Clave de Ordenación | Distinta, definida en LSI      | Diferente, definida en GSI    |
| Creación            | Solo al crear la tabla         | Se puede agregar/modificar    |
| Consistencia        | Consistencia fuerte posible    | Solo consistencia eventual    |
| Uso de Partición    | Misma partición que tabla base | Nueva partición independiente |
| Número Máximo       | 5 por tabla                    | 20 por tabla                  |
| Costo               | Bajo (misma partición)         | Más alto (nueva partición)    |

---

## 🎯 **Buenas Prácticas para LSI**

✅ **1. Planificar Ítems y Consultas**

- Define LSIs solo si sabes que consultarás frecuentemente por esos atributos.

✅ **2. Usa Proyecciones Adecuadas**

- Usa `ALL` solo si necesitas todos los atributos.
- Usa `INCLUDE` para limitar atributos en índices grandes.

✅ **3. Evita Hot Partitions**

- Si tienes muchas actualizaciones para un solo valor de clave de partición, puede causar **hot partitions**.

✅ **4. Considera GSIs si Necesitas Más Flexibilidad**

- Si prevés necesitar índices adicionales o diferentes claves de partición, es mejor optar por **GSIs**.

✅ **5. Monitorea con Amazon CloudWatch**

- Monitorea el tamaño de la tabla y el consumo de capacidad para prevenir particiones calientes.

---

## 📊 **Comparativa de Casos de Uso para LSI y GSI**

| Caso de Uso                          | LSI                          | GSI                             |
| ------------------------------------ | ---------------------------- | ------------------------------- |
| Consultar historial de usuario       | Ideal para ordenar por fecha | No necesario                    |
| Buscar pedidos por estado            | Rápido si es misma partición | GSI si es clave diferente       |
| Indexar múltiples atributos          | Máximo 5 índices             | Hasta 20 índices                |
| Consultas por diferentes particiones | No posible                   | GSI permite partición diferente |

aws dynamodb create-table \
 --table-name 'Music' \
 --attribute-definitions \
 'AttributeName=Artist,AttributeType=S' \
 'AttributeName=SongTitle,AttributeType=S' \
 'AttributeName=AlbumTitle,AttributeType=S' \
 --key-schema \
 'AttributeName=Artist,KeyType=HASH' \
 'AttributeName=SongTitle,KeyType=RANGE' \
 --provisioned-throughput \
 'ReadCapacityUnits=10,WriteCapacityUnits=5' \
 --local-secondary-indexes \
 "[{\"IndexName\": \"AlbumTitleIndex\", \"KeySchema\": [{\"AttributeName\": \"Artist\", \"KeyType\": \"HASH\"}, {\"AttributeName\": \"AlbumTitle\", \"KeyType\": \"RANGE\"}], \"Projection\": {\"ProjectionType\":\"INCLUDE\",\"NonKeyAttributes\":[\"Gender\",\"Year\"]}}]"

## 📚 **¿Qué son RCU y WCU en DynamoDB?**

En DynamoDB, la capacidad de lectura y escritura se mide en **unidades de capacidad (Capacity Units)**:

- ✅ **RCU (Read Capacity Units):** Define cuántos datos puedes leer por segundo.
- ✅ **WCU (Write Capacity Units):** Define cuántos datos puedes escribir por segundo.

El consumo de RCU y WCU depende del **modo de capacidad** de la tabla:

- **Capacidad Aprovisionada (Provisioned Mode):** Asignas manualmente RCU y WCU.
- **Capacidad Bajo Demanda (On-Demand Mode):** DynamoDB escala automáticamente, pero cuesta más si hay tráfico constante.

---

## 📚 **1. ¿Qué es una RCU (Read Capacity Unit)?**

Una **RCU (Unidad de Capacidad de Lectura)** permite leer:

- **1 KB** de datos por segundo con consistencia fuerte.
- **2 KB** por segundo si la lectura es eventual.
- **4 KB** si usas lecturas transaccionales (fuertemente consistentes y atómicas).

---

### 🎯 **Fórmulas para Cálculo de RCU**

- **Lectura Consistente Fuerte:**
  \[
  RCU = \frac{\text{Tamaño del ítem (KB)}}{1}
  \]
- **Lectura Eventual:**
  \[
  RCU = \frac{\text{Tamaño del ítem (KB)}}{2}
  \]
- **Lectura Transaccional:**
  \[
  RCU = \frac{\text{Tamaño del ítem (KB)}}{4}
  \]

---

### ✅ **Ejemplo de Cálculo de RCU**

- **Tamaño del ítem:** 4 KB
- **Lectura Consistente Fuerte:**
  \[
  RCU = \frac{4}{1} = 4 \text{ RCUs por lectura.}
  \]
- **Lectura Eventual:**
  \[
  RCU = \frac{4}{2} = 2 \text{ RCUs por lectura.}
  \]
- **Lectura Transaccional:**
  \[
  RCU = \frac{4}{4} = 1 \text{ RCU por lectura.}
  \]

---

## 📚 **2. ¿Qué es una WCU (Write Capacity Unit)?**

Una **WCU (Unidad de Capacidad de Escritura)** permite escribir:

- **1 KB** de datos por segundo.
- Las **escrituras transaccionales** requieren el doble de capacidad.

---

### 🎯 **Fórmulas para Cálculo de WCU**

- **Escritura Estándar:**
  \[
  WCU = \frac{\text{Tamaño del ítem (KB)}}{1}
  \]
- **Escritura Transaccional:**
  \[
  WCU = \frac{\text{Tamaño del ítem (KB)}}{1} \times 2
  \]

---

### ✅ **Ejemplo de Cálculo de WCU**

- **Tamaño del ítem:** 2 KB
- **Escritura Estándar:**
  \[
  WCU = \frac{2}{1} = 2 \text{ WCUs por escritura.}
  \]
- **Escritura Transaccional:**
  \[
  WCU = \frac{2}{1} \times 2 = 4 \text{ WCUs por escritura transaccional.}
  \]

---

## ⚡️ **3. Modos de Capacidad en DynamoDB**

---

### ✅ **A. Modo Aprovisionado (Provisioned Mode)**

- Asignas manualmente **RCU** y **WCU**.
- Ideal para cargas **predecibles** o aplicaciones con **patrones estables**.
- Si superas la capacidad asignada, las operaciones fallan con `ProvisionedThroughputExceededException`.

---

#### 🎯 **Ejemplo de Creación de Tabla en Modo Aprovisionado**

```bash
aws dynamodb create-table \
  --table-name Pedidos \
  --attribute-definitions \
    AttributeName=PedidoID,AttributeType=S \
  --key-schema \
    AttributeName=PedidoID,KeyType=HASH \
  --provisioned-throughput \
    ReadCapacityUnits=5 \
    WriteCapacityUnits=2
```

- Se asignan **5 RCUs** y **2 WCUs**.

---

### ✅ **B. Modo Bajo Demanda (On-Demand Mode)**

- DynamoDB escala automáticamente para manejar cualquier tráfico.
- No necesitas definir RCU/WCU manualmente.
- **Pago por solicitud**, lo que puede resultar más costoso para cargas constantes.

---

#### 🎯 **Ejemplo de Creación de Tabla en Modo On-Demand**

```bash
aws dynamodb create-table \
  --table-name Pedidos \
  --attribute-definitions \
    AttributeName=PedidoID,AttributeType=S \
  --key-schema \
    AttributeName=PedidoID,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST
```

---

## 🧠 **4. Cálculo de RCU y WCU para una Tabla**

---

### 📚 **A. Cálculo para Lecturas**

- **Tamaño de ítem:** 3 KB
- **Lecturas Consistentes Fuertes:** 100 lecturas por segundo
  \[
  RCU = \frac{3}{1} \times 100 = 300 \text{ RCUs.}
  \]
- **Lecturas Eventuales:** 100 lecturas por segundo
  \[
  RCU = \frac{3}{2} \times 100 = 150 \text{ RCUs.}
  \]
- **Lecturas Transaccionales:** 100 lecturas por segundo
  \[
  RCU = \frac{3}{4} \times 100 = 75 \text{ RCUs.}
  \]

---

### 📚 **B. Cálculo para Escrituras**

- **Tamaño de ítem:** 2 KB
- **Escrituras Estándar:** 50 escrituras por segundo
  \[
  WCU = \frac{2}{1} \times 50 = 100 \text{ WCUs.}
  \]
- **Escrituras Transaccionales:** 50 escrituras por segundo
  \[
  WCU = \frac{2}{1} \times 2 \times 50 = 200 \text{ WCUs.}
  \]

---

## 📊 **5. Comparativa: Modo Aprovisionado vs. Bajo Demanda**

| Característica    | Modo Aprovisionado                | Modo Bajo Demanda                      |
| ----------------- | --------------------------------- | -------------------------------------- |
| Configuración     | Manual (RCU/WCU)                  | Automática                             |
| Costo             | Más barato para cargas constantes | Más costoso si el tráfico es constante |
| Escalabilidad     | Manual, requiere ajuste           | Automática                             |
| Límite de tráfico | Basado en RCU/WCU asignadas       | Ilimitado, pero pago por solicitud     |
| Ideal para        | Cargas predecibles                | Cargas impredecibles                   |

---

## 🚀 **6. Buenas Prácticas para Optimizar RCU y WCU**

---

### ✅ **1. Usa Modo Bajo Demanda para Cargas Variables**

- Si no sabes cuánto tráfico esperar o si la carga es impredecible, usa **modo bajo demanda** (`PAY_PER_REQUEST`).

---

### ✅ **2. Usa Modo Aprovisionado para Cargas Estables**

- Si tienes un tráfico estable, **modo aprovisionado** es más económico.
- Usa **Auto Scaling** para ajustar RCU/WCU automáticamente.

---

### ✅ **3. Reduce Tamaño de los Ítems**

- Los costos de RCU/WCU dependen del tamaño del ítem.
- Optimiza el diseño de los ítems para reducir el tamaño.

---

### ✅ **4. Usa Lecturas Eventuales si es Posible**

- Si no necesitas consistencia fuerte, usa lecturas eventuales para reducir el consumo de RCU.

---

### ✅ **5. Monitoreo con Amazon CloudWatch**

- Usa **CloudWatch** para monitorear el uso de RCU y WCU y ajustar automáticamente si es necesario.
- Métricas importantes:
  - `ConsumedReadCapacityUnits`
  - `ConsumedWriteCapacityUnits`

---

## 🎯 **7. Errores Comunes y Soluciones**

---

### ❗️ **1. ProvisionedThroughputExceededException**

✅ **Causa:**

- Se superaron las RCUs o WCUs asignadas.
  ✅ **Solución:**
- Habilitar **Auto Scaling** o cambiar a **modo bajo demanda**.

---

### ❗️ **2. Throttling de Solicitudes**

✅ **Causa:**

- Si muchas solicitudes exceden la capacidad asignada.
  ✅ **Solución:**
- Reintentar solicitudes fallidas (`Exponential Backoff`).

---

### ❗️ **3. Uso Ineficiente de RCU/WCU**

✅ **Causa:**

- Leer ítems grandes o no optimizar las consultas.
  ✅ **Solución:**
- Optimizar atributos y claves para mejorar eficiencia.
