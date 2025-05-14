"""
    This file will handle save files
"""

import json
import os

SAVE_DIR = "save_data/saves"

class SaveManager:
    def __init__(self, ecs, item_db):
        self.ecs = ecs
        self.item_db = item_db
        os.makedirs(SAVE_DIR, exist_ok=True)

    def get_save_slot(self):
        return [f for f in os.listdir(SAVE_DIR) if f.endswith(".json")]

    def get_save_path(self, slot):
        return os.path.join(SAVE_DIR, f"slot_{slot}.json")

    def save_game(self, player_id, slot):
        player_data = {}

        # Position
        pos = self.ecs.get_component(player_id, "Position")
        if pos:
            player_data["position"] = {"x": pos.x, "y": pos.y}

        # Inventory
        inventory = self.ecs.get_component(player_id, "Inventory")
        if inventory:
            player_data["inventory"] = [
                {"item_id": item.item_id} for item in inventory.slots
            ]

        # Save to file
        path = self.get_save_path(slot)
        with open(path, "w") as file:
            json.dump(player_data, file, indent=2)
        print(f"Game Saved to slot {slot}.")

    def load_game(self, slot):
        path = self.get_save_path(slot)
        if not os.path.exists(path):
            print(f"No save file in slot {slot}.")
            return None

        with open(path, "r") as file:
            data = json.load(file)

        # Create new player entity
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

        print(f"Game loaded from slot {slot}.")
        return player_id