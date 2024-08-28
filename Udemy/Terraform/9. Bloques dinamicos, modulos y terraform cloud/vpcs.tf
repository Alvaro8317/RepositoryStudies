resource "aws_vpc" "main_vpc_virginia" {
  cidr_block = var.virginia_cidr
  tags = {
    "Name" = "main_vpc_virginia-${local.sufix}"
  }
}

resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.main_vpc_virginia.id
  cidr_block              = var.subnets[0]
  map_public_ip_on_launch = true
  tags = {
    "Name" = "public_subnet-${local.sufix}"
  }
}

resource "aws_subnet" "private_subnet" {
  vpc_id     = aws_vpc.main_vpc_virginia.id
  cidr_block = var.subnets[1]
  tags = {
    "Name" = "private_subnet-${local.sufix}"
  }
  depends_on = [aws_subnet.public_subnet]
}

resource "aws_internet_gateway" "IGW" {
  vpc_id = aws_vpc.main_vpc_virginia.id

  tags = {
    Name = "IGW VPC Virginia-${local.sufix}"
  }
}

resource "aws_route_table" "public_crt" {
  vpc_id = aws_vpc.main_vpc_virginia.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.IGW.id
  }

  tags = {
    Name = "Public CRT-${local.sufix}"
  }
}

resource "aws_route_table_association" "association" {
  subnet_id      = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_crt.id
}

resource "aws_security_group" "sg_instance_ec2" {
  name        = "Segurity Group EC2 Instance TF"
  description = "Allow SSH inbound traffic and all egress traffic"
  vpc_id      = aws_vpc.main_vpc_virginia.id
  dynamic "ingress" {
    for_each = var.ingress_port_list
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = [var.sg_ingress_cidr]
    }
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "Segurity Group EC2 Instance TF-${local.sufix}"
  }
}

module "bucket-s3" {
  source      = "./modules/s3"
  bucket_name = lower(local.s3-sufix)
}

output "s3_arn" {
  value = module.bucket-s3.s3_bucket_arn
}
module "terraform_state_backend" {
  source     = "cloudposse/tfstate-backend/aws"
  version    = "1.5.0"
  namespace  = "example"
  stage      = "dev"
  name       = "terraform"
  attributes = ["state"]
  environment = "us-east-1"
  terraform_backend_config_file_path = "."
  terraform_backend_config_file_name = "backend.tf"
  force_destroy                      = false
}

