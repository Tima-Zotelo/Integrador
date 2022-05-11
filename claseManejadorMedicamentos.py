import csv
from claseMedicamentos import Medicamentos

class manejadorMedicamentos:
    def __init__ (self):
        self.__listaMedicamentos = []

    def cargaMedicamentos (self):
        file = open ('medicamentos.csv')
        reader = csv.reader(file, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                idCama = fila[0]
                idMedicamento = fila [1]
                nombreComercial = fila [2]
                monoDroga = fila [3]
                presentacion = fila [4]
                cantidadAplicada = fila [5]
                precioTotal = fila [6]
                medicamentoNuevo = Medicamentos(idCama, idMedicamento, nombreComercial, monoDroga, presentacion, cantidadAplicada, precioTotal)
                self.__listaMedicamentos.append(medicamentoNuevo)
        file.close()
        return self.__listaMedicamentos

    def buscarCama (self, index):
        total = 0
        print (f"Medicamento/Monodroga:      Presentación:       cantidad:              Precio:")
        for i in range (len(self.__listaMedicamentos)):
            if (index == self.__listaMedicamentos[i].getIdCama()):
                print (f'{self.__listaMedicamentos[i].getNombreComercial()} / {self.__listaMedicamentos[i].getMonoDroga()}      {self.__listaMedicamentos[i].getPresentacion()}             {self.__listaMedicamentos[i].getCantidadAplicada()}                     ${self.__listaMedicamentos[i].getPrecioTotal()}')
                total = total + self.__listaMedicamentos[i].getPrecioTotal()
        print (f"\ntotal adeudado:                                                        ${total}")

