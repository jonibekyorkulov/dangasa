import os
from pathlib import Path
import shutil
import re


class ModelManager:
    def __init__(self, app_name, model_name, project_name, fields) -> None:
        self.app_name = app_name
        self.model_name = model_name
        self.project_name = project_name
        self.fields = fields
    
    def create_views(self):
        try:
            app_name = self.app_name+'/views.py'
            if os.path.exists(app_name):
                
                self.add_views_file()
            else:
                # Create a new Python file
                self.create_views_file()
        except Exception as e:
            print(str(e))
            
    def create_views_file(self):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))

            # Faylni to'liq yo'l (absolute path) bilan topib olamiz
            source_file = os.path.join(current_dir, 'model_crud_files/views.py-tpl')

            new_text_file = Path(source_file)
            content = new_text_file.read_text()

            replacement_dict = {
                '{model_name}': self.model_name,  
                '{project_name}': self.project_name
            }
            
            for key, value in replacement_dict.items():
                content = content.replace(key, value)
                
            new_py_file = Path(self.app_name+'/views.py')
            new_py_file.write_text(content)
            
            print(f"views.py '{self.app_name}' created successfully.")
        except FileNotFoundError:
            print("views.py fayli topilmadi.")
        except PermissionError:
            print(f"Ruxsat mavjud emas '{self.app_name}' papkasiga nusxalash uchun.")
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}") 
            
    def add_views_file(self):
        old_py_file = Path(self.app_name+'/views.py')
        content = old_py_file.read_text()
        modules_to_import = [
            '\nfrom rest_framework.permissions import AllowAny',

            '\nfrom rest_framework.response import Response',

            '\nfrom core.pagination import CustomPagination',

            '\nfrom rest_framework import generics',

            f'\nfrom .models import {self.model_name}',

            f'\nfrom .serializers import {self.model_name}Serializer',
        ]
        
        new_models_to_add = {self.model_name}
        new_serializers_to_add = f'{self.model_name}Serializer'

        import_pattern = re.compile(r'import\s+(.*?)(?=\s|from|$)', re.MULTILINE)

        models_import_pattern = re.compile(r'from\s+\.\w+\s+import\s+', re.DOTALL)
        serializers_import_pattern = re.compile(r'from\s+\.\w+\s+import\s+', re.DOTALL)

        match = import_pattern.search(content)

        if match:
            # Izlash natijasini topish
            end_index = match.end()

            # Modullarni qo'shish
            new_content = content[:end_index]
            for module_to_import in modules_to_import:
                new_content += module_to_import + '\n'
            new_content += '\n' + content[end_index:]

        else:
            print("Import statement not found in the file.")

        
        new_py_file = Path(self.app_name+'/views.py')
        new_py_file.write_text(new_content)
        
        
        print(f"views.py  '{self.app_name}' update successfully.")



        
        
              
    def create_serializers(self):
        try:
            app_name = self.app_name+'/serializers.py'
            if os.path.exists(app_name):
                self.add_serializers_file()
            else:
                # Create a new Python file
                self.create_serializers_file()
        except Exception as e:
            print(str(e))
            
    def create_serializers_file(self):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))

            # Faylni to'liq yo'l (absolute path) bilan topib olamiz
            source_file = os.path.join(current_dir, 'model_crud_files/serializers.py-tpl')

            new_text_file = Path(source_file)
            content = new_text_file.read_text()

            replacement_dict = {
                '{model_name}': self.model_name,  
                '{fields}': '( '+', '.join([f"'{field[0]}'" for field in self.fields]) + ', )',
            }
            
            for key, value in replacement_dict.items():
                content = content.replace(key, value)
                
            new_py_file = Path(self.app_name+'/serializers.py')
            new_py_file.write_text(content)
            
            print(f"serializers.py '{self.app_name}' created successfully.")
        except FileNotFoundError:
            print("serializers.py fayli topilmadi.")
        except PermissionError:
            print(f"Ruxsat mavjud emas '{self.app_name}' papkasiga nusxalash uchun.")
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")
            
    def add_serializers_file(self):
        print('add_serializers_file')
    
    def create_urls(self):
        try:
            app_name = self.app_name+'/urls.py'
            if os.path.exists(app_name):
                self.add_urls_file()
            else:
            # Create a new Python file
                self.create_urls_file()
        except Exception as e:
            print(str(e))
    
    def create_tests(self):
        pass
    
    def add_urls_file(self):
        old_py_file = Path(self.app_name+'/urls.py')
        content = old_py_file.read_text()
        new_data_to_add = f"path('{self.model_name}/list/', {self.model_name}ListCreateApiView.as_view()),\n"
        new_views_to_add = f'{self.model_name}ListCreateApiView,'
        if new_data_to_add not in content:
            pattern = re.compile(r'urlpatterns\s*=\s*\[\s*', re.DOTALL)
            import_pattern = re.compile(r'from\s+\.views\s+import\s+', re.DOTALL)


            
            match = pattern.search(content)
            match_import = import_pattern.search(content)

            if match and match_import:
                # Izlash natijasini topish
                start_index = match.end()
                
                end_index_import = match_import.end(1)

                # Malumotni qo'shish
                
                new_content = content[:start_index] + new_data_to_add + '\n' + content[start_index:]
                new_content_import = new_content[:end_index_import - 1] + new_views_to_add + '\n' + new_content[end_index_import:]
                
                # Faylni qayta yozish
                new_py_file = Path(self.app_name+'/urls.py')
                new_py_file.write_text(new_content_import)
                
                
                print(f"urls.py  '{self.app_name}' update successfully.")
                

            else:
                print("urlpatterns pattern not found in the file.")
    
    def create_urls_file(self):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))

            # Faylni to'liq yo'l (absolute path) bilan topib olamiz
            source_file = os.path.join(current_dir, 'model_crud_files/urls.py-tpl')

            new_text_file = Path(source_file)
            content = new_text_file.read_text()

            replacement_dict = {
                '{model_name}': self.model_name,  
            }
            
            for key, value in replacement_dict.items():
                content = content.replace(key, value)
                
            new_py_file = Path(self.app_name+'/urls.py')
            new_py_file.write_text(content)
            
            print(f"urls.py '{self.app_name}' created successfully.")
        except FileNotFoundError:
            print("urls.py fayli topilmadi.")
        except PermissionError:
            print(f"Ruxsat mavjud emas '{self.app_name}' papkasiga nusxalash uchun.")
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")
    
    
    def main(self):
        self.create_views()
        self.create_serializers()
        self.create_urls()
        self.create_tests()