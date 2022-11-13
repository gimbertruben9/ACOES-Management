import {Component, Input, OnInit} from '@angular/core';
import {Project} from "../models/project";
import {ActivatedRoute, Router} from "@angular/router";
import {Services} from "../services/services";
import {Location} from '@angular/common';

@Component({
  selector: 'app-project-form',
  templateUrl: './project-form.component.html',
  styleUrls: ['./project-form.component.css']
})
export class ProjectFormComponent implements OnInit {

  name: string = ''
  ceco: string = ''
  sessionProject!: Project

  constructor(private router : Router, private route :
    ActivatedRoute, private services: Services, private _location: Location) { }

  ngOnInit(): void {
  }

  onAccept() {
    const newProject: Project = {
      name: this.name,
      ceco: this.ceco
    };

    this.name = '';
    this.ceco = '';

    this.services.add_project(newProject).subscribe((project) => this.sessionProject = project);
    this._location.back();

  }

  onCancel() {
    this._location.back();
  }
}


@Component({
  selector: 'app-admin-form',
  templateUrl: './admin-form.component.html',
  styleUrls: ['./project-form.component.css']
})
export class AdminFormComponent implements OnInit {

  project: Project = {
    ceco: "",
    name: ""
  };
  projectId?: number | null;
  admin: string = '';
  adminList: string[] = ['Jorge Lorenzo Salinas', 'Gabriel García Márquez', 'Pablo Neruda', 'Julio Cortazar', 'Mario Vargas Llosa']

  constructor(private router : Router, private route :
    ActivatedRoute, private services: Services, private _location: Location) { }

  ngOnInit(): void {
    this.projectId = (this.route.snapshot.paramMap.get('projectId') as number|null)
    this.getProject(this.projectId)
  }

  getProject(projectId: number | null) {

    if(projectId !== null){
      this.services.getProjectById(projectId).subscribe(project => {
        this.project = project['project']
      })
    }
  }

  onCancel() {
    this._location.back();
  }

  onAccept() {
    this.project.admin = this.admin
    this.services.putProject(this.project).subscribe(() => console.log("project archived"))
    this._location.back();
  }
}
