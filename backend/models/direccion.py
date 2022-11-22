from db import db


class DireccionModel(db.Model):
    __tablename__ = 'direccion'  # this is the table name
    __table_args__ = (db.UniqueConstraint('pais', 'ciudad', 'colonia', 'calle', 'descripcion'),)

    def __init__(self, pais, ciudad, colonia, calle, descripcion):
        self.pais = pais
        self.ciudad = ciudad
        self.colonia = colonia
        self.calle = calle
        self.descripcion = descripcion

    id = db.Column(db.Integer, primary_key=True)
    pais = db.Column(db.String(30), nullable=False)
    ciudad = db.Column(db.String(30), nullable=False)
    colonia = db.Column(db.String(30), nullable=False)
    calle = db.Column(db.String(30), nullable=False)
    descripcion = db.Column(db.String, nullable=False)


    def json(self):
        return {'id': self.id, 'pais': self.pais, 'ciudad': self.ciudad, 'colonia': self.colonia,
                'calle': self.calle, 'descripcion': self.descripcion}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(self, id):
        return DireccionModel.query.filter_by(id=id).first()

    @classmethod
    def get_all(self):
        return db.session.query(DireccionModel).all()