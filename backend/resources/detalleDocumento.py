from datetime import datetime
from flask_restful import Resource, reqparse
from lock import lock

from models.detalleDocumento import DetalleDocumentoModel
from models.persona import PersonaModel
from models.setupDocumentoPersona import SetupDocumentoPersonaModel


class DetalleDocumento(Resource):

    def get(self):
        parser = reqparse.RequestParser()

        parser.add_argument('fechaHoraCarga', type=str, required=False)
        parser.add_argument('idSetupDocumentoPersona', type=int, required=True)
        parser.add_argument('idEmpleado', type=int, required=True)

        data = parser.parse_args()

        detalle = DetalleDocumentoModel.get_by_id(datetime.strptime(data['fechaHoraCarga'], "%Y-%m-%d %H:%M:%S"),
                                                  data['idSetupDocumentoPersona'], data['idEmpleado'])

        return {'detalleDocumento': detalle.json()}, 200 if detalle else 404

    def post(self, id=None):
        parser = reqparse.RequestParser()

        parser.add_argument('fechaHoraCarga', type=str, required=True)
        parser.add_argument('fechaExpedicion', type=str, required=True)
        parser.add_argument('comentario', type=str, required=True)
        parser.add_argument('pathDestinoAdjunto', type=str, required=True)
        parser.add_argument('nombreAdjuntoOriginal', type=str, required=True)

        parser.add_argument('idSetupDocumentoPersona', type=int, required=True)
        parser.add_argument('idEmpleado', type=int, required=True)
        data = parser.parse_args()

        with lock.lock:

            detalle = DetalleDocumentoModel(fechaHoraCarga=datetime.strptime(data['fechaHoraCarga'], "%Y-%m-%d %H:%M:%S"), fechaExpedicion=datetime.strptime(data['fechaExpedicion'], "%Y-%m-%d"),
                                            comentario=data['comentario'], pathDestinoAdjunto=data['pathDestinoAdjunto'],
                                            nombreAdjuntoOriginal=data['nombreAdjuntoOriginal'])
            detalle.add_empleado(PersonaModel.get_by_id(data['idEmpleado']))
            detalle.add_setupDocPersona(SetupDocumentoPersonaModel.get_by_id(data['idSetupDocumentoPersona']))

            detalle.save_to_db()

            return {'detalleDocumento': detalle.json()}, 200 if detalle else 404

    def delete(self):
        parser = reqparse.RequestParser()

        parser.add_argument('fechaHoraCarga', type=str, required=False)
        parser.add_argument('idSetupDocumentoPersona', type=int, required=True)
        parser.add_argument('idEmpleado', type=int, required=True)

        data = parser.parse_args()
        with lock.lock:
            DetalleDocumentoModel.get_by_id(datetime.strptime(data['fechaHoraCarga'], "%Y-%m-%d %H:%M:%S"), data['idSetupDocumentoPersona'],
                                                  data['idEmpleado']).delete_from_db()

    def put(self, id):
        parser = reqparse.RequestParser()

        parser.add_argument('fechaHoraCarga', type=str, required=False)
        parser.add_argument('fechaExpedicion', type=str, required=False)
        parser.add_argument('comentario', type=str, required=False)
        parser.add_argument('pathDestinoAdjunto', type=str, required=False)
        parser.add_argument('nombreAdjuntoOriginal', type=str, required=False)

        parser.add_argument('idSetupDocumentoPersona', type=int, required=False)
        parser.add_argument('idEmpleado', type=int, required=False)
        data = parser.parse_args()

        with lock.lock:
            detalle = DetalleDocumentoModel.get_by_id(datetime.strptime(data['fechaHoraCarga'], "%Y-%m-%d %H:%M:%S"), data['idSetupDocumentoPersona'],
                                                  data['idEmpleado'])

            if detalle:
                if data['fechaHoraCarga']:
                    detalle.fechaHoraCarga = datetime.strptime(data['fechaHoraCarga'], "%Y-%m-%d %H:%M:%S")
                if data['fechaExpedicion']:
                    detalle.fechaExpedicion = datetime.strptime(data['fechaExpedicion'], "%Y-%m-%d")
                if data['comentario']:
                    detalle.comentario = data['comentario']
                if data['pathDestinoAdjunto']:
                    detalle.pathDestinoAdjunto = data['pathDestinoAdjunto']
                if data['idSetupDocumentoPersona']:
                    detalle.add_setupDocPersona(SetupDocumentoPersonaModel.get_by_id(data['idSetupDocumentoPersona']))
                if data['idEmpleado']:
                    detalle.add_empleado(PersonaModel.get_by_id(data['idEmpleado']))

            try:
                detalle.save_to_db()
            except:
                return {"message": "An error occurred inserting the document detail."}, 500

            return {'detalleDocumento': detalle.json()}, 200 if detalle else 404