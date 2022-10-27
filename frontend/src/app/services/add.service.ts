import {Injectable} from '@angular/core';
import {HttpClient, HttpParams, HttpHeaders} from '@angular/common/http'


import { Observable } from 'rxjs';
import {Project} from "../models/project";
import {Person} from "../models/person";
import {environment} from "../../environments/environment";

@Injectable({
  providedIn: 'root'
})

export class AddService {
  error!: string

  constructor(private http:HttpClient) {

  }

  add_project(project: Project): Observable<Project> {
    console.log('Post Project', project);
    return this.http.post<Project>(`${environment.baseApiUrl}/project`, project);
  }

  add_person(person: Person): Observable<Person> {
    console.log('Post Person', person)
    return this.http.post<Person>(`${environment.baseApiUrl}/person`, person);
  }

  get_projects(): Observable<any> {
    console.log('Get Projects');
    return this.http.get<any>(`${environment.baseApiUrl}/projects`);
  }

  get_people(): Observable<any>{
    console.log('Get People')
    return this.http.get<any>(`${environment.baseApiUrl}/people`)
  }

  delete_project(id: number): Observable<Object> {
    console.log("Delete project: ", id)
    console.log("URL: ", `${environment.baseApiUrl}/project/${id}`)
    return this.http.delete(`${environment.baseApiUrl}/project/${id}`)
  }

  delete_person(id: number): Observable<Object> {
    console.log("Delete person: ", id)
    console.log("URL: ", `${environment.baseApiUrl}/person/${id}`)
    return this.http.delete(`${environment.baseApiUrl}/person/${id}`)
  }

  putProject(project: Project): Observable<Project> {
    console.log('Put Project', project);
    return this.http.put<Project>(`${environment.baseApiUrl}/project/${project.id}`, project);
  }

  putPerson(person: Person): Observable<Person> {
    console.log('Put Person', person);
    return this.http.put<Person>(`${environment.baseApiUrl}/person/${person.id}`, person);
  }
}
