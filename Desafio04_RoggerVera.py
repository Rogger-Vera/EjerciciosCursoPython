# Desafio 04 - Rogger Vera
#Un conserje de un salón de fiestas dispone de una lista de nombres de los invitados a un festejo.
#(Generá una lista de nombres de por lo menos 10 nombres)
#A medida que van llegando los asistentes el conserje solicita sus nombres, y si el asistente está en la lista de invitados debe:
#Dejarlo ingresar al salón (simulalo con un mensaje por pantalla)
#Agregar el nombre a otra lista de asistentes
#Borrar el nombre de la lista de invitados
#Si el asistente no está en la lista de invitados, debe rechazar su ingreso (simulalo con un mensaje por pantalla)
#A un determinado horario pactado con los anfitriones, cierra la puerta y ya no permite los ingresos.
#Esto lo realiza ingresando el nombre clave 'FIN'
#Luego de cerrar el ingreso, el conserje debe informar la cantidad de invitados, la cantidad de asistentes y la cantidad de ausentes.


nombres_de_invitados = ["Ana", "Andres", "Belen", "Beto", "Camila", "Carlos", "Debora", "Dardo", "Flor", "Gaston"]
invitados = nombres_de_invitados
asistentes = []

print()
nombre = input("Bienvenido a la fiesta, por favor ingrese su nombre: ")

while nombre.upper() != "FIN":
  if nombre.capitalize() in nombres_de_invitados:
    asistentes.append(nombre.capitalize())
    nombres_de_invitados.remove(nombre.capitalize())
    print("\t- Gracias por venir", nombre.capitalize(),"por favor ingrese al salon.")
  else:
    print("\t- Usted no puede ingresar, ya que no esta en la lista de invitados.")  
  nombre = input("Bienvenido a la fiesta, por favor ingrese su nombre: ")

print ()
print ("Cantidad de invitados:", len(nombres_de_invitados+asistentes))
print ("Cantidad de asistentes:", len(asistentes))
print ("Cantidad de ausentes:", len(nombres_de_invitados))

