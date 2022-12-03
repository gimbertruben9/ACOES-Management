from flask import Flask
from flask_restful import Api

from resources.contrato import Contrato
from resources.detalleDocumento import DetalleDocumento
from resources.direccion import Direccion
from resources.documento import Documento
from resources.organizacion import Organizacion, OrganizacionList
from resources.persona import Persona, PersonaList, PersonasPorProyecto
from resources.proyecto import Proyecto, ProyectoList, ProyectoDesarchivadoList
from resources.rol import Rol
from resources.setupDocumentoPersona import SetupDocumentoPersona
from resources.tipoDocumento import TipoDocumento
from resources.tipoVinculacion import TipoVinculacion
from resources.usuario import Usuario

from db import db
from flask_migrate import Migrate

from flask_cors import CORS
from flask import render_template

app = Flask(
    __name__,
    static_folder='dist/static',
    template_folder='dist/templates'
)
api = Api(app)
CORS(app, resources={r'/*': {'origins': '*'}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def render_angular():
    return render_template("index.html")


# @app.route('/')
# def hello_world():
#    return "Hello World!"


api.add_resource(Proyecto, '/proyecto/<int:id>', '/proyecto')
api.add_resource(ProyectoList, '/proyectos')
api.add_resource(ProyectoDesarchivadoList, '/proyectos-desarchivados')

api.add_resource(Persona, '/persona/<int:id>', '/persona')
api.add_resource(PersonaList, '/personas')
api.add_resource(PersonasPorProyecto, '/personasPorProyecto/<int:idProyecto>/<int:idTipoVinculacion>')

api.add_resource(Contrato, '/contrato/<int:id>', '/contrato')

api.add_resource(Direccion, '/direccion/<int:id>', '/direccion')

api.add_resource(Organizacion, '/organizacion/<int:id>', '/organizacion')
api.add_resource(OrganizacionList, '/organizaciones')

api.add_resource(TipoVinculacion, '/tipoVinculacion/<int:id>', '/tipoVinculacion')

api.add_resource(DetalleDocumento, '/detalleDocumento')

api.add_resource(SetupDocumentoPersona, '/setupDocumentoPersona/<int:id>', '/setupDocumentoPersona')

api.add_resource(Documento, '/documento/<int:id>', '/documento')

api.add_resource(TipoDocumento, '/tipoDocumento/<int:id>', '/tipoDocumento')

api.add_resource(Usuario, '/usuario/<int:id>', '/usuario')

api.add_resource(Rol, '/rol/<int:id>', '/rol')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
