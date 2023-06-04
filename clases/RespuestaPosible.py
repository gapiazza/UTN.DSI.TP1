class RespuestaPosible:
    def __init__(self, descripcion, valor):
        self.descripcion = descripcion
        self.valor = valor

    def getRespuesta(self):
        return self

    def getDescripcionRta(self):
        return self.descripcion

