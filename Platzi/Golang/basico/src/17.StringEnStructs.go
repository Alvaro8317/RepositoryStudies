package main

import "fmt"

type pc struct {
	ram   int
	brand string
	disk  int
}

func (myPc pc) String() string {
	return fmt.Sprintf("Tengo %d GB de RAM, %d GB de disco y es un %s", myPc.ram, myPc.disk, myPc.brand)
}

func stringsEnStructs() {
	myPc := pc{ram: 16, brand: "asus", disk: 100}
	/* Los Struct tiene un método llamado String que se puede sobreescribir, comportamiento
	similar al polimorfismo */
	fmt.Println(myPc)
}
