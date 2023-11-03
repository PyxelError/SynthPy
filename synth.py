import pygame as pg

from tone import Tone
from note import Note

pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
while run:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.KEYDOWN:
            print(event.key)
            if event.key == 97:
                Note.Play_chord([Note('C4', .2)])
            if event.key == 115:
                Note.Play_chord([Note('D4', .2)])
            if event.key == 100:
                Note.Play_chord([Note('E4', .2)])
            if event.key == 102:
                Note.Play_chord([Note('F4', .2)])
            if event.key == 103:
                Note.Play_chord([Note('G4', .2)])
            if event.key == 104:
                Note.Play_chord([Note('A4', .2)])
            if event.key == 106:
                Note.Play_chord([Note('B4', .2)])

pg.quit()