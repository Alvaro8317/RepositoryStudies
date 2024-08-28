resource "aws_vpc" "main_vpc_virginia" {
  cidr_block = var.virginia_cidr
  tags = {
    "Name" = "main_vpc_virginia"
  }
}

resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.main_vpc_virginia.id
  cidr_block              = var.subnets[0]
  map_public_ip_on_launch = true
  tags = {
    "Name" = "public_subnet"
  }
}

resource "aws_subnet" "private_subnet" {
  vpc_id     = aws_vpc.main_vpc_virginia.id
  cidr_block = var.subnets[1]
  tags = {
    "Name" = "private_subnet"
  }
}
