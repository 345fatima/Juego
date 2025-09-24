def cargarPanel (coordenada_personaje, personaje, movimientos,objetos_restantes):
    ancho = 40  # ancho del panel
    # espacio útil entre los bordes y los espacios
    interior = ancho -4
    
    # Encabezado
    print("╔" + "═" * (ancho - 2) + "╗")
    print("║{:^{width}}║".format("📍🅟 🅐 🅝 🅔 🅛  🅓 🅔  🅒 🅞 🅝 🅣 🅡 🅞 🅛📍", width=ancho-2))
    print("╠" + "═" * (ancho - 2) + "╣")
    
    # Contenido
    print("║ {:<36} ║".format(f"Coordenadas: {coordenada_personaje}",  w=interior))
    print("║ {:<36} ║".format(f"Personaje: {personaje}",  w=interior))
    print("║ {:<36} ║".format(f"Movimientos: {movimientos}",  w=interior))
    print("║ {:<{w}} ║".format(f"Objetos restantes: {objetos_restantes}", w=interior))
    
    # Pie de panel
    print("╚" + "═" * (ancho - 2) + "╝")

    