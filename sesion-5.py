#sesion 5

#diccionarios

televisores = {
    "marca": "Samsung",
    "precio": 5400000,
    "pulgadas": 50,
    "color": "negro",
    "resolucion": "4k"
}

print(televisores["marca"])
print(televisores["precio"])
print(televisores["pulgadas"])
print(televisores["color"])
print(televisores["resolucion"])

#consultar informacion get
#corchetes

print(televisores["precio"])
#print(televisores["disponible"])

#llaves

print(televisores.get("disponible"))
print(televisores.get("precio"))
print(televisores.get("pulgadas"))

#agregar informacion

televisores["disponible"] = False
print(televisores)

#modificar informacion

televisores["precio"] = 6000000
print(televisores)

#eliminar informacion

del televisores["disponible"]
print(televisores)

#consultar grupos de datos

#print(televisores.keys())
#print(televisores.values())
print(televisores.items())

#coleccion de registros

electrodomesticos_cocina = [
    {
        "producto": "microondas",
        "marca": "LG",
        "litros": 22,
        "color": "plateado",
        "disponible": True
    },
    {
        "producto": "sanduchera",
        "marca": "oster",
        "color": "negro",
        "disponible": True
    }
]

print(electrodomesticos_cocina[0]["marca"])
print(electrodomesticos_cocina[1]["marca"])
    
    
#conjuntos  

canales = {"Instagram", "Facebook", "TikTok"}

print(canales)

#agregar un canal
canales.add("LinkedIn")

print(canales)

#comprobar si un elemento esta en el conjunto

print("Instagram" in canales)

print("Youtube" in canales)

#unir conjuntos

campania_a = {"Instagram", "Facebook", "TikTok"}
campania_b = {"LinkedIn", "Youtube", "TikTok"}

campania_c = campania_a | campania_b
print(campania_c)

campania_d = campania_a & campania_b
print(campania_d)

campania_e = campania_a - campania_b
print(campania_e)
