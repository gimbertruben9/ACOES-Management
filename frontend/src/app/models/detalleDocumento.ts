export interface DetalleDocumento {
  id?: number;
  idSetupDocumentoPersona: number;
  idEmpleado: number;
  fechaHoraCarga?: string;
  fechaExpedicion?: string;
  comentario?: string;
  pathDestinoAdjunto?: string;
  nombreAdjuntoOriginal?: string;
  documento: string;
  descripcionDocumento: string;
  tipoDocumento: string;
  diasExpira?: number;
  caduca?: string;
  situacionDocumental?: number;
}
