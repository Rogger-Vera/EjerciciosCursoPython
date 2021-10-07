# Desafio 02 - Rogger Vera
#Una persona compra un terreno rectangular del cual le informan su frente y su profundidad (ambos datos expresados en metros)
#Como medida temporal decide alambrar el perímetro con una malla metálica tejida que se vende por metro lineal.
#Para hacer mas fácil la circulación por el terreno, decide construir en la mitad del terreno, una vereda de 50 cm de ancho y del largo total de la profundidad del terreno. Los mosaicos se venden por metro cuadrado.
#También decide emprolijar la superficie del terreno que no ocupa la vereda, cubriéndola con baldosas de césped que se venden por metro cuadrado.
#Deberás solicitar al usuario que te ingrese los datos del ancho y largo del terreno y luego calcular las cantidades necesarias de malla, mosaicos y baldosas de césped.
#Mostrar las cantidades calculadas aclarándolas e indicando las unidades correctas.

print("Ingrese el ancho y el largo del terreno en metros para calcular la cantidad de metros necesarios de malla metalica, mosaicos para vereda y baldosas de cesped.")
print("\n")

ancho= float(input("Ingrese el ancho del terreno: "))
largo= float(input("Ingrese el largo del terreno: "))
print("\n")

mallamet= ancho*2+largo*2
vereda= 0.5*largo
cesped= ((ancho*largo)-vereda)

print("\t- Cantidad de malla metalica:", mallamet,"m.")
print("\t- Cantidad de mosaicos para vereda:",vereda,"m2.")
print("\t- Cantidad de baldosas de cesped:",cesped,"m2.")
