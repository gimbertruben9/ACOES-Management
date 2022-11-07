import { Component, OnInit, Inject } from '@angular/core';
import {Project} from "../models/project";
import {Services} from "../services/services";
import {Router} from "@angular/router";

import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';

@Component({
  selector: 'app-projects-list',
  templateUrl: './projects-list.component.html',
  styleUrls: ['./projects-list.component.css'],
})
export class ProjectsListComponent implements OnInit {

  proList: Project[] = [];

  projectName: string = '';

  constructor(private services: Services, private router : Router, public dialog: MatDialog) { }

  ngOnInit(): void {
    this.get_all_projects()
  }

  private get_all_projects() {
    this.proList = []
    this.services.get_projects().subscribe(projects => {
      this.proList = projects['projects']
      console.log("All projects", this.proList)
    });
  }

  addProject() {
    this.router.navigate(['/project-form'])
  }

  deleteProject(project: Project) {
    if(confirm("Estás seguro que quieres eliminar el proyecto?")) {
      console.log("Deleting project: ", project)
      if (project.id !== undefined){
        this.services.delete_project(project.id).subscribe(() => console.log("project deleted"));
        window.location.reload()
      }
    }


  }

  editProject(project: Project) {

  }

  adminProject(project: Project) {
    this.projectName = project.a
    this.router.navigate(['/admin-form', project.a])
  }
}
