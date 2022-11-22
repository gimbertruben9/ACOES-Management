from db import db


class TipoVinculacionModel(db.Model):
    __tablename__ = 'tipoVinculacion'  # this is the table name
    __table_args__ = (db.UniqueConstraint('idTipo', 'descTipoVinculacion'),)

    def __init__(self, idTipo, descTipoVinculacion):
        self.idTipo = idTipo
        self.descTipoVinculacion = descTipoVinculacion

    id = db.Column(db.Integer, primary_key=True)
    idTipo = db.Column(db.String(1), nullable=False, unique=True)
    descTipoVinculacion = db.Column(db.String(30), nullable=False)


    def json(self):
        return {'id': self.id, 'idTipo': self.idTipo, 'descTipoVinculacion': self.descTipoVinculacion}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(self, id):
        return TipoVinculacionModel.query.filter_by(id=id).first()

    @classmethod
    def get_all(self):
        return db.session.query(TipoVinculacionModel).all()