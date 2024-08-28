variable "instances_in_set" {
  description = "Name of instances in a set"
  type        = set(string)
  default     = ["apache"]
}

resource "aws_instance" "instance_test" {
  ami                    = var.ec2_specs.ami
  for_each               = toset(var.instances)
  instance_type          = var.ec2_specs.instance_type
  subnet_id              = aws_subnet.public_subnet.id
  key_name               = data.aws_key_pair.ec2_key_pair.key_name
  vpc_security_group_ids = [aws_security_group.sg_instance_ec2.id]
  user_data              = file("./scripts/user-data.sh")
  tags = {
    Name = "${each.value}-${local.sufix}"
  }
}
