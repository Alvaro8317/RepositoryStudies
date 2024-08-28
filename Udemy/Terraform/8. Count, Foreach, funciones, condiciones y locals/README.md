# Count, Foreach, funciones, condiciones y locals

Con count, se puede usar en conjunto con la función `length()` y un array dentro de las variables para poder iterar cada valor como la siguiente manera:

```hcl

resource "aws_instance" "instance_test" {
  ami                    = var.ec2_specs.ami
  count                  = length(var.instances)
  instance_type          = var.ec2_specs.instance_type
  subnet_id              = aws_subnet.public_subnet.id
  key_name               = data.aws_key_pair.ec2_key_pair.key_name
  vpc_security_group_ids = [aws_security_group.sg_instance_ec2.id]
  user_data              = file("./scripts/user-data.sh")
  tags = {
    Name = var.instances[count.index]
  }
}

```

En el ejemplo anterior, el count indica cuántos recursos se necesitan, puede ser un número entero, por otro lado, el **for each solo puede ser usado con variables sets y maps**, de lo contrario, dará "The given for each argument value is unsuitable". Con foreach no mostrará en base al índice, sino en base al valor en el plan.

Con foreach muestra también el nombre de la instancia, en cambio con count, lo hace en base a su índice.
Foreach trata sus elementos como un map, esto da una ventaja porque si se elimina una instancia de la variable, ejemplo, ya no se quiere desplegar mysql, solo se eliminará esta sin interferir en las demás, si fuera un count en base al índice, eliminaría todas las que están en mysql en adelante, porque se modificaría el índice de cada instancia.

En Terraform, tanto count como for_each son mecanismos que permiten la creación de múltiples recursos o módulos de forma dinámica, pero tienen diferentes propósitos y casos de uso. Aquí te explico las diferencias principales:

## Propósito y Usos Comunes

count:

Propósito: Se usa para crear un número fijo de recursos basados en un valor numérico o una expresión booleana.

Usos comunes: Crear un número específico de instancias de un recurso o módulo.

Ejemplo: Crear 3 instancias de un servidor:

```hcl

resource "aws_instance" "example" {
count = 3
ami = "ami-123456"
instance_type = "t2.micro"
}
```

for_each:

Propósito: Se usa para crear recursos o módulos en función de un conjunto de elementos (mapas o listas).

Usos comunes: Crear recursos basados en claves únicas, como elementos de un mapa o identificadores únicos en una lista.

Ejemplo: Crear una instancia por cada entrada en un mapa de configuraciones:

```hcl

resource "aws_instance" "example" {
for_each = {
server1 = "ami-123456"
server2 = "ami-789012"
}
ami = each.value
instance_type = "t2.micro"
}
```

## Identificación de Recursos

count:

Los recursos se identifican usando índices numéricos (0, 1, 2, ...).
Esto puede ser problemático si la lista de recursos cambia y los índices se reordenan, lo que puede provocar la recreación de recursos innecesariamente.
for_each:

Los recursos se identifican por claves únicas definidas en el mapa o lista.
Esto ofrece una mayor estabilidad, ya que los recursos se asocian con identificadores únicos que no cambian a menos que el mapa o lista cambien. 3. Tipo de Datos Aceptados
count:
Acepta un valor numérico o booleano (true se convierte en 1 y false en 0).
Es ideal cuando necesitas repetir un recurso un número específico de veces.
for_each:
Acepta mapas (map) o conjuntos (set).
Es más flexible cuando necesitas iterar sobre un conjunto de valores únicos. 4. Acceso a Valores en la Iteración
count:

Se accede a los valores con count.index.
Esto solo te da acceso al índice numérico, lo que puede limitar las posibilidades de personalización en ciertos casos.
for_each:

Se accede a los valores con each.key (clave) y each.value (valor).
Proporciona acceso tanto a la clave como al valor, lo que permite mayor flexibilidad en la configuración del recurso. 5. Ejemplos Comparativos
count: Crear 5 instancias del mismo tipo de recurso.

```hcl
resource "aws_instance" "example" {
count = 5
ami = "ami-123456"
instance_type = "t2.micro"
}
for_each: Crear instancias con diferentes configuraciones.
```

```hcl
resource "aws_instance" "example" {
for_each = {
server1 = "ami-123456"
server2 = "ami-789012"
}
ami = each.value
instance_type = "t2.micro"
}
```

## Funciones en terraform

Para acceder a la consola de terraform y practicar las funciones, se usa `terraform console`, desde aquí no es posible desplegar recursos o destruirlos.

### Funciones

#### Funciones numéricas

- length: Devuelve la longitud de una lista, mapa o cadena.
  `length([1, 2, 3, 4, 5])  # Resultado: 5`
- toset: Convierte una lista en un conjunto, eliminando elementos duplicados.
- max: Devuelve el valor máximo entre los números proporcionados.
- min: Devuelve el valor mínimo entre los números proporcionados.
- ceil: Redondea un número hacia arriba al entero más cercano.
- floor: Redondea un número hacia abajo al entero más cercano.

#### Funciones de String

