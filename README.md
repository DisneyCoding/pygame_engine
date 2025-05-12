# Pygame 2D Game Engine

Welcome to the **Pygame 2D Game Engine** – a flexible, scalable engine built with Python and Pygame. Designed for developers who want to create rich 2D games, this engine aims to provide a modular structure, easy-to-use APIs, and support for custom game mechanics like RPG elements, ECS architecture, crafting, UI, and more.

## 🎮 Features (Planned and Current)

### ✅ Core Features
- Entity-Component-System (ECS) architecture
- Modular scene management
- Delta time–based game loop
- Resolution scaling and fullscreen support
- Built-in asset management (images, sounds, fonts)

### 🧱 Game Systems
- Sprite-based rendering system
- Basic physics & collision system (AABB)
- Input system (keyboard, mouse)
- Camera system with parallax scrolling support
- Tilemap loader and renderer (Tiled `.tmx` support)

### 🧰 Utility Systems
- Debug console and logger
- Configuration file support (`.json`, `.ini`)
- Save/load system (using JSON or CSV)
- Modular modding support

### 🧙 RPG/Game Mechanics (Planned)
- Skill & stats system
- Inventory and item database
- Crafting system (recipes, workstations)
- Quest system (main and side quests)
- NPCs with simple AI/dialogue system
- Bestiary & codex tracking
- Professions system (farming, mining, fishing, etc.)

### 💡 UI Framework
- UI elements (buttons, labels, sliders, tooltips)
- In-game menus (inventory, settings, pause menu)
- Drag-and-drop support
- Custom font and text rendering system

---

## 📦 Installation

Clone this repository:
```bash
git clone https://github.com/yourusername/pygame-2d-engine.git
cd pygame-2d-engine
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

Run the engine's demo:
```bash
python main.py
```

---

## 🛠️ Usage

The engine is modular and organized into folders such as:

- `core/`: Game loop, ECS, and main engine systems
- `systems/`: Rendering, input, physics, etc.
- `components/`: Reusable component definitions (Position, Sprite, Health, etc.)
- `resources/`: Game assets (sprites, sounds, maps)
- `scenes/`: Different game scenes (menu, gameplay, pause, etc.)

### Example Entity Initialization:
```python
player = Entity()
player.add_component(Position(x=100, y=200))
player.add_component(Sprite(image="player.png"))
player.add_component(Health(current=100, max=100))
```

---

## 🧑‍💻 Contributing

PRs, feedback, and ideas are welcome! If you want to contribute:
- Fork the repo
- Create a new branch
- Submit a pull request

---

## 🌐 Links

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Tiled Map Editor](https://www.mapeditor.org/)
- [Python Official Site](https://www.python.org/)

---

Built with ❤️ using Python & Pygame.
