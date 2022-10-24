import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {ProjectFormComponent} from "./project-form/project-form.component";
import {PersonFormComponent} from "./person-form/person-form.component";
import {SelectionPageComponent} from "./selection-page/selection-page.component";
import {ProjectsListComponent} from "./projects-list/projects-list.component";
import {PeopleListComponent} from "./people-list/people-list.component";

const routes: Routes = [
  {path: '', component: SelectionPageComponent, pathMatch: 'full'},
  {path: 'project-form', component: ProjectFormComponent, pathMatch: 'full'},
  {path: 'person-form', component: PersonFormComponent, pathMatch: 'full'},
  {path: 'projects-list', component: ProjectsListComponent, pathMatch: 'full'},
  {path: 'people-list', component: PeopleListComponent, pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
