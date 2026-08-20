# Redshift: control de acceso de grano fino

> Curso: AWS Certified Data Engineer – Associate (DEA-C01)

El **control de acceso de grano fino** permite a los administradores de bases de datos gestionar
el acceso a un nivel mucho más detallado que los métodos tradicionales vistos en
[21-access-control.md](21-access-control.md) (ej. `GRANT SELECT` sobre una tabla o esquema
completo).

## Seguridad a nivel de columna

Es la opción más básica: se concede `SELECT` solo sobre una o varias **columnas específicas** de
una tabla.

```sql
GRANT SELECT (order_id, customer_name) ON orders TO usuario;
```

- Si el usuario consulta la tabla, solo podrá ver las columnas sobre las que se le haya concedido
  acceso explícitamente.

## Seguridad a nivel de fila (Row-Level Security)

Permite definir **políticas** que restringen qué **filas** puede ver un usuario, usando
**condiciones SQL** para determinar el acceso.

Ejemplo: restringir el acceso según el `store_id` de una tabla, comparándolo con el usuario
actual a través de una tabla de seguridad (ej. una tabla `managers` que relaciona cada gestor con
su tienda):

```sql
CREATE RLS POLICY store_policy
WITH (store_id INTEGER)
USING (store_id IN (
    SELECT manager_store_id
    FROM managers
    WHERE manager_username = CURRENT_USER
));
```

- La política se define sobre una **columna de la tabla** (`store_id`) que se quiere restringir.
- Se apoya en una **tabla de seguridad** (`managers`) para determinar qué valores de esa columna
  puede ver cada usuario — comparando con `CURRENT_USER`.
- Ejemplo: si el usuario actual es `J Smith` y la tabla `managers` indica que gestiona la tienda
  `1`, la política solo devolverá las filas donde `store_id = 1` — ese gestor solo verá los datos
  de su propia tienda.

> ⚠️ Al igual que con los roles, una política creada debe **adjuntarse (attach)** a una tabla y a
> un rol/usuario antes de que tenga efecto — crear la política no es suficiente por sí sola.

## Enmascaramiento dinámico de datos (Dynamic Data Masking)

Es, en realidad, un **tipo específico de seguridad a nivel de columna**: la columna sigue siendo
visible (por ejemplo, para poder seguir usándola en agregaciones), pero su **contenido se
enmascara** cuando contiene información sensible.

Opciones de enmascaramiento:

- **Enmascarar el valor completo** (ej. ocultar por completo una columna de email).
- **Enmascarar parcialmente mediante una expresión**, ej. mostrar solo los primeros caracteres:

  ```sql
  SUBSTRING(email, 1, 3) || '***'
  ```

- **Aplicar una función hash** sobre el valor (ej. sobre el email). Esto equivale a una
  **tokenización**: un mismo valor de entrada siempre produce el mismo hash (mismo token), por lo
  que sigue siendo útil para agregaciones o joins, pero no revela ninguna información personal —
  es una cadena aparentemente aleatoria.

### Aplicar (attach) una política de enmascaramiento

```sql
ATTACH MASKING POLICY nombre_politica
ON tabla (columna)
TO ROLE nombre_rol;
```

- Al igual que las políticas de RLS, una política de enmascaramiento debe crearse y luego
  **adjuntarse** a una tabla, columna y rol concretos.

### Prioridad entre políticas

- Cuando **varias políticas** aplican sobre el mismo dato, se puede definir una **prioridad**:
  cuanto mayor la prioridad, más fuerte (más restrictiva) es la política.
- Ante un conflicto entre políticas aplicables a un mismo usuario, **siempre gana la política de
  mayor prioridad**.

## Resumen

| Mecanismo                         | Qué controla                                                                                         |
| --------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Seguridad a nivel de columna      | Qué columnas puede ver un usuario.                                                                   |
| Seguridad a nivel de fila (RLS)   | Qué filas puede ver un usuario, mediante condiciones SQL.                                            |
| Enmascaramiento dinámico de datos | Un tipo de seguridad a nivel de columna: la columna es visible, pero su valor se enmascara u ofusca. |
