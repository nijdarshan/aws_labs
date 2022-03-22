#!/bin/bash
sudo su
yum update -y
yum install -y httpd
systemctl start httpd.service
systemctl enable httpd.service
echo "<h1> At $(hostname -f) </h1>" > /var/www/html/index.html
