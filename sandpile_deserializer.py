import json
from ast import literal_eval as make_tuple

def deserialize_sendpile(file):
    """
    Deserializes a json file to a matrix of sand grains.
    JSON is expected to have the format: { "(x, y)": n,...}
    :param file: JSON file to load
    :return: Dictionary in the form of (x, y) -> no of sand grains
    """
    with open(file) as data_file:
        return {tuple([int(i) for i in make_tuple(k)]): v for k, v in json.load(data_file).items()}