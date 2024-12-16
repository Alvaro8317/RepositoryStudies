# Concurrencia

## Canales

Los **canales** son una herramienta fundamental en Go que simplifica el intercambio de datos entre goroutines. Actúan como vías de comunicación que permiten enviar y recibir datos de manera síncrona o asíncrona, facilitando la colaboración y coordinación entre diferentes partes de un programa concurrente.

### Declaración y Referencia

Un canal permite enviar y recibir datos de un tipo específico. Los canales son tratados por referencia, lo que significa que un canal creado de la siguiente manera:

```go
var nombres chan string
```

inicialmente apunta a `nil`, lo que indica que aún no se ha asignado memoria para él.

### Envío y Recepción de Datos

El operador `<-` se utiliza para interactuar con los canales. Para **enviar** datos a un canal, se utiliza la siguiente sintaxis:

```go
nombres <- "Alvaro Garzón"
```

Para **leer** datos de un canal, se utiliza el mismo operador, pero en el orden inverso:

```go
nuevoNombre := <-nombres
```

### Tipos de Canales

- **Canales sin búfer**: En este caso, la goroutine emisora se bloquea hasta que una goroutine receptora recibe la información del canal. Esto garantiza que los datos se transmitan de manera sincronizada.

- **Canales con búfer**: La goroutine emisora se bloqueará si intenta enviar datos a un canal que ya ha alcanzado su capacidad máxima. Los canales con búfer permiten que múltiples valores sean enviados sin bloquear la goroutine emisora, hasta que el búfer esté lleno.

### Cierre de Canales

Un canal cerrado puede seguir entregando sus respectivos valores. Sin embargo, después de que se vacíe, comenzará a entregar _zero values_ (valores cero) del tipo asociado al canal. Esto puede dificultar la identificación de un valor cero como un dato válido o como un _zero value_. Por esta razón, se recomienda iterar sobre los canales utilizando `range`.

Por ejemplo:

```go
canal := make(chan int, 3)
canal <- 1
canal <- 2
canal <- 3
close(canal)

for num := range canal {
    fmt.Println("Recibiendo datos del canal:", num)
}
fmt.Println("Fin")
```

Si el canal está vacío pero no cerrado, el bucle `for` esperará indefinidamente hasta que se reciban más valores o el canal se cierre.

### Resumen

Los canales son una herramienta poderosa para manejar la concurrencia en Go. Facilitan la comunicación entre goroutines, garantizando la sincronización y la seguridad de los datos. La comprensión adecuada de los canales y su uso puede mejorar significativamente la calidad y la eficiencia del código concurrente.
