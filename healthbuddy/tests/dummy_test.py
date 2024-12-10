import pytest
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db
def test_dummy_view(client):
    response = client.get(reverse('homePage')) 
    assert response.status_code == 200
    assert b"Features" in response.content  
    pass
