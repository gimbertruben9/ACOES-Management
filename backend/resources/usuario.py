from flask_restful import Resource, reqparse
from lock import lock
from models.persona import PersonaModel
from models.usuario import UsuarioModel


class Usuario(Resource):

    def get(self, id):
        user = UsuarioModel.get_by_id(id)
        return {'usuario': user.json()}, 200 if user else 404

    def post(self, id=None):
        parser = reqparse.RequestParser()

        parser.add_argument('nombreUsuario', type=str, required=True)
        parser.add_argument('correo', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        parser.add_argument('estado', type=str, required=True)
        parser.add_argument('idRolUsuario', type=int, required=True)

        parser.add_argument('idPersona', type=int, required=True)
        data = parser.parse_args()

        with lock.lock:
            user = UsuarioModel(nombreUsuario=data['nombreUsuario'], correo=data['correo'], password=data['password'],
                                estado=data['estado'], idRolUsuario=data['idRolUsuario'])
            user.add_person(PersonaModel.get_by_id(data['idPersona']))

            user.save_to_db()

            return {'usuario': user.json()}, 200 if user else 404

    def delete(self, id):
        with lock.lock:
            UsuarioModel.get_by_id(id).delete_from_db()

    def put(self, id):
        parser = reqparse.RequestParser()

        parser.add_argument('nombreUsuario', type=str, required=False)
        parser.add_argument('correo', type=str, required=False)
        parser.add_argument('password', type=str, required=False)
        parser.add_argument('estado', type=str, required=False)
        parser.add_argument('idRolUsuario', type=int, required=False)

        parser.add_argument('idPersona', type=int, required=False)
        data = parser.parse_args()

        with lock.lock:
            user = UsuarioModel.get_by_id(id)

            if user:
                if data['nombreUsuario']:
                    user.nombreUsuario = data['nombreUsuario']
                if data['correo']:
                    user.correo = data['correo']
                if data['password']:
                    user.password = data['password']
                if data['estado']:
                    user.estado = data['estado']
                if data['idRolUsuario']:
                    user.idRolUsuario = data['idRolUsuario']
                if data['correo']:
                    user.add_person(PersonaModel.get_by_id(data['idPersona']))

            try:
                user.save_to_db()
            except:
                return {"message": "An error occurred inserting the user."}, 500

            return {'usuario': user.json()}, 200 if user else 404
