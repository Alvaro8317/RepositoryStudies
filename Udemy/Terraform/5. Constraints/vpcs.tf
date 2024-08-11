resource "aws_vpc" "main_vpc_virginia" {
  cidr_block = "10.10.0.0/16"
  tags = {
    Name = "VPC_Virginia"
    Env  = "Dev"
  }
}

resource "aws_vpc" "main_vpc_ohio" {
  cidr_block = "10.10.0.0/16"
  provider   = aws.ohio
  tags = {
    Name = "VPC_Virginia"
    Env  = "Dev"
  }
}
