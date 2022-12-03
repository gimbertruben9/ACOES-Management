from db import db


class ProyectoModel(db.Model):
    __tablename__ = 'proyecto'  # this is the table name
    __table_args__ = (db.UniqueConstraint('idOrganizacion', 'nombre'),)

    def __init__(self, nombre, centroCoste):
        self.nombre = nombre
        self.centroCoste = centroCoste
        self.archived = False

    id = db.Column(db.Integer, primary_key=True)
    idOrganizacion = db.Column(db.Integer, db.ForeignKey("organizacion.id"), nullable=False)
    nombre = db.Column(db.String(45), nullable=False, unique=True)
    idCoordinador = db.Column(db.Integer, db.ForeignKey("persona.id"), nullable=True)
    centroCoste = db.Column(db.String(60), nullable=False)
    archived = db.Column(db.Boolean, nullable=False)

    # relacion N-1
    organizacion = db.relationship("OrganizacionModel", foreign_keys=[idOrganizacion])

    def json(self):
        return {'id': self.id, 'idOrganizacion': self.idOrganizacion, 'nombre': self.nombre, 'idCoordinador': self.idCoordinador,
                'centroCoste': self.centroCoste, 'archived': self.archived}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def add_org(self, org):
        self.organizacion = org

    def add_idCoordinador(self, idCoordinador):
        self.idCoordinador = idCoordinador

    @classmethod
    def get_by_id(self, id):
        return ProyectoModel.query.filter_by(id=id).first()

    @classmethod
    def get_all(self):
        return db.session.query(ProyectoModel).all()

    @classmethod
    def get_all_unarchived(self):
        return db.session.query(ProyectoModel).filter_by(archived=False).all()
