# Aplicacion para lista de compras

# Opciones, engadir producto, eliminar producto, amosar lista, sair.

list_compra = ['Limones', 'Naranjas', 'Queso', 'Pavo']

# engadir produto


def añadir_elemento(lista):
    elemento = input('Engadir elemento: ')
    lista.append(elemento)
    print(lista)

