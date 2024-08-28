
resource "aws_instance" "instance_test" {
  ami           = "ami-0ae8f15ae66fe8cda"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.public_subnet.id
  tags = {
    Name = "Instance test"
  }
}
