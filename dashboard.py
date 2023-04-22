
from common import get_all_data, save_data
from flask import request, jsonify
import constants

def get_sales_report():
    try:
        
            file_data = get_all_data(constants.ORDER_HISTORY_FILE_NAME).get_json()
            
            item_counts = {}

            for key, value in file_data.items():
                for item in value:
                    for data in item["items_placed"]:
                        if data["name"] in item_counts:
                            item_counts[data["name"]] += 1
                        else:
                            item_counts[data["name"]] = 1

            item_array = []
            for item_name, item_count in item_counts.items():
                item_array.append({"name": item_name, "count": item_count})
          
            return item_array, 200

    except Exception as e:
        print("Error:", e)
        response_data = {'status': 'Error in creating new user', 'message': str(e)}
        return {"response": response_data, "status_code": 422}


def get_stocks():
    try:
            file_data = get_all_data(constants.STORE_DETAILS_FILE_NAME).get_json()

            return file_data['menu_items'], 200

    except Exception as e:
        print("Error:", e)
        response_data = {'status': 'Error in creating new user', 'message': str(e)}
        return {"response": response_data, "status_code": 422}


def update_stocks():
    try:
            param = request.get_json()
            file_data = get_all_data(constants.STORE_DETAILS_FILE_NAME).get_json()

            for item in file_data['menu_items']:
                if param['id'] == item['id']:
                    item['quantity'] = param['quantity'] + item['quantity']

            save_data(constants.STORE_DETAILS_FILE_NAME, file_data)   
            return jsonify({'success': True}), 200

    except Exception as e:
        print("Error:", e)
        response_data = {'status': 'Error in creating new user', 'message': str(e)}
        return {"response": response_data, "status_code": 422}