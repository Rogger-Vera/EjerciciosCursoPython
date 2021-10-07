"""
Desafio09_RoggerVera

Consigna
Los años bisiestos son aquellos que son múltiplos de 400 o, que son múltiplos de 4 pero no de 100.
Esta regla del calendario gregoriano actual se aplica desde 1583.

Como dato curioso de ese año, al día Jueves 4 de Octubre le siguió el Viernes 15 de Octubre.
Es decir que los días 5 de Octubre al 14 de Octubre de 1583 nunca existieron.
Esta resolución se tomó para corregir un desfase de aproximadamente 10 días que tenia el calendario juliano usado en esa época con el año solar real.
https://es.wikipedia.org/wiki/Año_bisiesto

Usando listas de comprensión, generá y mostrá una lista de los años bisiestos desde el 1583 al 2050.
Observá que los años 1700, 1800 y 1900 no fueron bisiestos.

Usando la lista anterior, generá y mostrá otra lista de los bisiestos que fueron final de década (múltiplos de 10).

Usando segmentos, mostrá los primeros 10 elementos de la lista del punto anterior.

"""

lista_años_bisiestos = [x for x in range(1583, 2051) if x % 400 ==0 or (x % 4 == 0 and x % 100 != 0)]
    
print("Lista de los años bisiestos desde el 1583 al 2050")
print("------------------------------------------------- \n", lista_años_bisiestos, "\n")

bisiestos_final_decada = [x for x in lista_años_bisiestos if x % 10 ==0] 

print("Lista de los años bisiestos que fueron final de década")
print("------------------------------------------------------ \n", bisiestos_final_decada, "\n")

print("Primeros 10 elementos de la lista del punto anterior")
print("---------------------------------------------------- \n", bisiestos_final_decada[:10], "\n")

