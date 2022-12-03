export interface Project {
  id?: number;
  idOrganizacion: number;
  nombre: string;
  idCoordinador?: number;
  centroCoste: string;
  archived?: boolean;
  n_empleados?: number;
  n_voluntarios?: number;
  n_docs?: number;
  nombreCoordinador?: string;
}
