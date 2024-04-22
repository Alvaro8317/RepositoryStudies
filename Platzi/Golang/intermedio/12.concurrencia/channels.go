package main

import "fmt"

func mainChannels() {
	// c := make(chan int)     /* Así, el canál estaría bloqueado, es un canál sin ningún tipo de buffer */
	/* Este es un canal con buffer porque tiene una capacidad para 3 elementos */
	/* Una de las ventajas de buffer es que tiene una cantidad limitada para recibir datos */
	/*  */
	c2 := make(chan int, 3)
	/* Cuando se hace la siguiente operación, se espera que go ya tenga lista una función con una rutina distinta */
	// c <- 1
	c2 <- 1
	c2 <- 2
	c2 <- 2
	/* Aquí se llena el buffer, ocurre lo mismo que un canal sin buffer */
	c2 <- 2
	// c2 <- 3
	fmt.Println(<-c2)
	fmt.Println(<-c2)
	fmt.Println(<-c2)
}
