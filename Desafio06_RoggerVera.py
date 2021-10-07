"""
Desafio06_RoggerVera

Consigna

Un hexágono regular es un polígono de 6 lados iguales

Si observas la figura anterior, el hexágono está formado por 6 triángulos equiláteros iguales.
Ademas, cada lado de los triángulos coincide con la medida del lado del hexágono.

A cada triangulo equilátero lo podemos dividir a la mitad para formar 2 triángulos rectángulos.
De ese triangulo rectángulo, conocemos el valor de la hipotenusa igual al lado del hexágono (a en la figura) y el valor de uno de los catetos que vale la mitad del lado del hexágono (a/2 en la figura).
Nos quedaría como desconocido el otro cateto (h en la figura).

Como queremos averiguar la superficie total del hexágono, debemos conocer las superficies de los 6 triángulos equiláteros. 
Pero para averiguar la superficie de cada triangulo equilátero, antes debemos averiguar la superficie de cada uno de los 2 triángulos rectángulos que lo componen. 

Escribí una función que reciba el lado de un hexágono y devuelva su superficie.
Para eso podes importar y usar todas las funciones del modulo math que necesites.
También podes escribir todas las funciones auxiliares que creas necesarias (para calcular superficies de triángulos equiláteros, triángulos rectángulos, catetos desconocido, etc.)
Probá su funcionamiento con varios valores de lado.

"""

from math import sqrt

def altura(lado):
    medio_lado = lado / 2
    return sqrt(lado**2 - medio_lado**2)

def superficie_triangulo(lado):
    return lado * altura(lado) / 2

def superficie_hexagono(lado):
    return superficie_triangulo(lado) * 6

print(superficie_hexagono(3))
print(superficie_hexagono(25.3))
print(superficie_hexagono(231.22))
print()
