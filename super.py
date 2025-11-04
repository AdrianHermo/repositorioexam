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

