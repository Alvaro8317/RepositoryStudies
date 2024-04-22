package main

import "fmt"

const nums = 3

/* Es buena práctica especificarle en una función si un canál será de lectura o de escritura, para este caso será de escritura */
func Emisor(canalAEmitir chan<- int) {
	for i := 1; i <= nums; i++ {
		canalAEmitir <- i
		fmt.Println(i, "Dato enviado correctamente al canál")
	}
}

/* Parámetro de un canál para solo lectura */
func Receptor(canalARecibir <-chan int) {
	for i := 1; i <= nums; i++ {
		/* Se bloquea hasta que Emisor le dé datos */
		numeroRecibido := <-canalARecibir
		fmt.Println("Dato recibido correctamente del canál: ", numeroRecibido)
	}
}

func main() {
	/* Se crea el canal */
	ch := make(chan string)
	/* Se lanza una goroutine distinta que se ejecuta en paralelo */
	go func() {
		fmt.Println("He enviado un dato al canál: ")
		ch <- "Hola"
	}()
	/* La go routine principal se bloquea hasta que haya un dato disponible en el canál, si siempre se queda esperando a un dato y no lo recibe, da un "all goroutines are asleep - deadlock" */
	recibido := <-ch
	fmt.Println("He recibido: ", recibido)
	/* Estos son canáles sin búfer, estos se bloquean hasta que alguna otra goroutine reciba el dato que ya envió, para este caso, Emisor quedará bloqueado hasta que Receptor reciba los mensajes del canál */
	chIntegers := make(chan int)
	/* Crea una nueva go routine para emitir */
	go Emisor(chIntegers)
	Receptor(chIntegers)
	/*
		! Canales con búfer
		* Estos canales tienen un espacio definido de datos que pueden guardar en memoria
		* Estos canales almacenan espacio hasta que se una go routine los llene, una vez llenos si se intenta enviar un dato a un canál lleno, la go routine se bloqueará hasta que otra go routine reciba algún dato del canál
		* Estos canáles se crean con make pero se les especifica la cantidad de datos
	*/
	chConBufer := make(chan string, 5)
	chConBufer <- "Hola, no me bloqueo porque este canal puede almacenar 5 elementos, si fuera un canál sin búfer me bloquearía porque al enviar, me bloqueo hasta que otra go routine reciba mi información"
	recibidoDelCanalConBufer := <-chConBufer
	fmt.Println(recibidoDelCanalConBufer)
}
