import os
from pathlib import Path

def create_swagger_generator_file(prject_name):
    new_file = Path(prject_name+"/generator.py")
    
    code = f"""from drf_yasg.generators import OpenAPISchemaGenerator


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema
    """
    new_file.write_text(code)
    print(f"generator.py created successfully.")

def main_swagger_generator(prject_name):
    try:
        app_name = prject_name+'/generator.py'
        if os.path.exists(app_name):
            print("generator.py already exists!")
        else:
        # Create a new Python file
            create_swagger_generator_file(prject_name)
    except Exception as e:
        print(str(e))