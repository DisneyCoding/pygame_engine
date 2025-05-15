"""
    This file will hold the InputSystem class
"""

from ecs.system import System
from ecs.component import Velocity
from ecs.component import PlayerInput

import pygame

class InputSystem(System):
    def __init__(self, ecs):
        self.ecs = ecs


    def update(self, dt):
        keys = pygame.key.get_pressed()

        for entity in self.ecs.get_entities_with(PlayerInput, Velocity):
            input_comp = self.ecs.get_component(entity, PlayerInput)
            vel = self.ecs.get_component(entity, Velocity)

            vel.dx = 0
            vel.dy = 0

            if keys[pygame.K_w] or keys[pygame.K_UP]:
                vel.dy = -input_comp.speed
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                vel.dy = input_comp.speed
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                vel.dx = -input_comp.speed
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                vel.dx = input_comp.speed