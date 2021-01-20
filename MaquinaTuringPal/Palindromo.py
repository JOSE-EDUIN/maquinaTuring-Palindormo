import string
import sys
from MaquinaT import Maquina_Turing

def mT_palindromo(inicial_string):
        
    # Definir el conjunto de caracteres (caracteres permitidos para el palíndromo)
    caracter_list = list(string.ascii_lowercase)
    caracter_list.append(' ') # para permitir espacios

    # String Inicial
    print('Comprobacion: ' + inicial_string)
    print('- - -')
    inicial_list = list(inicial_string)

    # Comprobación rápida de que solo utilizó caracteres permitidos
    for i in inicial_list:
        if i not in caracter_list:
            print('Error! Caracter inicial >',i,'< no esta en la lista de caracteres permitidos!')
            sys.exit()

    # Añadir a la lista
    inicial_list.append(0)

    # Configurar la máquina de turing
    i_cabezal = 0
    i_estado = 'q1' # initial state
    i_cinta_list = inicial_list

    # Iniciar la clase 
    runMaquina = Maquina_Turing(i_estado,i_cabezal,i_cinta_list)
    print(runMaquina.getEstado(),runMaquina.getCabezal(),runMaquina.getLista())

    # Correr la lista
    ctr=0
    while runMaquina.getEstado() != 'qy' and runMaquina.getEstado() != 'qn' and ctr < 1000:
        runMaquina.actualizarMaquina(caracter_list)
        print(runMaquina.getEstado(),runMaquina.getCabezal(),runMaquina.getLista())
        ctr += 1
    print('- - -')

    # Resultado de aceptación
    if (runMaquina.getEstado() == 'qy'):
        print(inicial_string,'**Es un palíndromo** Pasos:',ctr)
    else:
        print(inicial_string,'**No es un palíndromo** Pasos:',ctr)