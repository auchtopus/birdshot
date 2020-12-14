import collections
import os, json, re
from typing import List
from pathlib import Path
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email

root_path = Path(__file__).resolve().parents[1]

class WtFormBuilder():
    def __init__(self, schema_path, output_dir = None):
        with open(schema_path, "r") as schema_json:
            self.schema = json.load(schema_json, object_pairs_hook=collections.OrderedDict)
        self.form_fields = collections.OrderedDict(self.schema['fields'])
        self.form_name = self.schema["form_name"]
        self.output_dir = output_dir
        self.field_types = set()
        self.validator_types = set()
        self.imports = []
        # FormBlock.generate_script(self)

    def get_fields(self):
        for field in self.form_fields:
            print(field)
        
    def parse_validators(self, validators: List[str])->str:
        validator_calls = []
        for val in validators:
            split = re.split('(|)', val)
            val_call = split[0]

            # check to see if validators class is written out or included above
            if "validators" in val_call:
                validator_calls.append(val_call.split(".")[1])
            else:
                validator_calls.append(val_call)
        return validator_calls

    def generate_fields(self):
        for field in self.form_fields:
            print(field)

    def build_form(self, fields):
        new_form = type(self.form_name, (FlaskForm), {fields})
        new_form.company_name = "Hello!"


if __name__ == "__main__":
    print(root_path)
    form_builder = WtFormBuilder(f"{root_path}/email_templates/json_schema_sample.json")
    form_builder.get_fields()