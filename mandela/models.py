from django.db import models

class Biography(models.Model):
    """
    A model to represent the biography of a person.

    Attributes:
        content (str): The content of the biography.
    """
    content = models.TextField()
    

class Quote(models.Model):
    """
    A model to represent a quote along with its source.

    Attributes:
        content (str): The content of the quote.
        source (str): The source of the quote.
    """
    content = models.TextField()
    source = models.CharField(max_length=100)

class Legacy(models.Model):
    """
    A model to represent the legacy of a person.

    Attributes:
        content (str): The content of the legacy.
    """
    content = models.TextField()
