from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

PARTY = {}

THRESHOLD_TABLE={
        '1': {'easy': 25, 'medium': 50, 'hard': 75, 'deadly': 100},
        '2': {'easy': 50, 'medium': 100, 'hard': 150, 'deadly': 200},
        '3': {'easy': 75, 'medium': 150, 'hard': 225, 'deadly': 400},
        '4': {'easy': 125, 'medium': 250, 'hard': 375, 'deadly': 500},
        '5': {'easy': 250, 'medium': 500, 'hard': 750, 'deadly': 1100},
        '6': {'easy': 300, 'medium': 600, 'hard': 900, 'deadly': 1400},
        '7': {'easy': 350, 'medium': 750, 'hard': 1100, 'deadly': 1700},
        '8': {'easy': 450, 'medium': 900, 'hard': 1400, 'deadly': 2100},
        '9': {'easy': 550, 'medium': 1100, 'hard': 1600, 'deadly': 2400},
        '10': {'easy': 600, 'medium': 1200, 'hard': 1900, 'deadly': 2800},
        '11': {'easy': 800, 'medium': 1600, 'hard': 2400, 'deadly': 3600},
        '12': {'easy': 1000, 'medium': 2000, 'hard': 3000, 'deadly': 4500},
        '13': {'easy': 1100, 'medium': 2200, 'hard': 3400, 'deadly': 5100},
        '14': {'easy': 1250, 'medium': 2500, 'hard': 3800, 'deadly': 5700},
        '15': {'easy': 1400, 'medium': 2800, 'hard': 4300, 'deadly': 6400},
        '16': {'easy': 1600, 'medium': 3200, 'hard': 4800, 'deadly': 7200},
        '17': {'easy': 2000, 'medium': 3900, 'hard': 5900, 'deadly': 8800},
        '18': {'easy': 2100, 'medium': 4200, 'hard': 6300, 'deadly': 9500},
        '19': {'easy': 2400, 'medium': 4900, 'hard': 7300, 'deadly': 10900},
        '20': {'easy': 2800, 'medium': 5700, 'hard': 8500, 'deadly': 12700}
        }

def abort_if_party_member_doesnt_exist(member_id):
        if member_id not in PARTY:
                abort(404, message="Todo {} doesn't exist!".format(member_id))

def abort_if_difficulty_id_doesnt_exist(difficulty_id):
        if difficulty_id not in ['easy', 'medium', 'hard', 'deadly']:
                abort(404, message="Difficulty {} doesn't exist!".format(difficulty_id))

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help="Name cannot be blank!")
parser.add_argument('level', required=True, help="Character level cannot be blank!")

# Member
# Xhows a single Member and lets you delete a Member.
class Member(Resource):
	def get(self, member_id):
		abort_if_party_member_doesnt_exist(member_id)
		return PARTY[member_id]

	def delete(self, member_id):
		abort_if_party_member_doesnt_exist(member_id)
		del PARTY[member_id]
		return '', 204

	def put(self, member_id):
		args = parser.parse_args()
		member = {'name': args['name'], 'level': args['level']}
		PARTY[member_id] = member
		return member, 201
	


# TodoList
# shows a list of all members, and lets you POST to add new tasks
class Party(Resource):
        def get(self):
                return PARTY
        def post(self):
                args = parser.parse_args()
                if PARTY.keys():
                        member_id = int(max(PARTY.keys()).lstrip('member')) + 1
                        member_id = 'member%i' % member_id
                else:
                        member_id = 'member1'
                PARTY[member_id] = {'name': args['name'], 'level': args['level']}
                return PARTY[member_id], 201

class Partytreshold(Resource):
        def get(self, difficulty_id):
                abort_if_difficulty_id_doesnt_exist(difficulty_id)
                print(difficulty_id)
                party_threshold = 0
                for member in PARTY.keys():
                        party_threshold = party_threshold + THRESHOLD_TABLE[PARTY[member]['level']][difficulty_id]
                return party_threshold

# Actually setup the Api resource routing here
api.add_resource(Party, '/party', endpoint='party')
api.add_resource(Member, '/party/<member_id>', endpoint='member')
api.add_resource(Partytreshold, '/partythreshold/<string:difficulty_id>', endpoint='partytreshold')


@app.route('/')
def home():
        return "Hello, world"
# etc etc, flask app code

if __name__ == '__main__':
        app.run(debug=True)
