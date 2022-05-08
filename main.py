from claseManejadorCamas import manejadorCamas
from claseManejadorMedicamentos import manejadorMedicamentos

def main():
    print ('Main')
    listaCamas = manejadorCamas()
    listaCamas.cargaCamas()
    listaMedicamentos = manejadorMedicamentos()
    listaMedicamentos.cargaMedicamentos()
    nombre = input ('ingrese apellido y nombre para dar de alta: ')
    index = listaCamas.getIndice(nombre)
    listaMedicamentos.buscarCama(index)



if __name__ == '__main__':
    main()