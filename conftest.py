import pytest
from django.test.client import Client
from django.urls import reverse
from model_bakery import baker

data_for_history_queryset = [{
    'name': 'Passport_1',
    'content': 'Something_1'
}, {
    'name': 'Passport_2',
    'content': 'Something_2'
}, {
    'name': 'Passport_3',
    'content': 'Something_3'
}, {
    'name': 'Passport_4',
    'content': 'Something_4'
}]


@pytest.fixture()
def client():
    return Client()


@pytest.fixture()
def documents(db):
    return baker.make('Document', _quantity=3)


@pytest.fixture()
def documents_with_several_versions_of_doc_0(client, documents):
    url = reverse('update_document', kwargs={'pk': documents[0].pk})
    for data in data_for_history_queryset:
        client.post(url, data=data)
        return documents
