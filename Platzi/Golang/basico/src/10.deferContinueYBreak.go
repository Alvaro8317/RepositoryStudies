package main

import "fmt"

func deferContinueYBreak() {
	/* Defer -> Ejecutará el último código, es lo último que ejecutará al finalizar el código */
	/* Lo ideal es usar un solo defer por función, ideal para cerrar conexiones a la base de datos */
	defer fmt.Println("Hola")
	fmt.Println("mundo")
	/* Continue y break */
	for i := 0; i < 10; i++ {
		if i == 2 {
			continue
			/* Ideal cuando una condición en un ciclo for, se necesite que continue */
		}
		fmt.Println(i)
		if i == 8 {
			fmt.Println("Es 8, rompiendo el ciclo")
			break
		}
	}
}
