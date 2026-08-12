# Unidades de capacidad: WCU y RCU

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Propósito

En el modo de capacidad **Provisioned** hay que especificar explícitamente el rendimiento de lectura
y escritura mediante dos unidades: **WCU** (*Write Capacity Unit*) y **RCU** (*Read Capacity Unit*).
Entender cómo se calculan es importante tanto para dimensionar tablas en la práctica como para el
examen.

## Write Capacity Unit (WCU)

Representa la cantidad de escritura que se puede realizar por segundo en DynamoDB.

- **1 WCU = 1 escritura por segundo** para elementos de hasta **1 KB** de tamaño.
- Si el elemento es más pequeño de 1 KB (por ejemplo, 0.8 KB), sigue consumiendo **1 WCU** — no hay
  fracciones, siempre se redondea hacia arriba.
- Si el elemento es más grande, se multiplica proporcionalmente y se redondea al entero superior:
  - 3 KB → 3 WCU
  - 3.5 KB → 4 WCU (redondeo hacia arriba)

En el modo Provisioned hay que asignar el número de WCU en función de la carga de escritura
esperada. Es habitual sobreaprovisionar un poco para poder absorber picos inesperados sin sufrir
throttling, o bien usar **Auto Scaling** para ganar flexibilidad (ver
[12-capacity-modes.md](12-capacity-modes.md)).

> ⚠️ Se paga por el número de WCU aprovisionadas, se usen o no. Por tanto la planificación de
> capacidad impacta directamente en el coste: sobreaprovisionar sale más caro, pero
> infraaprovisionar provoca **throttling** — si las escrituras superan las WCU provisionadas,
> DynamoDB rechaza las solicitudes adicionales con `ProvisionedThroughputExceededException`.

Si el patrón de tráfico es difícil de predecir, suele ser mejor usar el modo **On-Demand** en lugar
de intentar afinar las WCU manualmente.

## Read Capacity Unit (RCU)

Es equivalente a la WCU pero para operaciones de lectura, con una unidad de medida distinta:

- **1 RCU = 1 lectura fuertemente consistente por segundo**, o **2 lecturas eventualmente
  consistentes por segundo**, para elementos de hasta **4 KB** de tamaño.
- Igual que con las WCU, para elementos más grandes se multiplica y se redondea al entero superior.

Las lecturas eventualmente consistentes cuestan la mitad porque ofrecen el doble de throughput (2
lecturas por RCU en vez de 1).

## Consistencia de lectura: eventual vs. fuerte

En una base de datos distribuida como DynamoDB, los datos se replican entre varias copias, y no
todas se actualizan en el mismo instante. La **consistencia de lectura** determina qué grado de
actualización garantiza una operación de lectura.

| Tipo                          | Garantía                                                                                                             | Rendimiento                                                                     | Coste                     |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------- |
| **Eventualmente consistente** | Puede devolver datos ligeramente obsoletos justo después de una escritura                                            | Mejor — admite más lecturas simultáneas                                         | Más barato (mitad de RCU) |
| **Fuertemente consistente**   | Devuelve siempre la versión más reciente, reflejando todas las escrituras que terminaron antes de iniciar la lectura | Menor — mayor latencia, debe esperar a que todas las copias estén sincronizadas | Más caro (doble de RCU)   |

- Usa lectura **eventualmente consistente** cuando esté bien tolerar unos segundos de retraso a
  cambio de mejor rendimiento y menor coste.
- Usa lectura **fuertemente consistente** para operaciones críticas donde siempre se necesita el
  dato más reciente.

## Cálculos de ejemplo

**Ejemplo 1 — lectura fuertemente consistente:**

Un elemento de **8 KB**, leído una vez por segundo, con lectura fuertemente consistente.

- 8 KB es el doble de 4 KB → se necesitan **2 RCU** para leer este elemento una vez por segundo.

**Ejemplo 2 — múltiples elementos con lectura eventualmente consistente:**

10 elementos de **3 KB** cada uno, cada uno leído una vez por segundo, con lectura eventualmente
consistente.

- Cada elemento (3 KB) cabe dentro del bloque de 4 KB → cuenta como 1 unidad de tamaño.
- Con lectura fuertemente consistente se necesitarían 10 RCU (una por elemento y segundo).
- Como cada RCU permite 2 lecturas eventualmente consistentes, solo se necesitan **5 RCU** para
  cubrir las 10 lecturas por segundo.

> ⚠️ El redondeo se aplica primero al tamaño del elemento contra el bloque correspondiente (1 KB
> para WCU, 4 KB para RCU) y después se multiplica por el número de operaciones por segundo.

## Próxima clase

Con WCU, RCU y el throttling ya entendidos, la siguiente clase cubre las mejores prácticas y
mecanismos disponibles en DynamoDB para mejorar el rendimiento y evitar el throttling.
