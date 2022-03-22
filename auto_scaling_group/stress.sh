#!/bin/bash
sudo amazon-linux-extras install epel -y
sudo yum install stress -y
stress --cpu 1 --timeout 600
