import { Component, OnInit } from '@angular/core';
import {AddService} from "../services/add.service";
import {Person} from "../models/person";
import {Router} from "@angular/router";

@Component({
  selector: 'app-people-list',
  templateUrl: './people-list.component.html',
  styleUrls: ['./people-list.component.css']
})
export class PeopleListComponent implements OnInit {

  perList: Person[] = [];

  constructor(private addService: AddService, private router : Router) { }

  ngOnInit(): void {
    this.get_all_people()
  }

  private get_all_people() {
    this.perList = []
    this.addService.get_people().subscribe(people => {
      this.perList = people['people']
    });
    console.log("All people", this.perList)
  }

  addPerson() {
    this.router.navigate(['/person-form']);
  }

  editPerson() {

  }

  deletePerson(person: Person) {
    console.log("Deleting person: ", person)
    if (person.id !== undefined){
      this.addService.delete_person(person.id).subscribe(() => console.log("person deleted"));
      window.location.reload()
    }
  }
}
