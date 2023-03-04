from django.apps import AppConfig

class JobappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' # or 'django.db.models.AutoField' if you prefer the default
    name = 'jobapp'
