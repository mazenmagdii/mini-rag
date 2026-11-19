from .BaseController import BaseController
from fastapi import UploadFile

class DataController(BaseController):
    def __init__(self, settings):
        super().__init__(settings)
        self.scale_size = 1048576

    def validate_uploaded_file(self, file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False
        if file.size > self.app_settings.FILE_MAX_SIZE * self.scale_size:
            return False
        return True

