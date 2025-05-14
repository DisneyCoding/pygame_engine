"""
    This file will hold the MovementSystem Class
"""

from ecs.system import System
from ecs.component import Position
from ecs.component import Velocity

class MovementSystem(System):
    def update(self, ecs, dt):
        for entity in ecs.get_entities_with(Position, Velocity):
            pos = ecs.get_component(entity, Position)
            vel = ecs.get_component(entity, Velocity)
            pos.x += vel.dx * dt
            pos.y += vel.dy * dt
            