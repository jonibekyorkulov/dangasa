from pathlib import Path
import os
import sys

def add_views_file(app_name, model_name, praject_name):
    new_file = Path(app_name)
    view_f = new_file.read_text()
    with new_file.open(mode="a") as file:
        code_library = str()
        code = str()
        if "from rest_framework.permissions import AllowAny" not in view_f:
            code_library += "\nfrom rest_framework.permissions import AllowAny\n"
        if "from rest_framework.response import Response" not in view_f:
            code_library += "\nfrom rest_framework.response import Response\n"
        if f"from {praject_name}.pagination import CustomPagination" not in view_f:
            code_library += f"\nfrom {praject_name}.pagination import CustomPagination\n"
        if "from rest_framework import generics" not in view_f:
            code_library += "\nfrom rest_framework import generics\n\n"
        if f"from .models import {model_name}" not in view_f:
            code_library += f"\nfrom .models import {model_name}\n"
        if f"from .serializers import {model_name}Serializer" not in view_f:
            code_library += f"\nfrom .serializers import {model_name}Serializer\n"
        
        if f"class {model_name}ApiView(generics.ListCreateAPIView):" not in view_f:
            code += f"\nclass {model_name}ApiView(generics.ListCreateAPIView):\n"
            code += f"\tqueryset = {model_name}.objects.all()\n"
            code += f"\tserializer_class = {model_name}Serializer\n"
            code += f"\tpagination_class = CustomPagination\n"
            code += f"\tpermission_classes = [AllowAny]\n\n"
            code += """\tdef list(self, request, *args, **kwargs):
		# You can customize the 'list' function here
		response = super().list(request, *args, **kwargs)
		# Additional logic or modification to the response data
		return response\n\n"""
            code += """\tdef get_queryset(self):
        # You can customize the 'get_queryset' function here
		return super().get_queryset()
    """
            
            print(f"View file '{app_name}' with class '{model_name}' created successfully.")
            
        else:
            print(f"{model_name}ApiView Class alridy exist")
            

        file.write(code_library + code)
    
    

def create_views_file(app_name, model_name, praject_name):
    new_file = Path(app_name)
    code_library += "from rest_framework.permissions import AllowAny\n"
    code_library += "from rest_framework.response import Response\n"
    code_library += f"from {praject_name}.pagination import CustomPagination\n"
    code_library += "from rest_framework import generics\n\n"
    code_library = f"\nfrom .models import {model_name}\n"
    code_library += f"from .serializers import {model_name}Serializer\n"
    code = f"class {model_name}ApiView(generics.ListCreateAPIView):\n"
    code += f"\tqueryset = {model_name}.objects.all()\n"
    code += f"\tserializer_class = {model_name}Serializer\n"
    code += f"\tpagination_class = CustomPagination\n"
    code += f"\tpermission_classes = [AllowAny]\n\n"
    code += """\tdef list(self, request, *args, **kwargs):
		# You can customize the 'list' function here
		response = super().list(request, *args, **kwargs)
		# Additional logic or modification to the response data
		return response\n\n"""
    code += """\tdef get_queryset(self):
        # You can customize the 'get_queryset' function here
		return super().get_queryset()
    """
    new_file.write_text(code_library + code)
    print(f"View file '{app_name}' with class '{model_name}' created successfully.")
    


def main_views(app_name, model_name, praject_name):
    try:
        app_name = app_name+'/views.py'
        if os.path.exists(app_name):
            
            add_views_file(app_name, model_name, praject_name)
        else:
            # Create a new Python file
            create_views_file(app_name, model_name, praject_name)
    except Exception as e:
        print(str(e))
        