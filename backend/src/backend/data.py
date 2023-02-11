from fetch_all_data import fetch_all_buildings, fetch_building_data, StatisticType
from database import DatabaseConnection
from sqlite3 import Connection
import csv
import datetime

from typing import Iterable, Any


def populate_database(database: str):
    """Populates the database with data from all the buildings"""
    with DatabaseConnection(database) as db_conn:
        create_db_schema(db_conn)

        buildings = fetch_all_buildings()
        for building in buildings:
            print(f"Fetching minimums for {building}")
            building_min_csv = fetch_building_data(building, StatisticType.MINIMUM)
            parsed = parse_csv(building_min_csv)
            formatted = format_for_inserton(parsed)
            print(f"Inserting minimums for {building} into db")
            with db_conn:
                db_conn.executemany("""
                    INSERT OR IGNORE INTO samples(building_code, timestamp) VALUES (:building, :timestamp);
                """, formatted)
                db_conn.executemany("""
                    UPDATE samples SET min = :sample WHERE building_code = :building AND timestamp = :timestamp;
                """, formatted)

            print(f"Fetching averages for {building}")
            building_avg_csv = fetch_building_data(building, StatisticType.AVERAGE)
            parsed = parse_csv(building_avg_csv)
            formatted = format_for_inserton(parsed)
            print(f"Inserting averages for {building} into db")
            with db_conn:
                db_conn.executemany("""
                    INSERT OR IGNORE INTO samples(building_code, timestamp) VALUES (:building, :timestamp);
                """, formatted)
                db_conn.executemany("""
                    UPDATE samples SET average = :sample WHERE building_code = :building AND timestamp = :timestamp;
                """, formatted)

            print(f"Fetching maximums for {building}")
            building_max_csv = fetch_building_data(building, StatisticType.MAXIMUM)
            parsed = parse_csv(building_max_csv)
            formatted = format_for_inserton(parsed)
            print(f"Inserting maximums for {building} into db")
            with db_conn:
                db_conn.executemany("""
                    INSERT OR IGNORE INTO samples(building_code, timestamp) VALUES (:building, :timestamp);
                """, formatted)
                db_conn.executemany("""
                    UPDATE samples SET max = :sample WHERE building_code = :building AND timestamp = :timestamp;
                """, formatted)


def format_for_inserton(parsed: Iterable[tuple[str]]) -> list[dict[str, Any]]:
    return [
        {"building": bdg, "timestamp": to_unix_timestamp(datestring), "sample": float(value)}
        for bdg, datestring, value in parsed
    ]


def parse_csv(source: str) -> Iterable[tuple[str]]:
    lines = source.splitlines()
    return csv.reader(lines)


def to_unix_timestamp(datestring: str) -> int:
    date_format = datetime.datetime.strptime(datestring, "%Y-%m-%d %H:%M:%S")
    return datetime.datetime.timestamp(date_format)


def create_db_schema(connection: Connection):
    """Creates the db schema if not already present"""
    with connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS samples (
                building_code VARCHAR(64) NOT NULL,
                timestamp INTEGER NOT NULL,
                min REAL,
                max REAL,
                average REAL,
                PRIMARY KEY (building_code, timestamp)
            )
        """)

        connection.execute("""
            CREATE INDEX IF NOT EXISTS idx_buildings_timestamps ON samples (building_code, timestamp)
        """)


if __name__ == "__main__":
    populate_database("test.db")

