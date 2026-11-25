# #sesion 3
# # tipos de datos

# # enteros (int)

# edad = 25
# cantidad = 0
# temperatura = -50

# # flotantes (float)
# precio = 10.5
# pi = 3.1416
# peso = 25.2
# print(edad, cantidad, temperatura, precio, pi, peso)

# # booleanos (bool)
# requiere_inscripcion = True
# esta_lluvioso = False
# print(requiere_inscripcion, esta_lluvioso)

# #type() nos permite conocer el tipo de dato de una variable

# print(type(edad))
# print(type(precio))
# print(type(requiere_inscripcion))
# print(type(pi))

# #que pasa si no convierto el tipo de dato

# print(edad + requiere_inscripcion) # esto nos dara un error porque no podemos sumar un entero con un booleano

# cantidad = 10

# print (cantidad * 3)

# #registro de ventas

producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad vendida: "))
precio = float(input("Ingrese el precio unitario: "))

total = cantidad * precio

print("Producto:", producto)
print("Total:", total)
