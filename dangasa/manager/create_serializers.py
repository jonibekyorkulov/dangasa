from pathlib import Path
import os
import sys

def add_serializers_file(app_name, model_name, fields):
    new_file = Path(app_name)
    serializers_f = new_file.read_text()
    with new_file.open(mode="a") as file:
        code_library = str()
        code = str()
        if f"from rest_framework import serializers" not in serializers_f:
            code_library += f"\nfrom rest_framework import serializers\n"
        if f"from .models import {model_name}" not in serializers_f:
            code_library += f"\nfrom .models import {model_name}\n\n"
        
        if f"class {model_name}Serializer(serializers.ModelSerializer):" not in serializers_f:
            code += f"\nclass {model_name}Serializer(serializers.ModelSerializer):\n"
            code += f"\tclass Meta:\n"
            code += f"\t\tmodel = {model_name}\n"
            code += f"""\t\tfields = ["""
            for i in fields:
                code += f"'{i[0]}',"
            
            code += "]\n\n"
            code += """\tdef validate(self, attrs):
            #Validate any fields
            return super().validate(attrs)
        """
    
            print(f"Serializers file '{app_name}' with class '{model_name}' created successfully.")
            
        else:
            print(f"{model_name}Serializer Class alridy exist")
            

        file.write(code_library + code)
    
    

def create_serializers_file(app_name, model_name, fields):
    new_file = Path(app_name)
    code_library = f"\nfrom rest_framework import serializers\n"
    code_library += f"from .models import {model_name}\n\n"
    code = f"class {model_name}Serializer(serializers.ModelSerializer):\n"
    code += f"\tclass Meta:\n"
    code += f"\t\tmodel = {model_name}\n"
    code += f"""\t\tfields = ["""
    for i in fields:
        code += f"'{i[0]}',"
    code += "]\n\n"
    code += """\tdef validate(self, attrs):
        #Validate any fields
		return super().validate(attrs)
    """
    
    new_file.write_text(code_library + code)
    print(f"Serializers file '{app_name}' with class '{model_name}' created successfully.")
    


def main_serializers(app_name, model_name, fields):
    try:
        app_name = app_name+'/serializers.py'
        if os.path.exists(app_name):
            add_serializers_file(app_name, model_name, fields)
        else:
        # Create a new Python file
            create_serializers_file(app_name, model_name, fields)
    except Exception as e:
        print(str(e))
        