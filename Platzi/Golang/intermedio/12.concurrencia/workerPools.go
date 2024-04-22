package main

import (
	"fmt"
)

func Worker(id int, jobs <-chan int, results chan<- int) {
	for job := range jobs {
		fmt.Printf("Worker with id %d started fib with %d\n", id, job)
		fib := Finobacci(job)
		fmt.Printf("Worker with id %d, job %d and fib with %d\n", id, job, fib)
		results <- fib
	}
}

func Finobacci(n int) int {
	if n <= 1 {
		return n
	}
	// time.Sleep(2 * time.Second)
	return Finobacci(n-1) + Finobacci(n-2)
}

func mainWP() {
	tasks := []int{2, 3, 4, 5, 7, 10, 12, 40}
	numberWorkers := 3
	jobs := make(chan int, len(tasks))
	results := make(chan int, len(tasks))
	/* Se crean los workers */
	for i := 0; i < numberWorkers; i++ {
		go Worker(i, jobs, results)
	}
	for _, value := range tasks {
		jobs <- value
	}
	close(jobs)
	for j := 0; j < len(tasks); j++ {
		<-results
	}
}
