from django.test import TestCase, Client
import json

class UserTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.valid_user = {
            "id": "123456782",
            "name": "Test User",
            "phone": "0521234567",
            "address": "Somewhere 1"
        }

    def test_get_all_users(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_valid_user(self):
        response = self.client.post('/users/create/', data=json.dumps(self.valid_user), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['name'], "Test User")