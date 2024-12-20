# Un bot que informa a los usuarios del tiempo de descomposición de un determinado objeto doméstico.

def tiempo_descomp(objeto):
    #Diccionario de objetos
    descomposicion = {
        "papel": "2 a 5 meses",
        "vidrio": "4,000 años o más",
        "plástico": "500 a 1,000 años",
        "lata de aluminio": "80 a 200 años",
        "cáscara de plátano": "2 a 10 días",
        "bolsa de plástico": "150 a 300 años",
        "botella de vidrio": "Infinito (no se descompone, pero puede reciclarse)",
        "neumático": "50 a 80 años",
        "colilla de cigarro": "10 a 12 años",
        "pañal desechable": "450 años",
        "madera pintada": "13 años",
        "cáscara de naranja": "6 meses",
        "pañuelo de papel": "2 a 4 semanas",
        "movil": "1000 años"
        }
    #Buscar objetos en el diccionario
    if objeto in descomposicion:
        tiempo = descomposicion[objeto]
        resultado = f"el tiempo de descomposicion de {objeto} es: {tiempo}"
        return resultado
    else:
        return "Ese objeto no esta en nuestra base de datos"







