from django.db.models import CharField, Model, TextField
from simple_history.models import HistoricalRecords


class Document(Model):
    name = CharField(max_length=30)
    content = TextField()
    history = HistoricalRecords()

    def __str__(self):
        return self.name
