"""Run a small local weather classification pipeline."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

from src.api_client import fetch_batch_weather
from src.classifier import classify_records


DATA_DIR = Path("data")
RESULTS_DIR = Path("results")


def save_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def save_counts_csv(path: Path, counts: Counter[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["primary_weather_type", "count"])

        for weather_type, count in counts.most_common():
            writer.writerow([weather_type, count])


def main() -> None:
    station_id = "GDN_01"
    limit = 100

    print(f"Fetching {limit} weather records for {station_id}...")
    records = fetch_batch_weather(station_id=station_id, limit=limit)

    print("Classifying records...")
    classified_records = classify_records(records)

    counts = Counter(
        record["primary_weather_type"]
        for record in classified_records
    )

    raw_path = DATA_DIR / "sample_raw" / f"{station_id}_raw.json"
    classified_path = DATA_DIR / "sample_classified" / f"{station_id}_classified.json"
    counts_path = RESULTS_DIR / "weather_type_counts.csv"

    save_json(raw_path, records)
    save_json(classified_path, classified_records)
    save_counts_csv(counts_path, counts)

    print("\nWeather type counts:")
    for weather_type, count in counts.most_common():
        print(f"{weather_type}: {count}")

    print(f"\nSaved raw data to: {raw_path}")
    print(f"Saved classified data to: {classified_path}")
    print(f"Saved counts to: {counts_path}")


if __name__ == "__main__":
    main()