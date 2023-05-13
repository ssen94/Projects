from  utilities.data_type_utilities import get_now_for_json

def build(context):

    ret = {
        "migrationDate": get_now_for_json()
    }
    return ret

