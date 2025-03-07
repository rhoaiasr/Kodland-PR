import random
def gen_pass(long):
    caract =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" # Caracteres posible para la contraseña

    psw_generada = "" # Variable para generar la contraseña

    for i in range(long):
        psw_generada += random.choice(caract) # Generacion de la contraseña con la longitud seleccionada (cantidad de letras)
    
    return psw_generada # Mostrar en discord la contraseña generada