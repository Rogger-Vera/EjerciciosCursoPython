# Desafio 03 - Rogger Vera
# Un docente tiene dos listas de nombres de alumnos, una de aprobados y otra de reprobados.
# Creá 2 listas de nombres de por lo menos 5 elementos cada una.
# Solicitá que se ingrese por teclado un nombre, y de acuerdo al mismo informar alguna de las 3 posibles situaciones:
# El alumno esta aprobado
# El alumno está reprobado
# El alumno no se encuentre en las listas.

aprobados = ["Andrea", "Carlos", "Laura", "Miguel", "Pablo"]
reprobados = ["Ana", "Brenda", "Jose", "Nadia", "Rodrigo"]

nombre = input("Ingrese el nombre del alumno que desea buscar: ")

if nombre.capitalize() in aprobados:
  print("\t- El alumno esta aprobado.")
elif nombre.capitalize() in reprobados:
  print("\t- El alumno esta reprobado.")
else:
  print("\t- El alumno no se encuentra en las listas.")    


