import requests
import re
from urllib.parse import urlencode
from enum import IntEnum, StrEnum


class DataResolution(IntEnum):
    HOURLY = 3600
    DAILY = 86400


class StatisticType(StrEnum):
    MINIMUM = "min"
    MAXIMUM = "max"
    AVERAGE = "average"


def fetch_all_buildings() -> list[str]:
    """Returns all building codes from the energy-time-series-map.ttl file"""
    url = "https://data.southampton.ac.uk/dumps/energy-time-series-map/2019-02-04/energy-time-series-map.ttl"
    response = requests.get(url)
    # Pattern match on "" that are not within a <>, i.e. not URIs, that begin with elec
    buildings = re.findall(r'(?<!<)"(elec[^"]*)', response.text)

    return buildings


def fetch_building_data(building: str, type: StatisticType = StatisticType.AVERAGE, resolution: DataResolution = DataResolution.HOURLY) -> str:
    """
    Returns
    -------
    CSV-formatted string with the `building`'s energy consumption data
    """
    parameters = urlencode({
        "action": "fetch",
        "series": building,
        "format": "csv",
        "type": str(type),
        "resolution": str(resolution),
        "startTime": 0
    })
    url = f"https://data.southampton.ac.uk/time-series?{parameters}"
    energy_csv = requests.get(url)
    return energy_csv.text


def write_data_to_file(data: str, filename: str):
    """Dumps data to a csv file"""
    with open(filename, 'w') as f:
        f.write(data)


def dump_all_data(type: StatisticType = StatisticType.AVERAGE, resolution: DataResolution = DataResolution.HOURLY):
    """
    Dumps all data
    """
    for building in fetch_all_buildings():
        write_data_to_file(fetch_building_data(building, type, resolution),
                        "./soton-datashame/backend/src/backend/data/" + building.replace('/', '-') + "-" + type + ".csv")
        print("Fetched " + building)


def main():
    TEST_BUILDING_ID = "elec/b16/ekw"
    energyCsv = fetch_building_data(TEST_BUILDING_ID)
    print(energyCsv)


if __name__ == "__main__":
    main()
