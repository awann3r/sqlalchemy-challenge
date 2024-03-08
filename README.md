# SQLAlchemy-challenge
## Background
For this module challenge, we are tasked to leverage what we've learned in module 10 to analyze the climate in Hawaii 
before a long holiday vacation! 

## Challenge Summary
The required outputs from this challenge can be found within this repository:
* Jupyter Notebook with climate analysis 
* API SQLite Connection & Landing Page
* Resources folder with data files
* Image files from analysis

## Instructions
The objective of this challenge is to use Python and SQLAlchemy to do a basic climate analysis and data exploration. 
Additionally, design a Flask API based on the queries that was developed.

#### Analyze and Explore the Climate Data
The climate_starter.ipnyb file shows the analysis and data exploration conducted using the database provided in the 
Resources folder (`hawaai.sqlite`). Leveraged the `create_engine()` to connect the database, and `automap_base()`
to refelect the tables into classes. From there, an analysis of the precipitation for a year was queried and plotted as
a bar graph (file saved in repository as `Precipitation_Hawaii`). Another analysis was condected to query the most active stations.From this, further query was done to analyze the temperature observations (TOBS) of previous 12 months and plotted as a histogram (file saved in repository as `Temperatures_station_USC00519281`).

#### Desing Climate App
The app.py file shows the creation of a server API using Flask and engine session connections from the database provided in
Resources folder (`hawaii.sqlite`). Used Flask to create the various routes which included a homepage that showed all the api routes available for selection. Each api route returns information queried from the database.
NOTE: I was unable to finish the last two routes (`/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`) as I ran out of time researching how to query the data.





