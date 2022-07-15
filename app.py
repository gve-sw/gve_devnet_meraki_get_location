""" Copyright (c) 2022 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied. 
"""

import pprint
import datetime as dt
import pandas as pd
import json
import meraki
from flask import Flask, render_template, request


# REQUIRED CONFIG VALUES:
MERAKI_VALIDATION_KEY = ""
MERAKI_API_KEY = ""
SUPPRESS_MERAKI_LOGGING = True

app = Flask(__name__)
dashboard = meraki.DashboardAPI(api_key=MERAKI_API_KEY, suppress_logging=SUPPRESS_MERAKI_LOGGING)


@app.route("/")
def home():
    return render_template("home.html")


# Meraki Scanning API Listener
@app.route("/location_info", methods=["GET", "POST"])
def location_info():
    # Meraki Dashboard will send location payloads via POST request
    if request.method == "POST":
        print("Receiving POST from the Meraki Dashboard - Saving EXCEL file")
        # Store Location JSON payload
        location_data = request.json
        # Test Prints
        # print(location_data)
        # pprint.pprint(location_data)
        observations = pd.read_json(json.dumps(location_data["data"]["observations"]))
        observations.to_excel(f'observations{dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.xlsx')
        return render_template("test.html")
    print("Receiving GET request for Meraki Validation key - Sending Meraki Validation key")
    return MERAKI_VALIDATION_KEY


if __name__ == "__main__":
    app.run(debug=True, port=8080)
