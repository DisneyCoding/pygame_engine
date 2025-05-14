"""
    This file will hold the base Component Class
"""

class Component:
    pass

class PlayerInput(Component):
    def __init__(self, speed=200):
        self.speed = speed


class Position(Component):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Sprite(Component):
    def __init__(self, surface):
        self.surface = surface

class Velocity(Component):
    def __init__(self, dx=0, dy=0):
        self.dx = dx
        self.dy = dy
        