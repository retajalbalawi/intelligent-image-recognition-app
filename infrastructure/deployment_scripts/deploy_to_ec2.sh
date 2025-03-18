#!/bin/bash

echo "Deploying app to EC2 instance..."

scp -i your-key.pem backend/target/app.jar ubuntu@your-ec2-ip:~/

ssh -i your-key.pem ubuntu@your-ec2-ip "java -jar app.jar &"
