from re import S


class Medicamentos:
   
    __idCama = int,
    __idMedicamento = int,
    __nomComercial = str,
    __monoDroga = str,
    __presentacion = str,
    __cantAplicada = int,
    __precioTotal = float

    def __init__ (self, idCama=None, idMedicamento=None, nomComercial=None, monoDroga=None, present=None, cantAplicada=None, precioTotal=None):
        self.__idCama = idCama
        self.__idMedicamento = idMedicamento
        self.__nomComercial = nomComercial
        self.__monoDroga = monoDroga
        self.__presentacion = present
        self.__cantAplicada = cantAplicada
        self.__precioTotal = precioTotal

    def __repr__(self):
        return str(self.__dict__)

    def getIdCama (self):
        return self.__idCama

    def getIdMedicamento (self):
        return self.__idMedicamento

    def getNombreComercial (self):
        return self.__nomComercial

    def getMonoDroga (self):
        return self.__monoDroga

    def getPresentacion (self):
        return self.__presentacion
    
    def getCantidadAplicada (self):
        return self.__cantAplicada
    
    def getPrecioTotal (self):
        return self.__precioTotal