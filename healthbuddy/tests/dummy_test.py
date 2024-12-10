import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_dummy_view(client):
    response = client.get(reverse("homePage"))
    assert response.status_code == 200
    assert b"Thank you for trusting us with your health journey" in response.content
