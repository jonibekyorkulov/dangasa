from pathlib import Path
import os
import sys

def create_pagination_file(app_name):
    new_file = Path(app_name)
    code = """from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from typing_extensions import OrderedDict
from datetime import datetime


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        if self.request.query_params.get('page_size'):
            page_size = self.request.query_params.get('page_size')
        else:
            page_size = 10
        return Response(OrderedDict([
            ('server_time', datetime.now()),
            ('count', self.page.paginator.count),
            ('page_count', self.page.paginator.num_pages),
            ('page', self.page.number),
            ('page_size', int(page_size)),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
    """
    new_file.write_text(code)
    
    print(f"pagination.py created successfully.")


def main_pagination(app_name):
    try:
        app_name = app_name+'/pagination.py'
        if os.path.exists(app_name):
            print("pagination.py already exists!")
        else:
        # Create a new Python file
            create_pagination_file(app_name)
    except Exception as e:
        print(str(e))
        