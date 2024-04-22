package main

import "fmt"

/* Aquí se definirán los canáles de solo lectura, solo escritura y que implicaría confundirse y escribir sobre un canál que debería de ser solo lectura */

func Generator(c chan<- int) {
	for i := 0; i <= 10; i++ {
		c <- i
	}
	close(c)
}

/*
* Escritura <-
* <- Lectura
 */

func Double(in <-chan int, out chan<- int) {
	for value := range in {
		out <- 2 * value
	}
	close(out)
}

func PrintValues(c <-chan int) {
	for value := range c {
		fmt.Println(value)
	}
}

func mainPipelines() {
	generator := make(chan int)
	doubles := make(chan int)
	go Generator(generator)
	go Double(generator, doubles)
	PrintValues(doubles)
}
