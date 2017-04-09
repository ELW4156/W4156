# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.user import User
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestUsersController(BaseTestCase):
    """ UsersController integration test stubs """

    def test_createuser_username_get(self):
        """
        Test case for createuser_username_get

        Create User
        """
        response = self.client.open('/v1/createuser/{username}'.format(username='username_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_listusers_get(self):
        """
        Test case for listusers_get

        List users
        """
        response = self.client.open('/v1/listusers',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
