import pygame as py
import random
from circle import Circle
py.init()
w = py.display.set_mode((700, 700))
FPS = 60
clock = py.time.Clock()
circle = []
for i in range(5000):
    circle.append(Circle(w,(random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)),
                i*2, i*2, 20))
while True:
    #w.fill((250, 250, 250))
    for item in circle:
        item.draw()
        item.razv()
    py.display.update()
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()
    clock.tick(FPS)