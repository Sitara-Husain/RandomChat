"""
Create Chat related models here.
"""
# Django imports
from django.db import models


class SentenceCorpus(models.Model):
    """
    A Django model to store a corpus of sentences.

    Attributes:
        sentence (CharField): A field to store the sentences.
            Maximum length is set to 500 characters.
    """

    sentence = models.CharField(max_length=500)

    def __str__(self):
        """
        Returns the string representation of the object.

        Returns:
            str: The sentence stored in the object.
        """
        return self.sentence

    class Meta:
        """
        Metadata for the SentenceCorpus model.
        """
        db_table = "sentence_corpus"
        verbose_name = "Sentence Corpus"
