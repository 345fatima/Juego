import random
#random entre 1 25
#random entre 1 20



def numero_ancho():
    return random.randint(0,24)

def numero_alto():
    return random.randint(0,19)

#objetos
objetos_ramdom = [
    [numero_ancho(),numero_alto()],
    [numero_ancho(),numero_alto()],
    [numero_ancho(),numero_alto()],
    [numero_ancho(),numero_alto()]
]

# Bonus
bonus_ramdom = [
    [numero_ancho(),numero_alto()],
    [numero_ancho(),numero_alto()],
    [numero_ancho(),numero_alto()],
    [numero_ancho(),numero_alto()]
]

