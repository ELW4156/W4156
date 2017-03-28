import os
import unittest
import tempfile
import userservice
from userservice import app, init_db


# https://damyanon.net/flask-series-testing/
# Note - flask has some
class ApplicationTests(unittest.TestCase):

    def setUp(self):
        self.db_fd, userservice.app.config['DATABASE'] = tempfile.mkstemp()
        userservice.app.config['TESTING'] = True
        self.app = app.test_client()
        with userservice.app.app_context():
            userservice.init_db()

    def test_connect(self):
        res = self.app.get('/')
        print(res)

    def test_create_user(self):
        res = self.app.get("/createuser/brian")

    def test_create_duplicate_user(self):
        res = self.app.get("/createuser/brian")
        print(res.data)
        res = self.app.get("/createuser/brian")
        print(res.data)

    def test_list_users(self):
        pass

    def test_total_users(self):
        #res = self.app.get("/totalusers")
        pass

    def test_for_this_bug(self):
        pass

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(userservice.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()