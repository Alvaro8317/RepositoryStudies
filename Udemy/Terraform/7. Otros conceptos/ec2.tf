
resource "aws_instance" "instance_test" {
  ami                    = var.ec2_specs.ami
  instance_type          = var.ec2_specs.instance_type
  subnet_id              = aws_subnet.public_subnet.id
  key_name               = data.aws_key_pair.ec2_key_pair.key_name
  vpc_security_group_ids = [aws_security_group.sg_instance_ec2.id]
  user_data              = file("./scripts/user-data.sh")
  tags = {
    Name = "Instance test"
  }
  provisioner "local-exec" {
    command = "echo Instance created with the IP ${aws_instance.instance_test.public_ip} >> instance_data.txt"
  }

  provisioner "local-exec" {
    when    = destroy
    command = "echo Instance deleted with the IP ${self.public_ip} >> instance_data.txt"
  }

  # provisioner "remote-exec" {
  #   inline = [
  #     "echo 'Hola mundo' > ~/saludo.txt"
  #   ]
  #   connection {
  #     type        = "ssh"
  #     host        = self.public_ip
  #     user        = "ec2-user"
  #     private_key = file("SOLID.pem")
  #   }
  # }

  # lifecycle {
  #   create_before_destroy = true
  # }
}


# resource "aws_instance" "my_web_server" {

# }
