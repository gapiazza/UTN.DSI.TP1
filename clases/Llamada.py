class Llamada:
    def __init__(self, descripcionOperador, detalleSccionRequerida, duracion, encuestaEnviada, ObservacionAuditor, cliente):
        self.descripcionOperador = descripcionOperador
        self.detalleSccionRequerida = detalleSccionRequerida
        self.duracion = duracion
        self.encuestaEnviada = encuestaEnviada
        self.ObservacionAuditor = ObservacionAuditor
        # Este es un atributo referencial (cambioEstado va a ser una lista, ya que, la relación es un o muchos (? )
        self.cambios_estado = []
        self.respuestasDeEncuesta = []
        self.cliente = cliente

    def agregarCambioEstado(self, cambio_estado):
        self.cambios_estado.append(cambio_estado)
        
    def agregarRespuestaDeEncuesta(self, respuestaEncuesta):
        self.respuestasDeEncuesta.append(respuestaEncuesta)

    def esDePeriodo(self, fecha_inicio, fecha_fin):
        for cambio_estado in self.cambios_estado:
            if cambio_estado.esEstadoInicial():
                fecha_hora_inicio = cambio_estado.getFechaHoraInicio()
                if fecha_inicio <= fecha_hora_inicio <= fecha_fin:
                    return True
        return False
    
    def tieneEncuestaRespondida(self):
        if len(self.respuestasDeEncuesta) > 0:
            return True


    def getDuracion(self):
        return self.duracion

    def tieneRespuesta():
        pass

    def determinarUltimoEstado():
        pass

    def getNombreClienteLlamada(self):
        return self.cliente.getNombre()
    
    def determinarUltimoEstado(self):
        cambioEstadoActual = self.cambios_estado[0]
        for cambioEstado in self.cambios_estado:
            cambioEstadoActual = cambioEstado.esUltimoCambioEstado(cambioEstadoActual)
        return cambioEstadoActual.getNombreEstado()
    
    def getRespuestas(self):
        for unaRespuesta in self.respuestasDeEncuesta:
            unaRespuesta.getDescripcionRta()


    def mostrarDatosLlamada(self):
        nombreCliente = self.getNombreClienteLlamada()
        ultimoEstado = self.determinarUltimoEstado()
        duracion = self.duracion
        respuestas = self.getRespuestas()
        return {}




# A llenar despues 
listaLlamadas = []