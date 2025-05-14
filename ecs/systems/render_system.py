"""
    This file holds the RenderSystem class
"""

from ecs.system import System
from ecs.component import Position
from ecs.component import Sprite

class RenderSystem(System):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface

    def update(self, ecs, dt):
        for entity in ecs.get_entities_with(Position, Sprite):
            pos = ecs.get_component(entity, Position)
            sprite = ecs.get_component(entity, Sprite)

            self.surface.blit(sprite.surface, (pos.x, pos.y))