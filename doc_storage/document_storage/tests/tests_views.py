from django.test.client import Client
import pytest
from django.urls import reverse
from document_storage.models import Document


# Create your tests here.


def test_create_document(db, client):
    response = client.post(reverse('create_document'), data={'name': 'Passport_1', 'content': 'Very import document'})
    assert response.status_code == 302
    assert response.url == reverse('create_document')
    assert Document.objects.all().count() == 1


def test_list_documents(documents, client):
    response = client.get(reverse('list_documents'))
    assert response.status_code == 200
    assert response.context['docs']


def test_update_document(documents, client):

    response = client.post(reverse('update_document', kwargs={'pk': documents[0].pk}), data={'name': 'Passport_changed',
                                                                                             'content': 'Changed'})

    assert response.status_code == 302

