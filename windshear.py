from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
import requests
import os

load_dotenv()

app = Flask(__name__)
CORS(app, origins=["https://wolverine1621.github.io"])

def query_avwx(fmt, icao):
    url = "https://avwx.rest/api/"

    if fmt != "metar" and fmt != "taf":
        return "FMT ERROR"

    url = url + fmt + '/' + icao + "?format=json"



    headers = {"Authorization": os.environ.get("AVWX_KEY")}

    return requests.get(url, headers=headers).content.decode('utf-8')

@app.route("/api/v1/metar")
def get_metar():
    icao = request.args.get("icao")

    return query_avwx("metar", icao)

@app.route("/api/v1/taf")
def get_taf():
    icao = request.args.get("icao")

    return query_avwx("taf", icao)

