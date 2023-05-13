import json


def save_objects_as_json(base_folder, folder_path, file_name, load_obj):
    print('Inside save function')
    output_filename = base_folder + folder_path + str(file_name) + ".json"

    f = open(output_filename, "w")
    f.writelines(object_to_json(load_obj))



def object_to_json(load_obj):
    return json.dumps(load_obj, indent=2)


def save_json_to_file(base_folder, folder_path, file_name, load_obj):
    output_filename = base_folder + folder_path + str(file_name) + ".json"

    with open(output_filename, 'w') as f:
        json.dump(load_obj,f, indent =2)

    return True
