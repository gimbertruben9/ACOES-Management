from datetime import datetime
from flask_restful import Resource, reqparse
from lock import lock

from models.persona import PersonaModel
from models.proyecto import ProyectoModel
from models.contrato import ContratoModel
from models.tipoVinculacion import TipoVinculacionModel


class Persona(Resource):

    def get(self, id):
        person = PersonaModel.get_by_id(id)
        return {'persona': person.json()}, 200 if person else 404

    def post(self, id=None):
        parser = reqparse.RequestParser()

        parser.add_argument('primerNombre', type=str, required=True)
        parser.add_argument('segundoNombre', type=str, required=True)
        parser.add_argument('primerApellido', type=str, required=True)
        parser.add_argument('segundoApellido', type=str, required=True)
        parser.add_argument('telefono', type=str, required=True)
        parser.add_argument('correo', type=str, required=True)
        parser.add_argument('codigoEmpleado', type=str, required=True)
        parser.add_argument('fechaNacimiento', type=str, required=True)
        parser.add_argument('puesto', type=str, required=True)
        parser.add_argument('fechaInicio', type=str, required=True)
        parser.add_argument('fechaFinal', type=str, required=True)
        parser.add_argument('genero', type=str, required=True)
        parser.add_argument('numPasaporte', type=str, required=True)
        parser.add_argument('salario', type=float, required=True)
        parser.add_argument('centroCoste', type=str, required=True)

        parser.add_argument('idTipoVinculacion', type=int, required=True)
        parser.add_argument('idDireccion', type=int, required=True)
        parser.add_argument('idContrato', type=int, required=False)
        parser.add_argument('idProyecto', type=int, required=True)
        data = parser.parse_args()

        with lock.lock:

            person = PersonaModel(primerNombre=data['primerNombre'], segundoNombre=data['segundoNombre'], primerApellido=data['primerApellido'],
                                  segundoApellido=data['segundoApellido'], telefono=data['telefono'], correo=data['correo'],
                                  codigoEmpleado=data['codigoEmpleado'], fechaNacimiento=datetime.strptime(data['fechaNacimiento'], "%Y-%m-%d"),
                                  puesto=data['puesto'], fechaInicio=datetime.strptime(data['fechaInicio'], "%Y-%m-%d"),
                                  fechaFinal=datetime.strptime(data['fechaFinal'], "%Y-%m-%d"), genero=data['genero'],
                                  numPasaporte=data['numPasaporte'], salario=data['salario'], centroCoste=data['centroCoste'],
                                  idDireccion=data['idDireccion'])
            person.add_project(ProyectoModel.get_by_id(data['idProyecto']))
            person.add_tipoVinculacion(TipoVinculacionModel.get_by_id(data['idTipoVinculacion']))

            if data['idContrato']:
                person.add_contrato(ContratoModel.get_by_id(data['idContrato']))

            person.save_to_db()

            return {'persona': person.json()}, 200 if person else 404

    def delete(self, id):
        with lock.lock:
            PersonaModel.get_by_id(id).delete_from_db()

    def put(self, id):
        parser = reqparse.RequestParser()

        parser.add_argument('primerNombre', type=str, required=True)
        parser.add_argument('segundoNombre', type=str, required=True)
        parser.add_argument('primerApellido', type=str, required=True)
        parser.add_argument('segundoApellido', type=str, required=True)
        parser.add_argument('telefono', type=str, required=True)
        parser.add_argument('correo', type=str, required=True)
        parser.add_argument('codigoEmpleado', type=str, required=True)
        parser.add_argument('fechaNacimiento', type=str, required=True)
        parser.add_argument('puesto', type=str, required=True)
        parser.add_argument('fechaInicio', type=str, required=True)
        parser.add_argument('fechaFinal', type=str, required=True)
        parser.add_argument('genero', type=str, required=True)
        parser.add_argument('numPasaporte', type=str, required=True)
        parser.add_argument('salario', type=float, required=True)
        parser.add_argument('centroCoste', type=str, required=True)

        parser.add_argument('idTipoVinculacion', type=int, required=True)
        parser.add_argument('idDireccion', type=int, required=True)
        parser.add_argument('idContrato', type=int, required=False)
        parser.add_argument('idProyecto', type=int, required=True)
        data = parser.parse_args()

        with lock.lock:
            person = PersonaModel.get_by_id(id)

            if person:
                if data['primerNombre']:
                    person.primerNombre = data['primerNombre']
                if data['segundoNombre']:
                    person.segundoNombre = data['segundoNombre']
                if data['primerApellido']:
                    person.primerApellido = data['primerApellido']
                if data['segundoApellido']:
                    person.segundoApellido = data['segundoApellido']
                if data['telefono']:
                    person.telefono = data['telefono']
                if data['correo']:
                    person.correo = data['correo']
                if data['codigoEmpleado']:
                    person.codigoEmpleado = data['codigoEmpleado']
                if data['fechaNacimiento']:
                    person.fechaNacimiento = datetime.strptime(data['fechaNacimiento'], "%Y-%m-%d")
                if data['puesto']:
                    person.puesto = data['puesto']
                if data['fechaInicio']:
                    person.fechaInicio = datetime.strptime(data['fechaInicio'], "%Y-%m-%d")
                if data['fechaFinal']:
                    person.fechaFinal = datetime.strptime(data['fechaFinal'], "%Y-%m-%d")
                if data['genero']:
                    person.genero = data['genero']
                if data['numPasaporte']:
                    person.numPasaporte = data['numPasaporte']
                if data['salario']:
                    person.salario = data['salario']
                if data['centroCoste']:
                    person.centroCoste = data['centroCoste']
                if data['idTipoVinculacion']:
                    person.add_tipoVinculacion(TipoVinculacionModel.get_by_id(data['idTipoVinculacion']))
                if data['idDireccion']:
                    person.idDireccion = data['idDireccion']
                if data['idContrato']:
                    person.add_contrato(ContratoModel.get_by_id(data['idContrato']))
                if data['idProyecto']:
                    person.add_project(ProyectoModel.get_by_id(data['idProyecto']))

            try:
                person.save_to_db()
            except:
                return {"message": "An error occurred inserting the person."}, 500

            return {'person': person.json()}, 200 if person else 404


class PersonaList(Resource):

    def get(self):
        allPeople = PersonaModel.get_all()
        people = []

        for person in allPeople:
            people.append(person.json())

        return {'personas': people}, 200 if people else 404
