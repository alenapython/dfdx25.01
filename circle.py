import random

import pygame as py
class Circle:
    def __init__(self, win, colour, x, y, r):
        self.win = win
        self.colour = colour
        self.x = x
        self.y = y
        self.r = r
        self.is_jump = False
        self.jump_counter=0
        self.speed = random.randint(1, 5)

    def draw(self):
        py.draw.circle(self.win, self.colour, (self.x, self.y), self.r)

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
    def keypress(self, key, dx, dy):
        if key[py.K_UP]:
            self.y = self.y - dy
        elif key[py.K_DOWN]:
            self.y = self.y + dy
        elif key[py.K_LEFT]:
            self.x = self.x - dx
        elif key[py.K_RIGHT]:
            self.x = self.x + dx
        elif key[py.K_SPACE]:
            self.is_jump =True
    def jump(self):
        if self.is_jump is True:
            if self.jump_counter >= -30:
                self.y -= self.jump_counter
                self.jump_counter -=2
            else:
                self.jump_counter = 30
                self.is_jump = False
    def razv(self):
        self. x = self.x + self.speed
        if self.x > 700:
            self.speed = -self.speed
        if self.x < 0:
            self.speed = -self.speed




