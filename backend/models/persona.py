from db import db


class PersonaModel(db.Model):
    __tablename__ = 'persona'  # this is the table name
    __table_args__ = (db.UniqueConstraint('primerNombre', 'segundoNombre', 'primerApellido', 'segundoApellido', 'numPasaporte'),)

    def __init__(self, primerNombre, segundoNombre, primerApellido, segundoApellido, telefono, correo, codigoEmpleado,
                 fechaNacimiento, puesto, fechaInicio, fechaFinal, genero, numPasaporte, salario, centroCoste, idDireccion):
        self.primerNombre = primerNombre
        self.segundoNombre = segundoNombre
        self.primerApellido = primerApellido
        self.segundoApellido = segundoApellido
        self.telefono = telefono
        self.correo = correo
        self.codigoEmpleado = codigoEmpleado
        self.fechaNacimiento = fechaNacimiento
        self.puesto = puesto
        self.fechaInicio = fechaInicio
        self.fechaFinal = fechaFinal
        self.genero = genero
        self.numPasaporte = numPasaporte
        self.salario = salario
        self.centroCoste = centroCoste
        self.idDireccion = idDireccion

    id = db.Column(db.Integer, primary_key=True)
    primerNombre = db.Column(db.String(30), nullable=False)
    segundoNombre = db.Column(db.String(30), nullable=True)
    primerApellido = db.Column(db.String(30), nullable=False)

    segundoApellido = db.Column(db.String(30), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(60), nullable=False)
    codigoEmpleado = db.Column(db.String(60), nullable=False)
    fechaNacimiento = db.Column(db.DateTime, nullable=False)
    puesto = db.Column(db.String(60), nullable=False)
    fechaInicio = db.Column(db.DateTime, nullable=False)
    fechaFinal = db.Column(db.DateTime, nullable=False)
    genero = db.Column(db.String(10), nullable=False)
    numPasaporte = db.Column(db.String(20), nullable=False, unique=True)
    salario = db.Column(db.Float, nullable=False)
    centroCoste = db.Column(db.String(60), nullable=False)

    idTipoVinculacion = db.Column(db.Integer, db.ForeignKey("tipoVinculacion.id"), nullable=False)
    idDireccion = db.Column(db.Integer, db.ForeignKey("direccion.id"), nullable=False)
    idContrato = db.Column(db.Integer, db.ForeignKey("contrato.id"), nullable=True)
    idProyecto = db.Column(db.Integer, db.ForeignKey("proyecto.id"), nullable=False)

    # relacion N-1
    proyecto = db.relationship("ProyectoModel", foreign_keys=[idProyecto])
    contrato = db.relationship("ContratoModel", foreign_keys=[idContrato])
    tipoVinculacion = db.relationship("TipoVinculacionModel", foreign_keys=[idTipoVinculacion])

    def json(self):
        return {'id': self.id, 'primerNombre': self.primerNombre, 'segundoNombre': self.segundoNombre, 'primerApellido': self.primerApellido,
                'segundoApellido': self.segundoApellido, 'telefono': self.telefono, 'correo': self.correo, 'codigoEmpleado': self.codigoEmpleado,
                'fechaNacimiento': self.fechaNacimiento.isoformat(), 'puesto': self.puesto, 'fechaInicio': self.fechaInicio.isoformat(),
                'fechaFinal': self.fechaFinal.isoformat(), 'genero': self.genero, 'numPasaporte': self.numPasaporte, 'salario': self.salario,
                'centroCoste': self.centroCoste, 'idTipoVinculacion': self.idTipoVinculacion, 'idDireccion': self.idDireccion,
                'idContrato': self.idContrato, 'idProyecto': self.idProyecto}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def add_contrato(self, contrato):
        self.contrato = contrato

    def add_project(self, project):
        self.proyecto = project

    def add_tipoVinculacion(self, tipoVinculacion):
        self.tipoVinculacion = tipoVinculacion


    @classmethod
    def get_by_id(self, id):
        return PersonaModel.query.filter_by(id=id).first()

    @classmethod
    def get_all(self):
        return db.session.query(PersonaModel).all()

    @classmethod
    def get_number_by_project(self, idProyecto, idTipoVinculacion):
        return PersonaModel.query.filter_by(idProyecto=idProyecto, idTipoVinculacion=idTipoVinculacion).count()

