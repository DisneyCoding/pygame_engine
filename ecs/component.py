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

class Item(Component):
    def __init__(self, item_id, data):
        self.item_id = item_id
        self.data = data

class Inventory(Component):
    def __init__(self, size=20):
        self.slots = []
        self.max_size = size

    def add_item(self, item: Item):
        if len(self.slots) < self.max_size:
            self.slots.append(item)
            return True
        return False