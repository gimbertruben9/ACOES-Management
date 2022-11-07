import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {MatToolbarModule} from '@angular/material/toolbar';

import {HttpClientModule} from '@angular/common/http'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProjectFormComponent, AdminFormComponent } from './project-form/project-form.component';
import { PersonFormComponent } from './person-form/person-form.component';
import { HomePageComponent } from './home-page/home-page.component';

import {MatRadioModule} from "@angular/material/radio";
import {MatButtonToggleModule} from "@angular/material/button-toggle";
import {MatFormFieldModule} from "@angular/material/form-field";
import {MatSelectModule} from "@angular/material/select";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {ProjectsListComponent} from './projects-list/projects-list.component';
import {EditPersonDialog, PeopleListComponent} from './people-list/people-list.component';
import { NavbarComponent } from './navbar/navbar.component';
import {MatButtonModule} from "@angular/material/button";
import {MatIconModule} from "@angular/material/icon";
import {MatDialogModule} from "@angular/material/dialog";
import {MatInputModule} from "@angular/material/input";
import { BrowserAnimationsModule} from "@angular/platform-browser/animations";
import { DocumentsListComponent } from './documents-list/documents-list.component';

@NgModule({
  declarations: [
    AppComponent,
    ProjectFormComponent,
    PersonFormComponent,
    HomePageComponent,
    ProjectsListComponent,
    PeopleListComponent,
    NavbarComponent,
    EditPersonDialog,
    DocumentsListComponent,
    AdminFormComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    MatToolbarModule,
    MatRadioModule,
    MatButtonToggleModule,
    MatFormFieldModule,
    MatSelectModule,
    FormsModule,
    ReactiveFormsModule,
    MatButtonModule,
    MatIconModule,
    MatDialogModule,
    MatInputModule,
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
