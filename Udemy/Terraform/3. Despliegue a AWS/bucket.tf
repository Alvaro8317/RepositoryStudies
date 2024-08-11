resource "aws_s3_bucket" "s3_bucket" {
  count  = 6
  bucket = "alvaro8317-dev-${random_string.sufix[count.index].id}"
  tags = {
    Terraform   = "Practice"
    Environment = "Dev"
  }
}

resource "random_string" "sufix" {
  count   = 6
  length  = 8
  special = false
  upper   = false
  numeric = false
}
