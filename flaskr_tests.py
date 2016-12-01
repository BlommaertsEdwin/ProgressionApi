import unittest

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
	    print "Set Up"

    def tearDown(self):
	    print "Tear Down"

    def test_empty_db(self):
	    print "First test"
	    rv = self.app.get('/')
	    assert b'No entries here so far' in rv.data

if __name__ == '__main__':
    unittest.main()
