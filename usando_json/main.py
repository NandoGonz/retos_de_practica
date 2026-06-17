import json

archivo_datos = "datos.json"
data = {"nombre": "Luis Fernando", "edad": 29, "profesión": "comerciante"}

with open(archivo_datos, "w", encoding="UTF-8") as archivo:
    json.dump(data, archivo, indent=4)

with open(archivo_datos, "r", encoding="UTF-8") as archivo:
    datos_recuperados = json.load(archivo)

print(datos_recuperados)

# --------------------------------------------------#
# primero leemos el archivo para poder modificarlo  #
# --------------------------------------------------#
with open(archivo_datos, "r", encoding="UTF-8") as archivo:
    datos = json.load(archivo)

datos["edad"] = 30  # Modifica un valor numérico
datos["items"] = "relojes"
datos["nuevo_campo"] = True  # Añade una clave completamente nueva

with open(archivo_datos, "w", encoding="UTF-8") as archivo:
    json.dump(datos, archivo, indent=4)

with open(archivo_datos, "r", encoding="UTF-8") as archivo:
    mostrar_datos = json.load(archivo)

print(mostrar_datos)
