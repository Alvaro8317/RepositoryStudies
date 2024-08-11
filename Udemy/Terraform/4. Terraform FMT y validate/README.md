# 4. Terraform FMT y validate

## Terraform fmt

Se puede hacer uso de terraform fmt para formatear el código de terraform y formatearlo, es decir, aplicará indentación donde sea necesario, si no se indica el nombre a formatear, lo hará en todos que acabe en `.tf`, para ejecutarlo en todos se usa `terraform fmt` y para un solo archivo, solo se debe de especificar el nombre del archivo que es `terraform fmt terraform.tf`

## Terraform validate

Con este comando se puede validar la sintaxis de los archivos terraform bajo el comando `terraform validate`, si se ejecuta plan, también mostrará el error, con plan se conecta el provider, en cambio, con validate validará sintaxis, es decir, con plan puede tardar mucho tiempo entonces se recomienda que ante proyectos grandes de terraform, se ejecute primero terraform validate y después plan. Si la sintaxis es correcta, mostrará "The configuration is valid".

## Lista de comandos vista hasta ahora

- `terraform init` -> Inicializa un proyecto terraform
- `terraform plan` -> Muestra el plan en base a los archivos terraform que encuentre
- `terraform apply` -> Despliega los recursos
- `terraform destroy` -> Elimina los recursos
- `terraform fmt` -> Formatea el código de los archivos terraform
- `terraform validate` -> Valida la sintaxis de los archivos terraform
- `terraform show` -> Muestra los recursos que están desplegados

## Restringir versiones de providers o terraform / Constraints

Si no se tienen consistencias en las versiones de terraform en un equipo, se pueden tener problemas de incompatibilidad, por lo que terraform permite especificarle la versión tanto de terraform como de los providers, existen las siguientes constraints:

- `0.15.0` -> Versión exacta
- `>= 0.15` -> Versión 0.15 o superior
- `~= 0.15` -> Versión 0.15 o superior siempre y cuando no sea un cambio grande, es decir, que la versión no sea superior a la 0.99 por dar un ejemplo, no actualizaría si hay una versión 1.0 porque ya no sería una versión menor y podría ser disruptiva, es la más usada.
- `<= 0.15, < 2.0.0` -> Constraint más flexible, permite cualquier versión entre la 0.15.0 hasta la 2.0
