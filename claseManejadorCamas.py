# -*- coding: utf-8 -*-
import csv
from datetime import datetime
from claseCamas import Camas

class manejadorCamas:
    def __init__(self):
        self.__listaCama = []


    def cargaCamas (self):
        file = open ('camas.csv')
        reader = csv.reader(file, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                idCama = fila[0]
                habitacion = fila [1]
                estado = fila [2]
                apNom = fila [3]
                diag = fila [4]
                fechaInt = fila [5]
                fechaAlta = fila [6]
                camaNueva = Camas(idCama, habitacion, estado, apNom, diag, fechaInt, fechaAlta)
                self.__listaCama.append(camaNueva)
        file.close()
        return self.__listaCama

    def getIndice (self, nomPac):
        for i in range(len(self.__listaCama)):
            if (nomPac == self.__listaCama[i].getNyA()):
                fecha = datetime.now().strftime('%Y-%m-%d %H:%M')
                self.__listaCama[i]._Camas__fechaAlta = fecha
                print (f"""
Paciente: {self.__listaCama[i].getNyA()}    Cama: {self.__listaCama[i].getIdCama()}     Habitacion: {self.__listaCama[i].getHabitacion()}
Diagnostico: {self.__listaCama[i].getDiagnostico()}         Fecha de internacion: {self.__listaCama[i].getFechaInternacion()}
Fecha de Alta {self.__listaCama[i].getFechaAlta()}
""")
                return self.__listaCama[i].getIdCama()
