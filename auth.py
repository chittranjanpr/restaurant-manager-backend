from flask import request, jsonify
from datetime import datetime

from common import get_all_data, get_clockin_and_clockout, save_data, create_new_user

import constants

def auth_login():
    data = get_all_data(constants.STORE_DETAILS_FILE_NAME)
    data = data.get_json()['users']
    param1 = request.get_json()

    get_data = get_clockin_and_clockout()
    get_data = get_data.get_json()

    user_id = param1['password']
    now = datetime.now()
    date = now.strftime("%m/%d/%Y")   

    user_data = {
        "name": get_data[user_id]['name'],
         "is_clock_in": get_data[user_id]['is_clock_in'],
    }
    for i in range(len(get_data[user_id]['session_details'])):
        if get_data[user_id]['session_details'][i]['date'] == date:
            user_data = { 
                "clock_in_time": get_data[user_id]['session_details'][i]['clock_in_time'],
                "clock_out_time": get_data[user_id]['session_details'][i]['clock_out_time'], **user_data
            }

    check = False
    
    for i in range (len(data)):
         if data[i]['password'] ==  eval(param1['password']):
            check = True

    return jsonify({ 'success': check, "resp": user_data }), 200

def clock_in():
    try:
        get_data = get_clockin_and_clockout()
        get_data = get_data.get_json()
        data = request.get_json()
        user_id = data.get('user_id')
        toggle_text = data.get('toggle_text')
        
        now = datetime.now()
        date = now.strftime("%m/%d/%Y")

        if toggle_text == 'clock_in':
            get_data[user_id]['is_clock_in'] = True
            get_data[user_id]['session_details'].append({
                "date": date,
                "clock_in_time": data.get('time_client'),
                "clock_out_time": "",
            })

        if toggle_text == 'clock_out':
            for i in range(len(get_data[user_id]['session_details'])):
                if get_data[user_id]['session_details'][i]['date'] == date:
                    get_data[user_id]['session_details'][i]['clock_out_time'] = data.get('time_client')
                    get_data[user_id]['is_clock_in'] = False

        response_data = save_data(constants.SESSIONS_DETAILS_FILE_NAME, get_data)

        return jsonify({'success': True}), 200
    
    except Exception as e:
        print("Error", e)
        response_data = {'status': 'error', 'message': str(e)}
        return jsonify(response_data), 400


def create_user():
    try:
        param = request.get_json()
        name = param['name']
        password = param['password']
        is_admin = param['is_admin']
        data = { 
                "is_clock_in": False,
                "name": name,
                "password": password,
                "role": is_admin,
                "session_details": [
                    { "clock_in_time": "", "clock_out_time": "", "date": "" }
                ]
        }
        response_data = create_new_user(constants.SESSIONS_DETAILS_FILE_NAME, data, password)
        print(response_data)
        return jsonify(response_data['response']), response_data['status_code']

    except Exception as e:
        print("Error", e)
        response_data = {'status': 'error', 'message': str(e)}
        return jsonify(response_data), 400