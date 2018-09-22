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

        expected = {
            "active": True,
            "address": (
                "17 Hamilton St,\r\n"
                "Kingston, Ontario\r\n"
                "Canada\r\nK7K 1P1"
            ),
            "created_at": "2018-09-21T21:16:09.995000Z",
            "description": (
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                "Praesent placerat condimentum sem. Vivamus egestas "
                "imperdiet condimentum. Sed viverra erat id gravida "
                "aliquet. Suspendisse laoreet suscipit "
                "sem. Ut aliquet felis a lorem auctor consectetur. "
                "Mauris non erat euismod, volutpat diam ac, viverra ante. "
                "Proin at quam cursus, feugiat felis eu, egestas mi. "
                "Cras aliquam, neque quis gravida efficitur, nibh enim "
                "condimentum lorem, placerat tincidunt augue ligula ac erat. "
                "Sed diam diam, volutpat vitae sapien a, pellentesque "
                "efficitur nulla. Nulla vehicula neque in vulputate "
                "ultricies. In id eleifend ipsum. Nunc a mollis libero."
            ),
            "featured": False,
            "id": 1,
            "last_review": {
                "approved": True,
                "comment": "This place is so so!",
                "created_at": "2018-09-21T22:08:21.790000Z",
                "reviewer": {
                    "avatar": ("http://www.gravatar.com/avatar/"
                               "8cb5fa316e5e32877c4e8055f6f2afa4?d=404"),
                    "created_at": "2018-09-21T22:07:07.287000Z",
                    "email": "joab.mendes.r2d2@gmail.com",
                    "id": 1,
                    "name": "Joabe Mendes",
                    "updated_at": "2018-09-21T22:07:07.287000Z"
                },
                "stars": 2,
                "updated_at": "2018-09-21T22:08:21.790000Z"
            },
            "latitude": "44.2373589",
            "logo": "/media/member_logos/logo_uxEAY4R.png",
            "longitude": "-76.4946626",
            "name": "Member Example",
            "open_hours": (
                "Sunday: Closed\r\n"
                "Monday: 8am - 4pm\r\n"
                "Tuesday: 8am - 4pm\r\n"
                "Wednesday: 8am - 4pm\r\n"
                "Thursday: 8am - 4pm\r\n"
                "Friday: 8am - 4pm\r\n"
                "Saturday: 8am - 4pm"
            ),
            "photo": "/media/member_logos/body-background-05_26wH0NN.jpg",
            "products": (
                "Product 1,\r\n"
                "Product 2,\r\n"
                "Product 3,\r\n"
                "Product 4,\r\n"
                "Product 5,"
            ),
            "sectors": [
                {
                    "created_at": "2018-09-21T20:55:47.357000Z",
                    "icon": "",
                    "id": 1,
                    "title": "Restaurant",
                    "updated_at": "2018-09-21T20:55:47.357000Z"
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
                }
            ],
            "stars_average": 4,
            "updated_at": "2018-09-21T21:16:09.995000Z"
        }

        self.assertEqual(json_response, expected)

        # print(json.dumps(response.json(), indent=4, sort_keys=True))

    def test_get_featured_members(self):
        endpoint = '/api/v1/members/featured'

        response = self.client.get(endpoint)

        expected = [
            {
                "active": True,
                "address": (
                    "17 Hamilton St,\r\n"
                    "Kingston, Ontario\r\n"
                    "Canada\r\nK7K 1P1"
                ),
                "created_at": "2018-09-21T21:16:09.995000Z",
                "description": (
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                    "Praesent placerat condimentum sem. Vivamus egestas "
                    "imperdiet condimentum. Sed viverra erat id gravida "
                    "aliquet. Suspendisse laoreet suscipit "
                    "sem. Ut aliquet felis a lorem auctor consectetur. "
                    "Mauris non erat euismod, volutpat diam ac, viverra ante. "
                    "Proin at quam cursus, feugiat felis eu, egestas mi. "
                    "Cras aliquam, neque quis gravida efficitur, nibh enim "
                    "condimentum lorem, placerat tincidunt augue "
                    "ligula ac erat. Sed diam diam, volutpat vitae "
                    "sapien a, pellentesque efficitur nulla. Nulla "
                    "vehicula neque in vulputate ultricies. In id "
                    "eleifend ipsum. Nunc a mollis libero."
                ),
                "featured": True,
                "id": 3,
                "last_review": {},
                "latitude": "45.3373589",
                "logo": "/media/member_logos/logo_uxEAY4R.png",
                "longitude": "-76.5046626",
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
                "photo": "/media/member_logos/body-background-05_26wH0NN.jpg",
                "products": (
                    "Product 1,\r\n"
                    "Product 2,\r\n"
                    "Product 3,\r\n"
                    "Product 4,\r\n"
                    "Product 5,"
                ),
                "sectors": [
                    {
                        "created_at": "2018-09-21T20:56:01.363000Z",
                        "icon": "",
                        "id": 3,
                        "title": "Caf\u00e9",
                        "updated_at": "2018-09-21T20:56:01.363000Z"
                    }
                ],
                "stamps": [
                    {
                        "created_at": "2018-09-21T21:02:31.123000Z",
                        "description": (
                            "This member doesn't use "
                            "plastic in any of it's processes."
                        ),
                        "id": 1,
                        "image": "/media/stamp_files/plastic_free.png",
                        "title": "Plastic Free",
                        "updated_at": "2018-09-21T21:02:31.123000Z"
                    }
                ],
                "stars_average": 0,
                "updated_at": "2018-09-21T21:16:09.995000Z"
            }
        ]

        self.assertEqual(response.json(), expected)

        # print(json.dumps(response.json(), indent=4, sort_keys=True))

    def test_get_member_map(self):
        endpoint = '/api/v1/members/map/'

        response = self.client.get(endpoint)

        expected = [
            {
                "latitude": "44.2373589",
                "logo": "/media/member_logos/logo_uxEAY4R.png",
                "longitude": "-76.4946626",
                "name": "Member Example",
                "photo": "/media/member_logos/body-background-05_26wH0NN.jpg",
                "stars_average": 4
            },
            {
                "latitude": "44.3373589",
                "logo": "/media/member_logos/logo_uxEAY4R.png",
                "longitude": "-76.5046626",
                "name": "Member Example 2",
                "photo": "/media/member_logos/body-background-05_26wH0NN.jpg",
                "stars_average": 0
            },
            {
                "latitude": "45.3373589",
                "logo": "/media/member_logos/logo_uxEAY4R.png",
                "longitude": "-76.5046626",
                "name": "Member Example 3",
                "photo": "/media/member_logos/body-background-05_26wH0NN.jpg",
                "stars_average": 0
            }
        ]

        self.assertEqual(response.json(), expected)

        # print(json.dumps(response.json(), indent=4, sort_keys=True))
