"""
    Run This file for running the engine
"""

import pygame

from core.ecs import ECSManager
from core.item_loader import ItemDatabase
from ecs.component import Position, Velocity, Sprite, PlayerInput, Inventory, Item 
from ecs.systems.input_system import InputSystem
from ecs.systems.movement_system import MovementSystem
from ecs.systems.render_system import RenderSystem
from save_data.save_manager import SaveManager

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D ECS Game Example")
clock = pygame.time.Clock()

ecs = ECSManager()
item_db = ItemDatabase()
save_manager = SaveManager(ecs, item_db)

ecs.add_system(InputSystem(ecs))
ecs.add_system(MovementSystem(ecs))
ecs.add_system(RenderSystem(ecs, screen))

player_sprite = pygame.Surface((32, 32))
player_sprite.fill((255, 255, 255))

slot = input("Enter save slot to load (e.g. 1, 2, 3): ")

player = save_manager.load_game(slot)

if player is None:
    player = ecs.create_entity()
    ecs.add_component(player, Position(100, 100))
    ecs.add_component(player, Velocity())
    ecs.add_component(player, Sprite(player_sprite))
    ecs.add_component(player, PlayerInput(speed=200))
    ecs.add_component(player, Inventory(size=10))

running = True

inv = ecs.get_component(player, Inventory)
if inv:
    print("Player Inventory:")
    for item in inv.slots:
        print(f" - {item.data['name']} ({item.item_id})")

while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.K_p:
            save_manager.save_game(player, slot)

    ecs.update(dt)
    print(player.Position)
    pygame.display.flip()

pygame.quit