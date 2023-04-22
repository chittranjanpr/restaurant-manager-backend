import json
import os
from flask import jsonify

import constants

def get_all_data(fileName):
    if not os.path.exists(fileName):
        with open(fileName, 'w') as f:
            json.dump({}, f)
    with open(fileName, 'r') as f:
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

def create_new_user(file_name, data, password):
    try:
        with open(file_name,'r+') as file:
            file_data = json.load(file)

            # check duplicate user
            if password in file_data:
                raise ValueError('Password Exists..Try giving new password')
            else:
                file_data[password] = data
                file.seek(0)
                json.dump(file_data, file, indent = 4)
                return {"response": {'status': 'Successfully created new user', 'success': True}, "status_code": 200}

    except Exception as e:
        print("Error:", e)
        response_data = {'status': 'Error in creating new user', 'message': str(e)}
        return {"response": response_data, "status_code": 422}