import { Component, OnInit } from '@angular/core';
import {Project} from "../models/project";
import {ActivatedRoute, Router} from "@angular/router";
import {AddService} from "../services/add.service";
import {Location} from '@angular/common';

@Component({
  selector: 'app-project-form',
  templateUrl: './project-form.component.html',
  styleUrls: ['./project-form.component.css']
})
export class ProjectFormComponent implements OnInit {

  a!: string
  b!: string
  c!: string
  sessionProject!: Project

  constructor(private router : Router, private route :
    ActivatedRoute, private addService: AddService, private _location: Location) { }

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

    this.addService.add_project(newProject).subscribe((project) => this.sessionProject = project);
    this._location.back();

  }
}
