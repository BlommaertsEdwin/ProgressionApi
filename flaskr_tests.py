import os
import flaskr
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
	    echo "Set Up"

    def tearDown(self):
	    echo "Tear Down"

    def test_empty_db(self):
	    eacho "First test"
	    rv = self.app.get('/')
	    assert b'No entries here so far' in rv.data
