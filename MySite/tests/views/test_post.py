import pytest

from django.urls import reverse
from pip._vendor.requests import Response


@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home')
    response = client.get(url)

    assert response.status_code == 200
    assert response.content == b'Hello, world !'