"""
    This file will handle save files
"""

import json
import os

SAVE_PATH = "save_data/saves/slot_1.json"

class SaveManager:
    def __init__(self, ecs, item_db):
        self.ecs = ecs
        self.item_db = item_db

    def save_game(self, player_id):
        player_data = {}

        pos = self.ecs.get_component(player_id, "Position")
        if pos:
            player_data["position"] = {"x": pos.x, "y": pos.y}
        
        inventory = self.ecs.get_component(player_id, "Inventory")
        if inventory:
            player_data["inventory"] = [
                {"item_id": item.item_id} for item in inventory.slots
            ]
        
        os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)
        with open(SAVE_PATH) as file:
            json.dump(player_data, file, indent=2)
        print("Game Saved.")

    def load_game(self):
        if not os.path.exists(SAVE_PATH):
            print("No save file found.")
            return None
        
        with open(SAVE_PATH, "r") as file:
            data = json.load(file)

        player_id = self.ecs.create_entity()

        from ecs.component import Position, Inventory, Item
        pos = data.get("position", {"x": 0, "y": 0})
        self.ecs.add_component(player_id, Position(pos["x"], pos["y"]))

        inv = Inventory()
        for item_data in data.get("inventory", []):
            item_info = self.item_db.get(item_data["item_id"])
            if item_info:
                inv.add_item(Item(item_data["item_id"], item_info))
        self.ecs.add_component(player_id, inv)

        print("Game Loaded.")
        return player_id