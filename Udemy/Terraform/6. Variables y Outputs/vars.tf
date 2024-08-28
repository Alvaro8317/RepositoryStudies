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
