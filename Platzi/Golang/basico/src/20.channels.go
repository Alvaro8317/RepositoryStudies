package main

import "fmt"

/* Estos son para tareas extremadamente pesadas */
/* Cuando se agrega un channel en una función, lo ideal es que
se le indique si el canál será de entrada de datos o de salida */
// func sayChannel(text string, channel <-chan string) { Salida
func sayChannel(text string, channel chan<- string) { /* Entrada */
	/* <- simbolo para meter datos al canál */
	channel <- text
}

func channels() {
	/* Para usar la concurrencia se puede con:
	1. Time.sleep (le da tiempo a go para que haga las otras tareas con la concurrencia)
	2. WaitGroup (Complejo pero da un rendimiento superior, muy eficiente)
	3. Channels (Ideal para cuando no tiene que ser el mejor rendimiento)
	Los channels permiten compartir datos entre los goroutines */
	/* Primero se le indica un channel con el tipo de dato que procesará */
	/* Segundo va cuántos datos simultaneos manejará el canál, es opcional, pero da
	más rendimiento */
	myChannel := make(chan string, 1)
	fmt.Println("Hello")
	go sayChannel("Bye", myChannel)
	fmt.Println(<-myChannel)
}
