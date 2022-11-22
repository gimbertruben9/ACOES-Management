from db import db


class DetalleDocumentoModel(db.Model):
    __tablename__ = 'detalleDocumento'  # this is the table name
    __table_args__ = (db.UniqueConstraint('idSetupDocumentoPersona', 'idEmpleado', 'fechaHoraCarga'),)

    def __init__(self, fechaHoraCarga, fechaExpedicion, comentario, pathDestinoAdjunto, nombreAdjuntoOriginal):
        self.fechaHoraCarga = fechaHoraCarga
        self.fechaExpedicion = fechaExpedicion
        self.comentario = comentario
        self.pathDestinoAdjunto = pathDestinoAdjunto
        self.nombreAdjuntoOriginal = nombreAdjuntoOriginal

    # PKs
    id = db.Column(db.Integer, primary_key=True)
    idSetupDocumentoPersona = db.Column(db.Integer, db.ForeignKey("setupDocumentoPersona.id"), nullable=False)
    idEmpleado = db.Column(db.Integer, db.ForeignKey("persona.id"))
    fechaHoraCarga = db.Column(db.DateTime, nullable=False)

    fechaExpedicion = db.Column(db.DateTime, nullable=False)
    comentario = db.Column(db.String, nullable=False)
    pathDestinoAdjunto = db.Column(db.String, nullable=False)
    nombreAdjuntoOriginal = db.Column(db.String(60), nullable=False)

    # relacion 1-N
    persona = db.relationship("PersonaModel", foreign_keys=[idEmpleado])
    setupDocumentoPersona = db.relationship("SetupDocumentoPersonaModel", foreign_keys=[idSetupDocumentoPersona])

    def json(self):
        return {'idSetupDocumentoPersona': self.idSetupDocumentoPersona, 'idEmpleado': self.idEmpleado,
                'fechaHoraCarga': self.fechaHoraCarga.isoformat(),
                'fechaExpedicion': self.fechaExpedicion.isoformat(), 'comentario': self.comentario,
                'pathDestinoAdjunto': self.pathDestinoAdjunto,
                'nombreAdjuntoOriginal': self.nombreAdjuntoOriginal}

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

    # MIRAR SI FUNCIONA!!!
    @classmethod
    def get_by_id(self, idSetupDocumentoPersona, idEmpleado, fechaHoraCarga):
        return DetalleDocumentoModel.query.filter_by(idSetupDocumentoPersona=idSetupDocumentoPersona,
                                                     idEmpleado=idEmpleado, fechaHoraCarga=fechaHoraCarga).first()

    @classmethod
    def get_all(self):
        return db.session.query(DetalleDocumentoModel).all()
