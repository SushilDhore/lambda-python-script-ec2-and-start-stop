EC2 Instance Control with AWS Lambda


This repository contains Python scripts and configuration files to create AWS Lambda functions for starting and stopping EC2 instances. These scripts can be used to automate the management of your EC2 instances in response to various triggers.


Table of Contents
1) Introduction
2) Prerequisites


Introduction : 
Managing the state of AWS EC2 instances manually can be time-consuming. This repository provides two Python scripts and guidance to create AWS Lambda functions that automatically start or stop EC2 instances based on specific events. These functions can be triggered by various AWS services like CloudWatch Events, API Gateway, or even external events through AWS SDKs.

'Prerequisites'
Before you begin, ensure you have the following:

An AWS account with necessary permissions to create Lambda functions and manage EC2 instances.
Created lambda function must have appropriate IAM permission to call EC2 instance on behalf Lambda

" Contributing "
Contributions to this repository are welcome! 

If you find any issues or have improvements to suggest, please open an issue or create a pull request.