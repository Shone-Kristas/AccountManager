from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class UsersAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/create/'
        self.headers = {
            'x-Device': 'web',
        }

    def test_create_valid_user_1(self):
        valid_payload = {
            "surname": "Doe",
            "name": "John",
            "patronymic": "Alex",
            "birth_date": "2000-01-01",
            "passport_number": "AB1234567",
            "birth_place": "New York",
            "phone": "7234567890",
            "registration_address": "123 Main St, New York, USA",
        }
        response = self.client.post(self.url, data=valid_payload, format='json', headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_valid_user_2(self):
        valid_payload = {
            "surname": "Doe",
            "name": "John",
            "patronymic": "Alex",
            "birth_date": "2000-01-01",
            "passport_number": "AB1234567",
            "birth_place": "New York",
            "phone": "7234567890",
            "email": "john.doe@example.com",
            "registration_address": "123 Main St, New York, USA",
            "residential_address": "456 Elm St, New York, USA"
        }
        response = self.client.post(self.url, data=valid_payload, format='json', headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_validation_error(self):
        error_payload = {
            # "surname": "Doe",
            # "name": "John",
            # "patronymic": "Alex",
            "birth_date": "2000-01-01",
            "passport_number": "AB1234567",
            "birth_place": "New York",
            "phone": "7234567890",
            "email": "john.doe@example.com",
            "registration_address": "123 Main St, New York, USA",
            "residential_address": "456 Elm St, New York, USA"
        }
        response = self.client.post(self.url, data=error_payload, format='json', headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
        self.assertIn("The following fields are required: surname, name, patronymic", response.data["error"])

    def test_unsupported_device(self):
        headers = {
            'x-Device': 'unsupported',
        }
        valid_payload = {
            "surname": "Doe",
            "name": "John",
            "patronymic": "Alex",
            "birth_date": "2000-01-01",
            "passport_number": "AB1234567",
            "birth_place": "New York",
            "phone": "7234567890",
            "email": "john.doe@example.com",
            "registration_address": "123 Main St, New York, USA",
            "residential_address": "456 Elm St, New York, USA"
        }
        response = self.client.post(self.url, data=valid_payload, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Unsupported x-Device type', response.data['error'])