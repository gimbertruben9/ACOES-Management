from flask_restful import Resource, reqparse
from lock import lock
from models.tipoVinculacion import TipoVinculacionModel


class TipoVinculacion(Resource):

    def get(self, id):
        tipoVinculacion = TipoVinculacionModel.get_by_id(id)
        return {'tipoVinculacion': tipoVinculacion.json()}, 200 if tipoVinculacion else 404

    def post(self, id=None):
        parser = reqparse.RequestParser()

        parser.add_argument('idTipo', type=str, required=True)
        parser.add_argument('descTipoVinculacion', type=str, required=True)
        data = parser.parse_args()

        with lock.lock:
            tipoVinculacion = TipoVinculacionModel(idTipo=data['idTipo'], descTipoVinculacion=data['descTipoVinculacion'])

            tipoVinculacion.save_to_db()

            return {'tipoVinculacion': tipoVinculacion.json()}, 200 if tipoVinculacion else 404

    def delete(self, id):
        with lock.lock:
            TipoVinculacionModel.get_by_id(id).delete_from_db()

    def put(self, id):
        parser = reqparse.RequestParser()

        parser.add_argument('idTipo', type=str, required=False)
        parser.add_argument('descTipoVinculacion', type=str, required=False)
        data = parser.parse_args()

        with lock.lock:
            tipoVinculacion = TipoVinculacionModel.get_by_id(id)

            if tipoVinculacion:
                if data['idTipo']:
                    tipoVinculacion.idTipo = data['idTipo']
                if data['descTipoVinculacion']:
                    tipoVinculacion.descTipoVinculacion = data['descTipoVinculacion']

            try:
                tipoVinculacion.save_to_db()
            except:
                return {"message": "An error occurred inserting the tipoVinculacion."}, 500

            return {'tipoVinculacion': tipoVinculacion.json()}, 200 if tipoVinculacion else 404