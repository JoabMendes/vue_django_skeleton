# Django
from django.test import TestCase
from django.core.management import call_command
# DRF
from rest_framework.test import APIClient

# Models
from domain.models import Review, Reviewer

# import json
import os
os.environ['RECAPTCHA_TESTING'] = 'True'


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

    def test_get_member_reviews(self):

        endpoint = '/api/v1/reviews/member/1'

        response = self.client.get(endpoint)

        expected = {
            "data": [
                {
                    "approved": True,
                    "comment": "This place is really nice",
                    "created_at": "2018-09-21T22:07:39.777000Z",
                    "reviewer": {
                        "avatar": (
                            "http://www.gravatar.com/avatar/"
                            "8cb5fa316e5e32877c4e8055f6f2afa4?d=404"
                        ),
                        "created_at": "2018-09-21T22:07:07.287000Z",
                        "email": "joab.mendes.r2d2@gmail.com",
                        "id": 1,
                        "name": "Joabe Mendes",
                        "updated_at": "2018-09-21T22:07:07.287000Z"
                    },
                    "stars": 4,
                    "updated_at": "2018-09-21T22:07:39.777000Z"
                },
                {
                    "approved": True,
                    "comment": "This place is awesome!",
                    "created_at": "2018-09-21T22:08:05.885000Z",
                    "reviewer": {
                        "avatar": (
                            "http://www.gravatar.com/avatar/"
                            "8cb5fa316e5e32877c4e8055f6f2afa4?d=404"
                        ),
                        "created_at": "2018-09-21T22:07:07.287000Z",
                        "email": "joab.mendes.r2d2@gmail.com",
                        "id": 1,
                        "name": "Joabe Mendes",
                        "updated_at": "2018-09-21T22:07:07.287000Z"
                    },
                    "stars": 5,
                    "updated_at": "2018-09-21T22:08:05.885000Z"
                },
                {
                    "approved": True,
                    "comment": "This place is so so!",
                    "created_at": "2018-09-21T22:08:21.790000Z",
                    "reviewer": {
                        "avatar": (
                            "http://www.gravatar.com/avatar/"
                            "8cb5fa316e5e32877c4e8055f6f2afa4?d=404"
                        ),
                        "created_at": "2018-09-21T22:07:07.287000Z",
                        "email": "joab.mendes.r2d2@gmail.com",
                        "id": 1,
                        "name": "Joabe Mendes",
                        "updated_at": "2018-09-21T22:07:07.287000Z"
                    },
                    "stars": 2,
                    "updated_at": "2018-09-21T22:08:21.790000Z"
                }
            ],
            "offset": 0,
            "reviews_per_page": 10
        }

        self.assertEqual(response.json(), expected)

        # print(json.dumps(response.json(), indent=4, sort_keys=True))
