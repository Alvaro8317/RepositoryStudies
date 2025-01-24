# The Complete dbt (Data Build Tool) Bootcamp: Zero to Hero - Básicos de DBT

DBT es la T en una ETL, DBT no extrae los datos, pero si los transforma con modelos, secuencias y statements, en una analogía de una habitación oscura, hacer una transformación a mano es como una vela para iluminar la habitación, solo alumbrará para uno mismo, pero con DBT es como una literna potente que no solo iluminará para mí, sino para los demás, DBT implementa git, ci cd, software engineering y ambientes, donde se puede cambiar entre ambiente dev y prod fácilmente. Con DBT, tomará los modelos, entenderá las dependencias entre todos los modelos y creará un orden de dependencias.

## Modelos

Son el bloque de construcción básico de la lógica de negocio, se materializan como tablas, vistas, etc. Estos viven en archivos SQL en el directorio folders y los modelos pueden ser refereciados el uno al otro y usar plantillas y macros

## Common table expressions

En SQL, las **Common Table Expressions (CTEs)** son una forma de definir una tabla temporal dentro de una consulta, lo que permite estructurar y organizar mejor consultas complejas. Las CTEs son particularmente útiles cuando necesitas dividir un problema en pasos intermedios para facilitar la lectura y el mantenimiento del código.

---

## \*_SCD Tipo 1: Sobrescribir los valores_

En este caso, simplemente actualizamos los registros existentes en la tabla de destino.

```sql
WITH Actualizacion AS (
    SELECT
        n.ID_Cliente,
        n.Nombre,
        n.Direccion
    FROM Nuevos_Datos n
)
UPDATE Data_Warehouse dw
SET
    dw.Nombre = a.Nombre,
    dw.Direccion = a.Direccion
FROM Data_Warehouse dw
INNER JOIN Actualizacion a
    ON dw.ID_Cliente = a.ID_Cliente;
```

**Explicación:**

1. La CTE `Actualizacion` selecciona los datos nuevos desde la tabla `Nuevos_Datos`.
2. Se actualizan los registros en `Data_Warehouse` según los datos más recientes en `Nuevos_Datos`.

---

### **SCD Tipo 2: Preservar el historial**

Aquí se preserva el historial de cambios añadiendo nuevos registros y marcando los existentes como inactivos.

```sql
WITH Cambios AS (
    SELECT
        dw.ID_Cliente,
        dw.Direccion AS Direccion_Actual,
        n.Direccion AS Direccion_Nueva
    FROM Data_Warehouse dw
    INNER JOIN Nuevos_Datos n
        ON dw.ID_Cliente = n.ID_Cliente
    WHERE dw.Direccion <> n.Direccion
)

-- 1. Marcar registros antiguos como inactivos
UPDATE Data_Warehouse
SET
    Activo = FALSE,
    Fecha_Fin = CURRENT_TIMESTAMP
FROM Cambios c
WHERE Data_Warehouse.ID_Cliente = c.ID_Cliente
  AND Data_Warehouse.Direccion = c.Direccion_Actual;

-- 2. Insertar nuevos registros
INSERT INTO Data_Warehouse (ID_Cliente, Nombre, Direccion, Fecha_Inicio, Fecha_Fin, Activo)
SELECT
    n.ID_Cliente,
    n.Nombre,
    n.Direccion,
    CURRENT_TIMESTAMP AS Fecha_Inicio,
    NULL AS Fecha_Fin,
    TRUE AS Activo
FROM Nuevos_Datos n
INNER JOIN Cambios c
    ON n.ID_Cliente = c.ID_Cliente;
```

**Explicación:**

1. La CTE `Cambios` identifica los registros que necesitan actualización (los datos cuya dirección ha cambiado).
2. En el primer paso, los registros existentes en `Data_Warehouse` se actualizan para marcarse como inactivos (`Activo = FALSE`) y registrar una `Fecha_Fin`.
3. En el segundo paso, se insertan nuevos registros con los datos actualizados, una `Fecha_Inicio` y el estado `Activo = TRUE`.

