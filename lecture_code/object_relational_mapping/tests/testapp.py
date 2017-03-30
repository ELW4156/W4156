import os
import unittest
import tempfile
import json

import ormservice as service
from ormservice import app

# https://damyanon.net/flask-series-testing/
# http://flask.pocoo.org/docs/0.12/testing/
class ApplicationTests(unittest.TestCase):

    def assertSuccess(self, res):
        self.assertEqual(res.status, '200 OK')
        data = json.loads(res.data)
        self.assertTrue(data['success'])

    def assertFailure(self, res):
        self.assertEqual(res.status, '200 OK')
        data = json.loads(res.data)
        self.assertFalse(data['success'])

    def assertCount(self, res, count):
        self.assertSuccess(res)
        data = json.loads(res.data)
        self.assertEqual(data['count'], count)

    def setUp(self):
        self.db_fd, service.app.config['DATABASE'] = tempfile.mkstemp()
        service.app.config['TESTING'] = True
        self.app = app.test_client()
        with service.app.app_context():
            service.init_db()

    def test_connect(self):
        res = self.app.get('/')
        self.assertEqual(res.status, '200 OK')

    def test_create_user(self, name="brian"):
        res = self.app.get("/createuser/" + "awefwaef")
        self.assertSuccess(res)

        res = self.app.get("/createuser/" + "awefwaef")
        self.assertFailure(res)

        res = self.app.get("/listusers")


    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(service.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()