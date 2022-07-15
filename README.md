# Meraki - WIFI and BLE Location Tracking Dashboard

This code repository contains a proof-of-concept BLE and WIFI location-tracking dashboard which leverages Meraki's Scanning API.
This code generates an Excel report which contains information about the devices in the Meraki Network 

## Contacts
* Max Acquatella (macquate@cisco.com)

## Solution Components
* Meraki MR Access Points with Bluetooth radios
* Meraki Dashboard APIs
* Flask

## Installation/Configuration

**Clone repo:**
```bash
git clone <repo_url>
```

**Install required dependancies:**
```bash
pip install -r requirements.txt
```

**Install and enable NGROK**
1. Follow the instructions from the NGROK website: 
```http
https://dashboard.ngrok.com/get-started/setup
```
2. Once installed and enabled, run the following command: 
```bash
ngrok http 8080
```
3. Copy the publicly-reachable URL, it should look similar to the following EXAMPLE: 
```http 
https://96ba-162-197-165-177.ngrok.io
```
The address will change everytime NGROK is reset, the previous address is provided just as an example (it will not work if used). 
4. Save this address for point 5 of the following step.

**Configure Meraki Dashboard**

1. Log into the Meraki Dashboard & select the desired network.
2. Navigate to **Network Wide > Configure > General > Location and scanning**.
3. Ensure that `Scanning API` is enabled. 
4. Click `Add a POST URL`
   1. Add the publicly-reachable URL for this app, with the URL PATH `/location_info` (example: https://96ba-162-197-165-177.ngrok.io/location_info). Click `Validate`.
5. Ensure `API Version` is set to `V3` & `Radio Type` is set to `WIFI`.
6. Go to **Wireless > Configure > IoT Radio Settings** and switch "Scanning" and "Beaconing" to On.


**Configure required variables:**

In the primary application file, `app.py`, these are the required parameters to configure:
```python
# REQUIRED CONFIG VALUES:
MERAKI_VALIDATION_KEY = ""
MERAKI_API_KEY = ""
SUPPRESS_MERAKI_LOGGING = True
```

The`MERAKI_VALIDATION_KEY` & `MERAKI_API_KEY` must be configured. The validation key is provided by Meraki at the following Dashboard location: **Network Wide > Configure > General > Location and scanning**. 
 - `MERAKI_VALIDATION_KEY` is used by Meraki cloud to validate the receiver (this app). The first request sent by Meraki Scanning API will be a `GET` & this app must return the same Validation key provided by Meraki Dashboard.
 - `MERAKI_API_KEY` is obtained from **Organization > Configure > Settings > Dashboard API access > Check the box: `Enable access to the Cisco Meraki Dashboard API`**. Then, click on the provided `profile` link to be taken to your profile page (also accessible in the top right corner of the dashboard portal > My Profile). Scroll down to `API access` and generate a new key. 
 

## Usage

After all required configuration items are in place, run the application with the following command:

```bash
python app.py
```
NOTE: Make sure that NGROK in running (see step 2 of **Install and enable NGROK**)
If running the app locally, browse to `http://127.0.0.1:8080`. 

### **Notes on usage**

The Meraki Dashboard will send a GET request for the MERAKI_VALIDATION_KEY. This will print to the console the following message: `Receiving GET request for Meraki Validation key - Sending Meraki Validation key`
After this GET request, the Meraki Dashboard will start sending POST requests to the publicly-reachable URL every minute. The code will generate an Excel sheet with the required information.

NOTE:
Starting with Scanning API v3, Meraki requires a minimum of 3 access points to detect a BLE tag in order to provide accurate location information. If less than 3 access points detect a tag, then the only information provided is the nearest AP. If this occurs, this app will place the BLE tag label by the nearest AP.

The code will generate an EXCEL sheet every minute with the current date. These will be saved on the same folder where app.py is stored. The Excel sheet will contain information regarding SSID, bluetooth and WIFI endpoints in the location.

# Screenshots

**Example of the generated Excel sheet:**

![/IMAGES/example_excel.png](/IMAGES/example_excel.png)



### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.