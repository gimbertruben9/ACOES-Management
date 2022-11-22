from db import db


class OrganizacionModel(db.Model):
    __tablename__ = "organizacion"
    __table_args__ = (db.UniqueConstraint('nombre', 'rtn'),)

    def __init__(self, nombre, rtn):
        self.nombre = nombre
        self.rtn = rtn

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False, unique=True)
    rtn = db.Column(db.String(30), nullable=False)

    def json(self):
        return {'id': self.id, 'nombre': self.nombre, 'rtn': self.rtn}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(self, id):
        return OrganizacionModel.query.filter_by(id=id).first()

    @classmethod
    def get_all(self):
        return db.session.query(OrganizacionModel).all()
