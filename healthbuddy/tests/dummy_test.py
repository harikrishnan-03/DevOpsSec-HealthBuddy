import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_dummy_view(client):
    url = reverse("homePage12")  
    response = client.get(url)

    # Check that the status code is 200
    assert response.status_code == 200
