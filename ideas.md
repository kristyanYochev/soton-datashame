<!-- # Ideas

Come up with a list of ideas for the hackathon. We have 24 hours.

## Theme: Improve sustainability on campus

The three pillars of sustainability are: environmental, economic, and social. We can choose to focus on one or all three

### Recycler

App of some kind that if you scan a product, will tell you if it is recyclable or not.
Tells you closest place to recycle it.

### Campus CEX

Sell old electronics

### Electronic notes

Innovate the way we take notes in class
Notion, Google Docs, etc.
To improve sustainability, we can make

## Smart breakers/ heatMap/ PowerWatch

Do a university implementation of PowerWatch. Do a campus map of where power is being used. Use smart breakers to turn off power to certain areas, when not in use.
Profitable for the university, and for the environment.

## Open Data Visualisation

LETS REQUEST GIGABYTES OF DATA FROM THE UNIVERSITY
Create a data visualisation tool for the energy use of each building in the university.
Promotes sustainabality through guilt and shame.

## Technologies

React
Some kinda backend
API stuffs -->

# Documentation for Open Data Service Energy Time Series

## Introduction

The university has no idea what they are doing. They have a bunch of data, but no idea how to use it. We can help them out.
Find below a brief summary of the API calls needed to get the data we need.
Still figuring out any new parameters that need to be added to the API calls.

## API Call Params

Example URL: <https://data.southampton.ac.uk/time-series?action=fetch&series=elec/b59/ekw&format=html&type=max&resolution=3600&startTime=0>

### action

* fetch
* info

### series

The series of data to fetch. The series is a combination of the type of data and the building.
Find the list of buildings here: <https://data.southampton.ac.uk/time-series>
The old data uses the format ```elec/b59/ekw``` where ```b59``` is the building code and ```ekw``` is the type of data.
The new data uses the format ```wsavail/36-lvl04/units``` where units may be ```units``` or ```ratio```.
The
We have found that the majority of buidlings have data up to the very end of 2020. Some buildings then have room data up to the present day. These rooms seem to be computer rooms. Not all data is reliable.

May be better if we restrict the data to data published before 2021/2020

### format

* html
* csv
* json
  
### type

* min
* max
* average

### resolution

Only two identified resolutions so far, but can interpolate between them.

* 3600 - This is for hourly data
* 86400 - This is for daily data

### startTime

Fairly self explanatory. The start time of the data to fetch. This is in epoch time.
