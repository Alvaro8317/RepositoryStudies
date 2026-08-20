# Redshift: almacenamiento gestionado y tipos de nodo

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

## Almacenamiento gestionado (Redshift Managed Storage)

El **almacenamiento gestionado** solo puede usarse con un tipo de nodo específico (**RA3**, ver más
abajo) y combina dos componentes:

- **Almacenamiento local**: unidades **SSD de alto rendimiento**.
- **Amazon S3**: usado para **almacenamiento a más largo plazo**.

### Funcionamiento por temperatura de los datos

- Si un nodo crece **más allá del tamaño del SSD local**, los datos se **descargan
  automáticamente a S3**.
- La decisión de dónde vive cada bloque de datos se basa en su **temperatura de acceso**:
  - **Datos calientes (hot data)** — bloques de uso frecuente: se almacenan en **caché local en el
    SSD**, para garantizar **alto rendimiento**.
  - **Datos fríos (cold data)** — bloques de uso poco frecuente: se almacenan en la **capa de
    almacenamiento gestionada**, respaldada por **S3**, lo que resulta **más barato**.

> ⚠️ El **precio pagado por los datos es siempre el mismo**, independientemente de si están en el
> SSD de alto rendimiento o en S3 — el movimiento entre capas es transparente para el usuario.

## Tipos de nodo: RA3 vs. DC2

Redshift ofrece dos tipos de nodo de computación: **RA3** y **DC2**.

### Nodos RA3

- Usan el **Redshift Managed Storage** (descrito arriba).
- **Cómputo y almacenamiento están desacoplados**: se puede escalar y pagar por cada uno de forma
  **totalmente independiente**.
  - Esto evita tener que aumentar la capacidad de cómputo solo porque ha crecido el volumen de
    datos, y resulta más eficiente en coste.
- Soportan **múltiples zonas de disponibilidad (Multi-AZ)**: los nodos del cluster pueden
  desplegarse en distintas AZ — algo que **no es posible con los nodos DC2**.

### Nodos DC2

- Pensados para cargas de trabajo de almacén de datos **más intensivas en cómputo**, con mejor
  rendimiento en ese sentido.
- El **almacenamiento SSD está incluido localmente en el nodo** (no desacoplado del cómputo), lo
  que asegura siempre un **alto rendimiento**.
- Solo están disponibles en **una única zona de disponibilidad** (Single-AZ) — no se pueden usar en
  un cluster Multi-AZ.
- Al no estar desacoplado el almacenamiento del cómputo, si crecen los datos hay que **añadir más
  nodos de computación** para aumentar tanto la capacidad de almacenamiento como la de cómputo.
- Se recomiendan únicamente para **conjuntos de datos por debajo de 1 TB** (considerando el
  almacenamiento **comprimido**).

## Resumen: RA3 vs. DC2

| Característica                    | RA3                                                                 | DC2                                                      |
| --------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------------- |
| **Almacenamiento**                | Redshift Managed Storage (SSD + S3)                                 | SSD local, incluido en el nodo                           |
| **Cómputo y almacenamiento**      | Desacoplados — escalan y se pagan por separado                      | Acoplados — crecen juntos                                |
| **Multi-AZ**                      | Sí                                                                  | No — solo Single-AZ                                      |
| **Escalado por más datos**        | Ajustar solo el almacenamiento gestionado                           | Añadir más nodos de computación                          |
| **Tamaño de dataset recomendado** | Sin límite práctico por el desacople                                | Por debajo de 1 TB (almacenamiento comprimido)           |
| **Mejor para**                    | Cargas de trabajo generales, con independencia coste/almacenamiento | Cargas de trabajo intensivas en cómputo, dataset pequeño |
