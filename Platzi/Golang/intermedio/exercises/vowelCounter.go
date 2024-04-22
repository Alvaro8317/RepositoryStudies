package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

func CounterOfVowels(sentenceToMakeTheCount string) (counter int) {
	counter = 0
	vowels := map[rune]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true}

	// Iterar sobre el string
	for _, letter := range sentenceToMakeTheCount {
		// Convertir la letra a minúsculas
		letterLower := unicode.ToLower(letter)
		// Verificar si la letra es una vocal
		if vowels[letterLower] {
			counter++
		}
	}
	return counter
}

func main() {
	// Recommended: Do not edit the code below

	// Create a new scanner to read from standard input
	scanner := bufio.NewScanner(os.Stdin)

	// Check if there is input available
	if scanner.Scan() {
		// Get the scanned text
		inputText := scanner.Text()
		fmt.Println(CounterOfVowels(inputText))
		// Print the read text
		// fmt.Println(inputText)

	}
	// Your code can go here.
}
