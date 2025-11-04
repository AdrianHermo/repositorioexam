# Aplicacion para lista de compras

# Opciones, engadir producto, eliminar producto, amosar lista, sair.

list_compra = ['Limones', 'Naranjas', 'Queso', 'Pavo']

# engadir produto


def añadir_elemento(lista):
    elemento = input('Engadir elemento: ')
    lista.append(elemento)
    print(lista)

# eliminar produto


def eliminar_elemento(lista):
    print(lista)
    eliminar = str(input('Que elemento desea eliminar: '))
    if eliminar in lista:
        lista.remove(eliminar)

# enseñar lista final


def enseñar_lista(lista):
    print('Tu lista de la compra contiene:')
    for elemento in lista:
        print(elemento)

# cambiar la lista

def cambiar_lista(lista):
    print(lista)
    posicion =int(input("Eligue la posicion que quieres cambiar: "))
    nuevafruta = input("Que quieres añadir: ")
    cambiar_lista[posicion] = nuevafruta
    print(lista)

# Este es el menuu

def menu():
    while True:
        print(''' Opciones:
          [1] Añadir elemento a lista
          [2] Eliminar elemento de lista
          [3] Enseñar lista
          [4] Salir
          [5] Cambiar algo de la lista''')
        opcion = int(input('Elija una opcion: '))
        if opcion == 1:
            añadir_elemento(list_compra)
        elif opcion == 2:
            eliminar_elemento(list_compra)
        elif opcion == 3:
            enseñar_lista(list_compra)
        elif opcion == 5:
            cambiar_lista(list_compra)
        elif opcion == 4:
            break


menu()