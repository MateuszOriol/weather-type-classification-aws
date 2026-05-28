terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "project_bucket" {
  bucket = var.project_bucket_name
}

resource "aws_s3_bucket_public_access_block" "project_bucket_public_access" {
  bucket = aws_s3_bucket.project_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_emr_cluster" "weather_classification" {
  name          = var.cluster_name
  release_label = var.emr_release
  applications  = var.emr_applications

  service_role = var.emr_service_role

  log_uri = "s3://${aws_s3_bucket.project_bucket.bucket}/logs/elasticmapreduce/"

  ec2_attributes {
    key_name                          = var.ec2_key_pair
    instance_profile                  = var.emr_ec2_instance_profile
    subnet_id                         = var.subnet_id
    emr_managed_master_security_group = var.master_security_group_id
    emr_managed_slave_security_group  = var.slave_security_group_id
  }

  master_instance_group {
    instance_type = var.master_instance_type
    instance_count = 1
  }

  core_instance_group {
    instance_type  = var.core_instance_type
    instance_count = var.core_instance_count
  }

  termination_protection = false
  keep_job_flow_alive_when_no_steps = true

  auto_termination_policy {
    idle_timeout = var.idle_timeout_seconds
  }

  configurations_json = jsonencode([
    {
      Classification = "spark-defaults"
      Properties = {
        "spark.sql.shuffle.partitions" = "4"
      }
    }
  ])

  tags = {
    Project = "weather-type-classification"
    ManagedBy = "terraform"
  }
}