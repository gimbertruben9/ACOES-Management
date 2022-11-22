from db import db


class UsuarioModel(db.Model):
    __tablename__ = 'usuario'  # this is the table name
    __table_args__ = (db.UniqueConstraint('idRolUsuario', 'idPersona'),)

    def __init__(self, nombreUsuario, correo, password, estado, idRolUsuario):
        self.nombreUsuario = nombreUsuario
        self.correo = correo
        self.password = password
        self.estado = estado
        self.idRolUsuario = idRolUsuario

    id = db.Column(db.Integer, primary_key=True)
    nombreUsuario = db.Column(db.String(30), nullable=False)
    correo = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    estado = db.Column(db.String(60), nullable=False)

    idRolUsuario = db.Column(db.Integer, db.ForeignKey("rol.id"), nullable=False)
    idPersona = db.Column(db.Integer, db.ForeignKey("persona.id"), nullable=False)

    # relacion N-1
    persona = db.relationship("PersonaModel", foreign_keys=[idPersona])

    def json(self):
        return {'id': self.id, 'nombreUsuario': self.nombreUsuario, 'correo': self.correo, 'password': self.password,
                'estado': self.estado, 'idRolUsuario': self.idRolUsuario, 'idPersona': self.idPersona}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def add_person(self, persona):
        self.persona = persona

    @classmethod
    def get_by_id(self, id):
        return UsuarioModel.query.filter_by(id=id).first()

    @classmethod
    def get_all(self):
        return db.session.query(UsuarioModel).all()
