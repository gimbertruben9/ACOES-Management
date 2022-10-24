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
    console.log('Post Project', project)
    console.log('baseApiUrl', `${environment.baseApiUrl}/project`)
    return this.http.post<Project>(`${environment.baseApiUrl}/project`, project);
  }

  add_person(person: Person): Observable<Person> {
    console.log('Post Person', person)
    return this.http.post<Person>(`${environment.baseApiUrl}/person`, person);
  }

}