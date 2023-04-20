
from common import get_all_data
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

