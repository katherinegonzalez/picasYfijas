# ----------------------------------------------------------------------------------------
# MODULO: Picas y Fijas Helper
# ----------------------------------------------------------------------------------------
# Descripción: En este módulo se encuentran las funciones para poder implementar el juego de
# picas y fijas.
# ----------------------------------------------------------------------------------------
# Autor: Katherine Xiomar González Santacruz
# Version: 1.0
# [12.09.2022]
# ----------------------------------------------------------------------------------------
# IMPORTAR MÓDULOS
from random import randint
# ----------------------------------------------------------------------------------------
# FUNCIÓN: validarFinalizarInput
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para validar el valor ingresado por el usuario para
# finalizar el programa
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (str) mensaje
#       variable auxiliar: (bool) seguirPreguntando
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si seguir preguntando es false, el ciclo se rompe y se retorna el valor ingresado
#           por el usuario.
#           Si la condición no se cumple continua preguntando
#       Valor de retorno: (str) finalizar
# ----------------------------------------------------------------------------------------
def validarFinalizarInput (mensaje):
    seguirPreguntando = True
    while seguirPreguntando:
        finalizar = input(mensaje)
        seguirPreguntando = not (finalizar == 'si' or finalizar == 'no')
    return finalizar

# ----------------------------------------------------------------------------------------
# FUNCIÓN: validarNumeroSecreto
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para generar y validar cada uno de los números secretos,
# que sea un valor aleatorio, y que no se repita dentro de la lista de los 4 números secretos
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (lista) lista (lista de número secreto)
#       variable auxiliar: (bool) seguirgenerandoNum
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si seguirgenerandoNum es false, el ciclo se rompe y se retorna el número random
#           generado
#           Si la condición no se cumple vuelve a generar y a validar otro número aleatorio
#       Valor de retorno: (str) numero
# ----------------------------------------------------------------------------------------
def validarNumeroSecreto (lista):
    seguirgenerandoNum = True
    while seguirgenerandoNum:
        numero = randint(0, 9)
        if numero not in lista:
            seguirgenerandoNum = False
    return numero

# ----------------------------------------------------------------------------------------
# FUNCIÓN: validarInput
# ----------------------------------------------------------------------------------------
# Descripción: función auxiliar para validar uno a uno los números ingresados por el usuario,
# que no se repitan en la lista, que sea un número entero positivo, y que sea menor a 10.
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (lista) lista (lista de números ingresados)
#       variable auxiliar: (bool) seguirPreguntando
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si seguirPreguntando es false, el ciclo se rompe y se retorna el número ingresado
#           por el usuario.
#           Si la condición no se cumple se muestra un mensaje y se vuelve a pedir el número
#       Valor de retorno: (int) numeroIngresado
# ----------------------------------------------------------------------------------------
def validarInput (mensaje, lista):
    seguirPreguntando = True
    while seguirPreguntando:
        numeroIngresado = input(mensaje)
        if (numeroIngresado.isdigit() and int(numeroIngresado) < 10 and int(numeroIngresado) not in lista):
            seguirPreguntando = False
        else:
            print('El valor ingresado no es válido')
    return int(numeroIngresado)

# ----------------------------------------------------------------------------------------
# FUNCIÓN: numSecreto
# ----------------------------------------------------------------------------------------
# Descripción: función para generar una lista con 4 números aleatorios del 0 al 9 que no se repitan
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       (list) numeroSecreto
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           se retorna una lista con 4 números aleatorios
#       Valor de retorno: (lista) numeroSecreto
# ----------------------------------------------------------------------------------------
def numSecreto():
    numeroSecreto = []
    for i in range(4):
        num = validarNumeroSecreto(numeroSecreto)
        numeroSecreto.append(num)
    return numeroSecreto

# ----------------------------------------------------------------------------------------
# FUNCIÓN: numIntento
# ----------------------------------------------------------------------------------------
# Descripción: función para solicitar al usuario 4 números del 0 al 9 que no se repitan.
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       (list) numerosIntento, (int) num
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           se retorna una lista con 4 números ingresados por el usuario
#       Valor de retorno: (lista) numerosIntento
# ----------------------------------------------------------------------------------------
def numIntento():
    print('Ingrese uno a uno los 4 dígitos que usted crea que son el número secreto (deben ser enteros del 0 al 9): ')
    numerosIntento = []
    for i in range(4):
        num = validarInput('Ingrese número ' +str(i+1)+ ': ', numerosIntento)
        numerosIntento.append(num)
    return numerosIntento

# ----------------------------------------------------------------------------------------
# FUNCIÓN: picas
# ----------------------------------------------------------------------------------------
# Descripción: función para calcular el número de picas (números en la lista del número
# secreto, pero en diferente posición) que obtuvo el usuario.
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (lista) listaNumSecreto, (lista) listaNumIntento
#       variable auxiliar: (int) numeroPicas
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si alguno de los números en la listaNumIntento está en la listNumSecreto pero
#           tiene diferente psición, sumar a numeroPicas.
#       Valor de retorno: (int) numeroPicas
# ----------------------------------------------------------------------------------------
def picas(listaNumSecreto, listaNumIntento):
    numeroPicas = 0
    for i in range(len(listaNumSecreto)):
        if (listaNumIntento[i] in listaNumSecreto):
            indexNumSecreto = listaNumSecreto.index(listaNumIntento[i])
            if (indexNumSecreto != i):
                numeroPicas+=1
    return numeroPicas

# ----------------------------------------------------------------------------------------
# FUNCIÓN: fijas
# ----------------------------------------------------------------------------------------
# Descripción: función para calcular el número de fijas (números en la lista del número
# secreto en la misma posición) que obtuvo el usuario.
# ----------------------------------------------------------------------------------------
# PARÁMETROS & PRE-CONDICIONES
#       Variables de entrada: (lista) listaNumSecreto, (lista) listaNumIntento
#       variable auxiliar: (int) numeroFijas
# ----------------------------------------------------------------------------------------
# VALOR DE RETORNO & POSTCONDICIONES
#       PostCondiciones:
#           Si un item de listaNumSecreto y listaNumIntento son iguales y están en la misma
#           posición, sumar a numeroFijas
#       Valor de retorno: (int) numeroFijas
# ----------------------------------------------------------------------------------------
def fijas (listaNumSecreto, listaNumIntento):
    numeroFijas = 0
    for i in range(0, len(listaNumSecreto)):
        if(listaNumSecreto[i] == listaNumIntento[i]):
            numeroFijas+=1
    return numeroFijas





