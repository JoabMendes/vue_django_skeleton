# Django
from django.test import TestCase
from django.core.management import call_command
# DRF
from rest_framework.test import APIClient

# Models
from domain.models import Review, Reviewer

import os

os.environ['RECAPTCHA_TESTING'] = 'True'

# import json


class TestReviewAPI(TestCase):

    def setUp(self):

        # Set up fake data
        call_command('loaddata', 'seeds/auth', verbosity=0)
        call_command('loaddata', 'seeds/stamps', verbosity=0)
        call_command('loaddata', 'seeds/sector', verbosity=0)
        call_command('loaddata', 'seeds/member', verbosity=0)
        call_command('loaddata', 'seeds/reviewer', verbosity=0)
        call_command('loaddata', 'seeds/review', verbosity=0)

        self.client = APIClient()

    def test_get_review(self):
        endpoint = '/api/v1/reviews/1'
        response = self.client.get(endpoint)
        review = Review.objects.get(pk=1)
        json_response = response.json()
        self.assertEqual(
            review.stars, json_response['stars']
        )
        self.assertEqual(
            review.comment, json_response['comment']
        )
        self.assertEqual(
            review.reviewer.name, json_response['reviewer']['name']
        )
        self.assertEqual(
            review.reviewer.email, json_response['reviewer']['email']
        )

    def test_post_review_reviewer_dont_exists(self):
        endpoint = '/api/v1/reviews/'
        payload = {
            'reviewer': {
                'name': 'John Mayer',
                'email': 'john.mayer@mail.com'
            },
            'recaptcha': 'dummy value',
            'stars': 5,
            'comment': 'Nice place',
            'member': 1
        }
        response = self.client.post(
            endpoint, data=payload, format='json'
        )
        json_response = response.json()
        review = Review.objects.last()
        self.assertEqual(
            review.stars, json_response['stars']
        )
        self.assertEqual(
            review.comment, json_response['comment']
        )
        self.assertEqual(
            review.reviewer.name, json_response['reviewer']['name']
        )
        self.assertEqual(
            review.reviewer.email, json_response['reviewer']['email']
        )

        # print(json.dumps(response.json(), indent=4, sort_keys=True))

    def test_post_review_reviewer_exists(self):
        endpoint = '/api/v1/reviews/'
        reviewer = Reviewer.objects.last()
        payload = {
            'reviewer': {
                'name': reviewer.name,
                'email': reviewer.email
            },
            'recaptcha': 'dummy value',
            'stars': 5,
            'comment': 'Nice place',
            'member': 1
        }
        response = self.client.post(
            endpoint, data=payload, format='json'
        )
        json_response = response.json()
        review = Review.objects.last()
        self.assertEqual(
            review.stars, json_response['stars']
        )
        self.assertEqual(
            review.comment, json_response['comment']
        )
        self.assertEqual(
            review.reviewer.name, json_response['reviewer']['name']
        )
        self.assertEqual(
            review.reviewer.email, json_response['reviewer']['email']
        )

        # print(json.dumps(response.json(), indent=4, sort_keys=True))
