import json
import os
from flask import jsonify

import constants

def get_all_data():
    if not os.path.exists(constants.STORE_DETAILS_FILE_NAME):
        with open(constants.STORE_DETAILS_FILE_NAME, 'w') as f:
            json.dump({
                "users": [{
                    "name": "Chittranjann",
                    "password": 1234,
                    "id": 1234
                }]}, f)
    with open(constants.STORE_DETAILS_FILE_NAME, 'r') as f:
            json_data = json.load(f)   
     
    data = jsonify(json_data)

    return data

def get_clockin_and_clockout():
    if not os.path.exists(constants.SESSIONS_DETAILS_FILE_NAME):
        with open(constants.SESSIONS_DETAILS_FILE_NAME, 'w') as f:
            json.dump({
                "1234": {
                    "name": "Chittranjan",
                    "password": 1234,
                    "is_clock_in": False,
                    "session_details":[{
                        "date": "",
                        "clock_in_time": "",
                        "clock_out_time": ""
                    }]
                }}, f)
    with open(constants.SESSIONS_DETAILS_FILE_NAME, 'r') as f:
            json_data = json.load(f)   
     
    data = jsonify(json_data)

    return data

def save_data(file_name, data):
    try:
        jsonString = json.dumps(data)
        jsonFile = open(file_name, "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        return {"success": 'true'}

    except Exception as e:
        print("Error:", e)
        response_data = {'status': 'errorpppppp', 'message': str(e)}
        return jsonify(response_data), 400
