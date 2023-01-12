import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {Services} from "../services/services";
import {Location} from "@angular/common";
import {DocsPorPersona} from "../models/docsPorPersona";
import {DetalleDocumento} from "../models/detalleDocumento";

@Component({
  selector: 'app-documents-list',
  templateUrl: './documents-list.component.html',
  styleUrls: ['./documents-list.component.css']
})
export class DocumentsListComponent implements OnInit {

  docsPorPersona: DocsPorPersona[] = []

  constructor(private router : Router, private route :
    ActivatedRoute, private services: Services, private _location: Location) {}

  ngOnInit(): void {
    this.getPeople()
  }

  private getPeople() {
    this.services.get_people().subscribe(people => {
      const actual_date = new Date()
      for(let i=0; i<people['personas'].length; i++){

        this.services.get_all_detalleDoc(people['personas'][i].id).subscribe(detalles => {
          var newPersona: DocsPorPersona = {
            persona: people['personas'][i],
            docs: detalles['detallesDocumento']
          };

          newPersona.persona.situacionDocumental = 2

          let n_docs = 0

          for(let j=0; j<newPersona.docs.length; j++){
            if(newPersona.docs[j].fechaExpedicion!=undefined && newPersona.docs[j].diasExpira!=undefined){
              if(newPersona.docs[j].diasExpira!=-1){
                // @ts-ignore
                const date = new Date(Date.parse(newPersona.docs[j].fechaExpedicion))
                // @ts-ignore
                date.setDate(date.getDate() + newPersona.docs[j].diasExpira)

                const date2 = new Date(date)
                date2.setDate(date2.getDate() - 5)

                if(actual_date < date2){
                  newPersona.docs[j].situacionDocumental = 2
                }else if(actual_date >= date2 && actual_date < date){
                  newPersona.docs[j].situacionDocumental = 3
                }else{
                  newPersona.docs[j].situacionDocumental = 1
                  n_docs += 1
                }

                // @ts-ignore
                newPersona.docs[j].caduca = DocumentsListComponent.formatDate(date)
              }else{
                 newPersona.docs[j].situacionDocumental = 2
              }
            }else{
              newPersona.docs[j].situacionDocumental = 1
              n_docs += 1
            }
          }

          if(n_docs <= 3 && n_docs >= 1){
            newPersona.persona.situacionDocumental = 3
          }else if(n_docs > 3){
            newPersona.persona.situacionDocumental = 1
          }
          this.docsPorPersona.push(newPersona)
        })
      }
      console.log("All people", this.docsPorPersona)
    });
  }

  expandCell(person: DocsPorPersona) {
    person.persona.expand = !person.persona.expand
  }

  edit_doc(detalle: DetalleDocumento) {
    this.router.navigate(['/documents-form', detalle.id])
  }

  delete_doc(doc: DetalleDocumento) {
    if(confirm('Estás seguro de que quieres eliminar el documento?')){
      const newDoc: DetalleDocumento = {
        id: doc.id,
        descripcionDocumento: "",
        documento: "",
        idEmpleado: doc.idEmpleado,
        idSetupDocumentoPersona: doc.idSetupDocumentoPersona,
        tipoDocumento: ""

      }
      this.services.deleteDocument(doc).subscribe(a => {
        console.log('Document deleted')
        this.services.postDocument(newDoc).subscribe(documento => {
          console.log(documento)
          window.location.reload()
        })
      })
    }
  }

  private static padTo2Digits(num: number) {
    return num.toString().padStart(2, '0');
  }

  private static formatDate(date: Date) {
    return (
      [
        date.getFullYear(),
        DocumentsListComponent.padTo2Digits(date.getMonth() + 1),
        DocumentsListComponent.padTo2Digits(date.getDate()),
      ].join('-')
    );
  }
}
