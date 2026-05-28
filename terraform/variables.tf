variable "aws_region" {
  description = "AWS region used by AWS Academy Learner Lab."
  type        = string
  default     = "us-east-1"
}

variable "cluster_name" {
  description = "Name of the EMR cluster."
  type        = string
  default     = "weather-classification-emr"
}

variable "emr_release" {
  description = "Amazon EMR release version."
  type        = string
  default     = "emr-5.36.0"
}

variable "emr_applications" {
  description = "Applications installed on the EMR cluster."
  type        = list(string)
  default = [
    "Hadoop",
    "Hive",
    "Hue",
    "JupyterEnterpriseGateway",
    "Pig",
    "Spark"
  ]
}

variable "project_bucket_name" {
  description = "Globally unique S3 bucket name for project data, logs, and notebooks."
  type        = string
}

variable "ec2_key_pair" {
  description = "EC2 key pair for SSH access. In AWS Academy this is usually vockey."
  type        = string
  default     = "vockey"
}

variable "emr_service_role" {
  description = "Existing EMR service role."
  type        = string
  default     = "EMR_DefaultRole"
}

variable "emr_ec2_instance_profile" {
  description = "Existing EMR EC2 instance profile."
  type        = string
  default     = "EMR_EC2_DefaultRole"
}

variable "master_instance_type" {
  description = "Primary/master node instance type. Avoid Graviton/ARM instances ending with g."
  type        = string
  default     = "m5.xlarge"
}

variable "core_instance_type" {
  description = "Core node instance type. Avoid Graviton/ARM instances ending with g."
  type        = string
  default     = "m5.xlarge"
}

variable "core_instance_count" {
  description = "Number of core nodes."
  type        = number
  default     = 1
}

variable "idle_timeout_seconds" {
  description = "Auto-terminate cluster after this many idle seconds."
  type        = number
  default     = 3600
}

variable "subnet_id" {
  description = "Subnet ID used by the EMR cluster."
  type        = string
}

variable "master_security_group_id" {
  description = "Security group ID for EMR primary/master node."
  type        = string
}

variable "slave_security_group_id" {
  description = "Security group ID for EMR core/task nodes."
  type        = string
}