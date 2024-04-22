package main

import (
	"bufio"
	. "fmt"
	"os"
	"strings"
	"unicode"
)

func FormatTheSentence(sentenceToFormat string) string {
	return strings.Map(func(r rune) rune {
		if unicode.IsSpace(r) || r == ',' || r == '.' {
			return -1 
		}
		return unicode.ToLower(r) 
	}, sentenceToFormat)
}

func ValidateIfIsPalindrome(sentenceToEvaluate string) bool {
	var sentenceReverse string
	for i := len(sentenceToEvaluate) - 1; i >= 0; i-- {
		sentenceReverse += string(sentenceToEvaluate[i])
	}
	if sentenceReverse == sentenceToEvaluate {
		return true
	}
	return false
}

func main() {
	// Recommended: Do not edit the code below

	// Create a new scanner to read from standard input
	scanner := bufio.NewScanner(os.Stdin)

	// Check if there is input available
	if scanner.Scan() {
		// Get the scanned text
		inputText := scanner.Text()
		// Print the read text
		// fmt.Println(inputText)
		
		formatedInputText := FormatTheSentence(inputText)
		Println(ValidateIfIsPalindrome(formatedInputText))
	}
	// Your code can go here.
}
