import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  projects_btn!: boolean;
  people_btn!: boolean;
  documents_btn!: boolean;

  constructor() { }

  ngOnInit(): void {
    const url_actual = window.location.hash

    switch (url_actual) {
      case '#/projects-list':
        this.projects_btn = true
        this.people_btn = false
        this.documents_btn = false
        break

      case '#/people-list':
        this.projects_btn = false
        this.people_btn = true
        this.documents_btn = false
        break

      case '#/documents-form':
        this.projects_btn = false
        this.people_btn = false
        this.documents_btn = true
        break

      default:
        this.projects_btn = true
        this.people_btn = true
        this.documents_btn = true
        break
    }

  }

  goHome() {
    this.projects_btn = true
    this.people_btn = true
    this.documents_btn = true
  }

  click_projects() {
    this.projects_btn = true
    this.people_btn = false
    this.documents_btn = false
  }

  click_people() {
    this.projects_btn = false
    this.people_btn = true
    this.documents_btn = false
  }

  click_documents() {
    this.projects_btn = false
    this.people_btn = false
    this.documents_btn = true
  }
}
