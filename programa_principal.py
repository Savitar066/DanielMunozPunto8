from funciones import gen_num_aleatorios, fibonacci, ordenar_pila, eliminar_elem

# Generamos una lista denumeros aleatorios
numeros_aleatorios = gen_num_aleatorios(10, 1, 100)

# Calculamosla serie de Fibonacipara los números generados
serie_fibonacci = fibonacci(len(numeros_aleatorios))

# Creamosna pila con la serie de Fibonacci
pila = serie_fibonacci

pila_ordenada = []

while True:
    print("\nOpciones:")
    print("1: Ordenar la pila en orden ascendente")
    print("2: Buscar y eliminar un registro específico")
    print("3: Mostrar la pila ordenada después de eliminar el registro")
    print("4: Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Ordenar la pila en orden acendente
        pila_ordenada = ordenar_pila(pila)
        print("Pila ordenada:", pila_ordenada)
    elif opcion == "2":
        # Buscar y eliminar un registro especifico
        elem_a_eliminar = int(input("Ingrese el número a eliminar: "))
        pila_actualizada, encontrado = eliminar_elem(pila_ordenada, elem_a_eliminar)
        if encontrado:
            print("Elemento eliminado.")
            pila_ordenada = pila_actualizada  # Actualizar la pila ordenada después de eliminar el elemento
        else:
            print("El número no se encuentra en la lista.")
    elif opcion == "3":
        # Mostrar la pilaordenada despues de eliminar el registro
        print("Pila ordenada después de eliminar el elemento:", pila_ordenada)
    elif opcion == "4":
        # Salir del programa
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")