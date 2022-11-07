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

  a: string = ''
  b: string = ''
  c: string = ''
  sessionProject!: Project

  constructor(private router : Router, private route :
    ActivatedRoute, private services: Services, private _location: Location) { }

  ngOnInit(): void {
  }

  onAccept() {
    const newProject: Project = {
      a: this.a,
      b: this.b,
      c: this.c
    };

    this.a = '';
    this.b = '';
    this.c = '';

    //this.services.add_project(newProject).subscribe((project) => this.sessionProject = project);
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

  projectName: string | null = ''

  constructor(private router : Router, private route :
    ActivatedRoute, private services: Services, private _location: Location) { }

  ngOnInit(): void {
    this.projectName = this.route.snapshot.paramMap.get('projectName')
  }

  onCancel() {
    this._location.back();
  }

  onAccept() {

  }
}
