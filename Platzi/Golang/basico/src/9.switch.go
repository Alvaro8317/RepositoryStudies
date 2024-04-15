package main

import "fmt"

func switchSentence() {
	// module := 4 % 2 /* Primera forma */
	// switch module {
	switch module := 4 % 2; module { /* Alternativa */
	case 0:
		fmt.Println("Es par")
	default:
		fmt.Println("Es impar")
	}
	/* Sin condición, ideal cuando se evaluarán múltiples condiciones con un if */
	value := 200
	switch {
	case value > 100:
		fmt.Println("Es mayor a 100")
	case value < 0:
		fmt.Println("Es menor a 0")
	default:
		fmt.Println("Hay algo raro")
	}
}
