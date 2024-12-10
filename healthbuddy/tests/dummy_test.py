import pytest
from django.urls import reverse
from django.test import Client
from django.test import TestCase

# Dummy test to check basic Django view response
@pytest.mark.django_db
def test_dummy_view():
    response = self.client.get(reverse('homePage'))  
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Features")  
    pass
