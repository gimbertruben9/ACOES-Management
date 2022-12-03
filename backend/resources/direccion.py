from flask_restful import Resource, reqparse
from lock import lock
from models.direccion import DireccionModel


class Direccion(Resource):

    def get(self, id):
        direccion = DireccionModel.get_by_id(id)
        return {'direccion': direccion.json()}, 200 if direccion else 404

    def post(self, id=None):
        parser = reqparse.RequestParser()

        parser.add_argument('pais', type=str, required=True)
        parser.add_argument('ciudad', type=str, required=True)
        parser.add_argument('colonia', type=str, required=True)
        parser.add_argument('calle', type=str, required=True)
        parser.add_argument('descripcion', type=str, required=True)
        data = parser.parse_args()

        with lock.lock:
            direccion = DireccionModel(pais=data['pais'], ciudad=data['ciudad'], colonia=data['colonia'],
                                       calle=data['calle'], descripcion=data['descripcion'])

            direccion.save_to_db()

            return {'direccion': direccion.json()}, 200 if direccion else 404

    def delete(self, id):
        with lock.lock:
            DireccionModel.get_by_id(id).delete_from_db()

    def put(self, id):
        parser = reqparse.RequestParser()

        parser.add_argument('pais', type=str, required=False)
        parser.add_argument('ciudad', type=str, required=False)
        parser.add_argument('colonia', type=str, required=False)
        parser.add_argument('calle', type=str, required=False)
        parser.add_argument('descripcion', type=str, required=False)
        data = parser.parse_args()

        with lock.lock:
            direccion = DireccionModel.get_by_id(id)

            if direccion:
                if data['pais']:
                    direccion.pais = data['pais']
                if data['ciudad']:
                    direccion.ciudad = data['ciudad']
                if data['colonia']:
                    direccion.colonia = data['colonia']
                if data['calle']:
                    direccion.calle = data['calle']
                if data['descripcion']:
                    direccion.descripcion = data['descripcion']

            try:
                direccion.save_to_db()
            except:
                return {"message": "An error occurred inserting the address."}, 500

            return {'direccion': direccion.json()}, 200 if direccion else 404
