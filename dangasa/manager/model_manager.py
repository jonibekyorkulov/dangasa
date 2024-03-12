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
        pass
    
    def create_serializers(self):
        pass
    
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
            import_pattern = re.compile(r'\(([^)]*)\)', re.DOTALL)


            
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
            source_file = os.path.join(current_dir, 'model_crud_files/urls.txt')

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