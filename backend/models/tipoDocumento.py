from db import db


class TipoDocumentoModel(db.Model):
    __tablename__ = "tipoDocumento"

    def __init__(self, descTipoDocumento):
        self.descTipoDocumento = descTipoDocumento

    id = db.Column(db.Integer, primary_key=True)
    descTipoDocumento = db.Column(db.String(20), nullable=False, unique=True)

    def json(self):
        return {'id': self.id, 'descTipoDocumento': self.descTipoDocumento}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(self, id):
        return TipoDocumentoModel.query.filter_by(id=id).first()

    @classmethod
    def get_all(self):
        return db.session.query(TipoDocumentoModel).all()
