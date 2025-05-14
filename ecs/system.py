"""
    This file will have the System Base Class
"""

class System:
    def __init__(self):
        self.entities = set()
    
    def update(self, dt):
        raise NotImplementedError