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
