import sys
import sdl2
import sdl2.ext

sdl2.import_as_pygame()

class Player:
    def __init__(self, name, health, damage, speed):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed

