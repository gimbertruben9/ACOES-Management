from db import db


class ProjectsModel(db.Model):
    __tablename__ = 'projects'  # this is the table name
    __table_args__ = (db.UniqueConstraint('a', 'b', 'c'),)

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    id = db.Column(db.Integer, primary_key=True)
    a = db.Column(db.String(30), nullable=False)
    b = db.Column(db.String(30), nullable=False)
    c = db.Column(db.String(30), nullable=False)

    def json(self):
        return {'id': self.id, 'a': self.a, 'b': self.b, 'c': self.c}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(self, id):
        return ProjectsModel.query.filter_by(id=id).first()

    @classmethod
    def get_all(self):
        return db.session.query(ProjectsModel).all()
