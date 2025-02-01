import pygame as py
from circle import Circle
py.init()
w = py.display.set_mode((700, 700))
FPS = 30
clock = py.time.Clock()
circle = Circle(w, (34, 190, 255), 30, 30, 20)
circle2 = Circle(w, (100, 10, 255), 100, 100, 30)
while True:
    w.fill((230, 30, 140))
    key = py.key.get_pressed()
    circle.keypress(key, 2, 2)
    circle2.keypress(key, 5, 5)
    circle.jump()
    circle2.jump()
    circle.draw()
    circle2.draw()
    py.display.update()
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()
    clock.tick(FPS)