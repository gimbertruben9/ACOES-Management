from db import db


class SetupDocumentoPersonaModel(db.Model):
    __tablename__ = 'setupDocumentoPersona'  # this is the table name
    __table_args__ = (db.UniqueConstraint('idDocumento', 'idTipoDocumento', 'idTipoVinculacion'),)

    def __init__(self, diasExpira):
        self.diasExpira = diasExpira

    id = db.Column(db.Integer, primary_key=True)
    idDocumento = db.Column(db.Integer, db.ForeignKey("documento.id"))
    idTipoDocumento = db.Column(db.Integer, db.ForeignKey("tipoDocumento.id"))
    idTipoVinculacion = db.Column(db.Integer, db.ForeignKey("tipoVinculacion.id"))
    diasExpira = db.Column(db.Integer, nullable=False)

    # Relacion 1-N
    tipoVinculacion = db.relationship("TipoVinculacionModel", foreign_keys=[idTipoVinculacion])
    documento = db.relationship("DocumentoModel", foreign_keys=[idDocumento])
    tipoDocumento = db.relationship("TipoDocumentoModel", foreign_keys=[idTipoDocumento])


    def json(self):
        return {'id': self.id, 'idDocumento': self.idDocumento, 'idTipoDocumento': self.idTipoDocumento,
                'idTipoVinculacion': self.idTipoVinculacion, 'diasExpira': self.diasExpira}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    def add_documento(self, documento):
        self.documento = documento

    def add_tipoDocumento(self, tipoDocumento):
        self.tipoDocumento = tipoDocumento

    def add_tipoVinculacion(self, tipoVinculacion):
        self.tipoVinculacion = tipoVinculacion

    @classmethod
    def get_by_id(self, id):
        return SetupDocumentoPersonaModel.query.filter_by(id=id).first()

    @classmethod
    def get_all(self):
        return db.session.query(SetupDocumentoPersonaModel).all()