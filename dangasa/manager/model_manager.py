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
        pass
    
    def create_tests(self):
        pass
    
    def main(self):
        self.create_views()
        self.create_serializers()
        self.create_urls()
        self.create_tests()