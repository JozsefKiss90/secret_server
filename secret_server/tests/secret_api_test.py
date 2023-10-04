import uuid

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from datetime import timedelta
from django.utils import timezone
from base.models import Secret

class SecretAPITest(APITestCase):
    def setUp(self):
        self.url = reverse('create_secret')
        self.secret_data = {
            'secret_text': 'My Secret Text',
            'expireAfterViews': 8,
            'expireAfter': 5
        }
        self.secret = Secret.objects.create(
            secret_text='Some secret text',
            remaining_views=3,
        )

    def test_create_secret(self):
        response = self.client.post(self.url, self.secret_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('hash', response.data)

    def test_retrieve_secret(self):
        url = reverse('retrieve_secret', args=[self.secret.hash])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['secret_text'], 'Some secret text')

    def test_expired_secret(self):
        self.secret.expires_at = timezone.now() - timedelta(minutes=10)
        self.secret.save()
        print(f"secret expires at: {self.secret.expires_at}")
        print(f"expires_at: {self.secret.expires_at}, now: {timezone.now()}")

        url = reverse('retrieve_secret', args=[self.secret.hash])
        response = self.client.get(url)
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_410_GONE)

    def test_secret_not_found(self):
        non_existent_uuid = uuid.uuid4()
        url = reverse('retrieve_secret', args=[non_existent_uuid])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'], 'The requested secret does not exist.')

    def test_secret_unavailable(self):
        self.secret.remaining_views = 1  # Setting the remaining views to 1
        self.secret.save()

        url = reverse('retrieve_secret', args=[self.secret.hash])
        self.client.get(url)  # Consuming the last view

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'],
                         'The requested secret has reached its view limit and is no longer available.')

    def test_invalid_secret_data(self):
        url = reverse('create_secret')
        invalid_data = {
            'secret_text': '',
            'expireAfterViews': 8,
            'expireAfter': 5
        }
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertIn('This field may not be blank.', response.data.get('secret_text', []))
