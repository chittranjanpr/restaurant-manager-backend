from flask import request

from common import get_all_data

def checkout_save():
    data = get_all_data()
    data = data.get_json()['users']

    param1 = request.get_json()
    check = False

    for i in range (len(data)):
         if data[i]['password'] ==  eval(param1['password']):
            check = True

    return {'success': check}