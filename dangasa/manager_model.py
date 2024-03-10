# models_reader.py

import os
import django
import sys
from manager.create_views import main_views
from manager.create_views import main_views
from manager.create_serializers import main_serializers
from manager.create_urls import main_urls
# from manager.create_settings import main_settings
# from manager.create_swagger_generators import main_swagger_generator
# from manager.create_swagger_schema import main_swagger_schema
# from manager.create_pagination import main_pagination
from manager.config import DangasaConfig


from django.apps import apps
from django.conf import settings



# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Configure Django settings
django.setup(set_prefix=False)


def get_project_name():
    try:
        return settings.ROOT_URLCONF.split('.')[0]
    except AttributeError:
        return None
project_name = get_project_name()


def get_model_fields(app_name, model_name):
    try:
        model = apps.get_model(app_name, model_name)
        fields = [(field.name, field.get_internal_type()) for field in model._meta.fields]
        many_to_many_fields = [(field.name, field.get_internal_type()) for field in model._meta.many_to_many]
        foreign_key_fields = [(field.name, field.get_internal_type()) for field in model._meta.related_objects if field.field.many_to_one]

        return fields + many_to_many_fields + foreign_key_fields
    except LookupError:
        return None

def main():
    # Customize the app_name and model_name according to your project
    app_name = sys.argv[1]
    model_name = sys.argv[2]
    

    try:
        # Retrieve the model and print its fields
        fields = get_model_fields(app_name, model_name)
    
        DangasaConfig(project_name).main()
        if fields is not None:
            
            main_views(app_name, model_name, project_name)
            main_serializers(app_name, model_name, fields)
            main_urls(app_name, model_name)
            
        else:
            print(f"Error: Model '{model_name}' not found in app '{app_name}'.")

    except ImportError:
        print(f"Error: Module '{app_name}.models' not found.")
    except AttributeError:
        print(f"Error: Class '{model_name}' not found in module '{app_name}.models'.")

if __name__ == "__main__":
    main()
