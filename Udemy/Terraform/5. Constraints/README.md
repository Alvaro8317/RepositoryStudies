# 5. Constraints

## Restringir versiones de providers o terraform / Constraints

Si no se tienen consistencias en las versiones de terraform en un equipo, se pueden tener problemas de incompatibilidad, por lo que terraform permite especificarle la versión tanto de terraform como de los providers, existen las siguientes constraints:

- `0.15.0` -> Versión exacta
- `>= 0.15` -> Versión 0.15 o superior
- `~= 0.15` -> Versión 0.15 o superior siempre y cuando no sea un cambio grande, es decir, que la versión no sea superior a la 0.99 por dar un ejemplo, no actualizaría si hay una versión 1.0 porque ya no sería una versión menor y podría ser disruptiva, es la más usada.
- `<= 0.15, < 2.0.0` -> Constraint más flexible, permite cualquier versión entre la 0.15.0 hasta la 2.0

## Organización de constraints

Los providers suelen dejarse en archivos separados, para este caso se dejan en `providers.tf`
