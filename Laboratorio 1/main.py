from Trig import *
import datetime as dt
import os as os

Trigonometria = Trig() #instancia de la clase trig
opcionMenu = 0         #opcion del menu principal a elegir

#funcion para imprimir el seno de pi
def imprimeSeno(texto):
    resultado = 'El valor del seno de PI es: ' + texto
    return resultado

#funcion para imprimir el coseno de pi
def imprimeCoseno(texto):
    resultado = 'El valor del coseno de PI es: ' + texto
    return resultado

#funcion para imprimir la tangente de pi
def imprimeTangente(texto):
    resultado = 'El valor de la tangente de PI es: ' + texto
    return resultado

#funcion para generar el log dentro del archivo, en caso que no exista el archivo lo genera
def generarLog(textolog):
    ahora = str(dt.datetime.now())
    try:
        archivo = open('log.txt','x')
        archivo.write(textolog + ' || fecha del registro del log: ' + ahora)
        archivo.write('\n')
        archivo.close()
    except:
        with open('log.txt','a') as archivo:
            archivo.write(textolog + ' || fecha del registro del log: ' + ahora)
            archivo.write('\n')
            archivo.close()
    print('Log generado en el archivo....')


#CODIGO PRINCIPAL DE EJECUCCION
while(opcionMenu != 4):
    os.system('cls')
    print('----------------------------------------')
    print('         Menu principal')
    print('----------------------------------------')
    print('1.Consultar el seno de PI')
    print('2.Consultar el coseno de PI')
    print('3.Consultar la tangente de PI')
    print('4.Salir del programa')
    try:
        opcionMenu = int(input('Digite el numero de la opcion que desea realizar: '))
    except:
        opcionMenu = 0

    match(opcionMenu):
        case 1:
            print(imprimeSeno(str(Trigonometria.obtenerSin())))
            generarLog(imprimeSeno(str(Trigonometria.obtenerSin())))
            input('Digite Enter para continuar...')
        case 2:
            print(imprimeCoseno(str(Trigonometria.obtenerCos())))
            generarLog(imprimeCoseno(str(Trigonometria.obtenerCos())))
            input('Digite Enter para continuar...')
        case 3:
            print(imprimeTangente(str(Trigonometria.obtenerTan())))
            generarLog(imprimeTangente(str(Trigonometria.obtenerTan())))
            input('Digite Enter para continuar...')
        case 4:
            print('Gracias por utilizar el programa! Hasta pronto!..')
            input('Digite Enter para salir...')
        case _:
            print('ERROR: La opcion elegida no es valida, debe digitar un numero entre 1,2,3,4..')
    