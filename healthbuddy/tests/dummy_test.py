import pytest
from django.urls import reverse, NoReverseMatch


@pytest.mark.django_db
def test_dummy_view(client):
    try:
        # Attempt to reverse the URL
        url = reverse('homePage123')  # Replace 'homepage' with your actual URL name
    except NoReverseMatch:
        pytest.fail("The 'homePage123' URL name is not defined. Check your urls.py.")

    # Make the GET request
    response = client.get(url)

    # Assert the response status code is 200
    assert response.status_code == 200, "Homepage did not load successfully."
