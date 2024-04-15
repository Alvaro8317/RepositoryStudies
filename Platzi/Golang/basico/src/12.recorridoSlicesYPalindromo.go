package main

import (
	"fmt"
	"strings"
)

func isPalindrome(text string) {
	text = strings.ToLower(text)
	var textReverse string
	for i := len(text) - 1; i >= 0; i-- {
		textReverse += string(text[i])
	}
	if textReverse == text {
		fmt.Println("Es palindromo")
	} else {
		fmt.Println("No es palindromo")
	}
}
func recorridoSlices() {
	slice := []string{"Hola", "k", "ase"}
	for indice, valor := range slice {
		fmt.Printf("El indice %d, tiene un valor de: %s\n", indice, valor)
	}
	/* Solo tiene en cuenta el indice */
	for indice := range slice {
		fmt.Printf("El indice %d\n", indice)
	}
	isPalindrome("Ama")
}
