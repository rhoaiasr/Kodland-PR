import os
import random

def choicememes(directorio = "imagenes"):
    images_memes = os.listdir("imagenes")
    select_meme = random.choice(images_memes)
    #Ruta donde esta la imagend del meme
    return os.path.join (directorio, select_meme)


