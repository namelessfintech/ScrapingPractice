
# https://docs.python-guide.org/dev/virtualenvs/, packages managed by "source helloScrape/bin/activate"

from flask import Flask, request,redirect, url_for, render_template
from fetch import *
# import pymysql
# import sqlalchemy

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://forecast.weather.gov/MapClick.php?lat=40.6925&lon=-73.9904#.XAmGmRNKgWo"
    weather_data = fetcher(url)
    clean = weather_proccessor(weather_data)
    return render_template("index.html", data=clean)

app.run(debug=True)
