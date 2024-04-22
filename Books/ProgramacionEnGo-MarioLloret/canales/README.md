## Canales
Un canal simplifica el proceso de compartición de datos entre go routines, es una vía de comunicación que permite enviar y recibir datos de manera síncrona o asíncrona.

Un canal permite enviar y recibir datos de un tipo dado. Los canales son tratados por referencia, lo que quiere decir que un canal creado así:
```golang
var nombres chan string
```
Apunta a nil

El operador <- permite leer o escribir datos dentro de un canal, para enviar datos es así:
```golang
myChannelOfNames <- "Alvaro Garzón"
```
Para leer datos de un canál, se usa el mismo operaodr pero en otro orden, ejemplo:
```golang
newVariable := <- myChannelOfNames
```
Un canál sin búfer -> La go routine emisora se bloquea hasta que una receptora reciba la información del canál
Un canál con búfer -> La go routine emisora se bloquea si al enviar datos a un canál, tiene el búfer ya lleno
Los canales sin búfer después de cerrado pueden seguir entregando sus respectivos valores, después de vaciado el canál, entregará los zero values, por lo que será difícil identificar si un 0 es un valor correcto de un canál o es un zero value, por lo que se recomienda iterar los canáles con range, ejemplo:
```golang
channel := make(chan int, 3)
channel <- 1
channel <- 2
channel <- 3
close(channel)
for num := range channel{
  fmt.Println("Recibiendo datos del canál", num)
}
fmt.Println("Fin")
```
Si el canál está vacío pero no cerrado, el búcle for esperará indefinidamente hasta que se reciban más valores o el canál se cierre.