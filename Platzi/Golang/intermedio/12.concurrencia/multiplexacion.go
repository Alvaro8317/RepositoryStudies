package main

import (
	"fmt"
	"time"
)

func main() {
	c1 := make(chan int)
	c2 := make(chan int, 2)
	duration1 := 4 * time.Second
	duration2 := 2 * time.Second
	go DoSomething(duration1, c1, 1)
	go DoSomething(duration2, c2, 2)
	// fmt.Println(<-c1) /* Se imprime primero a pesar que dure el doble, esto porque el go routine principal se queda esperando datos del canál */
	// fmt.Println(<-c2)
	for i := 0; i < 2; i++ {
		/* Select es similar al switch */
		/* Select permite tener diferentes casos con diferentes canales dependiendo del que haya sido activado */
		/* Esto se llama multiplexar
		* Cuando una rutina se está comunicando con varios channels, es muy útil utilizar la palabra reservada select para poder interactuar de una manera más ordenada con todos los mensajes que están siendo recibidos
		 */
		select {
		case channelMsg1 := <-c1:
			fmt.Println(channelMsg1)
		case channelMsg2 := <-c2:
			fmt.Println(channelMsg2)

		}
	}
}

func DoSomething(i time.Duration, c chan<- int, param int) {
	time.Sleep(i)
	c <- param
}
