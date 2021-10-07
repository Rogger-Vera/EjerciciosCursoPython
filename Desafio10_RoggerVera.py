"""
Desafio10_RoggerVera

Consigna
Creá una lista de al menos 10 números enteros.

Usando la lista del punto anterior, obtené un string que contenga todos los elementos separados por comas (CSV)

Usando el string del punto anterior, obtené una lista de números enteros idéntica a la del 1er punto.
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)
print(type(numeros))

string = ",".join([str(x) for x in numeros])
print(string)
print(type(string))

enteros = [int(x) for x in string.split(",")]
print(enteros)
print(type(enteros))


