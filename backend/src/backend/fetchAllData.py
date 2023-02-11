import requests
import re


'''Returns all building codes from the energy-time-series-map.ttl file'''


def fetchAllBuildings():
    url = 'https://data.southampton.ac.uk/dumps/energy-time-series-map/2019-02-04/energy-time-series-map.ttl'
    response = requests.get(url)
    # Pattern match on "" that are not within a <>, i.e. not URIs, that begin with elec
    buildings = re.findall(r'(?<!<)"(elec[^"]*)', response.text)

    return buildings


'''Returns all energy data for a given building
    building: building code
    resolution: 3600 for hourly data, 86400 for daily data
'''


def fetchBuildingData(building: str, type: str = "average", resolution=3600) -> str:
    url = 'https://data.southampton.ac.uk/time-series?action=fetch&series=' + \
        building + '&format=csv&type=' + type + '&resolution=' + \
        str(resolution) + '&startTime=0'
    buildingMin = requests.get(url)
    return buildingMin.text


'''Dumps data to a csv file'''


def writeDataToFile(data: str, filename: str) -> None:
    with open(filename, 'w') as f:
        f.write(data)


def dumpAllData(type: str = "average", resolution=3600):
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
