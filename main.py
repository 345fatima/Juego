import os
import readchar  
from mapa import cargar_mapa, movimientos 

estado_juego = True 


    
def juego_1():

    #iniciar juego 
    global estado_juego
    Tecla = readchar.readchar()
    
    
    
    
    if Tecla in ("w", "s", "a", "d"):
        cargar_mapa(Tecla)

    if  movimientos <= 0:
        estado_juego = False 
    elif Tecla == "q": 
        print("Saliste del Jugo")
        estado_juego = False
    


while estado_juego:
    juego_1()
    
