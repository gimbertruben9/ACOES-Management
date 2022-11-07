import { Component, OnInit, Inject } from '@angular/core';
import {Project} from "../models/project";
import {Services} from "../services/services";
import {Router} from "@angular/router";

import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';

@Component({
  selector: 'app-projects-list',
  templateUrl: './projects-list.component.html',
  styleUrls: ['./projects-list.component.css']
})
export class ProjectsListComponent implements OnInit {

  proList: Project[] = [];
  projectEdit!: Project;
  projectAdd!: Project;

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
    //this.openAddDialog()
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
    if (project.id !== undefined) {
      this.openEditDialog(project.id)
    }
  }

  openEditDialog(id: number): void {
    const dialogRef = this.dialog.open(EditProjectDialog, {
      width: '300px',
      data: {id: id, a: '', b: '', c: ''}
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      this.projectEdit = result;
      this.services.putProject(this.projectEdit).subscribe(project => {
        console.log("Project edited: ", project)
        window.location.reload()
      });
    });
  }

  adminProject(project: Project) {

  }
}


@Component({
  selector: 'edit-project-dialog.component',
  templateUrl: 'edit-project-dialog.component.html',
  styleUrls: ['./projects-list.component.css']
})
export class EditProjectDialog {
  constructor(
    public dialogRef: MatDialogRef<EditProjectDialog>,
    @Inject(MAT_DIALOG_DATA) public project: Project,
  ) {}

  onNoClick(): void {
    this.dialogRef.close();
  }
}

