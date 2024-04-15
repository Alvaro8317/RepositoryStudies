package main

import (
	"fmt"
	"log"
	"strconv"
)

func ifElse() {
	value1 := 1
	value2 := 2
	if value1 == 1 {
		fmt.Println("value1 es 1")
	} else {
		fmt.Println("value1 no es 1 :(")
	}
	if value1 == 1 && value2 == 2 {
		fmt.Println("Asombroso, ambos cumplen la condición")
	}
	if value1 == 1 || value2 == 2 {
		fmt.Println("Solo uno cumple la condición 🤔")
	}
	if value1 != 10 {
		fmt.Println("Value1 no es 10 :3")
	}
	/* Text a number */
	value, err := strconv.Atoi("a53")
	/* nil indica si una función tuvo error o no */
	if err != nil {
		fmt.Println(err)
		fmt.Println(err)
		fmt.Println(err)
		log.Fatal(err)
	}
	fmt.Println("Value: ", value)
}
