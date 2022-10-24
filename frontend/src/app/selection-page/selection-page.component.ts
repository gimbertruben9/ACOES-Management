import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router";

@Component({
  selector: 'app-selection-page',
  templateUrl: './selection-page.component.html',
  styleUrls: ['./selection-page.component.css']
})
export class SelectionPageComponent implements OnInit {

  listOptions: string[]
  selectedOption!: string

  constructor(private router : Router) {
    this.listOptions = ['Nothing selected', 'Project', 'Person' ]
    this.selectedOption = this.listOptions[0]
  }

  ngOnInit(): void {
  }

  onAccept() {
    if (this.selectedOption=='Project') {
      this.router.navigate(['/project-form']);
    }else if (this.selectedOption=='Person') {
      this.router.navigate(['/person-form']);
    }

  }

  changeSelect(e: any) {
    this.selectedOption = e.target.value
  }
}
