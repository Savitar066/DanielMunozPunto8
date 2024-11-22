# definimos una funcion genera una lista de n numeros aleatorios entreinferior y superior usando la funcion randint delmodulo random.
def gen_num_aleatorios(n, inferior, superior):
    import random
    return [random.randint(inferior, superior) for _ in range(n)]

#con esta funcion calcula la serie de Fibonacci hasta n términos. Comienza con [0, 1] 
# y sigue añadiendo la suma de los dos últimos números de la lista hasta alcanzar ntérminos.
def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]
#definimoas una funcion toma una pila y la devuelve ordenada enorden ascendente usando la funcion sorted.
def ordenar_pila(pila):
    return sorted(pila)

#dewfinimos una funci elimina un elemento indicado de la pila si esta presente. Usa el método remove de las 
# listas para eliminar el elemento 
def eliminar_elem(pila, elem):
    if elem in pila:
        pila.remove(elem)
        return pila, True
    else:
        return pila, False