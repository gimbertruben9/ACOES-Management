import { Component, OnInit } from '@angular/core';
import {Project} from "../models/project";
import {AddService} from "../services/add.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-projects-list',
  templateUrl: './projects-list.component.html',
  styleUrls: ['./projects-list.component.css']
})
export class ProjectsListComponent implements OnInit {

  proList: Project[] = [];

  constructor(private addService: AddService, private router : Router) { }

  ngOnInit(): void {
    this.get_all_projects()
  }

  private get_all_projects() {
    this.proList = []
    this.addService.get_projects().subscribe(projects => {
      this.proList = projects['projects']
    });
    console.log("All projects", this.proList)
  }

  addProject() {
    this.router.navigate(['/project-form']);
  }

  editProject() {

  }

  deleteProject(project: Project) {
    console.log("Deleting project: ", project)
    if (project.id !== undefined){
      this.addService.delete_project(project.id).subscribe(() => console.log("project deleted"));
      window.location.reload()
    }
  }
}
