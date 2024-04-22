package main

import (
	"fmt"
	"sync"
	"time"
)

func mainSem() {
	channelInteger := make(chan int, 2)
	var wg sync.WaitGroup
	for i := 0; i < 10; i++ {
		/* El go routine principal se bloquea hasta que se consume datos del channel de la función pesada, por eso, con un canál con buffer se pueden definir la cantidad de tareas que puede correr paralelamente */
		channelInteger <- 1
		wg.Add(1)
		go heavyFunction(i, &wg, channelInteger)
	}
	wg.Wait()
}

func heavyFunction(i int, wg *sync.WaitGroup, channel <-chan int) {
	defer wg.Done()
	fmt.Printf("Id: %d started \n", i)
	time.Sleep(4 * time.Second)
	fmt.Printf("Id: %d finished \n", i)
	<-channel
}
