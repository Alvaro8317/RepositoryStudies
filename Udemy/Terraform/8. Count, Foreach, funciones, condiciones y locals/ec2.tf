variable "instances_in_set" {
  description = "Name of instances in a set"
  type        = set(string)
  default     = ["apache", "mysql", "jumpserver"]
}

resource "aws_instance" "instance_test" {
  ami = var.ec2_specs.ami
  # count                  = length(var.instances)
  # for_each               = var.instances_in_set
  for_each               = toset(var.instances)
  instance_type          = var.ec2_specs.instance_type
  subnet_id              = aws_subnet.public_subnet.id
  key_name               = data.aws_key_pair.ec2_key_pair.key_name
  vpc_security_group_ids = [aws_security_group.sg_instance_ec2.id]
  user_data              = file("./scripts/user-data.sh")
  tags = {
    # Name = var.instances[count.index]
    Name = "${each.value}-${local.sufix}"
  }
}

resource "aws_instance" "monitor_test" {
  count                  = var.enable_monitoring ? 1 : 0
  ami                    = var.ec2_specs.ami
  # for_each               = toset(var.instances)
  instance_type          = var.ec2_specs.instance_type
  subnet_id              = aws_subnet.public_subnet.id
  key_name               = data.aws_key_pair.ec2_key_pair.key_name
  vpc_security_group_ids = [aws_security_group.sg_instance_ec2.id]
  user_data              = file("./scripts/user-data.sh")
  tags = {
    Name = "Monitoreo-${local.sufix}"
  }
}