---

### **¿Por qué usar CTEs?**

1. **Claridad:** Separas la lógica en pasos intermedios, lo que facilita entender y depurar la consulta.
2. **Reutilización:** Puedes usar la misma CTE en múltiples partes de la consulta.
3. **Eficiencia:** Aunque depende del motor de base de datos, muchas implementaciones optimizan las CTEs para evitar recalcular resultados.

---

## Materializaciones en DBT

En **dbt**, las **materializaciones** son la forma en que los datos transformados son representados físicamente en el **Data Warehouse**. Estas definen cómo se ejecuta y almacena un modelo en el sistema, adaptándose a necesidades específicas de rendimiento, costo o funcionalidad.

### **Tipos de materialización en dbt**

1. **`view` (Vista):**

   - **Descripción:** Es la materialización por defecto. El modelo se define como una vista en SQL y no almacena datos físicamente, sino que ejecuta la consulta cada vez que se accede.
   - **Ventajas:**
     - Ligera y económica (sin almacenamiento adicional).
     - Útil para transformaciones simples y datos que cambian frecuentemente.
   - **Desventajas:**
     - Más lenta en consultas complejas o con grandes volúmenes de datos, ya que siempre ejecuta la consulta en tiempo real.
   - **Casos de uso:**
     - Cuando se necesitan transformaciones ligeras que no justifiquen almacenamiento físico.
   - **Configuración en dbt:**

     ```sql
     {{ config(materialized='view') }}
     ```

2. **`table` (Tabla):**

   - **Descripción:** Al elegir esta materialización, el modelo crea una tabla física que almacena los resultados de la consulta en el Data Warehouse.
   - **Ventajas:**
     - Consultas más rápidas, ya que los datos ya están almacenados.
     - Ideal para transformaciones costosas que no cambian frecuentemente.
   - **Desventajas:**
     - Requiere almacenamiento adicional y recrea la tabla completa en cada ejecución.
   - **Casos de uso:**
     - Cuando se necesita un rendimiento rápido para transformaciones complejas y estáticas.
   - **Configuración en dbt:**

     ```sql
     {{ config(materialized='table') }}
     ```

3. **`incremental` (Tabla incremental):**

   - **Descripción:** Carga solo nuevos o modificados registros en cada ejecución, en lugar de recrear toda la tabla.
   - **Ventajas:**
     - Reduce costos de computación y tiempo de ejecución al procesar únicamente los cambios.
     - Ideal para grandes volúmenes de datos.
   - **Desventajas:**
     - Requiere lógica adicional para manejar los registros incrementales.
   - **Casos de uso:**
     - Procesos que manejan datos en constante crecimiento, como logs, eventos, o datos históricos.
   - **Configuración en dbt:**

     ```sql
     {{ config(materialized='incremental') }}

     -- Lógica para manejar registros incrementales
     {% if is_incremental() %}
         SELECT * FROM mi_tabla_fuente
         WHERE updated_at > (SELECT MAX(updated_at) FROM {{ this }})
     {% else %}
         SELECT * FROM mi_tabla_fuente
     {% endif %}
     ```

4. **`ephemeral` (Efímero):**

   - **Descripción:** No se materializa físicamente en el Data Warehouse. Se convierte en una **CTE** (Common Table Expression) temporal que se utiliza directamente en otros modelos.
   - **Ventajas:**
     - Evita la creación de objetos adicionales en el Data Warehouse.
     - Útil para pasos intermedios o lógicas compartidas entre modelos.
   - **Desventajas:**
     - No puede ser reutilizada en múltiples ejecuciones, ya que es temporal.
   - **Casos de uso:**
     - Transformaciones intermedias que solo se necesitan para otros modelos.
   - **Configuración en dbt:**

     ```sql
     {{ config(materialized='ephemeral') }}
     ```

---

### **Comparativa entre materializaciones**

