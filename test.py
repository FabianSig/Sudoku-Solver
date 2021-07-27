import numpy


feld = [
        [0, 1, 0, 0, 3, 8, 0, 6, 0],
        [0, 0, 0, 0, 0, 1, 0, 4, 5],
        [5, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 9, 0, 1, 0, 0],
        [6, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 6, 0, 0, 2, 0],
        [0, 0, 0, 6, 1, 4, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 9]
    ]

def moeglich(x, y, zahl):
    global feld
    for i in range(9):
        if feld[y][i] == zahl:
            return False
    for i in range(9):
        if feld[i][x] == zahl:
            return False
    x1 = (x//3)*3
    y1 = (y//3)*3

    for i in range(3):
        for l in range(3):
            if feld[y1+i][x1+l] == zahl:
                return False
    return True

def loesen():
    global feld
    for y in range(9):
        for x in range(9):
            if feld[y][x] == 0:
                for zahl in range(1, 10):
                    if moeglich(x, y, zahl):
                        feld[y][x] = zahl
                        loesen()
                        feld[y][x] = 0
                return

    print(numpy.matrix(feld))

loesen()


