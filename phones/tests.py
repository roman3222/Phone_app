from unittest import TestCase
from rest_framework.test import APIClient


class TestSmpleViews(TestCase):
    def test_view(self):
        url = '/catalog/'
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
