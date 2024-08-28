locals {
  sufix    = "${var.tags.Project}-${var.tags.Env}"
  s3-sufix = "${var.tags.Project}-${random_string.sufix-s3.id}"
}

resource "random_string" "sufix-s3" {
  length  = 8
  special = false
  upper   = false
}
