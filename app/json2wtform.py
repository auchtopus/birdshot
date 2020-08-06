import os, json, re
from typing import List
from pathlib import Path
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email

root_path = Path(__file__).resolve().parents[1]

class FormBlock():
    def __init__(self, schema_path, output_dir):
        with open(schema_path, "r") as schema_json:
            self.schema = json.load(schema_json)
        self.form_name = self.schema["form_name"]
        self.output_dir = output_dir
        self.field_types = set()
        self.validator_types = set()
        self.imports = []
        self.class_declaration = []
        self.class_body = []
        FormBlock.generate_script(self)
        
    def parse_validators(self, validators: List[str])->str:
        validator_calls = []
        for val in validators:
            split = re.split('(|)', val)
            val_call = split[0]
            if "validators" in val_call:
                validator_calls.append(val_call.split(".")[1])
            else:
                validator_calls.append(val_call)
        return validator_calls

    def generate_field_standard():
        pass

    def generate_field_choices():
        pass
    
    def generate_field_boolean():

    def generate_field_decimal():
        pass

    def generate_script(self):
        standard_fields = ["DateField", "DateTimeField", "FileField", "FloatField", "SubmitField", "StringField"]
        choices_fields = ["RadioField", "SelectField", "SelectMultipleField"]
        for field in self.schema["fields"]:
            print(field)
            field = self.schema["fields"][field]
            print(field)
            if field["field_type"] in standard_fields:
                self.field_types.add(field["field_type"])
                self.validator_types = FormBlock.parse_validators(self, field["validators"])
                # verify that all of these fields exist?
                new_field_text = (f"{field} = {field['field_type']}("
                                    f"label = {field['label']},"
                                    f"validators = {field['validators']},"
                                    f"filters = {field['filters']},"
                                    f"widget = {field['widget']})")
                self.class_body.append(new_field_text)
            elif field["field_type"] in choices_fields:
                self.field_types.add(field["field_type"])
                self.validator_types = FormBlock.parse_validators(self, field["validators"])
                new_field_text = (f"{field} = {field['field_type']}("
                                    f"label = {field['label']},"
                                    f"validators = {field['validators']},"
                                    f"hoices = {field['choices']},"
                                    f"filters = {field['filters']},"
                                    f"widget = {field['widget']})")
                self.class_body.append(new_field_text)
            elif field["field_type"] == "BooleanField":
                self.field_types.add(field["field_type"])
                self.validator_types = FormBlock.parse_validators(self, field["validators"])
                new_field_text = (f"{field} = {field['field_type']}("
                                    f"label = {field['label']},"
                                    f"validators = {field['validators']},"
                                    f"false_values = {field['false_values']},"
                                    f"filters = {field['filters']},"
                                    f"widget = {field['widget']})")
                self.class_body.append(new_field_text)
            elif field["field_type"] == "DecimalField":
                self.field_types.add(field["field_type"])
                self.validator_types = FormBlock.parse_validators(self, field["validators"])
                new_field_text = (f"{field} = {field['field_type']}("
                                    f"label = {field['label']},"
                                    f"validators = {field['validators']},"
                                    f"filters = {field['filters']},"
                                    f"widget = {field['widget']},"
                                    f"places = {field['places']},"
                                    f"rounding = {field['rounding']},"
                                    f"use_locale = {field['use_locale']},"
                                    f"number_format = {field['number_format']})")
                self.class_body.append(new_field_text)
        self.imports.append(f"from flask_wtf import FlaskForm")
        self.imports.append(f"from wtforms import " + ", ".join(self.field_types))
        self.imports.append(f"from wtforms.validators import " + ", ".join(self.validator_types))
        self.class_declaration.append(f"class {self.schema['form_name']}(FlaskForm):")
        
    @staticmethod
    def render(text, indentation = 0):
        outstring = ""
        indentation = " "*indentation
        for line in text:
            new_line = indentation + line + "\n"
            outstring += new_line
        return outstring

    def __str__(self):
        return (f"{FormBlock.render(self.imports, 0)}"
                f"\n"
                f"{FormBlock.render(self.class_declaration, 0)}"
                f"\n"
                f"{FormBlock.render(self.class_body, 4)}")

    def generate_form(self, output_dir = None, form_name = None):
        if output_dir is None:
            output_dir = self.output_dir
        if form_name is None:
            form_name = self.form_name
        with open(f"{output_dir}/{form_name}.py", "w") as output_py:
            print(self, file = output_py)


if __name__ == "__main__":
    form = FormBlock("email_templates/json_schema_sample.json", "/forms")
    form.generate_form()