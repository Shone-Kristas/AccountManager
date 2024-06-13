from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from accounts.models import User





class GetUserTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            surname = "Doe",
            name = "John",
            patronymic = "Alex",
            birth_date = "2000-01-01",
            passport_number = "AB1234567",
            birth_place = "New York",
            phone = "7234567890",
            email = "john.doe@example.com",
            registration_address = "123 Main St, New York, USA",
            residential_address = "456 Elm St, New York, USA"
        )
        self.url = reverse('user-detail', kwargs={'pk': self.user.pk})

    def test_get_existing_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['surname'], self.user.surname)
        self.assertEqual(response.data['name'], self.user.name)


    def test_get_non_existing_user(self):
        invalid_url = reverse('user-detail', kwargs={'pk': self.user.pk + 1})
        response = self.client.get(invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('User not found', response.data['error'])