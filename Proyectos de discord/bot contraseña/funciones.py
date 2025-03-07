#Generar emojis al azar
import random
def gen_emojis ():
    emojis = [
        "\U0001f600", 
        "\U0001f602",  
        "\U0001f604",  
        "\U0001f60D",  
        "\U0001f618",  
        "\U0001f62D",  
        "\U0001f621",  
        "\U0001f631",  
        "\U0001f642", 
        "\U0001f923", 
        "\U0001f92A",  
        "\U0001f634",  
        "\U0001f970",  
    ]

    emoji = random.choice(emojis)

    return emoji

print (gen_emojis())
