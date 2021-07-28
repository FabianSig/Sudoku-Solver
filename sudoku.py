import pygame as py
from sys import exit



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
# Überprüft, welche Zahl in die Lücke passt
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
# sucht nach einem leeren Platz
def loesen():
    global feld
    for y in range(9):
        for x in range(9):
            if feld[y][x] == 0:
                for zahl in range(1, 10):
                    if moeglich(x, y, zahl):
                        feld[y][x] = zahl
                        if loesen():
                            return feld
                    feld[y][x] = 0 #backtracking
                return

    return feld

py.init()
screen = py.display.set_mode((540, 540))
py.display.set_caption("Siggi's Sodokulöser")
base_font = py.font.Font("font/freesansbold.ttf", 56)


while True:
    py.Surface.fill(screen, "white")

    #Zeichnen der senkrechten  Spielfeldlinien
    for i in range(10):
        if i % 3 == 0:
            py.draw.line(screen, "black", (60*i, 0), (60*i, 540), width=3)
        else:
            py.draw.line(screen, "black", (60*i, 0), (60*i, 540))

    #Zeichnen der waagrechten Spielfeldlinien
    for i in range(10):
        if i % 3 == 0:
            py.draw.line(screen, "black", (0, 60*i), (540, 60*i), width=3)
        else:
            py.draw.line(screen, "black", (0, 60*i), (540, 60*i))

    #platziert eine rotes Kästchen um den Mauszeiger
    input_rect = py.Rect((py.mouse.get_pos()[0] // 60) * 60, (py.mouse.get_pos()[1] // 60) * 60, 60, 60)
    py.draw.rect(screen, "red", input_rect, 2)

    #Platziert die Zahlen im Spielfeld
    for x in range(9):
        for y in range(9):
            text = str(feld[y][x])

            text_surface1 = base_font.render(text, True, "black")
            screen.blit(text_surface1,(y*60+16, x*60-5))


    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()               #terminiert das Fenster bei Klick auf das X
            exit()

        if event.type == py.KEYDOWN:
            if event.key == py.K_RETURN:        #zeigt die Lösung beim Drücken der Entertaste an
                loesen()
                for x in range(9):
                    for y in range(9):
                        text = str(feld[y][x])

            #lässt nur Zahleneingabe zu
            elif event.key == py.K_0 or event.key == py.K_1 or event.key == py.K_2 or event.key == py.K_3 or event.key == py.K_4 or event.key == py.K_5 or event.key == py.K_6 or event.key == py.K_7 or event.key == py.K_8 or event.key == py.K_9:
                for i in range(9):
                    for j in range(9):
                        if ((py.mouse.get_pos()[0] // 60), (py.mouse.get_pos()[1] // 60)) == (j, i):
                            feld[j][i] = event.unicode
            #Reset Knopf
            elif event.key == py.K_r:
                feld = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            #jede andere tase setzt das Feld zurück
            else:
                for i in range(9):
                    for j in range(9):
                        if ((py.mouse.get_pos()[0] // 60), (py.mouse.get_pos()[1] // 60)) == (j, i):
                            feld[j][i] = 0


    py.display.update()