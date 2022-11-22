from db import db


class ContratoModel(db.Model):
    __tablename__ = 'contrato'  # this is the table name
    # __table_args__ = (db.UniqueConstraint(''),)

    def __init__(self, tipoContrato):
        self.tipoContrato = tipoContrato

    id = db.Column(db.Integer, primary_key=True)
    tipoContrato = db.Column(db.String(20), nullable=False, unique=False)


    def json(self):
        return {'id': self.id, 'tipoContrato': self.tipoContrato}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(self, id):
        return ContratoModel.query.filter_by(id=id).first()

    @classmethod
    def get_all(self):
        return db.session.query(ContratoModel).all()