import os
from pathlib import Path
import shutil


class DangasaConfig:
    def __init__(self, project_name) -> None:
        self.project_name = project_name
    
        
        
        
    def create_settings(self):
        try:
            pro_name = self.project_name+'/dangasa_settings.py'
            if os.path.exists(pro_name):
                print("dangasa_settings.py already exists!")
            else:
                self.create_settings_file()
                self.append_main_settings()
        except Exception as e:
            print(str(e))
    
    def create_swagger_generators(self):
        try:
            pro_name = self.project_name+'/generator.py'
            if os.path.exists(pro_name):
                print("generator.py already exists!")
            else:
                self.create_swagger_generator_file()
        except Exception as e:
            print(str(e))
    
    def create_swagger_schema(self):
        try:
            pro_name = self.project_name+'/schema.py'
            if os.path.exists(pro_name):
                print("schema.py already exists!")
            else:
                self.create_swagger_schema_file()
                
            if os.path.exists(self.project_name+"/urls.py"):
                self.create_url_add_file()
            else:
                print(f"'{self.project_name}' urls.py does not exists!")
        except Exception as e:
            print(str(e))
    
    def create_pagination(self):
        try:
            pro_name =  self.project_name+'/pagination.py'
            if os.path.exists(pro_name):
                print("pagination.py already exists!")
            else:
                self.create_pagination_file()
        except Exception as e:
            print(str(e))
    
    def create_settings_file(self):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))

            source_file = os.path.join(current_dir, 'config_files/dangasa_settings.py')

            shutil.copy(source_file, self.project_name)
            print(f"dangasa_settings.py create to '{self.project_name}' created successfully.")
        except FileNotFoundError:
            print("dangasa_settings.py fayli topilmadi.")
        except PermissionError:
            print(f"Ruxsat mavjud emas '{self.project_name}' papkasiga nusxalash uchun.")
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}") 
    
    
    def append_main_settings(self):
        new_file = Path(self.project_name+'/settings.py')
        settings_f = new_file.read_text()
        with new_file.open(mode="a") as file:
            code_library = str()
            if "from .dangasa_settings import *" not in settings_f:
                code_library += "\n\nfrom .dangasa_settings import *\n\n"
                
            file.write(code_library)
    
    def create_swagger_generator_file(self):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))

            source_file = os.path.join(current_dir, 'config_files/generator.py')

            shutil.copy(source_file, self.project_name)
            print(f"generator.py create to '{self.project_name}' created successfully.")
        except FileNotFoundError:
            print("generator.py fayli topilmadi.")
        except PermissionError:
            print(f"Ruxsat mavjud emas '{self.project_name}' papkasiga nusxalash uchun.")
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")  
    
    
    def create_swagger_schema_file(self):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))

            source_file = os.path.join(current_dir, 'config_files/schema.py')

            shutil.copy(source_file, self.project_name)
            print(f"schema.py create to '{self.project_name}' created successfully.")
        except FileNotFoundError:
            print("schema.py fayli topilmadi.")
        except PermissionError:
            print(f"Ruxsat mavjud emas '{self.project_name}' papkasiga nusxalash uchun.")
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")
        
    
    def create_url_add_file(self):
        new_file = Path(self.project_name+"/urls.py")
        urls_f = new_file.read_text()
        with new_file.open(mode="a") as file:
            code_library = str()
            code = str()
            if "from .schema import swagger_urlpatterns" not in urls_f:
                code_library = "\n\nfrom .schema import swagger_urlpatterns\n\n"
            if "urlpatterns += swagger_urlpatterns" not in urls_f:
                code += "urlpatterns += swagger_urlpatterns\n\n"
            
            file.write(code_library + code)
            
    
    def create_pagination_file(self):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))

            source_file = os.path.join(current_dir, 'config_files/pagination.py')

            shutil.copy(source_file, self.project_name)
            print(f"pagination.py create to '{self.project_name}' created successfully.")
        except FileNotFoundError:
            print("pagination.py fayli topilmadi.")
        except PermissionError:
            print(f"Ruxsat mavjud emas '{self.project_name}' papkasiga nusxalash uchun.")
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")
        
       
      
    def main(self):
        self.create_settings()
        self.create_swagger_generators()
        self.create_swagger_schema()
        self.create_pagination()