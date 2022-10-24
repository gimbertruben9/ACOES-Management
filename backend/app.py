from flask import Flask
from flask_restful import Resource, Api, reqparse
from db import db
from flask_migrate import Migrate
from models.projects import ProjectsModel
from models.people import PeopleModel
from lock import lock
from flask_cors import CORS
from flask import render_template

app = Flask(
    __name__,
    static_folder='dist/static',
    template_folder='dist/templates'
)
api = Api(app)
CORS(app, resources={r'/*': {'origins': '*'}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

parser = reqparse.RequestParser()


@app.route('/')
def render_angular():
    return render_template("index.html")

# @app.route('/')
# def hello_world():
#    return "Hello World!"


class Project(Resource):

    def get(self, id):
        project = ProjectsModel.get_by_id(id)
        return {'project': project.json()}, 200 if project else 404

    def post(self, id=None):
        parser.add_argument('a', type=str)
        parser.add_argument('b', type=str)
        parser.add_argument('c', type=str)
        data = parser.parse_args()

        with lock.lock:
            project = ProjectsModel(a=data['a'], b=data['b'], c=data['c'])
            project.save_to_db()

            return {'project': project.json()}, 200 if project else 404

    def delete(self, id):
        with lock.lock:
            ProjectsModel.get_by_id(id).delete_from_db()

    def put(self, id):
        parser.add_argument('a', type=str)
        parser.add_argument('b', type=str)
        parser.add_argument('c', type=str)
        data = parser.parse_args()
        with lock.lock:
            project = ProjectsModel.get_by_id(id)

            if project:
                if data['a']:
                    project.name = data['a']
                if data['b']:
                    project.category = data['b']
                if data['c']:
                    project.sport = data['c']

            try:
                project.save_to_db()
            except:
                return {"message": "An error occurred inserting the project."}, 500

            return {'project': project.json()}, 200 if project else 404


class ProjectsList(Resource):

    def get(self):
        allProjects = ProjectsModel.get_all()
        projects = []

        for project in allProjects:
            projects.append(project.json())

        return {'projects': projects}, 200 if projects else 404


class Person(Resource):

    def get(self, id):
        people = PeopleModel.get_by_id(id)
        return {'people': people.json()}, 200 if people else 404

    def post(self, id=None):
        parser.add_argument('d', type=str)
        parser.add_argument('e', type=str)
        parser.add_argument('f', type=str)
        data = parser.parse_args()

        with lock.lock:
            person = PeopleModel(d=data['d'], e=data['e'], f=data['f'])
            person.save_to_db()

            return {'person': person.json()}, 200 if person else 404

    def delete(self, id):
        with lock.lock:
            PeopleModel.get_by_id(id).delete_from_db()

    def put(self, id):
        parser.add_argument('d', type=str)
        parser.add_argument('e', type=str)
        parser.add_argument('f', type=str)
        data = parser.parse_args()

        with lock.lock:
            person = PeopleModel.get_by_id(id)

            if person:
                if data['d']:
                    person.name = data['d']
                if data['e']:
                    person.category = data['e']
                if data['f']:
                    person.sport = data['f']

            try:
                person.save_to_db()
            except:
                return {"message": "An error occurred inserting the person."}, 500

            return {'person': person.json()}, 200 if person else 404


class PeopleList(Resource):

    def get(self):
        allPeople = PeopleModel.get_all()
        people = []

        for person in allPeople:
            people.append(person.json())

        return {'people': people}, 200 if people else 404


api.add_resource(Project, '/project/<int:id>', '/project')
api.add_resource(ProjectsList, '/projects')
api.add_resource(Person, '/person/<int:id>', '/person')
api.add_resource(PeopleList, '/people')

if __name__ == '__main__':
    app.run(port=5000, debug=True)