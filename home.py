from common import get_all_data

def fetch_store_details():
    data = get_all_data()
    data = data.get_json()
    del data['users']

    return data