import { Component, OnInit } from '@angular/core';
import {Project} from "../models/project";
import {AddService} from "../services/add.service";

@Component({
  selector: 'app-projects-list',
  templateUrl: './projects-list.component.html',
  styleUrls: ['./projects-list.component.css']
})
export class ProjectsListComponent implements OnInit {

  proList: Project[] = [];

  constructor(private addService: AddService) { }

  ngOnInit(): void {
    this.get_all_projects()
  }

  private get_all_projects() {

    this.addService.get_projects().subscribe(projects => {
      for (let i=0; i<projects['projects'].length; i++) {
        this.proList.push(projects['projects'][i])
      }
    });
    console.log("All projects", this.proList)
  }
}
