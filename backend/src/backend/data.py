from fetch_all_data import fetch_all_buildings, fetch_building_data
from database import DatabaseConnection
from sqlite3 import Connection


def populate_database(database: str):
    """Populates the database with data from all the buildings"""
    with DatabaseConnection(database) as db_conn:
        verify_db_schema(db_conn)


def verify_db_schema(connection: Connection):
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

