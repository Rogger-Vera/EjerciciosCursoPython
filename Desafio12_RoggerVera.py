"""
Desafio12_RoggerVera

Consigna
La serie de Fibonacci, es una serie infinita de números enteros formada por los elementos:

f0, f1, f2, f3, f4, f5, f6, ........, fn          donde ya están definidos los elementos f0 = 0 y f1 = 1

El resto de los términos se calculan como la suma de los 2 anteriores de la serie.

Por ejemplo:
f2 = f1 + f0 = 1 + 0 = 1
f3 = f2 + f1 = 1 + 1 = 2
f4 = f3 + f2 = 2 + 1 = 3
f5 = f4 + f3 = 3 + 2 = 5

Crea una función recursiva que reciba un argumento con el numero de termino, y que devuelva una lista con todos los términos de la serie de Fibonacci hasta el termino indicado.

Por ejemplo fibonacci(5) --> devuelve la lista [0, 1, 1, 2, 3, 5]

"""

def fibonacci(termino):
    if termino == 0 :
        return [0]
    elif termino == 1:
        return [0, 1]
    else:
        lista = fibonacci(termino -1)
        lista.append(lista[-1]+lista[-2])
        return lista
        
print(fibonacci(5))

