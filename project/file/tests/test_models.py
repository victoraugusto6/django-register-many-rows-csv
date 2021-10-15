import pytest
from model_bakery import baker

from project.file.models import File, import_data_create
from project.person.models import Person


@pytest.fixture
def csv_create():
    return baker.make(File, file='1_linha.csv', method='create')


@pytest.fixture
def csv_bulk():
    return baker.make(File, file='1_linha.csv', method='bulk')


def test_send_file_create(db, csv_create):
    import_data_create(csv_create.pk)

    assert File.objects.exists()
    assert Person.objects.exists()


def test_send_file_bulk_create(db, csv_bulk):
    import_data_create(csv_bulk.pk)

    assert File.objects.exists()
    assert Person.objects.exists()
