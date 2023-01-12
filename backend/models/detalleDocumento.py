from db import db

from models.documento import DocumentoModel
from models.setupDocumentoPersona import SetupDocumentoPersonaModel
from models.tipoDocumento import TipoDocumentoModel


class DetalleDocumentoModel(db.Model):
    __tablename__ = 'detalleDocumento'  # this is the table name
    __table_args__ = (db.UniqueConstraint('idSetupDocumentoPersona', 'idEmpleado', 'fechaHoraCarga'),)

    def __init__(self, setupDocumentoPersona, empleado):
        self.setupDocumentoPersona = setupDocumentoPersona
        self.persona = empleado

    # PKs
    id = db.Column(db.Integer, primary_key=True)
    idSetupDocumentoPersona = db.Column(db.Integer, db.ForeignKey("setupDocumentoPersona.id"), nullable=False)
    idEmpleado = db.Column(db.Integer, db.ForeignKey("persona.id"), nullable=False)
    fechaHoraCarga = db.Column(db.DateTime, nullable=True)

    fechaExpedicion = db.Column(db.DateTime, nullable=True)
    comentario = db.Column(db.String, nullable=True)
    pathDestinoAdjunto = db.Column(db.String, nullable=True)
    nombreAdjuntoOriginal = db.Column(db.String(60), nullable=True)

    # relacion 1-N
    persona = db.relationship("PersonaModel", foreign_keys=[idEmpleado])
    setupDocumentoPersona = db.relationship("SetupDocumentoPersonaModel", foreign_keys=[idSetupDocumentoPersona])

    def json(self):
        if (self.fechaHoraCarga is None and self.fechaExpedicion is None and self.comentario is None
                and self.pathDestinoAdjunto is None and self.nombreAdjuntoOriginal is None):
            return {'id': self.id, 'idSetupDocumentoPersona': self.idSetupDocumentoPersona, 'idEmpleado': self.idEmpleado,
                    'documento': self.get_documento(self.get_setupDocumentoPersona(self.idSetupDocumentoPersona).idDocumento).idTipoDocumento,
                    'descripcionDocumento': self.get_documento(self.get_setupDocumentoPersona(self.idSetupDocumentoPersona).idDocumento).descripcionDocumento,
                    'tipoDocumento': self.get_tipoDocumento(self.get_setupDocumentoPersona(self.idSetupDocumentoPersona).idTipoDocumento).descTipoDocumento}
        else:
            return {'id': self.id, 'idSetupDocumentoPersona': self.idSetupDocumentoPersona, 'idEmpleado': self.idEmpleado,
                    'fechaHoraCarga': self.fechaHoraCarga.isoformat(),
                    'fechaExpedicion': self.fechaExpedicion.strftime('%Y-%m-%d'), 'comentario': self.comentario,
                    'pathDestinoAdjunto': self.pathDestinoAdjunto,
                    'nombreAdjuntoOriginal': self.nombreAdjuntoOriginal,
                    'documento': self.get_documento(self.get_setupDocumentoPersona(self.idSetupDocumentoPersona).idDocumento).idTipoDocumento,
                    'descripcionDocumento': self.get_documento(self.get_setupDocumentoPersona(self.idSetupDocumentoPersona).idDocumento).descripcionDocumento,
                    'tipoDocumento': self.get_tipoDocumento(self.get_setupDocumentoPersona(self.idSetupDocumentoPersona).idTipoDocumento).descTipoDocumento,
                    'diasExpira': self.get_setupDocumentoPersona(self.idSetupDocumentoPersona).diasExpira}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def add_empleado(self, empleado):
        self.persona = empleado

    def add_setupDocPersona(self, setupDocumentoPersona):
        self.setupDocumentoPersona = setupDocumentoPersona


    @classmethod
    def get_by_UC(self, idSetupDocumentoPersona, idEmpleado, fechaHoraCarga):
        return DetalleDocumentoModel.query.filter_by(idSetupDocumentoPersona=idSetupDocumentoPersona,
                                                     idEmpleado=idEmpleado, fechaHoraCarga=fechaHoraCarga).first()

    @classmethod
    def get_by_id(self, id):
        return DetalleDocumentoModel.query.filter_by(id=id).first()

    @classmethod
    def get_all(self):
        return db.session.query(DetalleDocumentoModel).all()

    @classmethod
    def get_person_docs(self, idEmpleado):
        return DetalleDocumentoModel.query.filter_by(idEmpleado=idEmpleado)

    @classmethod
    def get_setupDocumentoPersona(self, idSetupDocumentoPersona):
        return SetupDocumentoPersonaModel.get_by_id(idSetupDocumentoPersona)

    @classmethod
    def get_documento(self, idDocumento):
        return DocumentoModel.get_by_id(idDocumento)

    @classmethod
    def get_tipoDocumento(self, idTipoDocumento):
        return TipoDocumentoModel.get_by_id(idTipoDocumento)
