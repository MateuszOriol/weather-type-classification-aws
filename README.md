# Weather Type Classification on AWS EMR

This project implements Project 5: Weather Type Classification.

The goal is to collect weather measurements from a shared REST API, classify each measurement into weather types, and produce a classified dataset with visual summaries.

## Weather Classes

Example classes:

- sunny
- cloudy
- rainy
- windy
- cold
- warm
- humid-hot
- storm-risk
- normal

## Architecture

The project uses:

- AWS Academy
- Amazon EMR on EC2
- EMR Studio / JupyterLab
- PySpark
- S3
- Terraform
- Python

## Project Structure

```text
weather-type-classification-aws/
├── docs/
│   └── classification_strategy.md
├── notebooks/
│   └── weather_classification_emr.ipynb
├── src/
│   ├── __init__.py
│   ├── api_client.py
│   ├── classifier.py
│   └── config.py
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── terraform.tfvars.example
├── requirements.txt
└── README.md