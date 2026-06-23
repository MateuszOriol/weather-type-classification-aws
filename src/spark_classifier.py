"""PySpark weather classification transformations."""

from __future__ import annotations

from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def add_weather_tags(df: DataFrame) -> DataFrame:
    """Add boolean weather tag columns to a Spark DataFrame."""
    return (
        df
        .withColumn(
            "is_rainy",
            (F.col("rain_mm") > 0.5) & (F.col("cloud_cover") > 70),
        )
        .withColumn(
            "is_windy",
            F.col("wind_speed") > 10,
        )
        .withColumn(
            "is_cloudy",
            (F.col("cloud_cover") > 80) & (F.col("rain_mm") == 0),
        )
        .withColumn(
            "is_warm",
            F.col("temperature") > 22,
        )
        .withColumn(
            "is_cold",
            F.col("temperature") < 5,
        )
        .withColumn(
            "is_sunny",
            (F.col("cloud_cover") < 30) & (F.col("rain_mm") == 0),
        )
        .withColumn(
            "is_storm_risk",
            (F.col("wind_speed") > 12)
            & (F.col("cloud_cover") > 75)
            & (F.col("pressure") < 1005),
        )
        .withColumn(
            "is_humid_hot",
            (F.col("humidity") > 85) & (F.col("temperature") > 24),
        )
    )


def add_primary_weather_type(df: DataFrame) -> DataFrame:
    """Add one primary weather type based on priority rules."""
    return df.withColumn(
        "primary_weather_type",
        F.when(F.col("is_storm_risk"), "storm-risk")
        .when(F.col("is_rainy"), "rainy")
        .when(F.col("is_windy"), "windy")
        .when(F.col("is_cloudy"), "cloudy")
        .when(F.col("is_sunny"), "sunny")
        .when(F.col("is_cold"), "cold")
        .when(F.col("is_warm"), "warm")
        .when(F.col("is_humid_hot"), "humid-hot")
        .otherwise("normal"),
    )


def add_weather_tags_array(df: DataFrame) -> DataFrame:
    """Add an array column with all matching weather tags."""
    tags_array = F.array_remove(
        F.array(
            F.when(F.col("is_storm_risk"), F.lit("storm-risk")),
            F.when(F.col("is_rainy"), F.lit("rainy")),
            F.when(F.col("is_windy"), F.lit("windy")),
            F.when(F.col("is_cloudy"), F.lit("cloudy")),
            F.when(F.col("is_sunny"), F.lit("sunny")),
            F.when(F.col("is_cold"), F.lit("cold")),
            F.when(F.col("is_warm"), F.lit("warm")),
            F.when(F.col("is_humid_hot"), F.lit("humid-hot")),
        ),
        None,
    )

    return df.withColumn(
        "weather_tags",
        F.when(F.size(tags_array) == 0, F.array(F.lit("normal"))).otherwise(tags_array),
    )


def classify_weather_df(df: DataFrame) -> DataFrame:
    """Apply full weather classification to a Spark DataFrame."""
    tagged_df = add_weather_tags(df)
    tagged_df = add_primary_weather_type(tagged_df)
    return add_weather_tags_array(tagged_df)


def get_weather_type_counts(df: DataFrame) -> DataFrame:
    """Count records by primary weather type."""
    return (
        df
        .groupBy("primary_weather_type")
        .count()
        .orderBy(F.desc("count"))
    )