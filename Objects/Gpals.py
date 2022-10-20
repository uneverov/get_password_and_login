import json
from os import getcwd


class Gpals:
    def __init__(self):
        self.json_data = f'{getcwd()}/gpals.json'

    def get_data(self):
        try:
            json_source = open(self.json_data)
            print(json_source)
            file_content = json_source.read()
            gpals = json.loads(file_content)
        except FileNotFoundError:

        #return gpals
