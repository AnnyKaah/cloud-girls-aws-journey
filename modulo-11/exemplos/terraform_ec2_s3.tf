provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "meu_bucket" {
  bucket = "meu-bucket-iac-2025"
  acl    = "private"
}

resource "aws_instance" "meu_ec2" {
  ami           = "ami-0c02fb55956c7d316"
  instance_type = "t2.micro"
  
  tags = {
    Name = "EC2-Terraform"
  }
}
