import json
from os import getcwd


def write_json(gpals):
    json_object = json.dumps(gpals)
    with open("gpals.json", "w") as outfile:
        outfile.write(json_object)


class Gpals:
    def __init__(self):
        self.default_gpals = {"test_name": "your_login;gpal;your_password"}
        self.gpals = None
        self.save_btn = None
        self.go_btn = None
        self.save_credential_lbl = None
        self.name_field = None
        self.save_credential_window = None
        self.json_data = f'{getcwd()}/gpals.json'
        self.get_data()

    def get_data(self):
        try:
            json_source = open(self.json_data)
            file_content = json_source.read()
            self.gpals = json.loads(file_content)
            if not self.gpals:
                self.default_gpals = self.default_gpals
                write_json(self.gpals)
        except FileNotFoundError:
            self.gpals = self.default_gpals
            write_json(self.gpals)
