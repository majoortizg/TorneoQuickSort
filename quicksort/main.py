from lista_enlazada import ListaEnlazada

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x <= pivote]
        mayores = [x for x in lista[1:] if x > pivote]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)
    
def leer_archivo_y_ordenar(nombre_archivo):
    lista_enlazada = ListaEnlazada()

    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read().strip()
        datos = contenido.split(',')

        # Convertir los datos a enteros (o flotantes si los datos no son enteros)
        datos = [int(dato.strip()) for dato in datos]

        # Cargar los datos en la lista enlazada
        for dato in datos:
            lista_enlazada.agregar(dato)

    print("Lista original:")
    lista_enlazada.imprimir()

    # Convertir la lista enlazada a lista normal de Python para ordenarla
    lista_normal = lista_enlazada.convertir_a_lista()

    # Aplicar Quick Sort
    lista_ordenada = quick_sort(lista_normal)

    # Volver a cargar la lista ordenada en la lista enlazada
    lista_enlazada.cargar_desde_lista(lista_ordenada)

    print("Lista ordenada:")
    lista_enlazada.imprimir()

leer_archivo_y_ordenar('datos.txt')