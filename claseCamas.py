class Camas:
    __idCama = int,
    __habitacion = str,
    __estado = bool,
    __apellidoNombre = str,
    __diag = str,
    __fechaInternacion = str,
    __fechaAlta = str

    def __init__ (self, idCama=None, habitacion=None, estado=None, apNom=None, diag=None, fechaInt=None, fechaAlta=None):
        self.__idCama = idCama
        self.__habitacion = habitacion
        self.__estado = estado
        self.__apellidoNombre = apNom
        self.__diag = diag
        self.__fechaInternacion = fechaInt
        self.__fechaAlta = fechaAlta

    def __repr__(self):
        return str(self.__dict__)

    def getNyA (self):
        return self.__apellidoNombre
    
    def getIdCama (self):
        return self.__idCama

    def getHabitacion (self):
        return self.__habitacion
    
    def getEstado (self):
        return self.__estado
    
    def getDiagnostico (self):
        return self.__diag

    def getFechaInternacion (self):
        return self.__fechaInternacion

    def getFechaAlta (self):
        return self.__fechaAlta

    def mostrarDatos(self, i):
        return
        

