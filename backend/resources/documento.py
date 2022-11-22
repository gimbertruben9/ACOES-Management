from flask_restful import Resource, reqparse
from lock import lock

from models.documento import DocumentoModel


class Documento(Resource):

    def get(self, id):
        doc = DocumentoModel.get_by_id(id)
        return {'documento': doc.json()}, 200 if doc else 404

    def post(self, id=None):
        parser = reqparse.RequestParser()

        parser.add_argument('idTipoDocumento', type=str, required=True)
        parser.add_argument('descripcionDocumento', type=str, required=True)
        data = parser.parse_args()

        with lock.lock:
            doc = DocumentoModel(idTipoDocumento=data['idTipoDocumento'], descripcionDocumento=data['descripcionDocumento'])

            doc.save_to_db()

            return {'documento': doc.json()}, 200 if doc else 404

    def delete(self, id):
        with lock.lock:
            DocumentoModel.get_by_id(id).delete_from_db()

    def put(self, id):
        parser = reqparse.RequestParser()

        parser.add_argument('idTipoDocumento', type=str, required=True)
        parser.add_argument('descripcionDocumento', type=str, required=True)
        data = parser.parse_args()

        with lock.lock:
            doc = DocumentoModel.get_by_id(id)

            if doc:
                if data['idTipoDocumento']:
                    doc.idTipoDocumento = data['idTipoDocumento']
                if data['descripcionDocumento']:
                    doc.descripcionDocumento = data['descripcionDocumento']

            try:
                doc.save_to_db()
            except:
                return {"message": "An error occurred inserting the document."}, 500

            return {'documento': doc.json()}, 200 if doc else 404