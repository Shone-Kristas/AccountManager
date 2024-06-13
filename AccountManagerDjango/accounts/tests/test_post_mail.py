from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class UsersAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/create/'
        self.headers = {
            'x-Device': 'mail',
        }

    def test_create_valid_user_1(self):
        valid_payload = {
            "name": "John",
            "email": "john.doe@example.com",
        }
        response = self.client.post(self.url, data=valid_payload, format='json', headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_valid_user_2(self):
        valid_payload = {
            "name": "John",
            "email": "john.doe@example.com",
            "birth_date": "2000-01-01",
            "passport_number": "AB1234567",
        }
        response = self.client.post(self.url, data=valid_payload, format='json', headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_another_user(self):
        another_payload = {
            "surname": "Smith",
            "name": "Jane",
            "patronymic": "",
            "birth_date": "1995-05-15",
            "passport_number": "CD9876543",
            "birth_place": "Los Angeles",
            "phone": "9876543210",
            "email": "jane.smith@example.com",
            "registration_address": "789 Oak St, Los Angeles, USA",
            "residential_address": "234 Pine St, Los Angeles, USA"
        }
        response = self.client.post(self.url, data=another_payload, format='json', headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_validation_error_1(self):
        error_payload = {
            "name": "John",
            "birth_date": "2000-01-01",
            "passport_number": "AB1234567",
        }
        response = self.client.post(self.url, data=error_payload, format='json', headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
        self.assertIn("Username and email are required for mail device.", response.data["error"])

    def test_create_validation_error_2(self):
        error_payload = {
            "email": "john.doe@example.com",
            "birth_date": "2000-01-01",
        }
        response = self.client.post(self.url, data=error_payload, format='json', headers=self.headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
        self.assertIn("Username and email are required for mail device.", response.data["error"])

    def test_unsupported_device(self):
        headers = {
            'x-Device': 'unsupported',
        }
        valid_payload = {
            "name": "John",
            "email": "john.doe@example.com",
        }
        response = self.client.post(self.url, data=valid_payload, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Unsupported x-Device type', response.data['error'])

