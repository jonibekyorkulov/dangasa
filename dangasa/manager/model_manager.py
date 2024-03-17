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
                self.create_views_file()
        except Exception as e:
            print(str(e))
            
    def create_views_file(self):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))

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
            end_index = match.end()

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
        if (f'{self.model_name}RetrieveUpdateDestroyAPIView' not in content):   
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
                self.create_serializers_file()
        except Exception as e:
            print(str(e))
            
    def create_serializers_file(self):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))

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
            end_index = match.end()

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
                self.create_urls_file()
        except Exception as e:
            print(str(e))
    
    
    def add_urls_file(self):
        old_py_file = Path(self.app_name+'/urls.py')
        content = old_py_file.read_text()
        new_data_to_add = f"path('{self.model_name}/list/', {self.model_name}ListCreateApiView.as_view()),\n"
        new_data_to_add_retrive = f"path('{self.model_name}/<int:pk>/', {self.model_name}RetrieveUpdateDestroyAPIView.as_view()),\n"
        new_views_to_add = f'{self.model_name}ListCreateApiView,'
        new_views_to_add_retrive = f'{self.model_name}RetrieveUpdateDestroyAPIView,'
        pattern = re.compile(r'urlpatterns\s*=\s*\[\s*', re.DOTALL)
        import_pattern = re.compile(r'from\s+\.views\s+import\s+', re.DOTALL)
        
        match = pattern.search(content)
        match_import = import_pattern.search(content)
        
        
            
        if match and match_import :
            if new_data_to_add not in content and new_data_to_add_retrive not in content:
                start_index = match.end()
                
                end_index_import = match_import.end()
                
                new_content = content[:start_index] + new_data_to_add + '\n' + content[start_index:]
                new_content = new_content[:start_index] + new_data_to_add_retrive + '\n' + new_content[start_index:]
                
                new_content_import = new_content[:end_index_import ] + new_views_to_add  + new_content[end_index_import:]
                new_content_import = new_content_import[:end_index_import ] + new_views_to_add_retrive  + new_content_import[end_index_import:]
                
                
                new_py_file = Path(self.app_name+'/urls.py')
                new_py_file.write_text(new_content_import)
                
                
                print(f"urls.py  '{self.app_name}' update successfully.")
            else:
                print(f"urls.py < {self.model_name}RetrieveUpdateDestroyAPIView > or < {self.model_name}ListCreateApiView > alredy used.")
            

        else:
            try:
                current_dir = os.path.dirname(os.path.abspath(__file__))


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