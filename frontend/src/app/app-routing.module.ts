import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {AdminFormComponent, ProjectFormComponent} from "./project-form/project-form.component";
import {PersonFormComponent} from "./person-form/person-form.component";
import {HomePageComponent} from "./home-page/home-page.component";
import {ProjectsListComponent} from "./projects-list/projects-list.component";
import {PeopleListComponent} from "./people-list/people-list.component";
import {DocumentsListComponent} from "./documents-list/documents-list.component";
import {DocumentsFormComponent} from "./documents-form/documents-form.component";

const routes: Routes = [
  {path: '', component: HomePageComponent, pathMatch: 'full'},
  {path: 'project-form', component: ProjectFormComponent, pathMatch: 'full'},
  {path: 'admin-form/:projectId', component: AdminFormComponent, pathMatch: 'full'},
  {path: 'person-form', component: PersonFormComponent, pathMatch: 'full'},
  {path: 'projects-list', component: ProjectsListComponent, pathMatch: 'full'},
  {path: 'people-list', component: PeopleListComponent, pathMatch: 'full'},
  {path: 'documents-list', component: DocumentsListComponent, pathMatch: 'full'},
  {path: 'documents-form', component: DocumentsFormComponent, pathMatch: 'full'},
  {path: '**', redirectTo: '', pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {useHash: true})],
  exports: [RouterModule]
})
export class AppRoutingModule { }
