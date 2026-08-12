# Práctica: configurar TTL

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Práctica guiada en la consola configurando [[17-ttl|TTL]] sobre una tabla de libros, para eliminar
automáticamente elementos en función de un atributo de fecha de caducidad.

## Por qué usar TTL

Además de ahorrar costes de almacenamiento, limpiar automáticamente elementos obsoletos con TTL
también **mejora el rendimiento y el coste de lecturas/escrituras**: con menos datos en la tabla, hay
menos datos que escanear en cada operación de Scan.

## Preparar el atributo de expiración en los elementos

- En cada elemento de la tabla se necesita un atributo numérico con la marca de tiempo de expiración
  en formato **Unix epoch** (usar un conversor de fecha a epoch si hace falta).
- Al crear un elemento nuevo, se añade este atributo como tipo **Number**, con el valor epoch
  correspondiente al momento en que debe expirar.

> ⚠️ Si un elemento **no tiene** este atributo, TTL nunca lo eliminará — solo se evalúan los
> elementos que tienen el atributo configurado presente.

## Activar TTL en la tabla

- En los detalles de la tabla → **Additional settings** → sección **TTL** (aparece deshabilitado por
  defecto) → activar.
- Hay que especificar el **nombre exacto del atributo** que contiene el timestamp de expiración —
  debe coincidir carácter por carácter con el atributo usado en los elementos.

> ⚠️ Un error de nombre de atributo (ej. usar `expiration_date` cuando el atributo real en los
> elementos se llama `expired_date`) hace que TTL no identifique ningún elemento para eliminar, sin
> dar ningún error explícito — la vista previa simplemente no muestra resultados. Si la vista previa
> sale vacía inesperadamente, lo primero a revisar es que el nombre del atributo introducido
> coincida exactamente con el de los elementos de la tabla.

### Vista previa (Preview)

Antes de confirmar, la consola permite **simular un instante de tiempo** y ejecutar una vista previa
para comprobar qué elementos se eliminarían con la configuración actual — útil para validar que el
atributo y el formato son correctos antes de activar TTL de verdad.

## Comportamiento tras activarlo

- Los elementos cuya fecha de expiración (en el atributo configurado) ya haya pasado se ponen en cola
  para su eliminación automática.
- El borrado **no es inmediato**: puede tardar hasta **48 horas**, y cuanto más grande sea la tabla,
  más puede tardar en reflejarse.
- El proceso de borrado por TTL no consume capacidad de escritura provisionada — utiliza la
  [[16-hot-partitions#burst-capacity|Burst Capacity]] de la tabla, no las WCU aprovisionadas.
