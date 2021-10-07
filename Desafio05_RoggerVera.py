"""
Desafio 05 - Rogger Vera

Consigna

De un triangulo rectángulo, conocemos el valor de los lados que forman el angulo recto (catetos) y desconocemos el valor del 3er lado (hipotenusa).

Escribí una función que reciba el valor de ambos catetos y devuelva el perímetro del triangulo (la suma de su 3 lados)
Como ayuda podes escribir otra función que calcule la hipotenusa y llamarla desde esta función de perímetro.

Escribí una función que reciba el valor de ambos catetos y devuelva la superficie del triangulo.

Proba las funciones perimetroTrianguloRectangulo() y superficieTrianguloRectangulo() con 2 o mas juegos de valores para observar su funcionamiento. 
"""

def hipotenusa(n1,n2):
    return ((n1**2)+(n2**2))**(1/2)

def perimetroTrianguloRectangulo(n1,n2):
    return hipotenusa(n1,n2)+n1+n2

def superficieTrianguloRectangulo(n1,n2):
    return (n1*n2)/2    


print("Calcule el perimetro y la supeficie de un triangulo rectangulo ingresando el valor de sus dos catetos.\n")
cateto1 = float(input("Ingrese el valor del primer cateto: "))
cateto2 = float(input("Ingrese el valor del segundo cateto: "))

print()
print("\t -El perimetro del triangulo rectangulo es:",perimetroTrianguloRectangulo(cateto1,cateto2))
print("\t -La superficie del triangulo rectangulo es:",superficieTrianguloRectangulo(cateto1,cateto2))
print()
