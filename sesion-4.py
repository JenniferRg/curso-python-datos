# # sesion 4
# # consultar cadenas de texto

# producto = "monitor"
# print(producto [0]) # m
# print(producto [1]) # o
# print(producto [2]) # n
# print(producto [3]) # i
# print(producto [4]) # t
# print(producto [5]) # o
# print(producto [6]) # r

# #f strings constuir mensajes con variables

# print(f"El producto es: {producto}")

# #posiciones positivas y negativas

# print(producto [6])
# print(producto [-1])
# print(producto [0])

# #extraer partes de una cadena de texto

# print(producto [0:3]) # mon
# print(producto [2:5]) # oni
# print(producto [2:]) # onitor
# print(producto [2:-3])

# #longitud de una cadena de texto

# producto = "memoria ram 16gb"
# longitud = len(producto)
# print("La longitud de la cadena de texto es:", longitud)

# #metodos de cadenas de texto
# #convertir a mayusculas

# producto = "memoria ram 16gb"
# print(producto.upper())

# #convertir a minusculas
# print(producto.lower())

# #capitalizar la primera letra de la cadena de texto

# print(producto.capitalize())

# #reemplaza un caracter por otro

# print(producto.replace("a", "e"))

# #agregar una letra al final de la cadena de texto

# print(producto + " s ")
# #eliminar espacios en blanco al inicio y al final de la cadena de texto

# print(producto.strip())

# #limpiar base de datos

# nombre = "   JUAN CARLOS LOPEZ GONZALEZ   "
# print(f"El nombre del cliente es: {nombre.strip().title()}")


#listas

lista = ["monitor",
         "teclado",
         "mouse",
         "pendrive"]

print(lista)

#operaciones básicas con listas

#agregar un elemento al final de la lista

lista.append("impresora")
print(lista)

#agregar un elemento en una posicion especifica de la lista

lista.insert(0, "disco duro")
print(lista)

#eliminar un elemento de la lista

lista.remove("pendrive")
print(lista)

#eliminar un elemento de la lista por su posicion

del lista[2]
print(lista)

#ordenar una lista

lista.sort()
print(lista)

#ordenar una lista en reversa

lista.sort(reverse=True)
print(lista)

#unir dos listas

lista2 = ["teclado inalambrico", "mouse inalambrico", "pendrive externo"]
lista3 = lista + lista2
print(lista3)

#convertir una cadena de texto en una lista

cadena = "monitor, teclado, mouse, pendrive"
lista4 = cadena.split(", ")
print(lista4)

#contar elementos de una lista

print(len(lista4))

#tuplas

ubicaciones-geograficas = ("latitud", "longitud", "altitud")
print(ubicaciones-geograficas)

coordinates = (19.432608, -99.133209, 2240)
print(coordinates)

estadistica-media = (10, 20, 30, 40, 50)
print(estadistica-media)

datos-personales = ("cedula", "nombre", "apellido", "edad")
print(datos-personales)