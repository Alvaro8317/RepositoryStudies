# Variables y OUTPUTS

Hasta ahora se han trabajado sin variables dejando por ejemplo los tags escritos en los resources, por ende, esto puede inferir en repetir código, con variables se puede reutilizar muchísimas cosas como los tags, un cidr para las vpc que se repite entre distintas vpc, etc. El hacer uso de variables hace más fácil la lectura y son más aceptadas.

## Asignando valores a las variables

Para hacer uso de las variables se debe de crear el elemento `variable` en los archivos terraform, como se ve a continuación:

```hcl
variable "virginia_cidr" {
  default = "10.01.10.01/16"
}
```

Pero, para hacer uso de las variables se puede de 3 maneras:

1. Escribiendo el valor por defecto en el archivo terraform
2. Escribiendo el valor en el apply cuando lo pregunte
3. Por medio de variables de entorno, estas tienen que empezar por `TF_VAR_nombreDeLaVariable`, ejemplo, `TF_VAR_virginia_cidr="10.10.0.0/16`. Para crear variables de entorno es con el comando `export` y para eliminarlas es con `unset`
4. En el comando del plan o apply con la bandera -var, ejemplo, `terraform plan -var ohio_cidr="10.20.0.0/16`
5. MÁS RECOMENDABLE, usando un archivo `variables.tf` donde se deja **solo la definición de las variables** y en otro archivo llamado `terraform.tfvars` se dejan los valores de las variables, este archivo no se suele ir al repositorio y tiene que llamarse sí o sí terraform.tfvars o terraform.tfvars.json, si uno quiere algo más representativo debe de ser así:

- \*.auto.tfvars
- \*.auto.tfvars.json

  Ya si uno desea hacer uso de un archivo de variables terraform con nombre totalmente personalizado, se puede hacer uso de `terraform plan --var-file nombreArchivoConVariables.tfvars`. Pero, lo más recomendable es hacer uso de terraform.tfvars

Para validar los valores de las variables, se pueden ver con terraform plan o apply

## Prioridad de variables

Si se encuentra la misma variable en variables de entorno y en tfvars, el archivo tfvars tendrá mayor prioridad, este es el orden de prioridad completo de las variables en Terraform, de la más baja a la más alta:

1. Valor predeterminado en el archivo de definición de la variable `(variable "name" { default = "value" })`
2. Variables de entorno `(TF_VAR_name=value)`
3. Archivo de variables `(ej. terraform.tfvars o \*.auto.tfvars)`
4. Archivo de variables pasado explícitamente en la línea de comandos `(terraform apply -var-file="custom.tfvars")`
5. Valores pasados directamente en la línea de comandos `(terraform apply -var="name=value")`

## Tipos de variables en terraform

Hay diferentes tipos de variables, hasta ahora solo se han visto variables que tienen un valor por defecto con default, pero se pueden adicionar estos valores:

- default -> Valor por defecto
- description -> Descripción
- type -> Tipo de dato, es posible: string, number, bool o any (Por defecto es any)
- sensitive -> Si es sensible o no, en caso de ser sensible, no se verá el valor de la variable

Hay algunos tipos de datos que tienen conversión de tipos de variables, si un número se va en comillas ejemplo "5", lo aceptará aún así, de igual manera viceversa, lo mismo sucede con booleanos, es decir, un "false" lo recibe sin problema siempre y cuando se haya especificado el tipo de dato.

### Listas

También se admiten variables de tipo lista, que es así:

```hcl
variable "lista_cidrs" {
  default = ["10.10.0.0/16", "10.20.0.0/16"]
  type = list(string)
}
```

Las listas admiten elementos repetidos, todos los elementos de una lista deben ser del mismo tipo.

### Mapas

Este es otro tipo de dato admitido en terraform que es llave valor

```hcl
variable "map_cidrs" {
  default = {
    "virginia" = "10.10.0.0/16",
    "ohio" = "10.20.0.0/16"
  }
  type = map(string)
}
resource "aws_vpc" "vpc_virginia" {
  cidr_block = var.map_cidrs["virginia"]
}
```

### Sets

Set no admite elementos repetidos y no se puede acceder a elementos puntuales, estos son conjuntos, se deben de hacer uso en su totalidad, se puede usar en conjunto con la función for_each

```hcl
variable "set_cidrs" {
  default = ["10.10.0.0/16", "10.20.0.0/16"]
  type = set(string)
}
```

### Objects

Object es similar a map, pero dentro del objeto se puede tener diferentes tipos de variables, es como una combinación de los anteriores

```hcl
variable "object_cidrs" {
  type = object({
  nombre = string
  cantidad = number
  cidrs = list(string)})
}
default = {
  cantidad = 1
  cidrs = ["10.10.0.0/16]
  nombre = "Virginia"
}
```

### Tuplas

Tupla es muy similar a las listas, pero la tupla puede contener diferentes tipos de elementos y se accede en base a índices empezando en 0

## Outputs / Salidas

Es un tipo de "variable" que permite exponer por pantalla elementos que al realizar un plan, son desconocidos, como un ARN de AWS, ejemplo, una dirección IP pública que puede tener una instancia, son datos que se conocen ya cuando se despliega la infraestructura. Para crear un output es:

```hcl
output "linux_public_ip" {
  value = aws_instance.linux.public_ip
  description = "Muestra la IP pública asignada a la instancia"
}
```

Además, se pueden obtener los output con `terraform output` y así, terraform mostrará todos los output disponibles, si se requiere acceder a uno en específico, se puede hacer uso de `terraform output linux_public_ip` donde es el nombre del output previamente creado.

¿Cómo se puede saber qué outputs se pueden obtener? Revisando la documentación, usualmente está al final conocida como `attributes reference` que son los atributos que se pueden obtener.
