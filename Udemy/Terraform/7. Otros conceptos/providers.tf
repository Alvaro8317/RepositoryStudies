terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">=4.43.0, <=5.62.0, !=4.43.0"
    }
  }
  required_version = ">=1.3.0"
}

provider "aws" {
  region = "us-east-1"
  default_tags {
    tags = var.tags
  }
}

