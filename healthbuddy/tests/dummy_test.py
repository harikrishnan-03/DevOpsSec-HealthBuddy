from django.test import TestCase
from django.urls import reverse

class DummyViewTest(TestCase):
    def test_dummy_view(self):
        """
        Test the basic functionality of the homepage.
        """
        response = self.client.get(reverse('homePage'))  
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Features")  
