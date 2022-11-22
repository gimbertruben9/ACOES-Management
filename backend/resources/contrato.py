from flask_restful import Resource, reqparse
from lock import lock
from models.contrato import ContratoModel


class Contrato(Resource):

    def get(self, id):
        contrato = ContratoModel.get_by_id(id)
        return {'contrato': contrato.json()}, 200 if contrato else 404

    def post(self, id=None):
        parser = reqparse.RequestParser()

        parser.add_argument('tipoContrato', type=str, required=True)
        data = parser.parse_args()

        with lock.lock:

            contrato = ContratoModel(tipoContrato=data['tipoContrato'])

            contrato.save_to_db()

            return {'contrato': contrato.json()}, 200 if contrato else 404

    def delete(self, id):
        with lock.lock:
            ContratoModel.get_by_id(id).delete_from_db()

    def put(self, id):
        parser = reqparse.RequestParser()

        parser.add_argument('tipoContrato', type=str, required=True)
        data = parser.parse_args()

        with lock.lock:
            contrato = ContratoModel.get_by_id(id)

            if contrato:
                if data['tipoContrato']:
                    contrato.contrato = data['contrato']
            try:
                contrato.save_to_db()
            except:
                return {"message": "An error occurred inserting the contract."}, 500

            return {'contrato': contrato.json()}, 200 if contrato else 404
