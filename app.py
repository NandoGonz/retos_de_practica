with open("ejemplo.txt", "w", encoding="UTF-8") as archivo:
    archivo.write("Ya es menos trabajo \n")
    archivo.write("Eso es lo que diria \n")
    archivo.write("Pero empieza lo bueno \n")

with open("ejemplo.txt", "a", encoding="UTF-8") as archivo:
    archivo.write("Me estoy esforzando")

with open("ejemplo.txt", "r", encoding="UTF-8") as archivo:
    info = archivo.readlines()


frases = []
for i in info:
    frases.append(i.strip())
print(frases)

# Creamos un filto
coincidencias = []
for i in frases:
    if "Pero" in i:
        coincidencias.append(i.strip())
print(coincidencias)
