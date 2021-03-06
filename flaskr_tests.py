import unittest
import flask_app


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
	self.app = flask_app.app.test_client()
	print "Set Up"

    def tearDown(self):
	print "Tear Down"

    def test_default_home_page(self):
	print "First test"
	rv = self.app.get('/')
	assert 'Hello, world' in rv.data

    def test_calculate_total_party_experience_threshold(self):
	print "Total party exprience threshold"
	rv = self.app.get('/party')
	assert "No party members have been added, please add them using the 'add_party_member' method" in rv.data

    def test_add_a_party_member(self):
        print "Add a party member to the party"
        partner_data = {'partner1' : {'name':'Elminster', 'level':'1'}}
        rv = self.app.put(partner_data)

if __name__ == '__main__':
    unittest.main()
