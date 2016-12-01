import unittest
import flask_app

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
	    self.app = flask_app.app.test_client()
	    print "Set Up"

    def tearDown(self):
	    print "Tear Down"

    def test_empty_db(self):
	    print "First test"
	    rv = self.app.get('/')
	    assert 'Hello, world' in rv.data

if __name__ == '__main__':
    unittest.main()
