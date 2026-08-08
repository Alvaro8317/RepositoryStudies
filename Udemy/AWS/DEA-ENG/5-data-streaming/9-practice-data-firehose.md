# Práctica: Crear un Firehose Delivery Stream

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Práctica guiada: configurar un flujo de Amazon Data Firehose usando un Kinesis Data Stream existente
como origen y un bucket S3 como destino, y comprobar que los datos llegan correctamente.

## Precio

En la consola de **Amazon Data Firehose**, antes de crear el flujo se puede consultar la calculadora
de costes: el precio se basa en la cantidad de datos ingeridos, con varios niveles según volumen. Por
ejemplo, los primeros 500 TB al mes cuestan alrededor de **$0.03 por GB** (el precio exacto depende de
la región). Para pruebas manuales con pocos datos, el coste es mínimo.

## Configuración del delivery stream

La configuración de un flujo de Firehose es muy sencilla: solo hace falta elegir **origen**,
**destino** y, opcionalmente, algunas casillas de transformación.

### Origen (source)

Se elige **Amazon Kinesis Data Streams** como origen — la opción más común — reutilizando el stream ya
creado en una práctica anterior ([[8-data-firehose]]). De la lista disponible se selecciona ese stream
y queda añadido a la configuración.

### Destino (destination)

Entre los destinos disponibles están OpenSearch, Amazon Redshift, Amazon S3 y servicios adicionales
como Snowflake o Splunk. Para esta práctica se elige **Amazon S3**, seleccionando el bucket creado
previamente.

### Nombre del flujo

Se le da un nombre descriptivo al delivery stream (por ejemplo, algo como `KDS-prueba-S3-<números>`).

### Transformación de datos (no usada en esta práctica)

La consola ofrece checkboxes integrados para:

- **Transformar registros con AWS Lambda**.
- **Convertir el formato de los registros** (ej. a Parquet/ORC).
- **Descomprimir los registros de origen**.

Ninguna de estas opciones se activa en esta práctica — se explorarán en una clase posterior.

### Opciones adicionales de destino S3

- **Dynamic partitioning** — se puede activar directamente desde esta pantalla.
- **Prefijo** y **prefijo de salida de error** — opcionales, con soporte para incluir la zona horaria
  cuando se usa un prefijo con fecha/hora.

En esta práctica se dejan todos estos ajustes por defecto (sin prefijo, sin partición dinámica).

### Buffering

El tamaño y el intervalo del búfer se configuran aquí (ver también [[8-data-firehose]] para el
concepto general):

| Límite de buffer | Rango |
| ----------------- | ----- |
| Tamaño | 1 MB – 128 MB |
| Intervalo de tiempo | 0 – 900 segundos |

Se cumple el límite que se alcance primero, y en ese momento se agrupa y entrega el lote. Se dejan los
valores por defecto para esta práctica.

### Compresión y cifrado

- **Compresión de los registros** — se puede activar fácilmente desde esta misma pantalla.
- **Cifrado del lado del servidor (SSE)** — disponible, pero no se activa en esta práctica.

### Tags

Como en el resto de servicios de AWS, se pueden añadir etiquetas al recurso. No se usan en esta
práctica.

## Creación y verificación

Tras crear el flujo (tarda solo 1-2 segundos en aprovisionarse), la consola muestra:

- El estado de la configuración (origen, destino, transformaciones).
- Métricas de datos entrantes una vez el flujo está en producción (bytes leídos, etc.).

> ⚠️ La configuración del delivery stream se puede **editar después de creado** — por ejemplo, para
> añadir transformaciones adicionales más adelante.

### Prueba con datos de demostración

La consola permite enviar datos de demostración directamente para probar el flujo:

1. Iniciar el envío de datos de prueba y dejarlo correr unos segundos.
2. Detener el envío.
3. Navegar al bucket S3 configurado como destino.

Como no se activó ninguna partición ni prefijo, los objetos se añaden **directamente en la raíz del
bucket**, sin subcarpetas. Se puede descargar y abrir cualquiera de los archivos generados para
comprobar que los datos de demostración llegaron correctamente.

Con esto queda validada la funcionalidad básica del flujo; en una práctica posterior se añadirán
transformaciones y opciones adicionales.
