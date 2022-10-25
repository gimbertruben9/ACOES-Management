import { Component, OnInit } from '@angular/core';
import {AddService} from "../services/add.service";
import {Person} from "../models/person";

@Component({
  selector: 'app-people-list',
  templateUrl: './people-list.component.html',
  styleUrls: ['./people-list.component.css']
})
export class PeopleListComponent implements OnInit {

  perList: Person[] = [];

  constructor(private addService: AddService) { }

  ngOnInit(): void {
    this.get_all_people()
  }

  private get_all_people() {

    this.addService.get_people().subscribe(people => {
      for (let i=0; i<people['people'].length; i++) {
        this.perList.push(people['people'][i])
      }
    });
    console.log("All people", this.perList)
  }
}
