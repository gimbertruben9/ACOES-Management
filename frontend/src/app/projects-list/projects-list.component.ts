import { Component, OnInit } from '@angular/core';
import {Project} from "../models/project";
import {Services} from "../services/services";
import {Router} from "@angular/router";

@Component({
  selector: 'app-projects-list',
  templateUrl: './projects-list.component.html',
  styleUrls: ['./projects-list.component.css'],
})
export class ProjectsListComponent implements OnInit {

  proList: Project[] = [];

  projectId?: number;

  constructor(private services: Services, private router : Router) { }

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

  archiveProject(project: Project) {
    if(confirm("Estás seguro que quieres archivar el proyecto?")) {
      console.log("Archiving project: ", project)
      if (project.id !== undefined){
        project.archived = true
        this.services.putProject(project).subscribe(() => console.log("project archived"));
        window.location.reload()
      }
    }
  }

  editProject(project: Project) {
  }

  adminProject(project: Project) {
    this.projectId = project.id
    this.router.navigate(['/admin-form', project.id])
  }
}
