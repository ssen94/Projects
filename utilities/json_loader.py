import json
import logging
import os
from collections import OrderedDict
from recordtype import recordtype


def custom_decoder(json_payload):
    json_payload.update({'uniq_key': None})
    return recordtype('X', json_payload())(*json_payload.values())


def decode(json_payload):
    x = json.loads(json_payload)
    return x


def load_ndjson_file_as_objects(input_folder, json_file_name, lambda_function):
    objs = OrderedDict()

    file_name = input_folder + "/" + json_file_name

    # if not os.path.exists(file_name):
    #     return objs

    logging.info('Loading file : {}'.format(json_file_name))

    f = open(file_name, "r")
    # print(f)

    for json_line in f:
        # Convert to an input obj
        extract_obj = decode(json_line)
        # print(extract_obj)

        # Evaluate lambda function to get the key
        dict_key = lambda_function(extract_obj)
        # print(dict_key)

        # Add to the objs
        objs[dict_key] = extract_obj
        # print(objs)

    return objs
