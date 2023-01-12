import {Injectable} from '@angular/core';
import {HttpClient, HttpParams, HttpHeaders} from '@angular/common/http'


import { Observable } from 'rxjs';
import {Project} from "../models/project";
import {Person} from "../models/person";
import {environment} from "../../environments/environment";
import {DetalleDocumento} from "../models/detalleDocumento";

@Injectable({
  providedIn: 'root'
})

export class Services {
  error!: string

  constructor(private http:HttpClient) {

  }

  add_project(project: Project): Observable<Project> {
    console.log('Post Project', project);
    return this.http.post<Project>(`${environment.baseApiUrl}/proyecto`, project);
  }

  add_person(person: Person): Observable<Person> {
    console.log('Post Person', person)
    return this.http.post<Person>(`${environment.baseApiUrl}/persona`, person);
  }

  get_projects(): Observable<any> {
    console.log('Get Projects');
    return this.http.get<any>(`${environment.baseApiUrl}/proyectos-desarchivados`);
  }

  get_people(): Observable<any>{
    console.log('Get People')
    return this.http.get<any>(`${environment.baseApiUrl}/personas`)
  }

  delete_project(id: number): Observable<Object> {
    console.log("Delete project: ", id)
    console.log("URL: ", `${environment.baseApiUrl}/proyecto/${id}`)
    return this.http.delete(`${environment.baseApiUrl}/proyecto/${id}`)
  }

  delete_person(id: number): Observable<Object> {
    console.log("Delete person: ", id)
    console.log("URL: ", `${environment.baseApiUrl}/persona/${id}`)
    return this.http.delete(`${environment.baseApiUrl}/persona/${id}`)
  }

  putProject(project: Project): Observable<Project> {
    console.log('Put Project', project);
    return this.http.put<Project>(`${environment.baseApiUrl}/proyecto/${project.id}`, project);
  }

  putPerson(person: Person): Observable<Person> {
    console.log('Put Person', person);
    return this.http.put<Person>(`${environment.baseApiUrl}/persona/${person.id}`, person);
  }

  getProjectById(id: number): Observable<any> {
    console.log('Get project with id: ', id)
    return this.http.get<any>(`${environment.baseApiUrl}/proyecto/${id}`);
  }

  get_orgs(): Observable<any> {
    console.log('Get Organizations')
    return this.http.get<any>(`${environment.baseApiUrl}/organizaciones`)
  }

  get_number_by_project(idProyecto?: number, idTipoVinculacion?: number): Observable<any> {
    console.log('Get number of people in project:', idProyecto)
    return this.http.get<any>(`${environment.baseApiUrl}/personasPorProyecto/${idProyecto}/${idTipoVinculacion}`)
  }

  get_project_admin(idCoordinador: number|undefined): Observable<any> {
    console.log('Get admin')
    return this.http.get<any>(`${environment.baseApiUrl}/persona/${idCoordinador}`)
  }

  get_all_detalleDoc(idEmpleado: number): Observable<any> {
    console.log('Get all detallesDocumento')
    return this.http.get<any>(`${environment.baseApiUrl}/detallesDocumento/${idEmpleado}`)
  }

  get_detalleDoc(idDetalle: number): Observable<any>{
    return this.http.get<any>(`${environment.baseApiUrl}/detalleDocumento/${idDetalle}`)
  }

  get_person(idPersona: number): Observable<any> {
    return this.http.get<any>(`${environment.baseApiUrl}/persona/${idPersona}`)
  }

  postDocument(detalle: DetalleDocumento): Observable<DetalleDocumento> {
    if(detalle.id != undefined){
      return this.http.post<DetalleDocumento>(`${environment.baseApiUrl}/detalleDocumento/${detalle.id}`, detalle)
    }
    else{
      return this.http.post<DetalleDocumento>(`${environment.baseApiUrl}/detalleDocumento`, detalle)
    }
  }

  putDocument(detalle: DetalleDocumento): Observable<DetalleDocumento> {
    return this.http.put<DetalleDocumento>(`${environment.baseApiUrl}/detalleDocumento/${detalle.id}`, detalle)
  }

  deleteDocument(detalle: DetalleDocumento): Observable<any> {
    return this.http.delete(`${environment.baseApiUrl}/detalleDocumento/${detalle.id}`)
  }
}
