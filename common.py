import json
import os
from flask import jsonify

def get_all_data():
    if not os.path.exists('data.json'):
        with open('data.json', 'w') as f:
            json.dump({
                "users": [{
                    "name": "Chittranjann",
                    "password": 1234
                }]}, f)
    with open('data.json', 'r') as f:
            json_data = json.load(f)   
     
    data = jsonify(json_data)

    return data