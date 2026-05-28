output "emr_cluster_id" {
  description = "ID of the created EMR cluster."
  value       = aws_emr_cluster.weather_classification.id
}

output "emr_cluster_name" {
  description = "Name of the created EMR cluster."
  value       = aws_emr_cluster.weather_classification.name
}

output "project_bucket_name" {
  description = "S3 bucket used for project files and logs."
  value       = aws_s3_bucket.project_bucket.bucket
}

output "emr_log_uri" {
  description = "S3 location for EMR logs."
  value       = aws_emr_cluster.weather_classification.log_uri
}