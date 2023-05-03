from django.urls import reverse
from ..models import Document


def test_create_document(documents, client):
    response = client.post(reverse('create_document'), data={
        'name': 'Passport_1',
        'content': 'Very import document'
    })
    assert response.status_code == 302
    assert response.url == reverse('create_document')
    assert Document.objects.all().count() == 4
    client.post(reverse('create_document'), data={
        'name': 'Passport_1',
        'content': 'Very import document'
    })
    assert Document.objects.all().count() == 4


def test_details_document(documents, client):
    response = client.get(
        reverse('details_document', kwargs={'pk': documents[0].pk}))

    assert response.status_code == 200
    assert response.context['doc'] == documents[0]


def test_list_documents(documents, client):
    response = client.get(reverse('list_documents'))
    assert response.status_code == 200
    list_documents = list(response.context['docs'])
    assert list_documents == documents


def test_update_document(documents, client):
    assert documents[0].history.all().count() == 1
    response = client.post(reverse('update_document',
                                   kwargs={'pk': documents[0].pk}), data={
                                                                        'name': 'Passport_changed',
                                                                        'content': 'Changed'
                                                                        })
    documents[0].refresh_from_db()
    assert response.status_code == 302
    assert documents[0].name == 'Passport_changed'
    assert documents[0].content == 'Changed'
    assert documents[0].history.all().count() == 2
    response = client.post(reverse('update_document',
                                   kwargs={'pk': documents[0].pk}), data={
                                                                          'name': 'Passport_changed',
                                                                          'content': 'Changed'
                                                                          })
    assert response.status_code == 302
    assert documents[0].history.all().count() == 2  # We make sure that record has not been updated and number of
    # versions has not beeb changed


def test_list_documents_versions(documents_with_several_versions_of_doc_0, client):
    response = client.get(
        reverse('versions_document', kwargs={'pk': documents_with_several_versions_of_doc_0[0].pk}))
    assert response.status_code == 200
    assert documents_with_several_versions_of_doc_0[0].history.all()
    assert list(response.context['docs'].all()) == list(documents_with_several_versions_of_doc_0[0].history.all())


def test_list_first_and_current_versions(documents_with_several_versions_of_doc_0, client):
    url = reverse('current_and_first_versions',
                  kwargs={'pk': documents_with_several_versions_of_doc_0[0].pk})
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['delta']
