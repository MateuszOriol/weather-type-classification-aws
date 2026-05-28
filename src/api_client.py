"""Client functions for the shared weather REST API."""

from __future__ import annotations

from typing import Any

import requests

from src.config import BASE_URL, DEFAULT_BATCH_LIMIT, get_api_token


def _headers() -> dict[str, str]:
    return {
        "Authorization": f"Bearer {get_api_token()}"
    }


def fetch_latest_weather(station_id: str) -> dict[str, Any]:
    """Fetch the latest weather measurement for one station."""
    response = requests.get(
        f"{BASE_URL}/weather/latest",
        params={"station_id": station_id},
        headers=_headers(),
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def fetch_batch_weather(
    station_id: str,
    limit: int = DEFAULT_BATCH_LIMIT,
) -> list[dict[str, Any]]:
    """Fetch a batch of weather measurements for one station."""
    response = requests.get(
        f"{BASE_URL}/weather/batch",
        params={
            "station_id": station_id,
            "limit": limit,
        },
        headers=_headers(),
        timeout=30,
    )
    response.raise_for_status()

    data = response.json()

    if isinstance(data, list):
        return data

    if isinstance(data, dict):
        for key in ("records", "items", "measurements", "data", "results"):
            value = data.get(key)
            if isinstance(value, list):
                return value

    raise ValueError(f"Unexpected API response format: {data}")


def fetch_available_stations() -> list[dict[str, Any]]:
    """Fetch available weather stations from the API."""
    response = requests.get(
        f"{BASE_URL}/weather/stations",
        headers=_headers(),
        timeout=30,
    )
    response.raise_for_status()

    data = response.json()

    if isinstance(data, list):
        return data

    if isinstance(data, dict) and "stations" in data:
        return data["stations"]

    raise ValueError(f"Unexpected API response format: {type(data)}")