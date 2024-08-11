terraform {
  required_providers {
    /* AWS Provider version */
    aws = {
      source  = "hashicorp/aws"
      version = ">=4.43.0, <=5.62.0, !=4.43.0"
    }
  }
  /* Terraform version */
  required_version = ">=1.3.0"
}

provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  region = "us-east-2"
  alias  = "ohio"
}
