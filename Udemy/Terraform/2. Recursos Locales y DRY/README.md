# 2. Recursos locales y DRY

## Múltiples providers

En terraform según la documentación existen providers oficiales de terraform pero también hay de la comunidad, algunos relevantes pueden ser como `random_string` y como el que se vió en la introducción, `local_file`, para el caso de random string, se puede hacer uso para generar palabras aleatorias como se observa en el archivo de terraform.tf, aquí se puede encontrar la [documentación](https://registry.terraform.io/providers/hashicorp/random/latest)

También existe `terraform show`, este mostrará los recursos que terraform creó, si se usa un destroy o no se ha desplegado nada, no mostrará nada.

El archivo `terraform.tfstate` lleva un registro de lo que se ha desplegado, además, terraform permite tener la infraestructura en múltiples archivos y poder referenciarse entre sí.

El id de cada recurso debe de ser único, el id es el nombre del recurso que los diferencia de los demás, de los cuáles podrán ser referenciados en otros recursos a pesar de tener el mismo contenido y ser el mismo tipo de recurso.

## DRY - Don't repeat yourself

Este principio aplica también para terraform, por lo que se puede hacer uso de una claúsula llamada `count`, con esto se le dice a terraform que cree 5 de esos