| **Materialización** | **Almacenamiento físico** | **Velocidad de consulta** | **Costo** | **Casos ideales**                                           |
| ------------------- | ------------------------- | ------------------------- | --------- | ----------------------------------------------------------- |
| **`view`**          | No                        | Lenta                     | Bajo      | Transformaciones ligeras y datos frecuentemente cambiantes. |
| **`table`**         | Sí                        | Rápida                    | Moderado  | Datos estáticos o transformaciones costosas.                |
| **`incremental`**   | Sí                        | Rápida                    | Bajo      | Grandes volúmenes de datos en constante crecimiento.        |
| **`ephemeral`**     | No                        | Depende del modelo final  | Bajo      | Lógicas intermedias o reutilizables.                        |

---

### **¿Cómo elegir una materialización en dbt?**

1. **Si buscas simplicidad y bajo costo:** Usa `view`.
2. **Si necesitas rendimiento y consultas rápidas:** Usa `table`.
3. **Si trabajas con grandes volúmenes de datos crecientes:** Usa `incremental`.
4. **Si necesitas pasos intermedios o cálculos temporales:** Usa `ephemeral`.

## Sources y seeds

Seeds son archivos locales que uno sube al warehouse desde dbt, sources o fuentes es una capa de abstracción en el tope de las tablas de entrada.

## Freshness

En dbt, **freshness** se refiere al concepto de asegurarse de que los datos que se están utilizando en un modelo o conjunto de modelos están actualizados y no son obsoletos. Es una medida de la "frescura" de los datos, es decir, cuánto tiempo ha pasado desde la última vez que los datos fueron actualizados o procesados.

La **frescura de los datos** es importante porque, en muchas aplicaciones, se necesita garantizar que los análisis, informes y dashboards se basen en datos actualizados. Si los datos no están frescos, puede haber inconsistencias o decisiones erróneas basadas en información desactualizada.

### ¿Cómo funciona en dbt?

En dbt, la frescura de los datos se gestiona principalmente a través de la funcionalidad de **"sources"** (fuentes de datos) y se configura con una validación de frescura (freshness check). Puedes establecer un límite de tiempo máximo aceptable para la "frescura" de tus datos en función de tus necesidades de negocio.

#### ¿Cómo se configura la frescura en dbt?

1. **Configurar la fuente de datos:**
   Para controlar la frescura de los datos, primero debes declarar tus **fuentes** en dbt. Esto se hace en el archivo `sources.yml`. Una vez que has definido tus fuentes, puedes agregarles un control de frescura.

   ```yaml
   sources:
     - name: my_source
       tables:
         - name: my_table
           freshness:
             warn_after: { seconds: 3600 } # advertencia si no se actualiza en 1 hora
             error_after: { seconds: 7200 } # error si no se actualiza en 2 horas
   ```

   En este ejemplo:

   - `warn_after`: Establece un umbral de tiempo (en segundos) después del cual dbt generará una advertencia si los datos no se han actualizado dentro de ese período. En el ejemplo es de **1 hora (3600 segundos)**.
   - `error_after`: Establece un umbral de tiempo (en segundos) después del cual dbt marcará el estado de los datos como un error si no se actualizan dentro de ese período. En el ejemplo es de **2 horas (7200 segundos)**.

2. **Comprobación de frescura durante el `dbt run`:**
   Cuando ejecutas un `dbt run`, dbt verificará la frescura de los datos de acuerdo con las configuraciones que hayas establecido en los archivos `sources.yml`. Si la frescura de los datos no cumple con los límites configurados (es decir, si los datos no se han actualizado en el tiempo establecido), dbt te mostrará una advertencia o error en la ejecución.

3. **Monitoreo y alertas:**
   La función de frescura puede ser útil en los pipelines de ETL donde los datos deben estar siempre actualizados. Si los datos no se actualizan a tiempo, las alertas pueden ser utilizadas para que el equipo de datos tome las medidas adecuadas.

### ¿Por qué es importante?

- **Garantiza decisiones basadas en datos actuales:** Cuando estás construyendo informes, dashboards o modelos analíticos, es crucial que los datos sean recientes para no basar decisiones en información que ya esté desactualizada.
- **Detecta problemas tempranos en los pipelines de datos:** Si los datos no se actualizan a tiempo, la validación de frescura te permitirá identificar problemas en tu pipeline de datos, como fallos en la actualización de la base de datos, en los procesos de ETL, o en las conexiones con las fuentes de datos.

