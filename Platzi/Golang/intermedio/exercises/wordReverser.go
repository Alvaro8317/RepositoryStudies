package main

import (
	"bufio"
	"fmt"
	"os"
)

func reverseText(textToReverse string) (textReversed string) {

	for i := len(textToReverse) - 1; i >= 0; i-- {
		textReversed += string(textToReverse[i])
	}
	return
}

func main() {
	// Recommended: Do not edit the code below

	// Create a new scanner to read from standard input
	scanner := bufio.NewScanner(os.Stdin)

	// Check if there is input available
	if scanner.Scan() {
		// Get the scanned text
		inputText := scanner.Text()
		fmt.Println(reverseText(inputText))
		// Print the read text
		// fmt.Println(inputText)
	}
	// Your code can go here.
}
