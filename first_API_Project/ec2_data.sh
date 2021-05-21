#!/bin/bash
# Use this for your user data (script from top to bottom)
#install httpd (linux 2 version)
yum update -y
yum install -y httpd
systemctrl start httpd
systemctrl enable httpd
echo  "<h1> hello world from $(hostname -f)</h1>" > /var/www/html/index.html