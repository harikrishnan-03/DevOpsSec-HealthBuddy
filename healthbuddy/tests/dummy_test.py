import pytest
from django.urls import reverse, NoReverseMatch


@pytest.mark.django_db
def test_dummy_view(client):
    url = reverse("unitTesting")
    response = client.get(url)
    assert response.status_code == 200
    assert response.content == b"Testing Done"
