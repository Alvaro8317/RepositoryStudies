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
