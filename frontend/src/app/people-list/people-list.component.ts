import {Component, Inject, OnInit} from '@angular/core';
import {AddService} from "../services/add.service";
import {Person} from "../models/person";
import {Router} from "@angular/router";

import {MatDialog, MAT_DIALOG_DATA, MatDialogRef} from "@angular/material/dialog";

@Component({
  selector: 'app-people-list',
  templateUrl: './people-list.component.html',
  styleUrls: ['./people-list.component.css']
})
export class PeopleListComponent implements OnInit {

  perList: Person[] = [];
  personEdit!: Person;

  constructor(private addService: AddService, private router : Router, public dialog: MatDialog) { }

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

  deletePerson(person: Person) {
    if(confirm("Estás seguro que quieres eliminar la persona?")) {
      console.log("Deleting person: ", person)
      if (person.id !== undefined) {
        this.addService.delete_person(person.id).subscribe(() => console.log("person deleted"));
        window.location.reload()
      }
    }
  }

  editPerson(person: Person) {
    if (person.id !== undefined) {
      this.openDialog(person.id)
    }
  }

  openDialog(id: number): void {
    const dialogRef = this.dialog.open(EditPersonDialog, {
      width: '300px',
      data: {id: id, d: '', e: '', f: ''}
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      this.personEdit = result;
      this.addService.putPerson(this.personEdit).subscribe(person => {
        console.log("Person edited: ", person)
        window.location.reload()
      });
    });
  }
}

@Component({
  selector: 'person-dialog.component',
  templateUrl: 'person-dialog.component.html',
  styleUrls: ['./people-list.component.css']
})
export class EditPersonDialog {
  constructor(
    public dialogRef: MatDialogRef<EditPersonDialog>,
    @Inject(MAT_DIALOG_DATA) public person: Person,
  ) {}

  onNoClick(): void {
    this.dialogRef.close();
  }
}

