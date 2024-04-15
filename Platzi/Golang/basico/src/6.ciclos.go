package main

import "fmt"

func ciclos() {
	/* Un ciclo es una tarea repetitiva
	en go solo hay un ciclo iterativo que es for */
	/* For condicional -> for convencional */
	fmt.Println("For condicional")
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}
	fmt.Println("For while")
	/* For while -> Un for hasta que una condición de cumpla, muy similar a while */
	counter := 0
	for counter < 10 {
		fmt.Println(counter)
		counter++
	}
	/* for forever -> Un ciclo infinito */
	fmt.Println("For forever")
	counterForever := 0
	for {
		fmt.Println(counterForever)
		counterForever++
		/* Siempre al haber un ciclo for forever debe de haber una forma de romper el ciclo como con un break */
		if counterForever == 100 {
			break
		}
	}
	fmt.Println("For range")
	listaNumerosPares := []int{2, 4, 6, 8, 10}
	for i, numeroParDelArray := range listaNumerosPares {
		fmt.Println("Valor de i:", i)
		fmt.Println("Valor de numeroParDelArray:", numeroParDelArray)
	}
}
