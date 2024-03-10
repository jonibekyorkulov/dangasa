from pathlib import Path
import os
import sys


def add_urls_file(app_name, model_name):
    new_file = Path(app_name)
    urls_f = new_file.read_text()
    with new_file.open(mode="a") as file:
        code_library = str()
        code = str()
        if f"from django.urls import path" not in urls_f:
            code_library += f"\nfrom django.urls import path\n"
        if f"from .views import {model_name}ApiView" not in urls_f:
            code_library += f"\nfrom .views import {model_name}ApiView\n\n"
        if f"path('{model_name}/list/', {model_name}ApiView.as_view())" not in urls_f:
            code = f"urlpatterns += [\n"
            code += f"\tpath('{model_name}/list/', {model_name}ApiView.as_view()),\n"
            code += f"]\n"
         
        print(f"Urls file '{app_name}' with class '{model_name}' created successfully.")

        file.write(code_library + code)
    
    

def create_urls_file(app_name, model_name):
    new_file = Path(app_name)
    code_library = f"\nfrom django.urls import path\n"
    code_library += f"from .views import {model_name}ApiView\n\n"
    
    code = f"urlpatterns = [\n"
    code += f"\tpath('{model_name}/list/', {model_name}ApiView.as_view()),\n"
    code += f"]\n"
    new_file.write_text(code_library + code)
    print(f"Urls file '{app_name}' with class '{model_name}' created successfully.")
    


def main_urls(app_name, model_name):
    try:
        app_name = app_name+'/urls.py'
        if os.path.exists(app_name):
            add_urls_file(app_name, model_name)
        else:
        # Create a new Python file
            create_urls_file(app_name, model_name)
    except Exception as e:
        print(str(e))
        