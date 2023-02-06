from django.apps import AppConfig


class OthersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'others'

    def ready(self):
        import others.signal
