"""
Chat config file
"""
from django.apps import AppConfig


class ChatConfig(AppConfig):
    """
    Chat config class
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.chat'
