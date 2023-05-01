from django.db.models import CharField, TextField, Model, ForeignKey, CASCADE
from django.urls import reverse
from simple_history.models import HistoricalRecords


# Create your models here.

class Document(Model):
    name = CharField(max_length=30)
    content = TextField()
    history = HistoricalRecords()

    def __str__(self):
        return self.name
