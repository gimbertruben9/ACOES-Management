from db import db


class ProjectsModel(db.Model):
    __tablename__ = 'projects'  # this is the table name
    __table_args__ = (db.UniqueConstraint('name', 'ceco'),)

    def __init__(self, name, ceco):
        self.name = name
        self.ceco = ceco
        self.n_employees = 0
        self.n_volunteers = 0
        self.n_docs = 0
        self.archived = False

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    admin = db.Column(db.String(45), nullable=True)
    ceco = db.Column(db.String(45), nullable=False)
    archived = db.Column(db.Boolean, nullable=False)
    n_employees = db.Column(db.Integer, nullable=False)
    n_volunteers = db.Column(db.Integer, nullable=False)
    n_docs = db.Column(db.Integer, nullable=False)

    def json(self):
        return {'id': self.id, 'name': self.name, 'admin': self.admin, 'ceco': self.ceco,
                'n_employees': self.n_employees, 'n_volunteers': self.n_volunteers,
                'n_docs': self.n_docs, 'archived': self.archived}

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

    @classmethod
    def get_all_unarchived(self):
        return db.session.query(ProjectsModel).filter_by(archived=False).all()
