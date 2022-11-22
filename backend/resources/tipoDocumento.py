from flask_restful import Resource, reqparse
from lock import lock

from models.tipoDocumento import TipoDocumentoModel


class TipoDocumento(Resource):

    def get(self, id):
        tipoDoc = TipoDocumentoModel.get_by_id(id)
        return {'tipoDocumento': tipoDoc.json()}, 200 if tipoDoc else 404

    def post(self, id=None):
        parser = reqparse.RequestParser()

        parser.add_argument('descTipoDocumento', type=str, required=True)
        data = parser.parse_args()

        with lock.lock:
            tipoDoc = TipoDocumentoModel(descTipoDocumento=data['descTipoDocumento'])

            tipoDoc.save_to_db()

            return {'tipoDocumento': tipoDoc.json()}, 200 if tipoDoc else 404

    def delete(self, id):
        with lock.lock:
            TipoDocumentoModel.get_by_id(id).delete_from_db()

    def put(self, id):
        parser = reqparse.RequestParser()

        parser.add_argument('descTipoDocumento', type=str, required=True)
        data = parser.parse_args()

        with lock.lock:
            tipoDoc = TipoDocumentoModel.get_by_id(id)

            if tipoDoc:
                if data['descTipoDocumento']:
                    tipoDoc.descTipoDocumento = data['descTipoDocumento']

            try:
                tipoDoc.save_to_db()
            except:
                return {"message": "An error occurred inserting the document type."}, 500

            return {'tipoDocumento': tipoDoc.json()}, 200 if tipoDoc else 404