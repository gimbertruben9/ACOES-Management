from flask_restful import Resource, reqparse
from lock import lock

from models.organizacion import OrganizacionModel
from models.proyecto import ProyectoModel


class Proyecto(Resource):

    def get(self, id):
        project = ProyectoModel.get_by_id(id)
        return {'proyecto': project.json()}, 200 if project else 404

    def post(self, id=None):
        parser = reqparse.RequestParser()

        parser.add_argument('nombre', type=str, required=True)

        parser.add_argument('idOrganizacion', type=int, required=True)
        parser.add_argument('idCoordinador', type=int, required=False)
        data = parser.parse_args()

        with lock.lock:
            project = ProyectoModel(nombre=data['nombre'])
            project.add_org(OrganizacionModel.get_by_id(data['idOrganizacion']))

            if data['idCoordinador']:
                project.add_idCoordinador(data['idCoordinador'])

            project.save_to_db()

            return {'proyecto': project.json()}, 200 if project else 404

    def delete(self, id):
        with lock.lock:
            ProyectoModel.get_by_id(id).delete_from_db()

    def put(self, id):
        parser = reqparse.RequestParser()

        parser.add_argument('nombre', type=str, required=True)

        parser.add_argument('idOrganizacion', type=int, required=True)
        parser.add_argument('idCoordinador', type=int, required=False)
        data = parser.parse_args()

        with lock.lock:
            project = ProyectoModel.get_by_id(id)

            if project:
                if data['nombre']:
                    project.nombre = data['nombre']
                if data['idCoordinador']:
                    project.idCoordinador = data['idCoordinador']
                if data['idOrganizacion']:
                    project.add_org(OrganizacionModel.get_by_id(data['idOrganizacion']))

            try:
                project.save_to_db()
            except:
                return {"message": "An error occurred inserting the project."}, 500

            return {'proyecto': project.json()}, 200 if project else 404


class ProyectoList(Resource):

    def get(self):
        allProjects = ProyectoModel.get_all()
        projects = []

        for project in allProjects:
            projects.append(project.json())

        return {'proyectos': projects}, 200 if projects else 404


class ProyectoDesarchivadoList(Resource):

    def get(self):
        allProjects = ProyectoModel.get_all_unarchived()
        projects = []

        for project in allProjects:
            projects.append(project.json())

        return {'proyectos': projects}, 200 if projects else 404
