#bool contiene los valores de True y False
# los tipo numericos, es false para el 0 (cero), true para los demas valores
valor = 0
resultado = bool(valor)
print(f"valor: {valor}, Resultado: {resultado}")

valor = 0.1
resultado = bool(valor)
print(f"valor: {valor}, Resultado: {resultado}")

#Tipo string -> False "", True demas valores
valor = ""
resultado = bool(valor)
print(f"valor: {valor}, Resultado: {resultado}")

valor = "hola"
resultado = bool(valor)
print(f"valor: {valor}, Resultado: {resultado}")

#Tipo colecciones -> False para colecciones vacias
#Tipo colecciones -> True para todas las demas
#Lista
valor = []
resultado = bool(valor)
print(f"valor de una lista vacia: {valor}, resultado: {resultado}")

valor = [2, 3, 4]
resultado = bool(valor)
print(f"valor de una lista con elementos: {valor}, resultado: {resultado}")

#tupla
valor = ()
resultado = bool(valor)
print(f"valor de una tupla vacia: {valor}, resultado: {resultado}")

valor = (5,)
resultado = bool(valor)
print(f"valor de una tupla con elementos: {valor}, resultado: {resultado}")

#diccionario
valor = {}
resultado = bool(valor)
print(f"valor de una diccionario vacio: {valor}, resultado: {resultado}")

valor = {"Nombre":"Juan", "Apellido":"Perez"}
resultado = bool(valor)
print(f"valor de una diccionario con elementos: {valor}, resultado: {resultado}")

#Sentencias de control con bool
if (1,):
    print("Regresa verdadero")
else:
    print("Regresa falso")

#ciclos
variable = 17
while variable:
    print("Regresa verdadero")
    break
else:
    print("Regresa falso")
