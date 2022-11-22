from flask_restful import Resource, reqparse
from lock import lock
from models.organizacion import OrganizacionModel


class Organizacion(Resource):

    def get(self, id):
        org = OrganizacionModel.get_by_id(id)
        return {'organizacion': org.json()}, 200 if org else 404

    def post(self, id=None):
        parser = reqparse.RequestParser()

        parser.add_argument('nombre', type=str, required=True)
        parser.add_argument('rtn', type=str, required=True)
        data = parser.parse_args()

        with lock.lock:
            org = OrganizacionModel(nombre=data['nombre'], rtn=data['rtn'])

            org.save_to_db()

            return {'organizacion': org.json()}, 200 if org else 404

    def delete(self, id):
        with lock.lock:
            OrganizacionModel.get_by_id(id).delete_from_db()

    def put(self, id):
        parser = reqparse.RequestParser()

        parser.add_argument('nombre', type=str, required=True)
        parser.add_argument('rtn', type=str, required=True)
        data = parser.parse_args()

        with lock.lock:
            org = OrganizacionModel.get_by_id(id)

            if org:
                if data['nombre']:
                    org.nombre = data['nombre']
                if data['rtn']:
                    org.rtn = data['rtn']

            try:
                org.save_to_db()
            except:
                return {"message": "An error occurred inserting the organization."}, 500

            return {'organizacion': org.json()}, 200 if org else 404