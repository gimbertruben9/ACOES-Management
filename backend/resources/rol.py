from flask_restful import Resource, reqparse
from lock import lock
from models.rol import RolModel


class Rol(Resource):

    def get(self, id):
        rol = RolModel.get_by_id(id)
        return {'rol': rol.json()}, 200 if rol else 404

    def post(self, id=None):
        parser = reqparse.RequestParser()

        parser.add_argument('nombreRol', type=str, required=True)
        parser.add_argument('tipoRol', type=str, required=True)
        data = parser.parse_args()

        with lock.lock:
            rol = RolModel(nombreRol=data['nombreRol'], tipoRol=data['tipoRol'])

            rol.save_to_db()

            return {'rol': rol.json()}, 200 if rol else 404

    def delete(self, id):
        with lock.lock:
            RolModel.get_by_id(id).delete_from_db()

    def put(self, id):
        parser = reqparse.RequestParser()

        parser.add_argument('nombreRol', type=str, required=False)
        parser.add_argument('tipoRol', type=str, required=False)
        data = parser.parse_args()

        with lock.lock:
            rol = RolModel.get_by_id(id)

            if rol:
                if data['nombreRol']:
                    rol.nombreRol = data['nombreRol']
                if data['rtn']:
                    rol.tipoRol = data['tipoRol']

            try:
                rol.save_to_db()
            except:
                return {"message": "An error occurred inserting the role."}, 500

            return {'rol': rol.json()}, 200 if rol else 404