import pytest
from django.urls import reverse

from project.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_resp_status_code(resp):
    assert resp.status_code == 200


def test_home_link(resp):
    assert_contains(resp, reverse('base:home'))
