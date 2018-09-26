# Django
from django.test import TestCase
from django.core.management import call_command
# DRF
from rest_framework.test import APIClient

# Models
from domain.models import Reviewer

# import json


class TestReviewerAPI(TestCase):

    def setUp(self):

        # Set up fake data
        call_command('loaddata', 'seeds/auth', verbosity=0)
        call_command('loaddata', 'seeds/stamps', verbosity=0)
        call_command('loaddata', 'seeds/sector', verbosity=0)
        call_command('loaddata', 'seeds/member', verbosity=0)
        call_command('loaddata', 'seeds/reviewer', verbosity=0)
        call_command('loaddata', 'seeds/review', verbosity=0)

        self.client = APIClient()

    def test_get_reviewer(self):
        endpoint = '/api/v1/reviewer/1'
        response = self.client.get(endpoint)
        reviewer = Reviewer.objects.get(pk=1)
        json_response = response.json()
        self.assertEqual(reviewer.email, json_response['email'])
        self.assertEqual(reviewer.name, json_response['name'])

        # print(json.dumps(response.json(), indent=4, sort_keys=True))

    def test_post_reviewer_not_exist(self):
        endpoint = '/api/v1/reviewer/'
        payload = {
            'name': 'John Mayer',
            'email': 'john.mayer@mail.com',
        }
        response = self.client.post(endpoint, payload, format='json')

        reviewer = Reviewer.objects.last()
        json_response = response.json()
        self.assertEqual(reviewer.email, json_response['email'])
        self.assertEqual(reviewer.name, json_response['name'])

        # print(json.dumps(response.json(), indent=4, sort_keys=True))

    def test_post_reviewer_exists(self):
        endpoint = '/api/v1/reviewer/'
        payload = {
            'name': 'John Mayer',
            'email': 'john.mayer@mail.com',
        }
        reviewer = Reviewer(
            name='John Mayer',
            email='john.mayer@mail.com'
        )
        reviewer.save()
        response = self.client.post(endpoint, payload, format='json')
        json_response = response.json()
        self.assertEqual(reviewer.email, json_response['email'])
        self.assertEqual(reviewer.name, json_response['name'])

        # print(json.dumps(response.json(), indent=4, sort_keys=True))
