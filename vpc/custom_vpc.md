# Create Custom VPC
Name: MyVPC
IPv4 CIDR Block: 10.0.0.0/16

# Create Subnets

Name: Public-1A
Availability Zone: us-east-1a
IPv4 CIDR Block: 10.0.1.0/24

Name: Public-1B
Availability Zone: us-east-1b
IPv4 CIDR Block: 10.0.2.0/24

Name: Private-1A
Availability Zone: us-east-1a
IPv4 CIDR Block: 10.0.3.0/24

Name: Private-1B
Availability Zone: us-east-1b
IPv4 CIDR Block: 10.0.4.0/24

# Create private route table

Name: Private-RT
VPC: MyVPC
Subnet associations: Private-1A, Private-1B

# Create Internet Gateway

Name: MyIGW
VPC: MyVPC

# Add IGW route to Public RT

Destination: 0.0.0.0/0
Target: IGW

# Create NAT Gateway

Name: my-nat-gw
Subnet: Public Subnet

# Add NGW route to Private RT

Destination: 0.0.0.0/0
Target: NGW

# Create a Security Group with 2 rules

Name: my-security-group

Inbound: All traffic 
Source: Anywhere IPv4

Outbound: All traffic 
Source: Anywhere IPv4
