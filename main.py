"""
    Run This file for running the engine
"""

import pygame

from core.ecs import ECSManager
from ecs.component import Position, Velocity, Sprite, PlayerInput
from ecs.systems.input_system import InputSystem
from ecs.systems.movement_system import MovementSystem
from ecs.systems.render_system import RenderSystem

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D ECS Game Example")
clock = pygame.time.Clock()

ecs = ECSManager()

ecs.add_system(InputSystem())
ecs.add_system(MovementSystem())
ecs.add_system(RenderSystem(screen))

player = ecs.create_entity()

player_sprite = pygame.Surface(32, 32)
player_sprite.fill((0, 255, 0))

ecs.add_component(player, Position(100, 100))
ecs.add_component(player, Velocity())
ecs.add_component(player, Sprite(player_sprite))
ecs.add_component(player, PlayerInput(speed=200))

running = True

while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    ecs.update(dt)
    pygame.display.flip()

pygame.quit