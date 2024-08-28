resource "aws_s3_bucket" "terraform-course-bucket" {
  bucket = lower(local.s3-sufix)
}
