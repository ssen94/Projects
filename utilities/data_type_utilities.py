from recordtype import recordtype
from datetime import datetime


def initialise_context():
    return recordtype('Context', ['json_object_map'], ['key'], ['json_obj'])


def get_now_for_json():
    ret = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    return ret
