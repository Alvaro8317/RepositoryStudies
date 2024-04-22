package main

import "fmt"

func mainDefer() {
	for i := 0; i <= 5; i++ {
		defer fmt.Println(i)
	}
}
