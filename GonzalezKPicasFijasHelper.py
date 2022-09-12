from random import randint

def validarFinalizarInput (mensaje):
    seguirPreguntando = True
    while seguirPreguntando:
        finalizar = input(mensaje)
        seguirPreguntando = not (finalizar == 'si' or finalizar == 'no')
    return finalizar

def validarNumeroSecreto (lista):
    seguirgenerandoNum = True
    while seguirgenerandoNum:
        numero = randint(0, 9)
        if numero not in lista:
            seguirgenerandoNum = False
    return numero

def validarInput (mensaje, lista):
    seguirPreguntando = True
    while seguirPreguntando:
        numeroIngresado = input(mensaje)
        if (numeroIngresado.isdigit() and int(numeroIngresado) < 10 and int(numeroIngresado) not in lista):
            seguirPreguntando = False
        else:
            print('El valor ingresado no es válido')
    return int(numeroIngresado)

def numSecreto():
    numeroSecreto = []
    for i in range(4):
        num = validarNumeroSecreto(numeroSecreto)
        print(num)
        numeroSecreto.append(num)
    return numeroSecreto

def numIntento():
    print('Ingrese uno a uno los 4 dígitos que usted crea que son el número secreto (deben ser enteros del 0 al 9): ')
    numerosIntento = []
    for i in range(4):
        num = validarInput('Ingrese número ' +str(i+1)+ ': ', numerosIntento)
        numerosIntento.append(num)
    return numerosIntento

def picas(listaNumSecreto, listaNumIntento):
    numeroPicas = 0
    for i in range(len(listaNumSecreto)):
        if (listaNumIntento[i] in listaNumSecreto):
            indexNumSecreto = listaNumSecreto.index(listaNumIntento[i])
            if (indexNumSecreto != i):
                numeroPicas+=1
    return numeroPicas

def fijas (listaNumSecreto, listaNumIntento):
    numeroFijas = 0
    for i in range(0, len(listaNumSecreto)):
        if(listaNumSecreto[i] == listaNumIntento[i]):
            numeroFijas+=1
    return numeroFijas





