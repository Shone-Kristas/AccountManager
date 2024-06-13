from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from accounts.models import User

class UserListViewTests(TestCase):
    def setUp(self):
        User.objects.create(surname='Doe', name='Jane', patronymic='Alex', phone='7234567890', email='john.doe@example.com')
        User.objects.create(surname='Smith', name='Jane', phone='7345678901', email='jane.smith@example.com')

        self.client = APIClient()
        self.url = '/users/search/'

    def test_search_by_surname(self):
        response = self.client.get(self.url, {'search': 'Doe'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_by_name(self):
        response = self.client.get(self.url, {'search': 'Jane'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_by_phone(self):
        response = self.client.get(self.url, {'search': '1234567890'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_search_by_email(self):
        response = self.client.get(self.url, {'search': 'john.doe@example.com'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_by_nonexistent_query(self):
        response = self.client.get(self.url, {'search': 'NONE'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_search_without_query(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 1)