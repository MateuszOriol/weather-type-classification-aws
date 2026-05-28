# Weather Type Classification Strategy

## Goal

The goal of this project is to classify weather measurements into readable weather types such as sunny, cloudy, rainy, windy, warm, cold, unstable, and storm-risk.

The classification is based on weather measurements from the shared REST API.

## Input Variables

The classification logic uses the following variables:

- temperature
- humidity
- pressure
- wind_speed
- rain_mm
- cloud_cover

## Rule-Based Classification

The first version of the project uses rule-based classification because the API provides measurements but does not provide manually labeled weather classes.

Example rules:

| Weather type | Rule |
|---|---|
| rainy | rain_mm > 0.5 and cloud_cover > 70 |
| windy | wind_speed > 10 |
| cloudy | cloud_cover > 80 and rain_mm == 0 |
| warm | temperature > 22 |
| cold | temperature < 5 |
| sunny | cloud_cover < 30 and rain_mm == 0 |
| storm-risk | wind_speed > 12 and cloud_cover > 75 and pressure < 1005 |
| humid-hot | humidity > 85 and temperature > 24 |

## Multiple Tags

A single weather record can match multiple conditions.

Example:

```text
temperature = 24
rain_mm = 1.2
cloud_cover = 90
wind_speed = 12