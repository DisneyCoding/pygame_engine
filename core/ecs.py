"""
    This file will handle the Entity Component System
"""

from ecs.entity import Entity
from ecs.system import System
from ecs.component import *
from collections import defaultdict

class ECSManager:
    def __init__(self):
        self.entities = set()
        self.components = defaultdict(dict)
        self.systems = []

    def create_entity(self):
        entity = Entity()
        self.entities.add(entity)
        return entity
    
    def add_component(self, entity, component):
        self.components[type(component)][entity.id] = component

    def get_component(self, entity, component_name):
        for comp in self.components[entity]:
            if comp.__class__.__name__ == component_name:
                return comp
            return None
            
    def get_entities_with(self, *component_types):
        result = []
        for entity in self.entities:
            if all(entity.id in self.components[ctype] for ctype in component_types):
                result.append(entity)
        return result
    
    def add_system(self, system):
        self.systems.append(system)

    def update(self, dt):
        for system in self.systems:
            system.update(self, dt)

