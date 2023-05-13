import configparser
import logging
import sys
import os
import time
import traceback
import json
from datetime import datetime

from utilities.logging_setup import setup_logging
from utilities.json_loader import load_ndjson_file_as_objects
from utilities.json_saver import save_objects_as_json, save_json_to_file
from utilities.data_type_utilities import initialise_context
from builders import builder_payload_with_context


def transform(input_folder):
    # print(input_folder)
    start_time = time.time()
    logging.info("Starting Nested Json Parsing Framework....")

    successful = 0

    try:

        json_object_map = {
            "input_jsons": load_ndjson_file_as_objects(input_folder + "/source", "input.ndjson", lambda c: c['key']),
        }
        # print(json_object_map)

        for key in json_object_map['input_jsons']:
            # print("Hello")

            try:
                logging.info(f'Parsing Json : {key}')

                # Build the context for passing to builders

                context = {}

                context['json_object_map'] = json_object_map
                context['key'] = key
                context['json_obj'] = json_object_map['input_jsons'][context['key']]

                # print(context)

                # perform the transformation to the output obj
                load_obj = builder_payload_with_context.build(context)

                logging.info('The json with key value : {} is successfully parsed'.format(key))

                
                save_json_to_file(input_folder , "/outputs/",  "Key - " + str(key) + "_transformed" , load_obj)

                successful += 1
                # print(successful)

            except Exception as e:
                pass

    except Exception as e:
        logging.error(traceback.format_exc())

    logging.info('Successfully Parsed {} Json'.format(successful))
    logging.info("Job execution Time : {} seconds ....".format((time.time() - start_time)))


if __name__ == '__main__':
    # Setup Logging
    setup_logging()

    # Load the configuration
    config = configparser.ConfigParser()
    config.read('application.ini')

    # Detrmine teh source folder
    source_folder = config['DEFAULT']['base_folder']
    # print(source_folder)

    # if len(sys.argv) > 1:
    #     source_folder = sys.argv[1]
    #     print(source_folder)

    logging.info(f"Using the Base folder : {source_folder}")

    # Start Transform

    transform(source_folder)
