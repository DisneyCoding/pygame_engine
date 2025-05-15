"""
    This file holds the RenderSystem class
"""

from ecs.system import System
from ecs.component import Position
from ecs.component import Sprite

import pygame

class RenderSystem(System):
    def __init__(self, ecs, surface):
        super().__init__()
        self.surface = surface
        self.ecs = ecs


    def update(self, dt):
        self.surface.fill((0, 0, 0))

        for entity in self.ecs.entities:
            pos = self.ecs.get_component(entity, Position)
            sprite = self.ecs.get_component(entity, Sprite)

            if pos is None or sprite is None or sprite.surface is None:
                continue

            self.surface.blit(sprite.surface, (pos.x, pos.y))
        
        pygame.display.flip()