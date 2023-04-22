from flask import request, jsonify
from datetime import datetime

from common import get_all_data, save_data

import constants

def checkout_save():
    api_data = request.get_json()
    order_history_data = get_all_data(constants.ORDER_HISTORY_FILE_NAME).get_json()

    now = datetime.now()
    date = now.strftime("%m/%d/%Y")
    obj = {}
    if date in order_history_data:
        total = 0
        for value in api_data['selected_items']:
            total = total + value['price']
        obj = {
            "user_id": api_data['user_id'],
            'date': date,
            "items_placed": api_data['selected_items'],
            "items_sub_total": total,
            "tax": constants.TAX,
            "total": total + (total * (constants.TAX / 100)),
            "restaurant_name": constants.RESTAURANT_NAME,
            "finalized": False,
            "order_id": len(order_history_data[date]) + 1
        }
        order_history_data[date].append(obj)
    else:
        total = 0
        for value in api_data['selected_items']:
            total = total + value['price']
        obj = {
            "user_id": api_data['user_id'],
            'date': date,
            "items_placed": api_data['selected_items'],
            "items_sub_total": total,
            "tax": constants.TAX,
            "total": total + (total * (constants.TAX / 100)),
            "restaurant_name": constants.RESTAURANT_NAME,
            "finalized": False,
            "order_id": 1
        }
        order_history_data[date] = [obj]
    save_data(constants.ORDER_HISTORY_FILE_NAME, order_history_data)

    return jsonify({'resp_data': obj, "success": True}), 200


def submit_order():
    api_data = request.get_json()
    order_history_data = get_all_data(constants.ORDER_HISTORY_FILE_NAME).get_json()

    file_data = get_all_data(constants.STORE_DETAILS_FILE_NAME).get_json()

    now = datetime.now()
    date = now.strftime("%m/%d/%Y")
    for i in range(len(order_history_data[date])):
        if order_history_data[date][i]['order_id'] == api_data['order_id']:
            order_history_data[date][i]['finalized'] = True

            # update quantity on each order
            for update_item in order_history_data[date][i]['items_placed']:
                for menu_item in file_data['menu_items']:
                    if(update_item['id'] == menu_item['id']):
                        print('menu itemss', update_item['quantity'])
                        menu_item['quantity'] -= update_item['quantity']
                        
                        # print('file_data', file_data)
                        save_data(constants.STORE_DETAILS_FILE_NAME, file_data)   

    save_data(constants.ORDER_HISTORY_FILE_NAME, order_history_data)

    return jsonify({"success": True}), 200

