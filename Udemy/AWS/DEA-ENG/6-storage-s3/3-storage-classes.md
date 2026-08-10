# Clases de almacenamiento de S3

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Por qué importan las clases de almacenamiento

Cuando se ingieren datos, normalmente se empieza guardándolos en la clase de almacenamiento
**estándar** de S3: en esta etapa inicial se suele necesitar acceso frecuente, alta disponibilidad y
buen rendimiento.

Con el tiempo, esos mismos datos suelen seguir un ciclo de vida:

1. Se accede a ellos con menos frecuencia → conviene mover a una clase de **acceso infrecuente**.
2. Eventualmente casi no se accede a ellos, pero hay que conservarlos por **cumplimiento normativo** →
   conviene mover a un **archivo a largo plazo**.
3. En algún punto pueden llegar a **borrarse**.

Todo esto se gestiona combinando las distintas **clases de almacenamiento** (este apunte) con
**Lifecycle Rules** que transicionan los datos automáticamente en función de su antigüedad (se ve en
el siguiente apunte).

## S3 Standard

La forma **por defecto** de almacenar datos a los que se accede con frecuencia:

- Latencia muy baja.
- Alta disponibilidad.
- Apropiada para el caso de uso general cuando se necesita acceso frecuente a los datos.

## S3 Intelligent-Tiering

Estrictamente no es solo una clase de almacenamiento, sino una **opción de nivelación automática**:
mueve los datos entre distintos niveles de acceso en función de su patrón de uso real, sin
intervención manual.

Es especialmente útil cuando **no se sabe de antemano** cuál va a ser el patrón de acceso, o cuando
ese patrón **cambia con el tiempo** — a cambio de un pequeño coste de monitorización, puede ser mucho
más rentable que mantener los datos en una única clase fija.

Niveles automáticos (activos por defecto):

| Nivel                      | Condición para pasar a este nivel | Tipo de acceso |
| -------------------------- | --------------------------------- | -------------- |
| **Frequent Access**        | Nivel inicial                     | Instantáneo    |
| **Infrequent Access**      | 30 días consecutivos sin acceso   | Instantáneo    |
| **Archive Instant Access** | 90 días consecutivos sin acceso   | Instantáneo    |

Niveles opcionales de archivo asíncrono (hay que activarlos explícitamente):

| Nivel                   | Tipo de acceso                                                                                    |
| ----------------------- | ------------------------------------------------------------------------------------------------- |
| **Archive Access**      | Asíncrono — hay que **restaurar** los datos antes de poder usarlos (puede tardar un par de horas) |
| **Deep Archive Access** | Asíncrono, incluso más lento/barato que el anterior                                               |

## S3 Express One Zone

Clase de **alto rendimiento**, pero de **una única zona de disponibilidad**.

- Diseñada para latencias consistentes de **milisegundos de un solo dígito**, para los datos con
  acceso más frecuente y aplicaciones muy sensibles a la latencia.
- Hasta **10 veces más rápida** en acceso y hasta **50% menos coste por solicitud** frente a S3
  Standard.
- Contrapartida: al estar en una sola zona de disponibilidad, los datos son algo **menos disponibles y
  duraderos** que en las clases multi-AZ.
- Los datos se almacenan en un tipo de bucket distinto: un **Amazon S3 directory bucket**, que soporta
  cientos de miles de solicitudes por segundo.

## S3 Standard-IA (Infrequent Access)

Pensada para datos a los que se accede **con menos frecuencia**, pero que aun así necesitan
**acceso rápido** (milisegundos) cuando se necesitan.

- **Coste de almacenamiento más bajo** que Standard.
- **Coste de acceso/recuperación más alto** — el ahorro solo compensa si de verdad se accede poco.
- Buen caso de uso: datos de larga duración que se consultan poco, pero que cuando se consultan deben
  responder rápido.

## S3 One Zone-IA

Misma idea que Standard-IA, pero en una **única zona de disponibilidad**.

- Menor disponibilidad que la variante multi-AZ.
- Recomendado solo para datos **recreables** o de los que ya existe otra copia en otro sitio (por
  ejemplo, una copia de seguridad secundaria) — al estar en una sola AZ, no conviene que sea la única
  copia existente de esos datos.

## Clases Glacier (archivo)

Pensadas para archivado a largo plazo. Hay tres variantes, que se diferencian sobre todo en **con qué
frecuencia se espera acceder a los datos** y en **cuánto tarda la recuperación**.

| Clase                          | Velocidad de recuperación                        | Frecuencia de acceso típica | Caso de uso                                                                    |
| ------------------------------ | ------------------------------------------------ | --------------------------- | ------------------------------------------------------------------------------ |
| **Glacier Instant Retrieval**  | Instantánea (milisegundos)                       | ~1 vez por trimestre        | Archivo al que se necesita acceso inmediato                                    |
| **Glacier Flexible Retrieval** | Asíncrona: de 1 minuto a 12 horas (configurable) | ~1-2 veces al año           | Copias de seguridad a largo plazo con necesidad ocasional de restaurar         |
| **Glacier Deep Archive**       | Asíncrona: hasta 12 horas                        | ~1-2 veces al año           | El almacenamiento más barato; adecuado cuando casi nunca se accede a los datos |

> ⚠️ A más velocidad/disponibilidad de recuperación, mayor coste de almacenamiento — y viceversa:
> **Deep Archive** es la clase más barata para almacenar, pero la más cara/lenta de recuperar.

## Resumen

**Clases "no Glacier":**

- **S3 Standard** — acceso frecuente, caso de uso general.
- **S3 Standard-IA** — acceso infrecuente pero de larga duración, con necesidad de respuesta en
  milisegundos.
- **S3 One Zone-IA** — variante de Standard-IA en una sola AZ, para datos recreables.
- **S3 Intelligent-Tiering** — transición automática entre niveles para patrones de acceso
  desconocidos o cambiantes.
- **S3 Express One Zone** — clase más reciente; almacenamiento de altísimo rendimiento para los datos
  de acceso más frecuente, en una sola AZ.

**Clases Glacier (archivo):**

- **Glacier Instant Retrieval** — acceso instantáneo, para datos consultados aprox. una vez al
  trimestre.
- **Glacier Flexible Retrieval** — restauración de 1 minuto a 12 horas, para datos consultados 1-2
  veces al año.
- **Glacier Deep Archive** — restauración de hasta 12 horas, la opción más económica, para archivado a
  muy largo plazo.

> ⚠️ No hace falta memorizar los precios exactos de cada clase (varían además según la región) — lo
> importante para el examen es identificar el **caso de uso correcto** de cada una.
