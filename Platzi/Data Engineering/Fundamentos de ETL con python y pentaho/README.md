# Curso de fundamentos de ETL con Python y Pentaho

Un ETL es extraer, transformar y cargar, el proceso de ETL es simplemente esto, se extraen datos de una fuente, se transforman en base a mis necesidades y cargarlo para su respectivo uso. ETL es extraer datos de diferentes fuentes, transformarlos para que cumplan con requisitos de calidad y cargarlos a un repositorio centralizado. ¿Qué ventaja me da? Me da una vista unificada y coherente de los datos para tomar decisiones más precisas y asegura la calidad de los datos al limpiar y normalizar. Además, se pueden detectar anomalías en el proceso de ETL y así se le puede dar fuentes confiables para machine learning y data science.

¿Cómo se usa una ETL actualmente? Las soluciones en la nube ya tienen servicios que cubren estas necesidades, pero también existen herramientas como con python. Se puede recolectar los datos con python, se validan los datos con pandas y se llevan a una base de datos.

## Conceptos base de ETL

### Source

De donde voy a extraer los datos para trabajar, estos datos pueden tener diferentes estructuras

### Target

Donde voy a hacer un load de mi ETL, puede ser postgres, snowflake, s3, redshift, entre muchos otros repositorios de datos

### Staging

Es un área (podría denominarse en memoria), un área de paso donde se hacen las transformaciones para luego cargarlas, suele ser un espacio de memoria.

### Data warehouse

Un lugar donde uno tiene una bodega de datos, la gran mayoría puede ser Big query, snowflake o amazon redshift.

Una de las maneras de cargar todas estas fuentes es con el **modelo de estrella**, es una tabla con solo métricas relevantes a negocio y unas tablas alrededor llamadas dimensiones.

**Aquí se tiene una estructura definida luego de una limpieza, casi siempre es una BD**

### Data Lake

En este, casi siempre es un **file system**, un repositorio donde tendrá la data raw, se tienen los archivos en distintos formatos, de distintas fuentes, pero guardados en su formato original. Los datos se transforman después de pasar por el data lake. No cuenta con buen soporte para hacer analítica

### Data lakehouse

Es una combinación de los dos anteriores, warehouse que suele ser tipo SQL, data lake que es un filesystem con datos raw, finalmente nace data lakehouse, los datos se guardan en raw en filesystem con una capa de consulta como spark para hacer analítica sin transformarlos antes.

¿Cómo usar Data Lakehouse? Con un proceso de _ELT_, donde se extraen los datos, se cargan tal cuál como están en un data lakehouse y finalmente se transforman para su respectivo análisis. A diferencia de ETL que transforma antes de cargarlo.

## Consideraciones de ETL

1. Calidad de los datos, cuáles son las transformaciones que debo de aplicar, cuál es el estado más óptimo de mis datos, se debe de tener claro el source y el target.
2. Se debe de definir si mi proceso será en batch o en streaming, batch es una tarea recurrente como una expresión CRON, se puede ejecutar una tarea a final del día, por otro lado, los procesos de streaming que tiene que ser near real time, como industrias en las que se hace un análisis constante.
3. ¿Mi ETL será incremental o total? Una ETL total es que va a cargar desde 0 todos mis datos incluyendo históricos, una incremental es que traerá solo los datos nuevos, de última hora por ejemplo.
4. Documentación, un proceso de ETL puede ser muy complejo como no, el mantener un ETL puede ser una tarea bastante complicada por lo que se debe de mantener actualizados los datos.

## Servicios y herramientas

## Sources

Es importante asegurarse de que los datos estén en un formato compatible con la herramienta de ETL que se está utilizando, si están los datos normalizados, si están en SQL, NoSQL, etc. La calidad de los datos es importante verificar la integridad de estos datos, con frecuencia de actualización se debe determinar la frecuencia con la que los datos deben ser extraidos y actualizados.

Acccesibilidad es importante para que se pueda extraer y cargar en el sistema, para que mi sistema pueda obtener los datos.

Seguridad, se debe de asegurar que los datos están protegidos y que solo las personas autorizadas tengan acceso a esta.

Eficiencia, se debe buscar la manera más eficiente de extraer y cargar los datos, para evitar retrasos y errores.

Escalabilidad, se debe de tener en cuenta si la solución de ETL es escalable y si es posible manejar una cantidad creciente de datos en el futuro. ¿Qué tanto crecerán las fuentes de datos?

## Transformación

¿Con qué estructura requiero los datos compatibles con el target? ¿Cómo debo relacionar los datos de distintas fuentes? Si esto no se tiene claro, se tiene que hacer antes un análisis de los datos.

- Normalización es normalizar los datos para lograr consistencia a lo largo del flujo de datos. ¿Cómo se debería de relacionar los datos entre diferentes fuentes?
- Duplicados, con qué estructura requiero los datos compatibles con el target y qué hacer con los duplicados
- Datos faltantes, qué ocurre con los datos faltantes en mi data?
- Agregaciones, debo agrupar los datos por alguna característica y buscar agregaciones como suma, promedio, máximo y demás.
