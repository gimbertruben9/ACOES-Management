export interface Person {
  id?: number;
  primerNombre: string;
  segundoNombre?: string;
  primerApellido: string;
  segundoApellido: string;
  telefono: string;
  correo: string;
  codigoEmpleado: string;
  fechaNacimiento: string;
  puesto: string;
  fechaInicio: string;
  fechaFinal: string;
  genero: string;
  numPasaporte: string;
  salario: number;
  centroCoste: string;
  idTipoVinculacion: number;
  idDireccion: number;
  idContrato: string;
  idProyecto: string;
  expand?: boolean;
}
