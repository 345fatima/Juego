import os
from modulos.panelControl import cargarPanel
from database.objetos import objetos_ramdom
from database.objetos import bonus_ramdom

#Realizamos invisible y visible nuestro texto 
width_mapa = 25
heigth_mapa = 20 
espacio_invisible = "   "
espacio_lleno= "[  ]"

coordenada_personaje = [5,10]
personaje =  "ᐅ"
movimientos = 30
coordenada_personaje = [10,25]
coordenada_personaje[1] = (coordenada_personaje [1] + 1)% width_mapa

coordenada_personaje[0]= (coordenada_personaje[0] + 1)% heigth_mapa
#objetos 
Lista_objetos = objetos_ramdom
Lista_bonus = bonus_ramdom
ico_objeto = "✿"
ico_bonus = "+3"

#Damos indicaciones de como lo queremos 
def cargar_mapa(mover_personaje):
    global movimientos
   
    # Menú  
    os.system("cls")
    if mover_personaje == "w":
        personaje =  "↑"
        coordenada_personaje[0] -=1
        coordenada_personaje[0]= (coordenada_personaje[0] + 1)% heigth_mapa
    elif mover_personaje == "s":
        personaje =  "↓"
        coordenada_personaje[0] +=1
        coordenada_personaje[0]= (coordenada_personaje[0] + 1)% heigth_mapa
    elif mover_personaje == "a":
        personaje =  "←"
        coordenada_personaje[1] -=1
        coordenada_personaje[1] = (coordenada_personaje [1] + 1)% width_mapa
    elif mover_personaje == "d":
        personaje =  "→"
        coordenada_personaje[1] +=1
        coordenada_personaje[1] = (coordenada_personaje [1] + 1)% width_mapa
    # movimientos 
    movimientos -= 1
    # si ya alcanzo un límite de movimientos
    if movimientos > 39:
        print(f"¡Game Over! Alcanzaste el límite de {movimientos} movimientos.")
        return  False
        

    # Cargar panel de control
    cargarPanel(coordenada_personaje , personaje, movimientos, len(Lista_objetos))

    
    #cargar mapa 
    print("+" + "-"* (width_mapa *3 - 1) + "+")
    for fila  in range(heigth_mapa):
        print ("|", end="")
        for columna in range(width_mapa):

            estado = 0

#agregar al persinaje al tablero 
            if(coordenada_personaje [0]== fila and coordenada_personaje[1]== columna):
                print(f" {personaje} ", end ="")

                #Eliminar el objeto solo si el objeto y el personaje comparte la misma coordenada (x,y)
                for cada_objeto in Lista_objetos:
                    if(cada_objeto[0] == fila and cada_objeto[1] == columna):
                        Lista_objetos.remove([cada_objeto[0],cada_objeto[1]])

                for cada_bonus in Lista_bonus:
                    if(cada_bonus[0] == fila and cada_bonus[1] == columna):
                        Lista_bonus.remove([cada_bonus[0],cada_bonus[1]])
                        movimientos +=3


            else:
               #imprime el objeto en el tablero 
               for cada_objeto in Lista_objetos:
                   if(cada_objeto[0] == fila and cada_objeto[1] == columna):
                       print(f" {ico_objeto} ",end="")
                       estado = 1
               
                # imprime el bonus en el tablero
               for cada_bonus in Lista_bonus:
                    if(cada_bonus[0] == fila and cada_bonus[1] == columna):
                        print(f" {ico_bonus}",end="")
                        estado = 1
                      
                # Imprime el espacio vacío solo si no fue ocupado por un objeto o bonus (estado)
               if (estado == 0):
                  print(espacio_invisible, end="")
            

#Imprimimos nuestras indicaciones   
        print("|")
    print("+" + "-"*(width_mapa * 3 - 1)  + "+")