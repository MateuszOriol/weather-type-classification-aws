"""Project configuration for the weather classification pipeline."""

from __future__ import annotations

import os

BASE_URL = "https://e6uw49pbah.execute-api.us-east-1.amazonaws.com/dev"

DEFAULT_STATIONS = [
    "GDN_01",
    "GDN_02",
    "GDY_01",
    "SOP_01",
]

DEFAULT_BATCH_LIMIT = 100


def get_api_token() -> str:
    """Return the weather API token from environment variables."""
    token = os.getenv("WEATHER_API_TOKEN")

    if not token:
        raise ValueError(
            "Missing WEATHER_API_TOKEN environment variable. "
            "Set it before running the pipeline."
        )

    return token