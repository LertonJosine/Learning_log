from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    texto = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.texto