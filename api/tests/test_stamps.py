
# Django
from django.test import TestCase
from django.core.management import call_command
# DRF
from rest_framework.test import APIClient

# Models
from domain.models import Stamp, Member

# import json


class TestStampAPI(TestCase):

    def setUp(self):

        # Set up fake data
        call_command('loaddata', 'seeds/auth', verbosity=0)
        call_command('loaddata', 'seeds/stamps', verbosity=0)
        call_command('loaddata', 'seeds/sector', verbosity=0)
        call_command('loaddata', 'seeds/member', verbosity=0)
        call_command('loaddata', 'seeds/reviewer', verbosity=0)
        call_command('loaddata', 'seeds/review', verbosity=0)

        self.client = APIClient()

    def test_get_stamp(self):
        endpoint = '/api/v1/stamps/1'
        response = self.client.get(endpoint)
        stamp = Stamp.objects.get(pk=1)
        json_response = response.json()
        self.assertEqual(stamp.title, json_response['title'])
        # print(json.dumps(response.json(), indent=4, sort_keys=True))

    def test_get_member_stamps(self):
        endpoint = '/api/v1/stamps/member/1'
        response = self.client.get(endpoint)
        json_response = response.json()
        member = Member.objects.get(pk=1)
        member_stamp = member.stamps.first()
        self.assertEqual(member_stamp.id, json_response[0]['id'])
        # print(json.dumps(response.json(), indent=4, sort_keys=True))
