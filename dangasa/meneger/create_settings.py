import os
from pathlib import Path


def create_settings_file(prject_name):
    new_file = Path(prject_name+"/dangasa_settings.py")
    code_library = f"\nfrom .settings import *\n\n"
    
    code = "INSTALLED_APPS += [\n"
    code += "\t'rest_framework',\n"
    code += "\t'drf_yasg',\n"
    code += "]\n\n"
    
    code += """REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_PAGINATION_CLASS': 'core.pagination.CustomPagination',
}
    """
    
    new_file.write_text(code_library+code)
    print(f"dangasa_settings.py created successfully.")
    
def append_main_settings(prject_name):
    new_file = Path(prject_name)
    settings_f = new_file.read_text()
    with new_file.open(mode="a") as file:
        code_library = str()
        if "from .dangasa_settings import *" not in settings_f:
            code_library += "\n\nfrom .dangasa_settings import *\n\n"
            
        file.write(code_library)
        
        
    

def main_settings(prject_name):
    try:
        app_name = prject_name+'/dangasa_settings.py'
        if os.path.exists(app_name):
            print("dangasa_settings.py already exists!")
        else:
        # Create a new Python file
            create_settings_file(prject_name)
            append_main_settings(prject_name+'/settings.py')
    except Exception as e:
        print(str(e))
        