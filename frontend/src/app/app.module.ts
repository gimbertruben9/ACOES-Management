import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {MatToolbarModule} from '@angular/material/toolbar';

import {HttpClientModule} from '@angular/common/http'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProjectFormComponent } from './project-form/project-form.component';
import { PersonFormComponent } from './person-form/person-form.component';
import { SelectionPageComponent } from './selection-page/selection-page.component';

import {MatRadioModule} from "@angular/material/radio";
import {MatButtonToggleModule} from "@angular/material/button-toggle";
import {MatFormFieldModule} from "@angular/material/form-field";
import {MatSelectModule} from "@angular/material/select";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import { ProjectsListComponent } from './projects-list/projects-list.component';
import { PeopleListComponent } from './people-list/people-list.component';
import { NavbarComponent } from './navbar/navbar.component';
import {MatButtonModule} from "@angular/material/button";
import {MatIconModule} from "@angular/material/icon";

@NgModule({
  declarations: [
    AppComponent,
    ProjectFormComponent,
    PersonFormComponent,
    SelectionPageComponent,
    ProjectsListComponent,
    PeopleListComponent,
    NavbarComponent,
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
    MatIconModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
