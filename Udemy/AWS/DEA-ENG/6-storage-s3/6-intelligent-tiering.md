# S3 Intelligent-Tiering en detalle

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Profundiza en la clase [[3-storage-classes|S3 Intelligent-Tiering]] vista antes: cómo funciona su
movimiento automático entre niveles y cómo configurar los niveles de archivo opcionales.

## Movimiento automático entre niveles

Es la característica central de esta clase: los datos se mueven automáticamente entre niveles de
acceso **sin intervención manual**, en función del uso real que se hace de cada objeto.

- Es un **muy buen valor por defecto** cuando el patrón de acceso a los datos **no es predecible** o
  **cambia con el tiempo** — todo esto se gestiona automáticamente a cambio de un coste de
  monitorización modesto.
- Niveles automáticos (activos por defecto, sin configuración adicional):

  | Nivel                      | Condición                               | Nota                            |
  | -------------------------- | --------------------------------------- | ------------------------------- |
  | **Frequent Access**        | Nivel inicial de cualquier objeto nuevo | —                               |
  | **Infrequent Access**      | 30 días consecutivos sin acceso         | —                               |
  | **Archive Instant Access** | 90 días consecutivos sin acceso         | Sigue siendo acceso instantáneo |

> ⚠️ El movimiento entre estos niveles automáticos es **bidireccional**: si un objeto que ya pasó a
> Infrequent Access (o Archive Instant Access) vuelve a consultarse, automáticamente se traslada de
> nuevo a Frequent Access. Esto es justo lo que lo diferencia de una Lifecycle Rule (ver más abajo).

## Niveles de archivo opcionales (configuración manual)

A diferencia de los tres niveles automáticos anteriores, los niveles de **archivo asíncrono** no están
activos por defecto — hay que habilitarlos explícitamente desde las **propiedades del bucket** →
**Intelligent-Tiering Configuration** (Archive Configuration).

Al crear una configuración de este tipo (por ejemplo, llamada `prueba`) se define:

- **Ámbito (scope)**: aplicar a todos los objetos del bucket, o filtrar por **prefijo** (ruta de
  carpeta) o por **etiquetas**.
- **Archive Access tier**: tras un número de días configurable sin acceso (ej. 180 días en este
  ejemplo), el objeto pasa a este nivel. Es aproximadamente **10% más barato** que Archive Instant
  Access, pero la recuperación deja de ser instantánea: pasa a ser **asíncrona**, de minutos a horas.
- **Deep Archive Access tier**: tras otro periodo adicional sin acceso (ej. otros 180 días más en este
  ejemplo), el objeto pasa a este nivel, todavía más barato. La recuperación puede tardar **hasta 12
  horas**.

> Los números de días concretos (180 + 180) son solo el ejemplo mostrado en la demo — lo importante
> para el examen es el concepto (dos niveles de archivo opcionales, cada vez más baratos y más lentos
> de recuperar), no memorizar cifras exactas.

## Diferencia entre S3 Intelligent-Tiering y las Lifecycle Rules

Ambos mecanismos automatizan cambios de clase de almacenamiento, pero **no son lo mismo** y resuelven
problemas distintos:

|                                                      | S3 Intelligent-Tiering                                                                     | [[4-lifecycle-rules\|Lifecycle Rules]]                                                                                    |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| **Qué dispara el cambio**                            | El **acceso real** a cada objeto (monitorización continua)                                 | El **tiempo transcurrido** desde la carga del objeto (antigüedad fija)                                                    |
| **Dirección**                                        | **Bidireccional** — un objeto vuelve automáticamente a Frequent Access si se vuelve a usar | **Unidireccional** — una vez transicionado por la regla, no vuelve atrás aunque se vuelva a acceder                       |
| **Necesita conocer el patrón de acceso de antemano** | No — pensado justo para cuando **no se sabe** o **cambia**                                 | Sí — se definen los días exactos porque el ciclo de vida **es predecible**                                                |
| **Coste de automatización**                          | Pequeño **coste de monitorización** por objeto, continuo                                   | **Coste de solicitud único** por objeto, solo cuando se ejecuta una transición                                            |
| **Alcance**                                          | Es en sí misma una clase de almacenamiento con niveles internos                            | Mecanismo más general: puede mover objetos entre **cualquier** clase de almacenamiento y también **expirarlos/borrarlos** |

En la práctica, ambos se pueden **combinar**: por ejemplo, usar una Lifecycle Rule para mover un objeto
a Intelligent-Tiering justo al subirlo (día 0), dejar que Intelligent-Tiering gestione automáticamente
el resto del ciclo de vida activo, y usar esa misma Lifecycle Rule para expirar (borrar) el objeto
tras un plazo largo predecible (ej. tres años) cuando ya se sabe que no hace falta conservarlo más.
