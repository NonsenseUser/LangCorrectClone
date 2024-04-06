from django.apps import AppConfig
from django.db.models.signals import post_save


class LangcorrectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'langCorrect'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals

