import {Person} from "./person";
import {DetalleDocumento} from "./detalleDocumento";

export interface DocsPorPersona {
  persona: Person
  docs: DetalleDocumento[]
}
