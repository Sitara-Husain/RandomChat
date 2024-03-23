"""
Chat: Django Admin customization
"""
# django imports
from django.contrib import admin

# local imports
from apps.chat.models import SentenceCorpus


@admin.register(SentenceCorpus)
class SentenceCorpusAdmin(admin.ModelAdmin):
    """
    admin interface for SentenceCorpus.
    """
    list_display = ('id', 'sentence')
