from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

PARTY = {}


def abort_if_party_member_doesnt_exist(member_id):
        if member_id not in PARTY:
                abort(404, message="Todo {} doesn't exist".format(member_id))


parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
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
# shows a list of all todos, and lets you POST to add new tasks
class Party(Resource):
        def get(self):
                return PARTY
        def post(self):
                args = parser.parse_args()
                return args
                #if PARTY.keys():
                #        member_id = int(max(PARTY.keys()).lstrip('member')) + 1
                #        member_id = 'member%i' % member_id
                #else:
                #        member_id = 'member1'
                #PARTY[member_id] = {'name': args['name'], 'level': args['level']}
                #return PARTY[member_id], 201

## Actually setup the Api resource routing here
##
api.add_resource(Party, '/party', endpoint='party')
api.add_resource(Member, '/party/<member_id>', endpoint='member')


@app.route('/')
def home():
        return "Hello, world"
# etc etc, flask app code

if __name__ == '__main__':
        app.run(debug=True)
