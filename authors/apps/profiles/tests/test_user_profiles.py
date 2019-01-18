import json

from rest_framework import status

from authors.apps.profiles.tests.base import BaseTestMethods
from authors.apps.authentication.models import User


class TestUserProfile(BaseTestMethods):
    """
    Test cases for user retrieving an existing profile
    """

    def test_retrieve_an_existing_profile(self):
        response = self.retrieve_user_profile()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content)['profile']['username'],
            "testuser"
        )
        self.assertEqual(
            json.loads(response.content)['profile']['bio'],
            ""
        )

    def test_a_non_existent_profile(self):
        response = self.client.get('/api/v1/profiles/testusers1')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            json.loads(response.content)['errors']['detail'],
            "The profile you requested does not exist."
        )

    def test_update_profile(self):
        user = User.objects.create_user(**self.user.get('user'))
        data = {
            "user": {
                "bio": "I love music",
                "image": "http://images.com/profile.jpg"
            }
        }

        response = self.client.put(
            '/api/v1/users/{}/'.format(user.id), data=data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)[
                         'user']['bio'], "I love music")

    def test_update_a_non_owner_profile(self):
        owner = User.objects.create_user(**self.user.get('user'))
        data = {
            "user": {
                "bio": "I love music",
                "image": "http://images.com/profile.jpg"
            }
        }
        user_data = {
            'user': {
                'username': 'frank',
                'email': 'frank@andela.com',
                'password': 'TestUser12#'
            }
        }
        non_owner = User.objects.create_user(**user_data['user'])
        response = self.client.put(
            '/api/v1/users/{}/'.format(non_owner.id), data=data, format='json',
            HTTP_AUTHORIZATION=f'Bearer {owner.token}')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(
            json.loads(response.content)['user']['detail'],
            "You are not allowed perform this action"
        )
