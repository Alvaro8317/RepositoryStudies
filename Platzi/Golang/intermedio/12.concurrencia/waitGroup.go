package main

import (
	"fmt"
	"sync"
	"time"
)

func mainWaitGroup() {
	/* Se crea el waitgroup */
	var waitGroup sync.WaitGroup
	for i := 0; i < 10; i++ {
		/* Se le suma en 1 para decirle a waitGroup que hay una go routine en proceso*/
		waitGroup.Add(1)
		go doSomething(i, &waitGroup)
	}
	/* Wait siempre espera a que llegue a 0 */
	waitGroup.Wait()
}
func doSomething(i int, wg *sync.WaitGroup) {
	/* defer se ejecuta siempre al final de cada función, se le indica que se murió esta go routine, con Done se reduce en 1 el contador del wg */
	defer wg.Done()
	fmt.Printf("Empezó la ejecución número: %d", i)
	fmt.Println("Iniciando proceso pesado")
	time.Sleep(2 * time.Second)
	fmt.Println("Finalizando proceso pesado")
}