- split: Divide una cadena en una lista utilizando un delimitador.

  ```hcl
  split(",", "a,b,c,d")  # Resultado: ["a", "b", "c", "d"]
  ```

- lower: Convierte una cadena a minúsculas.

  ```hcl
  lower("HELLO")  # Resultado: "hello"
  ```

- upper: Convierte una cadena a mayúsculas.

  ```hcl
  upper("hello")  # Resultado: "HELLO"
  ```

- title: Convierte la primera letra de cada palabra a mayúscula.

  ```hcl
  title("hello world")  # Resultado: "Hello World"
  ```

- substring: Extrae una subcadena dada una posición inicial y una longitud.

  ```hcl
  substring("Terraform", 0, 4)  # Resultado: "Terr"
  ```

- join: Une una lista de cadenas con un delimitador.

  ```hcl
  join(",", ["a", "b", "c"])  # Resultado: "a,b,c"
  ```

- length: Devuelve la longitud de una cadena.

  ```hcl
  length("Terraform")  # Resultado: 9
  ```

- index: Encuentra la posición de un valor en una lista.

  ```hcl
  index(["a", "b", "c"], "b")  # Resultado: 1
  ```

- element: Devuelve el elemento en una posición dada en una lista.

  ```hcl
  element(["a", "b", "c"], 1)  # Resultado: "b"
  ```

- contains: Verifica si una lista contiene un valor específico.

  ```hcl
  contains(["a", "b", "c"], "b")  # Resultado: true
  ```

#### Funciones de mapas

- keys: Devuelve las claves de un mapa.

  ```hcl
  keys({a = 1, b = 2, c = 3})  # Resultado: ["a", "b", "c"]
  ```

- values: Devuelve los valores de un mapa.

  ```hcl
  values({a = 1, b = 2, c = 3})  # Resultado: [1, 2, 3]
  ```

- lookup: Busca un valor en un mapa y devuelve un valor por defecto si no se encuentra.

  ```hcl
  lookup({a = 1, b = 2}, "c", 0)  # Resultado: 0
  ```

## Clausulas condiciones en terraform

Para realizar condiciones en terraform, no se hace como con if como en otros lenguajes de programación, se hace con una sintaxis similar a la de un operador ternario donde evalua una variable y en caso de ser true será el primer valor, caso contrario, segundo valor, ejemplo:
`count = var.enable_monitoring ? 1 : 0`, es decir, la sintaxis es `count = statementToValidate == True? 1 : 0`, se pueden evaluar las condiciones en `terraform console` como 1 == 1, 1 != 1, !(1 != 1), (1 == 1) && (2 == 2) etc.

## Locals

Los bloques locals en Terraform se utilizan para definir variables locales que pueden ser usadas en todo el archivo de configuración. Son útiles para estandarizar nombres, combinar variables, o simplemente evitar repetir código.

### Ejemplo 1: Nombres Estandarizados

En este ejemplo, se usa locals para crear una convención de nombres para los recursos.

```hcl
locals {
environment = "prod"
region = "us-east-1"

resource_name_prefix = "${local.environment}-${local.region}"
}

resource "aws_s3_bucket" "example" {
bucket = "${local.resource_name_prefix}-s3-bucket"
}
```

Explicación: El nombre del bucket será prod-us-east-1-s3-bucket.

### Ejemplo 2: Combinación de Variables

Aquí, locals se utiliza para combinar variables y simplificar el uso en múltiples recursos.

```hcl
variable "project_name" {
type = string
default = "myproject"
}

variable "environment" {
type = string
default = "dev"
}

locals {
full_project_name = "${var.project_name}-${var.environment}"
}

resource "aws_instance" "example" {
ami = "ami-123456"
instance_type = "t2.micro"

tags = {
Name = local.full_project_name
}
}
```

Explicación: El nombre de la instancia llevará el valor de local.full_project_name, que será myproject-dev.

### Ejemplo 3: Valores Derivados

locals puede también calcular valores derivados que se usan en múltiples partes del código.

```hcl
locals {
instance_count = length(var.availability_zones)
instance_type = var.instance_type == "prod" ? "t3.large" : "t3.micro"
}

resource "aws_autoscaling_group" "example" {
desired_capacity = local.instance_count
max_size = local.instance_count + 2
min_size = local.instance_count - 1

launch_configuration = aws_launch_configuration.example.id
}
```

Explicación: local.instance_count y local.instance_type se calculan basados en otras variables y se reutilizan en la configuración del grupo de autoescalado.

#### Uso Común de Locals

Nombres de Recursos: Como en los ejemplos, para estandarizar y evitar errores en la nomenclatura.
Cálculos Repetitivos: Evitar duplicar lógica o cálculos en múltiples partes del archivo.
Condiciones y Lógicas: Centralizar lógica condicional que afecte a múltiples recursos.
Estos ejemplos ilustran cómo locals puede hacer que tus configuraciones de Terraform sean más limpias, mantenibles y menos propensas a errores. ¡Espero que te sean útiles!

## Bloques dinamicos

Permiten tener un código más legible
