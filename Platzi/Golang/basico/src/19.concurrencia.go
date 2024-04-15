package main

import (
	"fmt"
	"sync"
	"time"
)

func say(text string, wg *sync.WaitGroup) {
	defer wg.Done()
	fmt.Println(text)
}

func concurrencia() {
	/* Concurrencia es de las mejores cosas de golang, la concurrencia es trabajar con
	múltiples cosas al tiempo mientras que paralelismo está haciendo múltiples cosas al mismo
	tiempo */
	/* Concurrencia te permite estar pendiente de varios procesos, comienzas uno, empiezas otro, ves si el anterior ya terminó, luego crear otro así
	El paralelismo, es usar varios hilos del procesador para hacer varios procesos a la vez, pero siempre estas esperando que la tarea termine. */
	/* Permite trabajar de manera más nativa el goroutine */
	var wg sync.WaitGroup
	fmt.Println("Hello")
	// say("Hello")
	wg.Add(1)
	/* Al dejarlo así, el say "hello" muere, lo que no permite ejecutar el say "world" */
	go say("World", &wg)
	wg.Wait()
	/* Para imprimir world, se puede con un time.Sleep pero no es lo ideal, lo que le dió
	el tiempo de ejecutarse World */
	/* Función anónima */
	go func(text string) {
		fmt.Println(text)
	}("Adios")
	time.Sleep(time.Second * 1)
}
