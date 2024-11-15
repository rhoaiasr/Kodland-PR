palabras = {"LADILLA": "Es cuando algo te fastidia o te aburre. Por ejemplo: Estoy ladillado significa estoy aburrido, deja la ladilla, deja el fastidiio",
           "SAPEGATO": "Es cuando algo te disgusta o quieres apartarlo, ya sea por desagrado o porque es algo que no es para ti",
           "CHIMBO": "Se usa para expresar que es algo malo, feo o inoportuno. Por ejemplo: En una salida de amigos a uno no le dan permiso para salir con los demas, lo cual es algo que se puede considerar inoportuno, osea, chimbo",
           "HARTAR": "Expresa que se esta comiendo mucho, de manera excesiva o con gula",
           "CREEPY" :"aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado"}


respuesta = input ("Seleccione una de la cual desconozca su significado").upper()

if respuesta in palabras.keys():
    print (palabras[respuesta])
else:
    print ("La palabra no esta registrada")
