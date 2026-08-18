# Ventajas y desventajas: on-premises vs. en la nube

> Curso: Data Warehouse - The Ultimate Guide (Udemy)

Continuando de [`1-on-premises-vs-cloud.md`](1-on-premises-vs-cloud.md), esta clase analiza en
detalle las ventajas y los retos (`challenges`) de cada enfoque, para poder responder a cuál es la
mejor opción para una empresa.

## Data Warehouse on-premises

### Ventajas

- **Control total**: la empresa posee toda la infraestructura de datos, puede decidir añadir
  recursos adicionales y cómo gestionarlos.
- **Cumplimiento normativo (percibido) más sencillo**: al controlar toda la infraestructura, suele
  ser más fácil (o las empresas creen que lo es, por costumbre) cumplir normativas de gobierno de
  datos o de `compliance` — por ejemplo, saben exactamente dónde están almacenados los datos.

> ⚠️ En la nube también es posible cumplir la mayoría de estas normativas; la percepción de que
> on-premises es más sencillo en este punto suele deberse más a la costumbre que a una limitación
> real de la nube.

### Desventajas

El control total tiene como contrapartida la **responsabilidad total**: la empresa es responsable
de que el `Data Warehouse` esté disponible, sea seguro y se mantenga actualizado.

- **Costes más altos**: incluye tanto costes iniciales (compra de infraestructura) como costes de
  mantenimiento continuo (actualizaciones, administración, personal dedicado a gestionarlo).
- **Infraestructura con vida útil limitada**: el hardware no puede usarse para siempre — si algo se
  rompe o surge una nueva tecnología necesaria, hay que adquirir nueva infraestructura.
- **Poca flexibilidad**: si la carga de trabajo aumenta, hay que comprar más infraestructura; si
  disminuye de repente, no es fácil "vender" el hardware sobrante. La capacidad queda fija en ambos
  sentidos.

## Data Warehouse en la nube

### Ventajas

- **Totalmente gestionado**: se delega la responsabilidad de la infraestructura al proveedor de la
  nube, a cambio de un poco menos de control directo.
- **Escalable**: si la empresa (y su carga de trabajo) crece, se pueden añadir suscripciones o
  recursos adicionales fácilmente — en algunos casos, incluso de forma automática, aplicando más
  recursos cuando la carga de trabajo aumenta y así manteniendo un rendimiento constante.
- **Más rentable**: los proveedores de la nube operan a una escala tan grande que logran una
  rentabilidad que los almacenes de datos on-premises normalmente no pueden igualar.
- **Seguridad gestionada**: generalmente la seguridad es mejor que en un `Data Warehouse`
  on-premises, ya que la gestiona el propio proveedor.
- **Fiabilidad**: los proveedores de la nube ofrecen acuerdos de nivel de servicio (`SLA`,
  `Service Level Agreement`) con tiempos de actividad garantizados, típicamente 99.9% o 99.99%.
- **Rapidez / time to market**: no hace falta pedir, instalar ni configurar hardware nuevo — los
  recursos están disponibles de inmediato, incluso para empresas pequeñas, permitiendo empezar a
  trabajar de inmediato.

### Desventajas

- **Menos control**: al delegar la infraestructura al proveedor, se pierde parte del control directo
  que sí se tiene on-premises.
- **Normativa más compleja en casos especiales**: si existen necesidades regulatorias muy
  específicas, cumplirlas en la nube puede ser algo más difícil — aunque, en general, suele haber
  soluciones disponibles para ello.

## Comparativa resumida

| Aspecto                | On-premises                                | En la nube                                                            |
| ---------------------- | ------------------------------------------ | --------------------------------------------------------------------- |
| Control                | Total                                      | Parcial (delegado al proveedor)                                       |
| Responsabilidad        | Total (empresa)                            | Compartida (proveedor gestiona infraestructura)                       |
| Costes                 | Altos (iniciales + mantenimiento)          | Generalmente más bajos (pago por uso, economías de escala)            |
| Escalabilidad          | Limitada, poco flexible                    | Alta, en ocasiones automática                                         |
| Seguridad              | Responsabilidad propia                     | Gestionada por el proveedor, normalmente mejor                        |
| Fiabilidad             | Depende de la empresa                      | `SLA` con uptime garantizado (99.9%–99.99%)                           |
| Time to market         | Lento (requiere comprar/instalar hardware) | Rápido (recursos disponibles de inmediato)                            |
| Cumplimiento normativo | Percibido como más sencillo                | Posible en la mayoría de casos; más complejo en casos muy específicos |

## Conclusión

Hoy en día, la mayoría de las empresas utilizan `Data Warehouses` en la nube, debido a que suelen
ser más rentables, más fiables, más seguros y más escalables que las alternativas on-premises. En la
mayoría de los casos, la nube es la mejor opción.

Además, los `Data Warehouses` en la nube suelen apoyarse en tecnologías más modernas, como el
almacenamiento en columnas (`columnar storage`) y el `Massive Parallel Processing` (`MPP`).

## Próximas clases

Profundizar en estas tecnologías modernas — `columnar storage` y `Massive Parallel Processing`
(`MPP`) — que usan los `Data Warehouses` en la nube.