- **Mejora la calidad de los datos:** Asegurarse de que los datos sean frescos es parte de mantener un control de calidad adecuado sobre los mismos, ya que evita depender de información que pueda estar obsoleta.

### ¿Cómo se usa en la práctica?

- Si tienes una fuente de datos que se actualiza a diario, puedes configurar la frescura para que te avise si la actualización no ocurre dentro de ese plazo. Esto te ayuda a mantener una alta disponibilidad y confiabilidad de los datos que están siendo procesados.
- Si trabajas con datos en tiempo real o con datos muy sensibles a la latencia (por ejemplo, datos de transacciones o de actividad de usuarios), la frescura se convierte en un factor aún más crítico.

En resumen, la **frescura** en dbt es una forma de garantizar que los datos que estás utilizando estén actualizados y, en caso de no ser así, recibir una advertencia o error para tomar las medidas adecuadas. Es una funcionalidad muy útil para mantener la calidad y fiabilidad de los datos dentro de tus pipelines de datos.

## **Snapshots en dbt**

Los **snapshots** en **dbt** permiten realizar un seguimiento de los cambios históricos en los datos. Esto es útil cuando necesitas capturar la evolución de los registros en el tiempo, creando una versión histórica de los datos.

### **Características de los snapshots**

1. **Ubicación:** Los snapshots se encuentran en el directorio **`snapshots/`** dentro de tu proyecto dbt.
2. **Estrategias:**
   - **Por timestamp (`timestamp`):**
     - Usa una clave única y un campo de **`updated_at`** para detectar cambios en los datos.
     - Solo registra cambios cuando el valor de **`updated_at`** se modifica.
   - **Por cambios (`check`):**
     - Compara un conjunto de columnas especificadas.
     - Registra un cambio si cualquier columna en el conjunto difiere entre versiones consecutivas.

### **Ejemplo de configuración de snapshot**

```sql
{% snapshot my_snapshot %}

{{ config(
    target_schema='snapshots',
    unique_key='id',
    strategy='timestamp', -- O 'check'
    updated_at='updated_at'
) }}

SELECT
    id,
    name,
    status,
    updated_at
FROM
    source('my_source', 'my_table')

{% endsnapshot %}
```

### **Casos de uso de snapshots**

- Rastrear historiales de registros de clientes o productos.
- Analizar cambios en estados o configuraciones a lo largo del tiempo.
- Construir sistemas de auditoría.

---

## **Tests en dbt**

Los tests en dbt permiten validar la calidad y consistencia de los datos, asegurando que cumplen con las reglas y expectativas del negocio.

### **Tipos de tests**

1. **Tests singulares (`singular`):**

   - Son consultas **SQL personalizadas** que validan condiciones específicas.
   - Esperan un conjunto de resultados vacío para indicar que la prueba se ha pasado correctamente.
   - **Ejemplo:**

     ```sql
     -- tests/custom_test.sql
     SELECT *
     FROM {{ ref('my_table') }}
     WHERE created_at > updated_at
     ```

2. **Tests genéricos (`generic`):**

   - Validan **restricciones comunes** como valores únicos, no nulos, aceptables o relaciones entre tablas.
   - Se configuran directamente en el archivo **`schema.yml`** del modelo.
   - **Tipos de validaciones comunes:**
     - **`unique`:** Garantiza que los valores sean únicos.
     - **`not_null`:** Asegura que no haya valores nulos.
     - **`accepted_values`:** Valida que los valores estén dentro de un conjunto permitido.
     - **`relationships`:** Comprueba la integridad referencial entre tablas.
   - **Ejemplo de configuración:**

     ```yaml
     version: 2

     models:
       - name: my_table
         columns:
           - name: id
             tests:
               - unique
               - not_null
           - name: status
             tests:
               - accepted_values:
                   values: ["active", "inactive", "pending"]
           - name: customer_id
             tests:
               - relationships:
                   to: ref('customers')
                   field: id
     ```

