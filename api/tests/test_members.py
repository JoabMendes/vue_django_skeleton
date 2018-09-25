# Django
from django.test import TestCase
from django.core.management import call_command
# DRF
from rest_framework.test import APIClient

# import json


class TestMembersAPI(TestCase):

    def setUp(self):
        # Set up fake data
        call_command('loaddata', 'seeds/auth', verbosity=0)
        call_command('loaddata', 'seeds/stamps', verbosity=0)
        call_command('loaddata', 'seeds/sector', verbosity=0)
        call_command('loaddata', 'seeds/member', verbosity=0)
        call_command('loaddata', 'seeds/reviewer', verbosity=0)
        call_command('loaddata', 'seeds/review', verbosity=0)

        self.client = APIClient()

    def test_get_member(self):
        endpoint = '/api/v1/members/1'

        response = self.client.get(endpoint)

        json_response = response.json()

        self.assertTrue('active' in json_response)
        self.assertTrue('address' in json_response)
        self.assertTrue('created_at' in json_response)
        self.assertTrue('featured' in json_response)
        self.assertTrue('id' in json_response)
        self.assertTrue('description' in json_response)
        self.assertTrue('last_review' in json_response)
        self.assertTrue('logo' in json_response)
        self.assertTrue('name' in json_response)
        self.assertTrue('open_hours' in json_response)
        self.assertTrue('photo' in json_response)
        self.assertTrue('products' in json_response)
        self.assertTrue('sectors' in json_response)
        self.assertTrue('stamps' in json_response)
        self.assertTrue('stars_average' in json_response)
        self.assertTrue('updated_at' in json_response)
        self.assertTrue('latitude' in json_response)
        self.assertTrue('longitude' in json_response)

        # print(json.dumps(response.json(), indent=4, sort_keys=True))

    def test_get_featured_members(self):
        endpoint = '/api/v1/members/featured'

        response = self.client.get(endpoint)

        expected = [
            {
                "active": True,
                "address": (
                    "278 Frontenac St\r\n"
                    "Kingston, ON \r\n"
                    "K7L 3S8\r\nCanada"
                ),
                "created_at": "2018-09-25T21:28:51.782000Z",
                "description": (
                    "Lorem ipsum dolor sit amet, consectetur adipiscing "
                    "elit. Praesent placerat condimentum sem. Vivamus "
                    "egestas imperdiet condimentum. Sed viverra erat id "
                    "gravida aliquet. Suspendisse laoreet suscipit sem. "
                    "Ut aliquet felis a lorem auctor consectetur. Mauris "
                    "non erat euismod, volutpat diam ac, viverra ante. "
                    "Proin at quam cursus, feugiat felis eu, egestas mi. "
                    "Cras aliquam, neque quis gravida efficitur, nibh "
                    "enim condimentum lorem, placerat tincidunt augue "
                    "ligula ac erat. Sed diam diam, volutpat vitae "
                    "sapien a, pellentesque efficitur nulla. Nulla "
                    "vehicula neque in vulputate ultricies. In "
                    "id eleifend ipsum. Nunc a mollis libero."
                ),
                "featured": True,
                "id": 3,
                "last_review": {},
                "latitude": 44.2303428,
                "logo": "/media/member_logos/logo_ogmAToL.png",
                "longitude": -76.4987999,
                "name": "Member Example 3",
                "open_hours": (
                    "Sunday: Closed\r\n"
                    "Monday: 8am - 4pm\r\n"
                    "Tuesday: 8am - 4pm\r\n"
                    "Wednesday: 8am - 4pm\r\n"
                    "Thursday: 8am - 4pm\r\n"
                    "Friday: 8am - 4pm\r\n"
                    "Saturday: 8am - 4pm"
                ),
                "photo": "/media/member_logos/body-background-05_bMyMd3h.jpg",
                "position": "44.2303428,-76.4987999",
                "products": (
                    "Product 1,\r\n"
                    "Product 2,\r\n"
                    "Product 3,\r\n"
                    "Product 4,\r\n"
                    "Product 5,"
                ),
                "sectors": [
                    {
                        "created_at": "2018-09-21T20:55:53.985000Z",
                        "icon": "glass",
                        "id": 2,
                        "title": "Cocktails",
                        "updated_at": "2018-09-22T18:57:14.130000Z"
                    }
                ],
                "stamps": [
                    {
                        "created_at": "2018-09-21T21:02:31.123000Z",
                        "description": (
                            "This member doesn't use plastic "
                            "in any of it's processes."
                        ),
                        "id": 1,
                        "image": "/media/stamp_files/plastic_free.png",
                        "title": "Plastic Free",
                        "updated_at": "2018-09-21T21:02:31.123000Z"
                    },
                    {
                        "created_at": "2018-09-21T21:04:23.428000Z",
                        "description": "Products of this member are vegan",
                        "id": 4,
                        "image": "/media/stamp_files/organic.png",
                        "title": "Organic",
                        "updated_at": "2018-09-21T21:04:23.428000Z"
                    }
                ],
                "stars_average": 0,
                "updated_at": "2018-09-25T21:28:51.782000Z"
            }
        ]

        self.assertEqual(response.json(), expected)

        # print(json.dumps(response.json(), indent=4, sort_keys=True))

    def test_get_member_map(self):
        endpoint = '/api/v1/members/map/'

        response = self.client.get(endpoint)

        expected = [
            {
                "latitude": 44.2374429,
                "logo": "/media/member_logos/logo_Rj92dbE.png",
                "longitude": -76.49472889999998,
                "name": "Member Example",
                "photo": "/media/member_logos/body-background-05_Mf1qbQS.jpg",
                "stars_average": 4
            },
            {
                "latitude": 44.24415459999999,
                "logo": "/media/member_logos/logo_d4igqAQ.png",
                "longitude": -76.51116669999999,
                "name": "Member Example 2",
                "photo": "/media/member_logos/body-background-05_Et16gbq.jpg",
                "stars_average": 0
            },
            {
                "latitude": 44.2303428,
                "logo": "/media/member_logos/logo_ogmAToL.png",
                "longitude": -76.4987999,
                "name": "Member Example 3",
                "photo": "/media/member_logos/body-background-05_bMyMd3h.jpg",
                "stars_average": 0
            }
        ]

        self.assertEqual(response.json(), expected)

        # print(json.dumps(response.json(), indent=4, sort_keys=True))

    def test_post_member_map_km_success(self):

        """
            Tests POST /api/v1/members/map/
            Using km as metrics and retuning a simplified member
            response body.
        """

        endpoint = '/api/v1/members/map/'

        payload = {
            'location': {
                'lat': 44.2334508,
                'long': -76.4987131
            },
            'ratio': 1
        }

        response = self.client.post(endpoint, data=payload, format='json')

        expected = [
            {
                "latitude": 44.2374429,
                "logo": "/media/member_logos/logo_Rj92dbE.png",
                "longitude": -76.49472889999998,
                "name": "Member Example",
                "photo": "/media/member_logos/body-background-05_Mf1qbQS.jpg",
                "stars_average": 4
            },
            {
                "latitude": 44.2303428,
                "logo": "/media/member_logos/logo_ogmAToL.png",
                "longitude": -76.4987999,
                "name": "Member Example 3",
                "photo": "/media/member_logos/body-background-05_bMyMd3h.jpg",
                "stars_average": 0
            }
        ]

        self.assertEqual(response.json(), expected)

        # print(json.dumps(response.json(), indent=4, sort_keys=True))

    def test_post_member_map_km_full_success(self):

        """
            Tests POST /api/v1/members/map/
            Using km as metrics and retuning a full member
            response body.
        """

        endpoint = '/api/v1/members/map/'

        payload = {
            'location': {
                'lat': 44.2334508,
                'long': -76.4987131
            },
            'ratio': 1,
            'full': True
        }

        response = self.client.post(endpoint, data=payload, format='json')

        self.assertEqual(len(response.json()), 2)

        for json_response in response.json():
            self.assertTrue('active' in json_response)
            self.assertTrue('address' in json_response)
            self.assertTrue('created_at' in json_response)
            self.assertTrue('featured' in json_response)
            self.assertTrue('id' in json_response)
            self.assertTrue('description' in json_response)
            self.assertTrue('last_review' in json_response)
            self.assertTrue('logo' in json_response)
            self.assertTrue('name' in json_response)
            self.assertTrue('open_hours' in json_response)
            self.assertTrue('photo' in json_response)
            self.assertTrue('products' in json_response)
            self.assertTrue('sectors' in json_response)
            self.assertTrue('stamps' in json_response)
            self.assertTrue('stars_average' in json_response)
            self.assertTrue('updated_at' in json_response)
            self.assertTrue('latitude' in json_response)
            self.assertTrue('longitude' in json_response)

        # print(json.dumps(response.json(), indent=4, sort_keys=True))

    def test_post_member_map_ml_success(self):

        """
            Tests POST /api/v1/members/map/
            Using miles as metrics and retuning a simplified member
            response body.
        """

        endpoint = '/api/v1/members/map/'

        payload = {
            'location': {
                'lat': 44.2334508,
                'long': -76.4987131
            },
            'ratio': 0.6,
            'metric': 'ml'
        }

        response = self.client.post(endpoint, data=payload, format='json')

        expected = [
            {
                "latitude": 44.2374429,
                "logo": "/media/member_logos/logo_Rj92dbE.png",
                "longitude": -76.49472889999998,
                "name": "Member Example",
                "photo": "/media/member_logos/body-background-05_Mf1qbQS.jpg",
                "stars_average": 4
            },
            {
                "latitude": 44.2303428,
                "logo": "/media/member_logos/logo_ogmAToL.png",
                "longitude": -76.4987999,
                "name": "Member Example 3",
                "photo": "/media/member_logos/body-background-05_bMyMd3h.jpg",
                "stars_average": 0
            }
        ]

        self.assertEqual(response.json(), expected)

    def test_post_member_map_ml_full_success(self):

        """
            Tests POST /api/v1/members/map/
            Using miles as metrics and retuning a full member
            response body.
        """

        endpoint = '/api/v1/members/map/'

        payload = {
            'location': {
                'lat': 44.2334508,
                'long': -76.4987131
            },
            'ratio': 0.6,
            'metric': 'ml',
            'full': True
        }

        response = self.client.post(endpoint, data=payload, format='json')

        self.assertEqual(len(response.json()), 2)

        for json_response in response.json():
            self.assertTrue('active' in json_response)
            self.assertTrue('address' in json_response)
            self.assertTrue('created_at' in json_response)
            self.assertTrue('featured' in json_response)
            self.assertTrue('id' in json_response)
            self.assertTrue('description' in json_response)
            self.assertTrue('last_review' in json_response)
            self.assertTrue('logo' in json_response)
            self.assertTrue('name' in json_response)
            self.assertTrue('open_hours' in json_response)
            self.assertTrue('photo' in json_response)
            self.assertTrue('products' in json_response)
            self.assertTrue('sectors' in json_response)
            self.assertTrue('stamps' in json_response)
            self.assertTrue('stars_average' in json_response)
            self.assertTrue('updated_at' in json_response)
            self.assertTrue('latitude' in json_response)
            self.assertTrue('longitude' in json_response)

    def test_post_member_map_location_failure(self):

        endpoint = '/api/v1/members/map/'

        payload = {
            'location': {
                'lat': 150,  # Invalid latitude
                'long': -76.4987131
            },
            'ratio': 1,
            'full': True
        }

        response = self.client.post(endpoint, data=payload, format='json')

        expected = {
            "error": "Invalid location parameter",
            "message": "Invalid location specified"
        }

        self.assertEqual(response.json(), expected)

        # print(json.dumps(response.json(), indent=4, sort_keys=True))

    def test_post_member_map_missing_param_failure(self):
        endpoint = '/api/v1/members/map/'

        payload = {
            'location': {
                'lat': 150,  # Invalid latitude
                'long': -76.4987131
            },
            'full': True
        }

        response = self.client.post(endpoint, data=payload, format='json')

        expected = {
            "error": "missing parameter",
            "message": "missing location or ratio parameters"
        }

        self.assertEqual(response.json(), expected)

        # print(json.dumps(response.json(), indent=4, sort_keys=True))
