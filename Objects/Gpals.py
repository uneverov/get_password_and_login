import json
from os import getcwd


class Gpals:
    def __init__(self):
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
        except FileNotFoundError:
            self.gpals = {
                "test_name": "your_login;gpal;your_password",
                }
            json_object = json.dumps(self.gpals)
            with open("gpals.json", "w") as outfile:
                outfile.write(json_object)
