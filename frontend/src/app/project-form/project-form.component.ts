import {Component, Input, OnInit} from '@angular/core';
import {Project} from "../models/project";
import {ActivatedRoute, Router} from "@angular/router";
import {Services} from "../services/services";
import {Location} from '@angular/common';
import {Organizacion} from "../models/organizacion";
import {Person} from "../models/person";

@Component({
  selector: 'app-project-form',
  templateUrl: './project-form.component.html',
  styleUrls: ['./project-form.component.css']
})
export class ProjectFormComponent implements OnInit {

  idOrganizacion: number = 0
  nombre: string = ''
  centroCoste: string = ''

  orgList: Organizacion[] = []

  sessionProject!: Project

  constructor(private router : Router, private route :
    ActivatedRoute, private services: Services, private _location: Location) { }

  ngOnInit(): void {
    this.get_all_orgs()
  }

  private get_all_orgs() {
    this.orgList = []
    this.services.get_orgs().subscribe(orgs => {
      this.orgList = orgs['organizaciones']
      console.log("All orgs", this.orgList)
    });
  }

  onAccept() {
    const newProject: Project = {
      idOrganizacion: this.idOrganizacion,
      nombre: this.nombre,
      centroCoste: this.centroCoste
    };

    this.nombre = '';
    this.centroCoste = '';
    this.idOrganizacion = 0;


    this.services.add_project(newProject).subscribe((project) => this.sessionProject = project);
    this._location.back();

  }

  onCancel() {
    this._location.back();
  }

  changeSelect(e: any) {
    this.idOrganizacion = e.target.value
  }
}


@Component({
  selector: 'app-admin-form',
  templateUrl: './admin-form.component.html',
  styleUrls: ['./project-form.component.css']
})
export class AdminFormComponent implements OnInit {

  project: Project = {
    idOrganizacion: 1,
    nombre: "",
    centroCoste: ""
  };
  projectId?: number | null;
  idCoordinador?: number;
  peopleList: Person[] = []

  constructor(private router : Router, private route :
    ActivatedRoute, private services: Services, private _location: Location) { }

  ngOnInit(): void {
    this.projectId = (this.route.snapshot.paramMap.get('projectId') as number|null)
    this.getProject(this.projectId)
    this.getPeople()
  }

  getProject(projectId: number | null) {

    if(projectId !== null){
      this.services.getProjectById(projectId).subscribe(project => {
        this.project = project['proyecto']
      })
    }
  }

  private getPeople() {
    this.services.get_people().subscribe(people => {
      this.peopleList = people['personas']
      console.log("All people", this.peopleList)
    });
  }

  onCancel() {
    this._location.back();
  }

  onAccept() {
    this.project.idCoordinador = this.idCoordinador
    this.services.putProject(this.project).subscribe(() => console.log("admin assigned"))
    this._location.back();
  }
}

@Component({
  selector: 'app-edit-project-form',
  templateUrl: './edit-project-form.component.html',
  styleUrls: ['./project-form.component.css']
})
export class EditProjectFormComponent implements OnInit {

  project: Project = {
    idOrganizacion: 1,
    nombre: "",
    centroCoste: ""
  };
  projectId?: number | null;

  orgList: Organizacion[] = []

  constructor(private router : Router, private route :
    ActivatedRoute, private services: Services, private _location: Location) { }

  ngOnInit(): void {
    this.projectId = (this.route.snapshot.paramMap.get('projectId') as number|null)
    this.getProject(this.projectId)
    this.get_all_orgs()
  }

  getProject(projectId: number | null) {

    if(projectId !== null){
      this.services.getProjectById(projectId).subscribe(project => {
        this.project = project['proyecto']
      })
    }
  }


  private get_all_orgs() {
    this.orgList = []
    this.services.get_orgs().subscribe(orgs => {
      this.orgList = orgs['organizaciones']
      console.log("All orgs", this.orgList)
    });
  }

  onAccept() {

    this.services.putProject(this.project).subscribe(() => console.log("admin assigned"))
    this._location.back();

  }

  onCancel() {
    this._location.back();
  }

  changeSelect(e: any) {
    this.project.idOrganizacion = e.target.value
  }
}
