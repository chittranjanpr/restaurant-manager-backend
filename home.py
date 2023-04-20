from common import get_all_data

import constants

def fetch_store_details():
    data = get_all_data(constants.STORE_DETAILS_FILE_NAME)
    data = data.get_json()
    del data['users']

    return data