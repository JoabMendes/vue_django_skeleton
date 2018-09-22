
# Django
from django.test import TestCase
from django.core.management import call_command
# DRF
from rest_framework.test import APIClient

# Models
from domain.models import Sector, Member

# import json


class TestSectorAPI(TestCase):

    def setUp(self):

        # Set up fake data
        call_command('loaddata', 'seeds/auth', verbosity=0)
        call_command('loaddata', 'seeds/stamps', verbosity=0)
        call_command('loaddata', 'seeds/sector', verbosity=0)
        call_command('loaddata', 'seeds/member', verbosity=0)
        call_command('loaddata', 'seeds/reviewer', verbosity=0)
        call_command('loaddata', 'seeds/review', verbosity=0)

        self.client = APIClient()

    def test_get_sector(self):
        endpoint = '/api/v1/sectors/1'
        response = self.client.get(endpoint)
        sector = Sector.objects.get(pk=1)
        json_response = response.json()
        self.assertEqual(sector.title, json_response['title'])
        # print(json.dumps(response.json(), indent=4, sort_keys=True))

    def test_get_member_sectors(self):
        endpoint = '/api/v1/sectors/member/1'
        response = self.client.get(endpoint)
        json_response = response.json()
        member = Member.objects.get(pk=1)
        member_sector = member.sectors.first()
        self.assertEqual(member_sector.id, json_response[0]['id'])
        # print(json.dumps(response.json(), indent=4, sort_keys=True))
