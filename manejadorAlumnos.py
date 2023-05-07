import csv
import numpy as np
from alumnos import Alumnos

class manejadorAlumnos:
    __cantidad = 0
    __dimension = 0 ## tamaño
    __incremento = 5

    def __init__(self, dimension, incremento=5):
        self.__alumnos = np.empty(dimension, dtype=Alumnos)
        self.__cantidad = 0
        self.__dimension = dimension

    def __str__(self):
        s = ""
        for i in range (len(self.__alumnos)):
            s += f'holaaa, {self.__alumnos[i].getNombre()}'
            #s += str(self.__alumnos[i].getDni()) + ',' + str(self.__alumnos[i].getApellido()) + ',' + str(self.__alumnos[i].getNombre()) + ',' + str(self.__alumnos[i].getAño()) + '\n'
        return s

    def getAlumno (self, indice):
        return self.__alumnos[indice]

    def agregarAlumno(self, a):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__alumnos.resize(self.__dimension)
        self.__alumnos[self.__cantidad]=a
        self.__cantidad += 1

    def carga (self):
        path = './alumnos.csv'
        archivo = open(path, 'r')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                dni = int (fila[0])
                apellido = fila[1]
                nombre = fila[2]
                carrera = fila[3]
                anho = int(fila[4])
                xAlumno = Alumnos (dni, apellido, nombre, carrera, anho)
                self.agregarAlumno(xAlumno)
        print ('carga de alumnos lista')
        archivo.close()

    def buscarDni(self,d):
        valorRetorno=None
        bandera=False
        indice=0
        while (indice<len(self.__alumnos) and not bandera):
            if (d == self.__alumnos[indice].getDni()):
                valorRetorno=indice
                bandera=True
            else:
                indice+=1
        return valorRetorno

