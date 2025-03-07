# Trabajaremos con la libreria open

with open ("text.txt", "r", encoding="utf-8") as f:
    print (f.read())

with open ("text.txt", "w", encoding="utf-8") as f:
    f.write("Reescribiendo....")

with open ("text.txt", "a", encoding="utf-8") as f:
    f.write("Texto agregado")

with open ("frog.png","rb") as f:
    contenido_binario = f.read()

print (contenido_binario)



