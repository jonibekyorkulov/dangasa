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
            source_file_main = os.path.join(current_dir, 'model_crud_files/views.py-tpl')
            source_file_list_create = os.path.join(current_dir, 'model_crud_files/ListCreateApiView.py-tpl')
            source_file_retrive = os.path.join(current_dir, 'model_crud_files/RetrieveAPIView.py-tpl')
            

            new_text_file_main = Path(source_file_main)
            content_main = new_text_file_main.read_text()
            
            new_text_file_retrive = Path(source_file_retrive)
            content_retrive = new_text_file_retrive.read_text()

            new_text_file_list_create = Path(source_file_list_create)
            content_list_create = new_text_file_list_create.read_text()

            replacement_dict = {
                '{model_name}': self.model_name,  
                '{project_name}': self.project_name
            }
            
            for key, value in replacement_dict.items():
                content_main = content_main.replace(key, value)
                content_list_create = content_list_create.replace(key, value)
                content_retrive = content_retrive.replace(key, value)
                
                
            new_py_file = Path(self.app_name+'/views.py')
            new_py_file.write_text(content_main + '\n' + content_list_create + '\n' + content_retrive)
            
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
            'from rest_framework.permissions import AllowAny',

            '\nfrom rest_framework.response import Response',

            '\nfrom core.pagination import CustomPagination',

            '\nfrom rest_framework import generics',

            f'\nfrom .models import {self.model_name}',

            f'\nfrom .serializers import {self.model_name}Serializer',
        ]
        

        import_pattern = re.compile(r'import\s+(.*?)(?=\s|from|$)', re.MULTILINE)


        match = import_pattern.search(content)
        new_content = str()
        if match:
            # Izlash natijasini topish
            end_index = match.end()

            # Modullarni qo'shish
            new_content = content[:end_index]
            for module_to_import in modules_to_import:
                if module_to_import not in content:
                    new_content += module_to_import + '\n'
            new_content += content[end_index:]

        else:
            for module_to_import in modules_to_import:
                if module_to_import not in content:
                    new_content += module_to_import + '\n'
            print("Import statement not found in the file.")
            
        content_list_create = str()
        if (f'{self.model_name}ListCreateApiView' not in content):   
            current_dir = os.path.dirname(os.path.abspath(__file__))
            source_file_list_create = os.path.join(current_dir, 'model_crud_files/ListCreateApiView.py-tpl')
            
            new_text_file_list_create = Path(source_file_list_create)
            content_list_create = new_text_file_list_create.read_text()
            
            replacement_dict = {
                '{model_name}': self.model_name,  
                '{project_name}': self.project_name
            }
            
            for key, value in replacement_dict.items():
                content_list_create = content_list_create.replace(key, value)
                
            
            
            print(f"views.py  '{self.app_name}' update successfully.")
        else:
            print(f"views.py  < {self.model_name}ListCreateApiView >  already exists.")
            
            
        content_retrive = str()
        if (f'{self.model_name}RetrieveAPIView' not in content):   
            current_dir = os.path.dirname(os.path.abspath(__file__))
            source_file_retrive = os.path.join(current_dir, 'model_crud_files/RetrieveAPIView.py-tpl')
            
            new_text_file_retrive = Path(source_file_retrive)
            content_retrive = new_text_file_retrive.read_text()
            
            replacement_dict = {
                '{model_name}': self.model_name,  
                '{project_name}': self.project_name
            }
            
            for key, value in replacement_dict.items():
                content_retrive = content_retrive.replace(key, value)
                
            
            
            print(f"views.py  '{self.app_name}' update successfully.")
        else:
            print(f"views.py  < {self.model_name}RetrieveAPIView >  already exists.")
        
        
        new_py_file = Path(self.app_name+'/views.py')
        new_py_file.write_text(new_content + '\n' + content_list_create + '\n' + content_retrive)
        

              
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
                
            if f'{self.model_name}Serializer' not in content:   
                current_dir = os.path.dirname(os.path.abspath(__file__))
                source_file_list_create = os.path.join(current_dir, 'model_crud_files/serializers_class.py-tpl')
                
                new_text_file_list_create = Path(source_file_list_create)
                content_list_create = new_text_file_list_create.read_text()

                
                
                for key, value in replacement_dict.items():
                    content_list_create = content_list_create.replace(key, value)
                    
                
                
                print(f"Serializer.py  '{self.app_name}' update successfully.")
            else:
                print(f"Serializer.py  < {self.model_name}Serializer >  already exists.")
            
            
            new_py_file = Path(self.app_name+'/serializers.py')
            new_py_file.write_text(content + '\n' + content_list_create)
            
            print(f"serializers.py '{self.app_name}' created successfully.")
        except FileNotFoundError:
            print("serializers.py fayli topilmadi.")
        except PermissionError:
            print(f"Ruxsat mavjud emas '{self.app_name}' papkasiga nusxalash uchun.")
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")
            
    def add_serializers_file(self):
        old_py_file = Path(self.app_name+'/serializers.py')
        content = old_py_file.read_text()
        modules_to_import = [
            f'\nfrom .models import {self.model_name}',
        ]
        
        if "from rest_framework import serializers" not in content:
            modules_to_import.append("from rest_framework import serializers")
        
        import_pattern = re.compile(r'import\s+(.*?)(?=\s|from|$)', re.MULTILINE)


        match = import_pattern.search(content)
        new_content = str()
        if match:
            # Izlash natijasini topish
            end_index = match.end()

            # Modullarni qo'shish
            new_content = content[:end_index]
            for module_to_import in modules_to_import:
                if module_to_import not in content:
                    new_content += module_to_import + '\n'
            new_content += content[end_index:]

        else:
            for module_to_import in modules_to_import:
                if module_to_import not in content:
                    new_content += module_to_import + '\n'
            print("Import statement not found in the file.")
        
        content_list_create = str()
        if f'{self.model_name}Serializer' not in content:   
            current_dir = os.path.dirname(os.path.abspath(__file__))
            source_file_list_create = os.path.join(current_dir, 'model_crud_files/serializers_class.py-tpl')
            
            new_text_file_list_create = Path(source_file_list_create)
            content_list_create = new_text_file_list_create.read_text()

            replacement_dict = {
                '{model_name}': self.model_name,  
                '{fields}': '( '+', '.join([f"'{field[0]}'" for field in self.fields]) + ', )',
            }
            
            for key, value in replacement_dict.items():
                content_list_create = content_list_create.replace(key, value)
                
            
            
            print(f"Serializer.py  '{self.app_name}' update successfully.")
        else:
            print(f"Serializer.py  < {self.model_name}Serializer >  already exists.")
        
        
        new_py_file = Path(self.app_name+'/serializers.py')
        new_py_file.write_text(new_content + '\n' + content_list_create)
        
        
        
        
    
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
        try:
            app_name = self.app_name+'/tests.py'
            if os.path.exists(app_name):
                self.add_tests_file()
            else:
            # Create a new Python file
                self.create_tests_file()
        except Exception as e:
            print(str(e))
            
    
    def add_tests_file(self):
        pass
    
    
    def create_tests_file(self):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))

            # Faylni to'liq yo'l (absolute path) bilan topib olamiz
            source_file = os.path.join(current_dir, 'test_case_file/test.py-tpl')

            new_text_file = Path(source_file)
            content = new_text_file.read_text()

            replacement_dict = {
                '{model_name}': self.model_name,  
                '{model_name_function}': self.model_name.lower(),  
                '{fields_setup_obj_1}' : ', '.join([f"{field[0]}='{self.model_name} {field[0]} 1'" for field in self.fields if field[0] not in ['id', 'uuid']]),
                '{fields_setup_obj_2}' : ', '.join([f"{field[0]}='{self.model_name} {field[0]} 2'" for field in self.fields if field[0] not in ['id', 'uuid']]),
                '{fields_create_obj_1}' : f'self.test_obj_1.{self.fields[1][0]}, "{self.model_name} {self.fields[1][0]} 1"',
                '{fields_create_obj_2}' : f'self.test_obj_2.{self.fields[1][0]}, "{self.model_name} {self.fields[1][0]} 2"',
                '{fields_read_obj_1}' : f"{self.fields[1][0]}='{self.model_name} {self.fields[1][0]} 1'",        
                '{fields_read_obj_2}' : f"{self.fields[1][0]}='{self.model_name} {self.fields[1][0]} 2'",
                '{fields_read_equal_obj_1}' : f"test_obj_1_db.{self.fields[1][0]}, '{self.model_name} {self.fields[1][0]} 1'", 
                '{fields_read_equal_obj_2}' : f"test_obj_2_db.{self.fields[1][0]}, '{self.model_name} {self.fields[1][0]} 2'",
                '{fields_first}' : f"{self.fields[1][0]}",
                '{update_text}' : f"Update Text {self.model_name} {self.fields[1][0]}",
                '{fields_delete_obj_1}' : f"'{self.model_name} {self.fields[1][0]} 1'"
            }
            
            for key, value in replacement_dict.items():
                content = content.replace(key, value)
                
            new_py_file = Path(self.app_name+'/tests.py')
            new_py_file.write_text(content)
            
            print(f"tests.py '{self.app_name}' created successfully.")
        except FileNotFoundError:
            print("tests.py fayli topilmadi.")
        except PermissionError:
            print(f"Ruxsat mavjud emas '{self.app_name}' papkasiga nusxalash uchun.")
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")
    
    def add_urls_file(self):
        old_py_file = Path(self.app_name+'/urls.py')
        content = old_py_file.read_text()
        new_data_to_add = f"path('{self.model_name}/list/', {self.model_name}ListCreateApiView.as_view()),\n"
        new_views_to_add = f'{self.model_name}ListCreateApiView,'
        if new_data_to_add not in content and new_data_to_add not in content:
            pattern = re.compile(r'urlpatterns\s*=\s*\[\s*', re.DOTALL)
            import_pattern = re.compile(r'from\s+\.views\s+import\s+', re.DOTALL)
            
            match = pattern.search(content)
            match_import = import_pattern.search(content)
            
            if match and match_import :
                # Izlash natijasini topish
                start_index = match.end()
                
                end_index_import = match_import.end()

                # Malumotni qo'shish
                
                new_content = content[:start_index] + new_data_to_add + '\n' + content[start_index:]
                
                new_content_import = new_content[:end_index_import ] + new_views_to_add  + new_content[end_index_import:]
                
                
                # Faylni qayta yozish
                new_py_file = Path(self.app_name+'/urls.py')
                new_py_file.write_text(new_content_import)
                
                
                print(f"urls.py  '{self.app_name}' update successfully.")
                

            else:
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
                    
                    print(f"urls.py '{self.app_name}' update successfully.")
                except FileNotFoundError:
                    print("urls.py fayli topilmadi.")
                except PermissionError:
                    print(f"Ruxsat mavjud emas '{self.app_name}' papkasiga nusxalash uchun.")
                except Exception as e:
                    print(f"Xatolik yuz berdi: {e}")
        
    
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