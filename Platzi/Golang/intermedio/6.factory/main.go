package main

import "fmt"

/*
* Con interfaces se puede usar el patrón de diseño abstract factory
* por convención, las interfaces empiezan con I
 */
/* INotificationFactory -> SMSNotification / EmailNotification */
type INotificationFactory interface {
	SendNotification()
	GetSender() ISender
}

/* ISender -> Struct SMSNotificationSender / EmailNotificationSender*/
type ISender interface {
	GetSenderMethod() string
	GetSenderChannel() string
}

/* SMS */
type SMSNotification struct {
}

func (SMSNotification) SendNotification() {
	fmt.Println("Sending notification via SMS")
}

func (SMSNotification) GetSender() ISender {
	return SMSNotificationSender{}
}

/* SMSSender */
type SMSNotificationSender struct {
}

func (SMSNotificationSender) GetSenderMethod() string {
	return "SMS"
}
func (SMSNotificationSender) GetSenderChannel() string {
	return "Twilio"
}

/* Email */
type EmailNotification struct {
}

func (EmailNotification) SendNotification() {
	fmt.Println("Sending notification via correo")
}

func (EmailNotification) GetSender() ISender {
	return EmailNotificationSender{}
}

/* EmailSender */
type EmailNotificationSender struct {
}

func (EmailNotificationSender) GetSenderMethod() string {
	return "Email"
}
func (EmailNotificationSender) GetSenderChannel() string {
	return "SES"
}

/* Instancia del factory, retorna un INotificationFactory o error */
/* Go no tiene un try catch, por lo que a una función se le devuelve el resultado y el error
* si el error es nil, es porque no hubo error */
func getNotificationFactory(notificationType string) (INotificationFactory, error) {
	if notificationType == "SMS" {
		return &SMSNotification{}, nil
	}
	if notificationType == "Email" {
		return &EmailNotification{}, nil
	}
	return nil, fmt.Errorf("No notification type")
}

func sendNotification(factory INotificationFactory) {
	factory.SendNotification()
}

func getMethod(factory INotificationFactory) {
	fmt.Println(factory.GetSender().GetSenderMethod())
}

func main() {
	smsFactory, _ := getNotificationFactory("SMS")
	emailFactory, _ := getNotificationFactory("Email")
	sendNotification(smsFactory)
	sendNotification(emailFactory)
	getMethod(smsFactory)
	getMethod(emailFactory)
}
