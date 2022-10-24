from db import db


class PeopleModel(db.Model):
    __tablename__ = 'people'  # this is the table name

    def __init__(self, d, e, f):
        self.d = d
        self.e = e
        self.f = f

    id = db.Column(db.Integer, primary_key=True)
    d = db.Column(db.String(30), unique=True)
    e = db.Column(db.String(30), unique=True)
    f = db.Column(db.String(30), unique=True)

    def json(self):
        return {'id': self.id, 'd': self.d, 'e': self.e, 'f': self.f}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(self, id):
        return PeopleModel.query.filter_by(id=id).first()

    @classmethod
    def get_all(self):
        return db.session.query(PeopleModel).all()
