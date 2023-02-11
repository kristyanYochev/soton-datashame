import sqlite3
from typing import Self

class DatabaseConnection:
    def __init__(self, database_path: str) -> None:
        self.connection = sqlite3.connect(database_path)

    def __enter__(self) -> sqlite3.Connection:
        return self.connection

    def __exit__(self, *args):
        self.connection.close()
