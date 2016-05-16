import os
import json

def read_config():
    config_file_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'configuration.json'
    )
    with open(config_file_path) as config_file:
        return json.load(config_file)
