"""Rule-based weather type classification logic."""

from __future__ import annotations

from typing import Any


def get_weather_tags(record: dict[str, Any]) -> list[str]:
    """Return all weather tags matching a single weather record."""
    temperature = float(record.get("temperature", 0) or 0)
    humidity = float(record.get("humidity", 0) or 0)
    pressure = float(record.get("pressure", 0) or 0)
    wind_speed = float(record.get("wind_speed", 0) or 0)
    rain_mm = float(record.get("rain_mm", 0) or 0)
    cloud_cover = float(record.get("cloud_cover", 0) or 0)

    tags: list[str] = []

    if rain_mm > 0.5 and cloud_cover > 70:
        tags.append("rainy")

    if wind_speed > 10:
        tags.append("windy")

    if cloud_cover > 80 and rain_mm == 0:
        tags.append("cloudy")

    if temperature > 22:
        tags.append("warm")

    if temperature < 5:
        tags.append("cold")

    if cloud_cover < 30 and rain_mm == 0:
        tags.append("sunny")

    if wind_speed > 12 and cloud_cover > 75 and pressure < 1005:
        tags.append("storm-risk")

    if humidity > 85 and temperature > 24:
        tags.append("humid-hot")

    if not tags:
        tags.append("normal")

    return tags


def get_primary_weather_type(tags: list[str]) -> str:
    """Select one primary weather type using priority rules."""
    priority = [
        "storm-risk",
        "rainy",
        "windy",
        "cloudy",
        "sunny",
        "cold",
        "warm",
        "humid-hot",
        "normal",
    ]

    for weather_type in priority:
        if weather_type in tags:
            return weather_type

    return "normal"


def classify_record(record: dict[str, Any]) -> dict[str, Any]:
    """Add weather classification fields to a single weather record."""
    tags = get_weather_tags(record)

    return {
        **record,
        "weather_tags": tags,
        "primary_weather_type": get_primary_weather_type(tags),
    }


def classify_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Classify a list of weather records."""
    return [classify_record(record) for record in records]