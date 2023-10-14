from django.apps import AppConfig


class TailorappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TailorApp'
    
    def ready(self):
        from TailorApp import signals
