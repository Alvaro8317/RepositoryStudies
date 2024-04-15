package main

import "fmt"

func message(text string, channel chan string) {
	channel <- text
}

func channelsCloseRangeYSelect() {
	/* Se pueden manejar múltiples channels */
	myChannel := make(chan string, 2)
	myChannel <- "Mensaje1"
	// myChannel <- "Mensaje2"
	/* Len indica la longitud */
	/* Cap indica la longitud máxima */
	fmt.Println(len(myChannel), cap(myChannel))

	/* Range y close */
	/* Close indica que se cerrara un canal, para que no pueda recibir más datos */
	/* Si se le intenta insertar más datos de los permitidos en el make, dará error */
	/* Lo ideal es cerrar los canales */
	close(myChannel)
	/* Range es para iterar un canál, aunque se recomienda cerrarlo antes */
	for message := range myChannel {
		fmt.Println(message)
	}
	/* Select */
	myChannelEmail := make(chan string)
	myChannelEmail2 := make(chan string)
	go message("mensaje1", myChannelEmail)
	go message("mensaje2", myChannelEmail2)
	for i := 0; i < 2; i++ {
		select {
		/* Message es para guardar la salida del canál */
		case message1 := <-myChannelEmail:
			fmt.Println("Email recibido de", message1)
		case message2 := <-myChannelEmail2:
			fmt.Println("Email recibido de", message2)
		}
	}
}
