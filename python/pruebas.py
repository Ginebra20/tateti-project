tablero = ["-", "-", "-",
           "-", "-", "-",
           "-", "-", "-"]


def menu():
    comienzoDelJuego = int(input("Elige una opcion: \n 1- Iniciar juego \n 2- Como jugar \n 3- Salir \n "))
    if comienzoDelJuego == 1:
        inicio()
    elif comienzoDelJuego == 2:
        comoJugar()
    elif comienzoDelJuego == 3:
        print("Nos vimos en Disney BRRROTHERRRR")


def comoJugar():
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")
    print("Ingresa un numero para elegir en que casilla marcar")
    volver = input("¿Quieres volver al menu? \n si/no: ")
    if volver.lower() == "si":
        menu()


def inicio():
    global jugador1, jugador2
    jugador1 = input("Jugador 1: Elige tu nombre: ")
    jugador2 = input("Jugador 2: Elige tu nombre: ")

    while jugador1 == jugador2:
        print("¿Son pelotudos?")
        print("No pueden elegir el mismo nombre de usuario")

        jugador1 = input("Jugador 1: Elige tu nombre de usuario nuevamente >:| ")
        jugador2 = input("Jugador 2: Tu tambien :D ")

    mostrarTablero()
    turnos()


def mostrarTablero():
    print(tablero[0] + "|" + tablero[1] + "|" + tablero[2])
    print(tablero[3] + "|" + tablero[4] + "|" + tablero[5])
    print(tablero[6] + "|" + tablero[7] + "|" + tablero[8])
    print("Bienvenido al Ta-Te-Ti")


def turnos():
    global jugador1, jugador2
    for i in range(9):
        if i % 2 == 0:
            print("Turno de " + jugador1)
            turno = "x"
        else:
            print("Turno de " + jugador2)
            turno = "o"
        elegirPosicion(turno)
        ganador()
        if winner == "x" or winner == "o":
            break
    if winner == "x":
        print("Ganaste " + jugador1)
    elif winner == "o":
        print("Ganaste " + jugador2)
    else:
        print("Tremendo empate brother")


def ganador():
    global winner
    if tablero[0] == tablero[1] == tablero[2] != "-":
        winner = tablero[0]
    elif tablero[3] == tablero[4] == tablero[5] != "-":
        winner = tablero[3]
    elif tablero[6] == tablero[7] == tablero[8] != "-":
        winner = tablero[6]
    elif tablero[0] == tablero[3] == tablero[6] != "-":
        winner = tablero[0]
    elif tablero[1] == tablero[4] == tablero[7] != "-":
        winner = tablero[1]
    elif tablero[2] == tablero[5] == tablero[8] != "-":
        winner = tablero[2]
    elif tablero[0] == tablero[4] == tablero[8] != "-":
        winner = tablero[0]
    elif tablero[2] == tablero[4] == tablero[6] != "-":
        winner = tablero[2]
    else:
        winner = None


def elegirPosicion(turno):
    global tablero
    jugada = False
    while not jugada:
        posicion = int(input("Elige una posicion del tablero: ")) - 1
        if tablero[posicion] == "-":
            jugada = True
        else:
            print("Esa posicion no esta disponible, elige otra")
    tablero[posicion] = turno
    mostrarTablero()


menu()