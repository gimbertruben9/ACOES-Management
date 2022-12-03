import { Component, OnInit } from '@angular/core';
import {Person} from "../models/person";
import {Document} from "../models/document";

@Component({
  selector: 'app-documents-list',
  templateUrl: './documents-list.component.html',
  styleUrls: ['./documents-list.component.css']
})
export class DocumentsListComponent implements OnInit {
/*
  people: Person[] = [ { d: "Pedro Piqueras", e: "", f: "", expand: false }, { d: "Rosalía de Castro", e: "", f: "", expand: false },
  { d: "Juan Valdés", e: "", f: "", expand: false }, { d: "Miguel de Cervantes", e: "", f: "", expand: false }, { d: "Antonio Machado", e: "", f: "", expand: false }]

  peopleDocs: Document[] = [ { personName: "Pedro Piqueras", documento: "Documento Identidad", expedido: "12/01/1995", caduca: "12/01/2000"},
  { personName: "Pedro Piqueras", documento: "CV", expedido: "09/06/1996", caduca: "09/06/1998"}]

 */

  constructor() {}

  ngOnInit(): void {
  }

  expandCell(person: Person) {
    //person.expand = !person.expand
  }
}
