terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">=4.43.0, <=5.62.0, !=4.43.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "3.4.3"
    }
  }
  required_version = ">=1.3.0"
}

provider "aws" {
  region     = "us-east-1"
  access_key = var.access_key
  secret_key = var.secret_key
  default_tags {
    tags = var.tags
  }
}

