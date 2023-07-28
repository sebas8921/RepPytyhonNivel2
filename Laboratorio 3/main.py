import api
import os

opcionMenu = 0  #opcion a elegir del menu

while opcionMenu != 4:
    os.system('cls')
    print('---------------------------------------------------------------------')
    print('MENU PRINCIPAL')
    print('Las bromas de Chuck norris (En ingles XD )')
    print('---------------------------------------------------------------------')
    print('1. Obtener una broma aleatoria')
    print('2. Ver la lista de cateorias disponibles')
    print('3. Obtener una broma de una categoria especifica')
    print('4. Salir del programa')
    opcionMenu = int(input('Digite el numero de la opcion del menu que desea realizar: \n'))
    match opcionMenu:
        case 1:
            os.system('cls')
            print('Broma generada de forma aleatoria')
            print('---------------------------------------------------------------------')
            print(api.getBromaAleatoria())
            input('Digite ENTER para continuar...')
        case 2:
            os.system('cls')
            print('Lista de categorias disponibles')
            print('---------------------------------------------------------------------')
            listaCategorias = api.getCategorias()
            for categoria in listaCategorias:
                print(categoria)
            input('Digite ENTER para continuar...')
        case 3:
            categoria = str(input('Digite la categoria de la cual desea obtener la broma: ')) 
            print('Broma para la categoria '+ categoria)
            print('---------------------------------------------------------------------')
            print(api.getCategoriaEspecifica(categoria))
            input('Digite ENTER para continuar...')
        case 4:
            print("Gracias por utilizar el programa, Hasta pronto!!")
        case _:
            print("ERROR: La opcion que elegio del menu es incorrecta....")




