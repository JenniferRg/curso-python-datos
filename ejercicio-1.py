# # Sesion 7

#ciclo for

guias = ["G001", "G002", "G003", "G004", "G005"]

for memoria in guias:
    print("Revisando envío:", memoria)

#for+range

for consecutivo in range(2):
    print("Revisando envío:", guias[consecutivo])

for consecutivo in range(2, 5):
    print("Revisando envío:", guias[consecutivo])
    
#contadores

contador = 0

for guia in guias:
    contador += 1
    print("Revisando", guia)

print("Total:", contador)

#acumulador de kms

distancias = [15, 22, 10, 18]

total_km = 0
cantidad_rutas = 0

for km in distancias:
    total_km += km
    cantidad_rutas += 1

print(total_km)
print(cantidad_rutas)

#while
# intentos de entrega

guia = "G001"

intentos = 0
entregado = False

while intentos < 3 and entregado == False:

    intentos += 1

    print("Guía:", guia)
    print("Intento de entrega:", intentos)

    resultado = input("¿Se entregó el paquete? (s/n): ").lower()

    if resultado == "s":
        entregado = True

if entregado:
    print("Envío entregado correctamente")
else:
    print("Envío no entregado. Requiere seguimiento")

print("Total de intentos:", intentos)

#contador de ruta por estados

# REGISTROS DE ENVIOS

envios = [
    {"guia": "G001", "estado": "Entregado"},
    {"guia": "G002", "estado": "En ruta"},
    {"guia": "G003", "estado": "Devuelto"},
    {"guia": "G004", "estado": "Entregado"},
    {"guia": "G005", "estado": "En ruta"}
]

# CONTADORES
entregados = 0
en_ruta = 0
devueltos = 0

# RECORRER LOS ENVIOS
for envio in envios:

    if envio["estado"] == "Entregado":
        entregados += 1

    elif envio["estado"] == "En ruta":
        en_ruta += 1

    else:
        devueltos += 1

# MOSTRAR RESULTADOS
print("RESUMEN DE ENVIOS")
print("Entregados:", entregados)
print("En ruta:", en_ruta)
print("Devueltos:", devueltos)

#frecuencias  de entregas por tiempos

tiempos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

grupo_1_3 = 0
grupo_4_6 = 0
grupo_7_9 = 0
grupo_10_12 = 0

for tiempo in tiempos:
    if 1 <= tiempo <= 3:
        grupo_1_3 += 1
    elif 4 <= tiempo <= 6:
        grupo_4_6 += 1
    elif 7 <= tiempo <= 9:
        grupo_7_9 += 1
    elif 10 <= tiempo <= 12:
        grupo_10_12 += 1

print("REPORTE DE TIEMPOS DE ENTREGA")
print("-----------------------------")
print("De 1 a 3 días:", grupo_1_3, "entregas")
print("De 4 a 6 días:", grupo_4_6, "entregas")
print("De 7 a 9 días:", grupo_7_9, "entregas")
print("De 10 a 12 días:", grupo_10_12, "entregas")

