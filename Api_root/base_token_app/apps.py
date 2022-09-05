from django.apps import AppConfig


class BaseTokenAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_token_app'
