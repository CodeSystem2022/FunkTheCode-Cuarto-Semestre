#dar formato a un string

nombre = "Ariel"
edad = 28

mensaje_con_formato = "Mi nombre es %s y tengo %d años " % (nombre, edad)


#creamos una tupla
persona = ("Carla", "Gomez", 5000.00)
mensaje_con_formato = "Hola %s %s . Tu sueldo es %.2f " # %persona # aqui le pasamos el objeto que es la tupla
#print(mensaje_con_formato % persona)


nombre = "Juan"
edad = 19
sueldo = 3000
# mensaje_con_formato = "Nombre {} Edad {} sueldo {:.2f}".format(nombre, edad, sueldo)
#print(mensaje_con_formato)

#mensaje = " Nombre {0} Edad {0} Sueldo {2:.2f} ".format(nombre, edad, sueldo)
#print(mensaje)

mensaje = "Nombre {n} Edad {e} Sueldo {s:.2f}".format(n=nombre, e=edad, s=sueldo)
#print(mensaje)

diccionario = {"Nombre" : "Ivan", "Edad" : 35, "Sueldo": 8000.00}
mensaje = "Nombre {dic[Nombre]} Edad {dic[Edad]} Sueldo {dic[Sueldo]:.2f} ".format(dic=diccionario)
print(mensaje)