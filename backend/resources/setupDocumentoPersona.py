from flask_restful import Resource, reqparse
from lock import lock
from models.documento import DocumentoModel

from models.setupDocumentoPersona import SetupDocumentoPersonaModel
from models.tipoDocumento import TipoDocumentoModel
from models.tipoVinculacion import TipoVinculacionModel


class SetupDocumentoPersona(Resource):

    def get(self, id):
        setupDoc = SetupDocumentoPersonaModel.get_by_id(id)
        return {'setupDocumentoPersona': setupDoc.json()}, 200 if setupDoc else 404

    def post(self, id=None):
        parser = reqparse.RequestParser()

        parser.add_argument('diasExpira', type=int, required=True)

        parser.add_argument('idDocumento', type=int, required=True)
        parser.add_argument('idTipoDocumento', type=int, required=True)
        parser.add_argument('idTipoVinculacion', type=int, required=True)

        data = parser.parse_args()

        with lock.lock:

            setupDoc = SetupDocumentoPersonaModel(diasExpira=data['diasExpira'])

            setupDoc.add_documento(DocumentoModel.get_by_id(data['idDocumento']))
            setupDoc.add_tipoDocumento(TipoDocumentoModel.get_by_id(data['idTipoDocumento']))
            setupDoc.add_tipoVinculacion(TipoVinculacionModel.get_by_id(data['idTipoVinculacion']))

            setupDoc.save_to_db()

            return {'setupDocumentoPersona': setupDoc.json()}, 200 if setupDoc else 404

    def delete(self, id):
        with lock.lock:
            SetupDocumentoPersonaModel.get_by_id(id).delete_from_db()

    def put(self, id):
        parser = reqparse.RequestParser()

        parser.add_argument('diasExpira', type=int, required=False)

        parser.add_argument('idDocumento', type=int, required=False)
        parser.add_argument('idTipoDocumento', type=int, required=False)
        parser.add_argument('idTipoVinculacion', type=int, required=False)

        data = parser.parse_args()

        with lock.lock:
            setupDoc = SetupDocumentoPersonaModel.get_by_id(id)

            if setupDoc:
                if data['diasExpira']:
                    setupDoc.diasExpira = data['diasExpira']
                if data['idDocumento']:
                    setupDoc.add_documento(DocumentoModel.get_by_id(data['idDocumento']))
                if data['idTipoDocumento']:
                    setupDoc.add_tipoDocumento(TipoDocumentoModel.get_by_id(data['idTipoDocumento']))
                if data['idTipoVinculacion']:
                    setupDoc.add_tipoVinculacion(TipoVinculacionModel.get_by_id(data['idTipoVinculacion']))

            try:
                setupDoc.save_to_db()
            except:
                return {"message": "An error occurred inserting the setupDocumentoPersona."}, 500

            return {'setupDocumentoPersona': setupDoc.json()}, 200 if setupDoc else 404


class SetupDocumentoPersonaList(Resource):

    def get(self, idTipoVinculacion=None):

        if idTipoVinculacion is None:
            allSetups = SetupDocumentoPersonaModel.get_all()
            setups = []

            for setup in allSetups:
                setups.append(setup.json())

            return {'setupsDocumentoPersona': setups}, 200 if setups else 404

        else:
            allSetups = SetupDocumentoPersonaModel.get_all_by_vinc(idTipoVinculacion)
            setups = []

            for setup in allSetups:
                setups.append(setup.json())

            return {'setupsDocumentoPersona': setups}, 200 if setups else 404