### **Comparativa entre tests**

| **Tipo**     | **Descripción**                                  | **Casos de uso**                             |
| ------------ | ------------------------------------------------ | -------------------------------------------- |
| **Singular** | Pruebas específicas con SQL personalizado.       | Validaciones únicas o condiciones complejas. |
| **Genérico** | Pruebas predefinidas para restricciones comunes. | Validar calidad general y reglas básicas.    |

---

## **Macros en dbt**

Las macros en **dbt** son **plantillas de código Jinja** que permiten **reutilizar lógica** o crear bloques de código dinámicos dentro de los modelos, tests, snapshots y más. Son especialmente útiles para evitar duplicación de código y mantener un proyecto dbt modular y eficiente.

---

### **¿Qué son las macros?**

- Son funciones personalizadas escritas en Jinja que puedes definir y reutilizar en múltiples partes de tu proyecto dbt.
- Se almacenan en el directorio **`macros/`** dentro de tu proyecto.
- dbt incluye un conjunto de macros integradas listas para usar.

---

### **Usos comunes de las macros**

1. **Lógica reutilizable:** Crear transformaciones o cálculos que se repiten en diferentes modelos.
2. **Automatización:** Generar dinámicamente consultas SQL o configuraciones de dbt.
3. **Custom Tests:** Crear **tests genéricos** personalizados para validar reglas de negocio específicas.
4. **Integración externa:** Importar librerías externas para ampliar la funcionalidad.

---

### **Ejemplo básico de macro**

**Definición de una macro:**

```jinja
-- macros/my_macros.sql
{% macro calculate_discount(price, discount_rate) %}
    {{ price }} * (1 - {{ discount_rate }})
{% endmacro %}
```

**Uso en un modelo:**

```sql
SELECT
    id,
    price,
    {{ calculate_discount('price', '0.2') }} AS discounted_price
FROM {{ ref('products') }}
```

---

### **Macros integradas en dbt**

dbt proporciona macros listas para usar, por ejemplo:

- **`ref`**: Para referenciar modelos.
- **`source`**: Para referenciar fuentes de datos.
- **`generate_schema_name`**: Para definir el esquema donde se almacenarán los modelos.
- **`run_query`**: Para ejecutar consultas SQL dinámicamente.
- **`log`**: Para imprimir mensajes en los registros de ejecución.

Ejemplo:

```jinja
{% set row_count = run_query('SELECT COUNT(*) FROM {{ ref('my_table') }}').table.rows[0][0] %}
{{ log('El número de filas es: ' ~ row_count, info=True) }}
```

---

### **Macros para tests genéricos**

Puedes crear macros para **tests personalizados** que se ejecuten en columnas o modelos.

**Definición de un test genérico:**

```jinja
-- macros/tests/is_positive.sql
{% macro test_is_positive(model, column_name) %}
SELECT *
FROM {{ model }}
WHERE {{ column_name }} < 0
{% endmacro %}
```

**Uso en `schema.yml`:**

```yaml
version: 2

models:
  - name: sales
    columns:
      - name: revenue
        tests:
          - is_positive
```

---

### **Importar macros de paquetes externos**

Puedes usar paquetes como **`dbt-utils`**, que incluyen macros predefinidas. Para importar:

1. Añade el paquete al archivo **`packages.yml`**:

   ```yaml
   packages:
     - package: dbt-labs/dbt_utils
       version: 0.9.6
   ```

2. Usa las macros del paquete:

   ```sql
   SELECT
       {{ dbt_utils.surrogate_key(['id', 'created_at']) }} AS unique_key
   FROM {{ ref('users') }}
   ```

---

### **Beneficios de las macros**

- **Reusabilidad:** Menos duplicación de código en el proyecto.
- **Flexibilidad:** Dinamismo para manejar múltiples configuraciones o escenarios.
- **Escalabilidad:** Facilita el mantenimiento al centralizar lógica repetida.
