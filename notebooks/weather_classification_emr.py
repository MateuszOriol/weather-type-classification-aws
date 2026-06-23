# Weather Type Classification on AWS EMR
#
# Project 5: Weather Type Classification
#
# This notebook collects weather data from the shared REST API,
# classifies weather records, summarizes weather types, and saves
# classified data to S3.

# %%
import os
import sys

PROJECT_ROOT = "/home/notebook/weather-type-classification-aws"

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# %%
from src.api_client import fetch_batch_weather
from src.spark_classifier import classify_weather_df, get_weather_type_counts

# %%
STATION_ID = "GDN_01"
LIMIT = 100

records = fetch_batch_weather(station_id=STATION_ID, limit=LIMIT)

len(records), records[:2]

# %%
raw_df = spark.createDataFrame(records)

raw_df.printSchema()
raw_df.show(5, truncate=False)

# %%
classified_df = classify_weather_df(raw_df)

classified_df.select(
    "timestamp",
    "station_id",
    "temperature",
    "humidity",
    "pressure",
    "wind_speed",
    "rain_mm",
    "cloud_cover",
    "primary_weather_type",
    "weather_tags",
).show(20, truncate=False)

# %%
counts_df = get_weather_type_counts(classified_df)

counts_df.show(truncate=False)

# %%
PROJECT_BUCKET = "weather-classification-tf-662832404229-2605"

classified_output_path = (
    f"s3://{PROJECT_BUCKET}/processed/weather_classified/station_id={STATION_ID}/"
)

counts_output_path = (
    f"s3://{PROJECT_BUCKET}/results/weather_type_counts/station_id={STATION_ID}/"
)

classified_df.write.mode("overwrite").parquet(classified_output_path)
counts_df.write.mode("overwrite").csv(counts_output_path, header=True)

classified_output_path, counts_output_path

# %%
# Convert counts to pandas for a simple chart.
# This is okay because the aggregated result is small.

counts_pdf = counts_df.toPandas()
counts_pdf

# %%
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.bar(
    counts_pdf["primary_weather_type"],
    counts_pdf["count"],
)
plt.title("Weather Type Counts")
plt.xlabel("Weather type")
plt.ylabel("Count")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()