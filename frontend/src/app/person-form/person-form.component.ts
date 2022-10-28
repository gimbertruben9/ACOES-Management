import { Component, OnInit } from '@angular/core';
import {Person} from "../models/person";
import {ActivatedRoute, Router} from "@angular/router";
import {AddService} from "../services/add.service";
import {Location} from "@angular/common";

@Component({
  selector: 'app-person-form',
  templateUrl: './person-form.component.html',
  styleUrls: ['./person-form.component.css']
})
export class PersonFormComponent implements OnInit {

  d!: string
  e!: string
  f!: string

  sessionPerson!: Person

  constructor(private router : Router, private route :
    ActivatedRoute, private addService: AddService, private _location: Location) { }

  ngOnInit(): void {
  }

  onAccept() {
    const newPerson: Person = {
      d: this.d,
      e: this.e,
      f: this.f
    };

    this.d = '';
    this.e = '';
    this.f = '';

    this.addService.add_person(newPerson).subscribe((person) => this.sessionPerson = person);
    this._location.back();

  }
}
