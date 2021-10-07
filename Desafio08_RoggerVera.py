"""
Desafio08_RoggerVera

Consigna
Nos entregaron un archivo personas.dat (ver archivo adjunto) que contiene varias lineas con el siguiente formato:
2 dígitos numéricos para la edad, un espacio y luego un nombre.

Nos piden generar a partir de la información de este archivo, 2 nuevos archivos:
menores.dat que contenga todas las lineas de los menores de 18 años
mayores.dat que contenga todas las lineas del resto de las personas

Escribí un programa que cumpla lo solicitado en el párrafo anterior, y ademas a modo de verificación, liste el contenido de ambos archivos anteponiendo un titulo a modo de encabezado, al estilo:

Menores
--------
(lista)

Mayores
--------
(lista)

"""


from os import write


Menores = []
Mayores = []

#Abrimos el archivo y sustraemos la informacion de las personas para separarlas en menores de 18 años y de 18 años o mas

with open("personas.dat", "r") as personas:
    archivo_personas = personas.readlines()

    for l in archivo_personas:
        edad = int(l[0] + l[1])
        if edad < 18:
            Menores.append(l)
        else:
            Mayores.append(l)

#Creamos el archivo menores.dat con los datos almacenados en la lista Menores. Tambien procedemos a leerlo y sacarlo por pantalla para verificar.

with open("menores.dat", "w") as menores:

    # Una forma de escribir los archivos es la siguiente:
    # for l in Menores:
    #     menores.write(l)

    # Otra forma mas sencilla:
    menores.writelines(Menores)

with open("menores.dat", "r") as menores:
    
    # leer = menores.readlines()
    # print("Menores\n--------")
    # for p in leer:
    #     print(p, end="")

    print("Menores\n--------")
    print(menores.read())

#print()

#Creamos el archivo mayores.dat con los datos almacenados en la lista Mayores. Tambien procedemos a leerlo y sacarlo por pantalla para verificar.

with open("mayores.dat", "w") as mayores:

    # for l in Mayores:
    #     mayores.write(l)

    mayores.writelines(Mayores)
        
with open("mayores.dat", "r") as mayores:    
    # leer = mayores.readlines()
    # print("Mayores\n--------")
    # for p in leer:
    #     print(p, end="")

    print("Mayores\n--------")
    print(mayores.read())

print()

