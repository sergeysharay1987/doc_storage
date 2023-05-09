import pytest
from django.test.client import Client
from django.urls import reverse
from model_bakery import baker

data_for_history_queryset = [{
    'name': 'Passport new',
    'content': 'Something'
}, {
    'name': 'Passport new one',
    'content': 'Something new one'
}, {
    'name': 'Passport new two',
    'content': 'Something new two'
}, {
    'name': 'Passport new three',
    'content': 'Something new three'
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


@pytest.fixture(params=[1, 10000])
def existing_and_non_existing_doc(request, documents):
    return documents[request.param]

