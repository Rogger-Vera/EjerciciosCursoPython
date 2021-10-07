"""
Desafio11_RoggerVera

Consigna
Te proveen un archivo CSV (valores separados por comas) llamado proceres.csv que contiene datos de algunos próceres.
Cada linea del archivo contiene los datos de un prócer, separados por comas.
Se te pide que leas el total del archivo en una variable llamada texto.

Usando la información en texto, generar una lista de lineas de texto lista1.

Usando la información en lista1 y usando map() generar otra lista2 que contenga listas de datos de los próceres (eliminación de comas).

Usando la información en lista2 y usando map() generar otra lista de diccionarios llamada proceres, al estilo de formato de registro que se detalla:

{
    'Nombre' : nnnn,
    'Apellido' : aaaa,
    'Ciudad natal': cccc,
    'Año natal': aaaa,
    'Año muerte': aaaa
}

Probablemente tengas que escribir una función auxiliar para ayudarte en esta tarea.

Usando map(), agregar un campo extra 'Edad' en cada registro de la lista proceres, basado en la diferencia de años de muerte y nacimiento.
Probablemente tengas que escribir una función auxiliar para ayudarte en esta tarea.

Finalmente usando la lista proceres, mostrar todos los datos por pantalla (campo y valor) dejando una linea en blanco entre cada prócer. Un ejemplo de salida seria:

Nombre:------ 
Apellido: ------
Ciudad natal: -----
Año natal: ----
Año muerte: ----
Edad: --

Si completas este trabajo, estas muy cerca de manejar archivos de datos y convertirlos a formatos que se manejan en las bases de datos.

agregar espacio con "\n"
separar con , CSv
pasar a diccionario para agregar un dato mas


"""

def lista_dic(lista):
    diccionario = {}
    claves = ["Nombre", "Apellido", "Ciudad natal", "Año natal", "Año muerte"]
    for pos in range(len(lista)):
            diccionario[claves[pos]] = lista[pos]
        
    return diccionario    

def agregar_edad(dic):
    
    añom = int(dic["Año muerte"])
    añon = int(dic["Año natal"])            
    dic["Edad"] = añom - añon
        
    return dic

with open("proceres.csv", "r", encoding=("UTF-8")) as proceres:
    texto = proceres.read()
    
lista1 = texto.split("\n")

lista2 = list(map(lambda p: p.split(","), lista1))

proceres = list(map(lista_dic, lista2))

proceres = list(map(agregar_edad, proceres))

for dic in proceres:
    for clave,valor in dic.items():
        print(clave+":",valor)
    print()


