from django.urls import path

from .views import (CreateDocumentView, IndexPageView, ListDocument,
                    ListFirstLastVersions, ListVersionDocument,
                    ReadDocumentView, UpdateDocument)

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('list_documents/', ListDocument.as_view(), name='list_documents'),
    path('create_document/', CreateDocumentView.as_view(), name='create_document'),
    path('details_document/<int:pk>', ReadDocumentView.as_view(), name='details_document'),
    path('update_document/<int:pk>', UpdateDocument.as_view(), name='update_document'),
    path('list_of_all_versions/<int:pk>', ListVersionDocument.as_view(), name='versions_document'),
    path('current_and_first_versions/<int:pk>', ListFirstLastVersions.as_view(),
         name='current_and_first_versions'),
]
