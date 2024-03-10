import os
from pathlib import Path

def create_swagger_schema_file(prject_name):
    new_file = Path(prject_name+"/schema.py")
    
    code = f"""from django.urls import re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .generator import BothHttpAndHttpsSchemaGenerator

schema_view = get_schema_view(
    openapi.Info(
        title="Project Title",
        default_version="v1",
        description="Project description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="example@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    generator_class=BothHttpAndHttpsSchemaGenerator,
    permission_classes=(permissions.AllowAny,),
)


swagger_urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
    """
    new_file.write_text(code)
    
    print(f"schema.py created successfully.")
    
def create_url_add_file(prject_name):
    new_file = Path(prject_name)
    urls_f = new_file.read_text()
    with new_file.open(mode="a") as file:
        code_library = str()
        code = str()
        if "from .schema import swagger_urlpatterns" not in urls_f:
            code_library = "\n\nfrom .schema import swagger_urlpatterns\n\n"
        if "urlpatterns += swagger_urlpatterns" not in urls_f:
            code += "urlpatterns += swagger_urlpatterns\n\n"
        
        file.write(code_library + code)
            
        

def main_swagger_schema(prject_name):
    try:
        app_name = prject_name+'/schema.py'
        if os.path.exists(app_name):
            print("schema.py already exists!")
        else:
        # Create a new Python file
            create_swagger_schema_file(prject_name)
            
        if os.path.exists(prject_name+"/urls.py"):
            create_url_add_file(prject_name+"/urls.py")
        else:
        # Create a new Python file
            print(f"{prject_name} urls.py does not exists!")
    except Exception as e:
        print(str(e))