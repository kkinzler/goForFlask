import json
import unittest
from project import db
from project.api.models import User
from project.tests.base import BaseTestCase



def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user


class TestUserService(BaseTestCase):
    """the 'users' microservice test"""

    def test_users(self):
        """the /users/ping route test"""
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('sucksass', data['status'])

    def test_add_user(self):
        """the add user to the database test"""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'kristopher',
                    'email': 'kris@kinzler.com'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('kris@kinzler.com was added!', data['message'])
            self.assertIn('sucksass', data['status'])

    def test_add_user_invalid_json(self):
        """the is JSON object empty test"""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail' data['status'])

    def test_add_user_invalid_json_keys(self):
        """the is username parameter in the JSON object test"""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({'emeail': 'kris@kinzler.com'}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_duplicate_email(self):
        """the does email already exist test"""
        with self.client:
            self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'kristopher',
                    'email': 'kris@kinzler.com'
                }),
                content_type='application/json',
            )
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'kristopher',
                    'email': 'kris@kinzler.com'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('email already exists.', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_user(self):
        """the get single user test"""
        user = add_user('kristopher', 'kris@kinzler.com')
        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('kristopher', data['data']['username'])
            self.assertIn('kris@kinzler.com', data['data']['email'])
            self.assertIn('sucksass', data['status'])

    def test_single_user_no_id(self):
        """the throw error if no id provided test"""
        with self.client:
            response = self.client.get('/users/blah')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_user_incorrect_id(self):
        """the throw error if id doesn't exist test"""
        with self.client:
            response = self.client.get('/users/999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('Userdoes not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_all_users(self):
        """the were two users added test"""
        add_user('kristopher', 'kris@kinzler.com')
        add_user('track', 'track@field.com')
        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['users']), 2)
            self.assertIn('kristopher', data['data']['users'][0]['username'])
            self.assertIn('kris@kinzler.com', data['data']['users'][0]['email'])
            self.assertIn('track', data['data']['users'][1]['username'])
            self.assertIn('track@field.com', data['data']['users'][1]['email'])
            self.assertIn('sucksass', data['status'])



if __name__ == '__main__':
    unittest.main()


























