"""
Desafio07_RoggerVera

Consigna
Nos pasaron el siguiente código:
lista = [5, 'casa', 0]

print(lista[3])
print(67 / lista[2])
print(-12 + lista[1])
print(listado[1])

print('- Final del programa -')

Y nos avisan que las primeras 4 lineas print generan errores que hacen detener el programa (comprobalo vos mismo)

Se te pide que, sin modificar esas 4 lineas print (que mas adelante van a tener sentido), soluciones el problema de que el programa se detiene sin completar la ultima linea, y que para cada error muestres un mensaje explicativo.

Sugerencia:
Escribí el código original y anotate los errores que va generando.
Luego encerrá cada linea print que genera error dentro de una estructura try-except que atienda el error que hayas anotado para cada linea.

"""

lista = [5, 'casa', 0]

try:
    print(lista[3])
except IndexError:
    print("Error indice de lista fuera de rango")
        
try:
    print(67 / lista[2])
except ZeroDivisionError:
    print("Error division por 0")

try:
    print(-12 + lista[1])
except TypeError:
    print("Error de tipo de datos")

try:
    print(listado[1])
except NameError:
    print("Error de nombre, 'listado' no esta definido")

print('- Final del programa -')
