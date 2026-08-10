# Práctica: Crear una Lifecycle Rule en S3

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

Práctica guiada: configurar una [[4-lifecycle-rules|Lifecycle Rule]] en la consola para un caso de uso
típico — acceso muy frecuente los primeros días y transición progresiva a clases de almacenamiento más
baratas hasta la eliminación final.

## Dónde se configura

Dentro del bucket, en la pestaña de **gestión (Management)** se encuentra la sección de Lifecycle
Rules, donde se pueden ver las reglas ya creadas y añadir nuevas (ej. `transicion-al-archivo`).

## Ámbito de la regla (scope)

La regla se puede aplicar a **todos los objetos** del bucket, o filtrarse de tres formas:

1. **Prefijo** — una ruta de carpeta concreta (ej. `csv/`), para que la regla solo afecte a esa
   subcarpeta.
2. **Etiquetas (tags)** — muy útil para definir políticas de ciclo de vida distintas según el **tipo
   de dato**, sin depender de dónde esté ubicado físicamente en el bucket.
3. **Tamaño del objeto** — por ejemplo, para aplicar la regla solo a objetos por encima de cierto
   tamaño.

## Acciones configuradas en este ejemplo

> Nota: en este bucket no se usa versionado, así que las acciones se aplican directamente sobre los
> propios objetos (no sobre "versiones actuales" separadas).

### Transiciones

- **Día 0 (inmediato)** → **S3 Intelligent-Tiering**. Se menciona como una **buena opción por
  defecto**: a partir de ahí, el propio Intelligent-Tiering mueve automáticamente los datos entre sus
  niveles de acceso frecuente/infrecuente (ver [[3-storage-classes]]).
- **Día 180** → **Glacier Instant Retrieval**.
- **Día 360** (180 días después de la transición anterior) → **Glacier Deep Archive**.

### Expiración

- **Día 720** → **expirar (eliminar) la versión actual de los objetos**.
  - En un **bucket sin versionado** (como en este caso): el objeto se **elimina permanentemente**.
  - En un **bucket con versionado**: en su lugar se añade un **marcador de borrado (delete marker)** y
    el objeto pasa a conservarse como **versión no actual** (tema de versionado, se ve más adelante).

La consola muestra una línea de tiempo visual con la secuencia completa: carga del objeto → 180 días →
Glacier Instant Retrieval → 180 días más → Glacier Deep Archive → expiración/borrado.

## Coste de las transiciones

> ⚠️ Cada transición de ciclo de vida genera un **coste de solicitud único por objeto**. Con muchos
> objetos pequeños, este coste puede llegar a ser relevante — hay que confirmarlo explícitamente
> (checkbox) antes de crear la regla.

## Combinar varias reglas

No hace falta meter toda la lógica en una sola regla: se pueden crear reglas **separadas**, por
ejemplo una dedicada solo a políticas de eliminación y otra dedicada solo a transiciones entre clases
de almacenamiento.

Para eliminar una regla ya creada: seleccionarla en la lista y usar la opción **Delete**.
