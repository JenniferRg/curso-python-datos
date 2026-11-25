#sesion 6
#if
cantidad_productos = 3
if cantidad_productos <= 3:
    print("bajo stock")
    
#if/else
total_compra = 30000
if total_compra == 100000:
    print("Descuento autorizado")
else:
    print("No aplica descuento")
    
#if/elif/else

cantidad = 4

if cantidad == 0:
    print("Producto agotado")
elif cantidad <= 5:
    print("Inventario bajo")
else:
    print("Producto disponible")
    
total_compra = 150000
cliente_frecuente = True

if total_compra >= 100000 and cliente_frecuente:
    print("Descuento autorizado")
else:
    print("No cumple las condiciones")
