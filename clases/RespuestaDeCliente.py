class RespuestaDeCliente:
    def __init__(self, fechaEncuesta, respuestaSeleccionada):
        self.fechaEncuesta = fechaEncuesta
        self.respuestaSeleccionada = respuestaSeleccionada
    
    def getDescripcionRta(self):
        return self.respuestaSeleccionada.getDescripcionRta()

    def obtenerEncuesta(self):
        pass

    def getRespuesta(self):
        return self
    