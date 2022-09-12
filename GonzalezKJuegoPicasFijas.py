# ----------------------------------------------------------------------------------------
# PROGRAMA: Juego de Picas y Fijas
# ----------------------------------------------------------------------------------------
# Descripción: Este programa permite jugar el Juego de Picas y Fijas contra el computador,
# el computador genera un número aleatorio de 4 dígitos, y el usuario tendrá que adivinarlo
# para poder ganar.

# ----------------------------------------------------------------------------------------
# Autor: Katherine Xiomar González Santacruz
# Version: 1.0
# [12.09.2022]
# ----------------------------------------------------------------------------------------
# IMPORTAR MODULOS
from GonzalezKPicasFijasHelper import *
# ----------------------------------------------------------------------------------------
# VARIABLES GLOBALES Y PRE-CONDICIONES
# ----------------------------------------------------------------------------------------

# Variables de entrada: (str) opcionIngresada
# pre-condiciones: opcionIngresada debe ser '1', '2', '3', '4', ó '0'
#                  salir != 'si'

# Variables auxiliares: (str) opcion
#                       opcion != '0'
#
# Explicación: opción es una variable auxiliar que guarda la opción ingresada por el usuario,
#              y se encarga de detener el ciclo cuando la opció seleccionada es '0'.
#              Si opcion es '0', el programa dejará de ejecutarse.
#              Si opcionIngresada es '1', se ejecuta la función digitosPorDerecha() del módulo importado
#              Si opcionIngresada es '2', se ejecuta la función digitosPorIzquierda() del módulo importado
#              Si opcionIngresada es '3', se ejecuta la función multiplicacionRusa() del módulo importado
#              Si opcionIngresada es '4', se ejecuta la función maxCD() del módulo importado
#              Si opcionIngresada es '0', se detiene el programa.
#
# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------
# Salida: Mensaje (str) informando los resultados de los cálculos realziados de acuerdo a
# la selección del usuario.

# Si opcionIngresada es un valor diferente de '0', '1', '2', '3' ó '4' mostrar un mensaje
# en pantalla, y solicitar el valor nuevamente.
# Si opcion == '0' , fin del programa.

# ----------------------------------------------------------------------------------------

def programa ():
    print('Bienvenido al juego Picas y Fijas')
    print('\n')
    print('He generado un número secreto de 4 dígitos, '
          'el cuál tendrás que adivinar para poder ganar.')
    print('\n')
    print('Número Secreto: [* * * *]')
    print('\n')
    listaNumSecreto = numSecreto()
    cantidadDeIntentos = 0
    numFijas = 0
    while (numFijas != 4):
        listaNumIntento = numIntento()
        cantidadDeIntentos +=1
        print('Los números de sus intento son: ', listaNumIntento)

        numFijas = fijas(listaNumSecreto, listaNumIntento)
        numPicas = picas(listaNumSecreto, listaNumIntento)
        print('El número de fijas es: ', numFijas)
        print('El número de picas es: ', numPicas)
        print('\n')

        if (numFijas == 4):
            print('!Has ganado! ¡Has adivinado el número secreto!')
            print('Número de intentos realizado: ', cantidadDeIntentos)
            print('El número secreto era: ', listaNumSecreto)
        else:
            print('¡Intenta nuevamente con otros números!')

salir = 'no'

while (salir != 'si'):
    print('\n')
    programa()
    salir = validarFinalizarInput('Si desea Finalizar el juego escriba si, de lo contrario, si quiere volver a jugar, escriba no: ')

