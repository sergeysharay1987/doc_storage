# from document_storage.tests.fixtures import *

import pytest
from django.test.client import Client
from model_bakery import baker


@pytest.fixture()
def client():
    return Client()


@pytest.fixture()
def documents(db):
    return baker.make('Document', _quantity=3)