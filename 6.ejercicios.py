goles_jugador1 = 10
goles_jugador2 = 8
goles_jugador3 = 14

maximo_goles = max(goles_jugador1, goles_jugador2, goles_jugador3)

if maximo_goles == goles_jugador1:
    print("Jugador 1 tiene el mayor numero de goles")
elif maximo_goles == goles_jugador2:
    print("Jugador 2 tiene el mayor numero de goles")
else:
    print("Jugador 3 tiene el mayor numero de goles")