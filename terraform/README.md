# Terraform - Weather Type Classification AWS Infrastructure

This Terraform configuration creates the AWS infrastructure for the Weather Type Classification project.

## Resources

- S3 bucket for project data and EMR logs
- EMR cluster on EC2
- Spark/Hadoop/Hive/Hue/Pig/JupyterEnterpriseGateway applications
- Auto-termination after idle time

## Usage

Copy the example variables file:

```bash
cp terraform.tfvars.example terraform.tfvars