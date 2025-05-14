"""
    This file will have the ItemDatabase Class
"""

import json

class ItemDatabase:
    def __init__(self, path="data/items.json"):
        self.items = {}
        self.load_items(path)

    def load_items(self, path):
        with open(path, "r") as file:
            data = json.load(file)

            item_list = data.get("items", [])
            for item in item_list:
                self.items[item['id']] = item

    def get(self, item_id):
        return self.items.get(item_id)