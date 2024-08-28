resource "aws_s3_bucket" "terraform-course-bucket" {
  bucket = var.bucket_name
}
