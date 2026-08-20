# Redshift: Data Sharing

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

**Data Sharing** permite compartir datos que están en un clúster de Redshift con otros clústeres,
otras cuentas y otras regiones, **sin copiarlos**.

## El problema

Supongamos que tenemos datos en un clúster **productor** (ej. el clúster de producción) y
queremos dar acceso a un clúster **consumidor** — quizás en una región distinta, o simplemente un
departamento diferente que también necesita esos datos, y que debería pagar y aportar su propia
capacidad de cómputo para consultarlos.

En vez de copiar los datos hacia el consumidor, Data Sharing permite **compartirlos en vivo**
desde el clúster original:

- Los datos **no se mueven** — se quedan en el clúster/región/cuenta original.
- El consumidor obtiene **acceso a los datos**, pero usa **su propia capacidad de cómputo** para
  consultarlos.
- Como los datos siguen viviendo en el origen, cada consumidor ve siempre la información **más
  actualizada y consistente**.

Se puede compartir entre distintos **clústeres**, **workgroups** (Redshift Serverless), **cuentas
de AWS**, **regiones** y **zonas de disponibilidad** — sin necesidad de mover los datos.

## Cómo funciona: `datashare`

1. En el **clúster productor**, un administrador crea un **`datashare`**.
2. El administrador añade **objetos de base de datos** (tablas, vistas, funciones definidas por el
   usuario, etc.) al `datashare` para compartirlos con los consumidores.
3. Este recurso, visto desde el clúster productor, se conoce como el **outbound datashare**
   (recurso compartido de salida).
4. En el **clúster/grupo consumidor**, un administrador puede recibir los datos que se han
   compartido con ellos — este recurso, visto desde el lado del consumidor, se conoce como el
   **inbound datashare** (recurso compartido de entrada).
5. Cada `datashare` está siempre asociado a una **base de datos específica**, y contiene los
   objetos de esa base de datos que se decide compartir (tablas, vistas, funciones definidas por
   el usuario, etc.).

## Tipos de datashare

| Tipo | Descripción |
| --- | --- |
| **Standard datashare** | Permite compartir datos entre clústeres, cuentas, regiones, zonas de disponibilidad y workgroups serverless. |
| **AWS Data Exchange datashare** | Permite licenciar y compartir datos a través de **AWS Data Exchange**. AWS se encarga de la facturación y los pagos. Proveedores homologados añaden datashares a sus productos, dando acceso a los suscriptores. |
| **AWS Lake Formation–managed datashare** | Usa **AWS Lake Formation** para definir y aplicar de forma centralizada permisos de acceso a nivel de **tabla, columna y fila** sobre los datos compartidos — control granular gestionado desde Lake Formation. |

## Consideraciones de coste y rendimiento

- El **consumidor** paga por todo el **cómputo** que utiliza para consultar los datos compartidos,
  así como por la **transferencia de datos entre regiones** que sea necesaria.
- El **productor** paga por el **almacenamiento** de los datos.
- El **rendimiento** de las consultas depende de la **capacidad de cómputo del clúster
  consumidor**, ya que el cómputo se ejecuta ahí, no en el productor.

## Limitaciones

- Soportado en todos los tipos de clúster **RA3** aprovisionados, y también en **Redshift
  Serverless**.
- Para compartir entre **cuentas** o **regiones**, tanto el clúster/namespace productor como el
  consumidor **deben estar cifrados** — aunque **no** es necesario que usen la misma clave de
  cifrado.
- Solo se pueden compartir **funciones definidas por el usuario** que sean **SQL** — no se
  soportan funciones en **Python** ni **Lambda**.
- Redshift **no admite** añadir **esquemas o tablas externas** a un datashare.
- Los **consumidores no pueden añadir** más datos u objetos a un datashare que están consumiendo
  (solo pueden consultarlo).

> ⚠️ El productor cobra por almacenamiento, el consumidor por cómputo — al diseñar quién consulta
> qué datos compartidos, conviene tener en cuenta dónde recaerá el coste de cómputo.
