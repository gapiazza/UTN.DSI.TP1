from main import *

class ControladorConsultaEncuesta:
    def consultarEncuesta(self, fechaHoraInicio, fechaHoraFin, llamadaSeleccionada, formatoSeleccionado, main):
       self.fechaHoraInicio = fechaHoraInicio
       self.fechaHoraFin = fechaHoraFin
       self.llamadasEnPeriodoRespondidas = []
       self.llamadaSeleccionada = llamadaSeleccionada
       self.formatoSeleccionado = formatoSeleccionado
       self.llamadas = []
       self.datosLlamada = {"Nombre de Cliente":""}

    def tomarSeleccionFechaInicio(self, fecha):
        self.fechaHoraInicio = fecha

    def tomarSeleccionFechaFin(self, fecha):
        self.fechaHoraFin = fecha

    def buscarLlamadasRespondidas(self):
        if len(llamadas) > 0:
            for unaLlamada in self.llamadas:
                if (unaLlamada.esDePeriodo(self.fechaHoraInicio, self.fechaHoraFin) and unaLlamada.tieneEncuestaRespondida()):
                    self.llamadasEnPeriodoRespondidas.append(unaLlamada)
                
    def agregarLlamadaEnPeriodo(self, llamada_en_periodo):
        self.llamada_en_periodo.append(llamada_en_periodo)

    def tomarSeleccionLlamada(self, llamadaSeleccionada):
        self.llamadaSeleccionada = llamadaSeleccionada
"""
    def obtenerDatosLlamada(self):
        nombreCliente = self.llamadaSeleccionada.getNombreClienteLlamada()
        self.datosLlamada["Nombre de Cliente"] = nombreCliente
        ultimoEstado = self.llamadaSeleccionada.determinarUltimoEstado()
"""

    def obtenerDatosLlamada(self):
        self.datosLlamada = self.llamadaSeleccionada.mostrarDatosLlamada()