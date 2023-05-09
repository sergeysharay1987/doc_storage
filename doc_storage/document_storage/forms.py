from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Document


def check_word(word):
    for symbol in word:
        if not symbol.isalpha():
            return False
    return True


def check_words(words):
    for word in words.split(' '):
        if not check_word(word):
            return False
    return True


class CreateDocForm(ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'content']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Document.objects.filter(name__iexact=name).count() and not self.initial:
            raise ValidationError('Name of the document must be unique')
        elif len(name.split(' ')) == 1 and not check_word(name) or len(name.split(' ')) > 1 and not check_words(name):
            raise ValidationError(f'Wrong symbol(s) in document name')
        return name