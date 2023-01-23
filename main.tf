# creating vpc

#syntex:
#resource "provider_resourcename" "logicalname"

resource "aws_vpc" "vpc1" {
    cidr_block = "10.1.0.0/16"
	tags = {
	  name = "Wipro-vpc"
	  env = "prod_vpc"
	}
}