import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {Services} from "../services/services";
import {Location} from "@angular/common";
import {DetalleDocumento} from "../models/detalleDocumento";

@Component({
  selector: 'app-documents-form',
  templateUrl: './documents-form.component.html',
  styleUrls: ['./documents-form.component.css']
})
export class DocumentsFormComponent implements OnInit {

  date?: string;

  idDetalle: number | null = 0;
  detalle: DetalleDocumento = {
    documento: "", tipoDocumento: "", descripcionDocumento: "", idEmpleado: 0, idSetupDocumentoPersona: 0

  };
  org: string = 'ACOES HONDURAS';
  trabajador?: string;

  constructor(private router : Router, private route :
    ActivatedRoute, private services: Services, private _location: Location) {}

  ngOnInit(): void {
    this.idDetalle = (this.route.snapshot.paramMap.get('idDetalle') as number|null)
    this.getDetalle()
    this.date = DocumentsFormComponent.formatDate(new Date())
  }

  onCancel() {
    this.router.navigate(['/documents-list'])
  }

  onAccept() {
    const date = new Date()
    this.detalle.fechaHoraCarga = DocumentsFormComponent.formatDateTime(date)

    this.services.putDocument(this.detalle).subscribe(detalle => {
      console.log("Put DetalleDocumento:", detalle)
    })
    this.router.navigate(['/documents-list'])
  }

  private getDetalle() {
    if(this.idDetalle != undefined){
      this.services.get_detalleDoc(this.idDetalle).subscribe(detalle => {
        this.detalle = detalle['detalleDocumento']
        console.log('DetalleDocumento:', this.detalle)
        this.services.get_person(this.detalle.idEmpleado).subscribe(persona => {
          this.trabajador = persona['persona'].primerNombre + ' ' + persona['persona'].segundoNombre + ' '
            + persona['persona'].primerApellido + ' ' + persona['persona'].segundoApellido
        })
      })
    }
  }

  private static padTo2Digits(num: number) {
    return num.toString().padStart(2, '0');
  }

  private static formatDateTime(date: Date) {
    return (
      [
        date.getFullYear(),
        DocumentsFormComponent.padTo2Digits(date.getMonth() + 1),
        DocumentsFormComponent.padTo2Digits(date.getDate()),
      ].join('-') +
      ' ' +
      [
        DocumentsFormComponent.padTo2Digits(date.getHours()),
        DocumentsFormComponent.padTo2Digits(date.getMinutes()),
        DocumentsFormComponent.padTo2Digits(date.getSeconds()),
      ].join(':')
    );
  }

  private static formatDate(date: Date) {
    return (
      [
        date.getFullYear(),
        DocumentsFormComponent.padTo2Digits(date.getMonth() + 1),
        DocumentsFormComponent.padTo2Digits(date.getDate()),
      ].join('-')
    );
  }

  onFileSelected(event: Event) {
    if(event != undefined){
      const target = event.target as HTMLInputElement;
      if (target.files && target.files.length > 0) {
        this.detalle.nombreAdjuntoOriginal = target.files[0].name
        this.detalle.pathDestinoAdjunto = target.value
      }
    }
  }
}
