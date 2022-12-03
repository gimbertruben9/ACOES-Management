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
      this.proList = projects['proyectos']
      console.log("All projects", this.proList)
      this.get_people_by_project()
    });
  }

  private get_people_by_project() {
    for(let i=0; i<this.proList.length; i++){
      this.services.get_number_by_project(this.proList[i].id, 1).subscribe(n_empleados => {
        this.proList[i].n_empleados = n_empleados['n_personas']
      },
        error => {
        this.proList[i].n_empleados = 0
        })

      this.services.get_number_by_project(this.proList[i].id, 2).subscribe(n_voluntarios => {
        this.proList[i].n_voluntarios = n_voluntarios['n_personas']
      },
        error => {
        this.proList[i].n_voluntarios = 0
        })

      if(this.proList[i].idCoordinador!=undefined){
        this.services.get_project_admin(this.proList[i].idCoordinador).subscribe(admin => {
          this.proList[i].nombreCoordinador = admin['persona'].primerNombre + ' ' + admin['persona'].segundoNombre + ' '  +
            admin['persona'].primerApellido + ' '  + admin['persona'].segundoApellido
        })
      }
    }

  }

  addProject() {
    this.router.navigate(['/project-form'])
  }

  archiveProject(project: Project) {
    if(confirm("Estás seguro que quieres archivar el proyecto?")) {
      console.log("Archiving project: ", project)
      if (project.id !== undefined){
        project.archived = true
        this.services.putProject(project).subscribe(() => {
          console.log("project archived")
          window.location.reload()
        });
      }
    }
  }

  editProject(project: Project) {
    this.projectId = project.id
    this.router.navigate(['/edit-project-form', project.id])
  }

  adminProject(project: Project) {
    this.projectId = project.id
    this.router.navigate(['/admin-form', project.id])
  }
}
