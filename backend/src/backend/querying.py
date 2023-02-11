from database import DatabaseConnection
from fetch_all_data import StatisticType

from typing import Self


class Query:
    def __init__(self) -> None:
        self.building: str = None
        self.stat_type: StatisticType = None
        self.year: int = None
        self.month: int = None
        self.day: int = None



class QueryBuilder:
    def __init__(self) -> None:
        self.query = Query()

    def building(self, building_code: str) -> Self:
        self.query.building = building_code
        return self
    
    def statistic_type(self, stat_type: StatisticType) -> Self:
        self.query.stat_type = stat_type
        return self
    
    def year(self, year: int) -> Self:
        assert 2000 <= year <= 2100
        self.query.year = year
        return self

    def month(self, month: int) -> Self:
        assert 1 <= month <= 12
        self.query.month = month
        return self

    def day(self, day: int) -> Self:
        assert 1 <= day <= 31
        self.query.day = day
        return self

    def build(self) -> Query:
        return self.query
