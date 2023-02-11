import requests
import re
import urllib.parse
from enum import Enum


class DataResolution(Enum):
    HOURLY = 3600
    DAILY = 86400


class StatisticType(Enum):
    MINIMUM = "min"
    MAXIMUM = "max"
    AVERAGE = "average"


def fetchAllBuildings() -> list[str]:
    """Returns all building codes from the energy-time-series-map.ttl file"""
    url = "https://data.southampton.ac.uk/dumps/energy-time-series-map/2019-02-04/energy-time-series-map.ttl"
    response = requests.get(url)
    # Pattern match on "" that are not within a <>, i.e. not URIs, that begin with elec
    buildings = re.findall(r'(?<!<)"(elec[^"]*)', response.text)

    return buildings


def fetchBuildingData(building: str, type: StatisticType = StatisticType.AVERAGE, resolution: DataResolution = DataResolution.HOURLY) -> str:
    """
    Returns
    -------
    CSV-formatted string with the `building`'s energy consumption data
    """
    parameters = urllib.parse.urlencode({
        "action": "fetch",
        "series": building,
        "format": "csv",
        "type": type,
        "resolution": resolution,
        "startTime": 0
    })
    url = f"https://data.southampton.ac.uk/time-series?{parameters}"
    energyCsv = requests.get(url)
    return energyCsv.text


def writeDataToFile(data: str, filename: str):
    """Dumps data to a csv file"""
    with open(filename, 'w') as f:
        f.write(data)


def dumpAllData(type: StatisticType = StatisticType.AVERAGE, resolution: DataResolution = DataResolution.HOURLY):
    """
    Dumps all data
    """
    for building in fetchAllBuildings():
        writeDataToFile(fetchBuildingData(building, type, resolution),
                        "./soton-datashame/backend/src/backend/data/" + building.replace('/', '-') + "-" + type + ".csv")
        print("Fetched " + building)


def main():
    dumpAllData("average")
    dumpAllData("min")
    dumpAllData("max")


if __name__ == "__main__":
    main()
