variable "virginia_cidr" {
  description = "CIDR Virginia"
  type        = string
  sensitive   = false
}

variable "subnets" {
  description = "List of subnets"
  type        = list(string)
}

variable "tags" {
  description = "Tags del proyecto"
  type        = map(string)
}

variable "sg_ingress_cidr" {
  description = "CIDR for ingress traffic"
  type        = string
}

variable "ec2_specs" {
  description = "Parameters of the instance"
  type        = map(string)
}

variable "instances" {
  description = "Name of the instances"
  type        = list(string)
  default     = ["apache"]
}

variable "enable_monitoring" {
  description = "Habilita el despliegue de un servidor de monitoreo"
  type        = bool
}

variable "ingress_port_list" {
  description = "List of ports to ingress"
  type        = list(number)
}

variable "access_key" {
  description = "Access key of AWS"
}

variable "secret_key" {
  description = "Secret key of AWS"
}
