
# Import the dependencies.
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
#################################################
# Database Setup
#################################################
# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# Declare a Base using `automap_base()`
Base = automap_base()
# Use the Base class to reflect the database tables
Base.prepare(engine, reflect=True)
# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create a session
session = Session(engine)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################
#define homepage
@app.route("/")
def homepage():
    return (
        f"Welcome to the Hawaii Climate API<br/>"
        f"List of available API routes:<br/>"
        f"<a href=\"/api/v1.0/precipitation\">/api/v1.0/precipitation</a><br/>"
        f"<a href=\"/api/v1.0/stations\">/api/v1.0/stations</a><br/>"
        f"<a href=\"/api/v1.0/tobs\">/api/v1.0/tobs</a><br/>"
        f"<a href=\"/api/v1.0/start\">/api/v1.0/start</a><br/>"
        f"<a href=\"/api/v1.0/start/end\">/api/v1.0/start/end</a><br/>"
    )
#define precipitation 
@app.route("/api/v1.0/precipitation")
def precipitation():
    prcp_query = session.query(Measurement.date, Measurement.prcp).all()
    session.close()
    prcp_list = []
    for date, prcp in prcp_query:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        prcp_list.append(prcp_dict)
    return jsonify(prcp_list)

#define station
@app.route("/api/v1.0/stations")
def station():
    station_list = session.query(Station.station).all()
    session.close()
    station_list = list(np.ravel(station_list))
    return jsonify(station_list)

#define tobs
@app.route("/api/v1.0/tobs")
def tobs():
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_date = dt.datetime.strptime(most_recent_date[0], '%Y-%m-%d')
    first_date = last_date - dt.timedelta(days=365)
    temps_data = session.query(Measurement.date, Measurement.tobs).\
        filter(func.strftime(Measurement.date) >= first_date, Measurement.station == 'USC00519281').\
        group_by(Measurement.date).\
        order_by(Measurement.date).all()
    session.close()
    tobs_list = []
    for date, tobs in temps_data:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_list.append(tobs_dict)
    return jsonify(tobs_list)

#define start date


#define start and end date

# run the flask app
if __name__ == "__main__":
    app.run(debug=True)
