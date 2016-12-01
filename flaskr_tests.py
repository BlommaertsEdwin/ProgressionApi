import os
import flaskr
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
	    print "Set Up"

    def tearDown(self):
	    print "Tear Down"

    def test_empty_db(self):
	    print "First test"
	    rv = self.app.get('/')
	    assert b'No entries here so far' in rv.data
