from db import db


class RolModel(db.Model):
    __tablename__ = 'rol'  # this is the table name
    __table_args__ = (db.UniqueConstraint('nombreRol', 'tipoRol'),)

    def __init__(self, nombreRol, tipoRol):
        self.nombreRol = nombreRol
        self.tipoRol = tipoRol

    id = db.Column(db.Integer, primary_key=True)
    nombreRol = db.Column(db.String(30), nullable=False)
    tipoRol = db.Column(db.String(60), nullable=False)

    def json(self):
        return {'id': self.id, 'nombreRol': self.nombreRol, 'tipoRol': self.tipoRol}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(self, id):
        return RolModel.query.filter_by(id=id).first()

    @classmethod
    def get_all(self):
        return db.session.query(RolModel).all()
