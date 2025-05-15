"""
    This file will hold the MovementSystem Class
"""

from ecs.system import System
from ecs.component import Position
from ecs.component import Velocity

class MovementSystem(System):
    def __init__(self, ecs):
        self.ecs = ecs

    def update(self, dt):
        for entity in self.ecs.get_entities_with(Position, Velocity):
            pos = self.ecs.get_component(entity, Position)
            vel = self.ecs.get_component(entity, Velocity)
            pos.x += vel.dx * dt
            pos.y += vel.dy * dt
            