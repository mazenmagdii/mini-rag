from helpers.config import get_settings, Settings

class BaseController:
    def __init__(self, settings):
        self.app_settings = get_settings()

    