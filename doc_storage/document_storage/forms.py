from django.core.exceptions import ValidationError
from django.forms import ModelForm
from document_storage.models import Document


class CreateDocForm(ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'content']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Document.objects.filter(name__iexact=name).count() and self.get_context():
            print(f'self.get_context(): {self.get_context()}')
            print(f'f.errors: {self.errors}')
            print(f'form is invalid')
            raise ValidationError('Name of the document must be unique')
        return name


class UpdateDocForm(CreateDocForm):

    def clean_name(self):
        # print(f'self.errors: {self.errors}')
        # print(f'')
        return self.cleaned_data['name']
