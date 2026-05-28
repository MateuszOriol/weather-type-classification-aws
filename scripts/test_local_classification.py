"""Quick local test for the weather API client and classifier."""

from src.api_client import fetch_batch_weather, fetch_latest_weather
from src.classifier import classify_record, classify_records


def main() -> None:
    station_id = "GDN_01"

    print(f"Fetching latest weather for {station_id}...")
    latest = fetch_latest_weather(station_id)
    classified_latest = classify_record(latest)

    print("\nLatest classified record:")
    print(classified_latest)

    print(f"\nFetching batch weather for {station_id}...")
    records = fetch_batch_weather(station_id, limit=10)
    classified_records = classify_records(records)

    print("\nClassified batch records:")
    for record in classified_records:
        print(
            record.get("timestamp"),
            record.get("station_id"),
            record.get("primary_weather_type"),
            record.get("weather_tags"),
        )


if __name__ == "__main__":
    main()