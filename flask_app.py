from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TODOS = {
                'todo1': {'task': 'build an API'},
                'todo2': {'task': '?????'},
                'todo3': {'task': 'profit!'},
                }

PARTY = {}


def abort_if_todo_doesnt_exist(todo_id):
        if todo_id not in TODOS:
                abort(404, message="Todo {} doesn't exist".format(todo_id))

def abort_if_party_member_doesnt_exist(todo_id):
        if todo_id not in TODOS:
                abort(404, message="Todo {} doesn't exist".format(todo_id))

def check_if_list_is_empty():
        if not PARTY:
                abort(404, message="No party members have been added, please add them using the 'add_party_member' method")

parser = reqparse.RequestParser()
parser.add_argument('task')

class Party(Resource):
        def get(self):
                check_if_list_is_empty()
                return "Ok"
        def post(self):
                return "Stub for posting"

class PartyMember(Resource):
        def get(self, member_id):
                abort_if_party_member_doesnt_exist(member_id)
                return PARTY[member_id]
        def delete(self, member_id):
                abort_if_party_member_doesnt_exist(member_id)
                del PARTY[member_id]
                return '', 204
        def put(self, member_id):
                args = parser.parse_args()
                PartyMember = {'name': args['name'], 'level': args['level']}
                PARTY[member_id] = PartyMember
                return task, 201

# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
	def get(self, todo_id):
		abort_if_todo_doesnt_exist(todo_id)
		return TODOS[todo_id]

	def delete(self, todo_id):
		abort_if_todo_doesnt_exist(todo_id)
		del TODOS[todo_id]
		return '', 204

	def put(self, todo_id):
		args = parser.parse_args()
		task = {'task': args['task']}
		TODOS[todo_id] = task
		return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
        def get(self):
                return TODOS
        def post(self):
                args = parser.parse_args()
                todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
                todo_id = 'todo%i' % todo_id
                TODOS[todo_id] = {'task': args['task']}
                return TODOS[todo_id], 201

## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos', endpoint='todos')
api.add_resource(Todo, '/todos/<todo_id>', endpoint='todo')
api.add_resource(Party, '/party', endpoint='party')
api.add_resource(PartyMember, '/partymember', endpoint='partymember')

@app.route('/')
def home():
        return "Hello, world"
# etc etc, flask app code

if __name__ == '__main__':
        app.run(debug=True)
