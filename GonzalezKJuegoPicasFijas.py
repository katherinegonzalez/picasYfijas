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

# Variables de entrada: (str) salir
# pre-condiciones: salir != 'si'
#
# Variables auxiliares: (lista) listaNumSecreto, (lista) listaNumIntento, (int) cantidadDeIntentos,
#                       (int) cantidadDeIntentos, (int) numFijas, (int) numPicas
# pre-condiciones: numFijas != '4'
#
# Explicación: salir es una variable para que el usuario decida si desea finalizar el programa,
#              listaNumSecreto, guarda el número secreto generado por el programa
#              listaNumIntento, guarda los numeros que el usuario ingresó
#              cantidadDeIntentos, cuenta las veces que el usuario intentó adivinar el número secreto
#              numFijas, guarda el número de fijas que calculó el programa, si es 4 el usuario gana.
#              numPicas, guarda el número de picas que calculó el programa
#
# ----------------------------------------------------------------------------------------
# POSTCONDICIONES
# ----------------------------------------------------------------------------------------
# Salida: Mensaje (str) informando el número de picas y fijas
#
# Si numFijas es igual a 4, mostrar mensaje en pantall diciendo que el usuario ganó
# Si salir == 'si' , fin del programa.
# Si salir == 'no' , Se ejecuta nuevamente el juego

# ----------------------------------------------------------------------------------------

def programaEjecutable ():
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
    programaEjecutable()
    salir = validarFinalizarInput('Si desea Finalizar el juego escriba si, de lo contrario, si quiere volver a jugar, escriba no: ')

