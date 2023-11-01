from django.db.models import CharField, Model, TextField, DateTimeField
from simple_history.models import HistoricalRecords


class Document(Model):
    name = CharField(max_length=30)
    description = TextField()
    history = HistoricalRecords()

    def __str__(self):
        return self.name
