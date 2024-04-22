package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func convertStrToNumbers(sliceInput string) []int {
	stringSplitted := strings.Split(sliceInput, ",")
	var numbers []int
	for _, numberInString := range stringSplitted {
		number, _ := strconv.Atoi(numberInString)
		numbers = append(numbers, number)
	}
	return numbers
}

func orderSlice(sliceOfNumbers []int) []int {
	sort.Ints(sliceOfNumbers)
	return sliceOfNumbers
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
		fmt.Println(orderSlice(convertStrToNumbers(inputText)))
	}
	// Your code can go here.
}
