from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Document


class CreateDocForm(ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'content']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Document.objects.filter(name__iexact=name).count() and not self.initial:
            raise ValidationError('Name of the document must be unique')

        return name

