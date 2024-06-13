from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

class UsersAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/create/'
        self.headers = {
            'x-Device': 'mail',
        }
        self.valid_payload = {
            "surname": "Doe",
            "name": "John",
            "patronymic": "Alex",
            "birth_date": "2000-01-01",
            "passport_number": "AB1234567",
            "birth_place": "New York",
            "phone": "1234567890",
            "email": "john.doe@example.com",
            "registration_address": "123 Main St, New York, USA",
            "residential_address": "456 Elm St, New York, USA"
        }
        self.invalid_payload = {
            "surname": "",  # Пустая строка для проверки обязательного поля
            "name": "John",
            "patronymic": "Alex",
            "birth_date": "2000-01-01",
            "passport_number": "AB1234567",
            "birth_place": "New York",
            "phone": "1234567890",
            "email": "john.doe@example.com",
            "registration_address": "123 Main St, New York, USA",
            "residential_address": "456 Elm St, New York, USA"
        }

    def test_create_valid_user(self):
        response = self.client.post(self.url,
                                    data=self.valid_payload,
                                    format='json',
                                    **self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['surname'], self.valid_payload['surname'])
        self.assertEqual(response.data['email'], self.valid_payload['email'])

    def test_create_invalid_user(self):
        response = self.client.post(self.url,
                                    data=self.invalid_payload,
                                    format='json',
                                    **self.headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('surname', response.data)