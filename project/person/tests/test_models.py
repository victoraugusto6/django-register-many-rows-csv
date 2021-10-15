import pytest
from model_bakery import baker

from project.person.models import Person


@pytest.fixture
def person():
    return baker.make(Person)


def test_create_person(db, person):
    assert Person.objects.exists()
