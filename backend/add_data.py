from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy

import data

from models.setupDocumentoPersona import SetupDocumentoPersonaModel
from models.documento import DocumentoModel
from models.rol import RolModel
from models.tipoVinculacion import TipoVinculacionModel
from models.tipoDocumento import TipoDocumentoModel
from models.contrato import ContratoModel
from models.organizacion import OrganizacionModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

organizaciones = []
contratos = []
tiposDocumento = []
tiposVinculacion = []
roles = []
documentos = []
setupsDocumentoPersona = []

for org in data.organizacion:
    organizacionModel = OrganizacionModel(nombre=org["nombre"], rtn=org["rtn"])
    organizaciones.append(organizacionModel)

for cont in data.contrato:
    contratoModel = ContratoModel(tipoContrato=cont["tipoContrato"])
    contratos.append(contratoModel)

for tipoDoc in data.tipoDocumento:
    tipoDocumentoModel = TipoDocumentoModel(descTipoDocumento=tipoDoc["descTipoDocumento"])
    tiposDocumento.append(tipoDocumentoModel)

for tipoVinc in data.tipoVinculacion:
    tipoVinculacionModel = TipoVinculacionModel(idTipo=tipoVinc["idTipo"],
                                                descTipoVinculacion=tipoVinc["descTipoVinculacion"])
    tiposVinculacion.append(tipoVinculacionModel)

for rol in data.rol:
    rolModel = RolModel(nombreRol=rol["nombreRol"], tipoRol=rol["tipoRol"])
    roles.append(rolModel)

for doc in data.documento:
    docModel = DocumentoModel(idTipoDocumento=doc["idTipoDocumento"], descripcionDocumento=doc["descripcionDocumento"])
    roles.append(docModel)

for setupDocPersona in data.setupDocumentoPersona:
    setupDocPersonaModel = SetupDocumentoPersonaModel(diasExpira=setupDocPersona["diasExpira"])

    setupDocPersonaModel.add_documento(DocumentoModel.get_by_id(setupDocPersona['idDocumento']))
    setupDocPersonaModel.add_tipoDocumento(TipoDocumentoModel.get_by_id(setupDocPersona['idTipoDocumento']))
    setupDocPersonaModel.add_tipoVinculacion(TipoVinculacionModel.get_by_id(setupDocPersona['idTipoVinculacion']))
    setupsDocumentoPersona.append(setupDocPersonaModel)

# Relationships

db.session.add_all(organizaciones)
db.session.add_all(contratos)
db.session.add_all(tiposDocumento)
db.session.add_all(tiposVinculacion)
db.session.add_all(roles)
db.session.add_all(documentos)
db.session.add_all(setupsDocumentoPersona)
db.session.commit()
