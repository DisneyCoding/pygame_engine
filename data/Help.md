# Json File Help

## Items

For making your own items, use the top template item, with empty strings, 0's, and empty dicts/lists

For the ```type``` category, which is to determine what type of item it is, they can be any one of the following:
- resource
- material
- weapon
- armor
- tool
- consumable
- food
- potion
- quest
- key
- blueprint
- container
- furniture
- misc

For the ```tool_type``` category, which determines if the item is a tool and which type, it can be any of these: 
- axe
- pickaxe
- shovel
- hoe
- hammer
- knife
- sickle
- fishing_rod
- net
- tongs
- mortar_pestle
- wrench
- saw
- needle

For the ```tags``` category, which is used for categorization, filtering, recipies, etc, it can be any of these:
- wood
- metal
- stone
- magic
- edible
- healing
- melee
- ranged
- magic_weapon
- projectile
- two_handed
- light_armor
- heavy_armor
- ingredient
- herb
- fuel
- fire
- cold
- electric
- poison
- alchemy
- cooking
- quest_item
- rare
- epic
- legendary
- unique

## Quests

For making your own quests, use the top template quest, with empty strings, 0's, and empty dicts/lists

For the ```type``` category, which says what you need to do to complete it, it can be any of these:
- collect       = Collect Items
- kill          = Defeat Enemies
- talk          = Talk to an NPC
- visit         = Reach a location
- craft         = Create an Item
- use           = Use an Item
- interact      = Activate/Interact with something
- defend        = Protect an object/NPC for a time
- escort        = Guide an NPC to safety
- explore       = Uncover or map an area
- deliver       = Bring an Item to someone
- solve         = Solve a Puzzle or Riddle

For the ```tags``` category, which is used to clasify quest, it can be any of these:
- main_story
- side
- tutorial
- daily
- faction
- repeatable
- hidden
- timed
- fetch
- combat
- exploration
- puzzle
- npc
- gathering
- trader

## Recipies

For making your own recipes, use the top template recipe, with empty strings, 0's, and empty dicts/lists

For the ```type``` category, which determines what kind of recipe it is, it can be any of these:
- crafting
- refining
- smelting
- cooking
- alchemy
- foraging
- enchanting
- tailoring
- brewing
- woodworking
- engineering

For the ```station``` category, which is used to identify where the recipe is crafted at, can be any of these:
- workbench             = Basic Crafting Station for early recipies
- advanced_workbench    = Upgraded version of the workbench for mid-late game crafting
- anvil                 = Craft metal weapons, armor, and tools
- forge                 = Smelt ore and heat metals
- smelter               = Mroe industrious smelting at large batches
- grindstone            = Sharpen and refine tools and blades
- alchemy_table         = Craft potions, tonics, and magic items
- cauldron              = Brew Potions or stew ingredients
- enchanting_table      = Enchant weapons, armor, and tools
- magic_circle          = Special Station for high tier magical crafting
- campfire              = Cook Basic Meals
- cooking_pot           = Prepare Stews, soups, and recipies with multiple ingredients
- stove                 = Home or tavern-level cooking
- oven                  = Bake Bread, pastries, or other heated dishes
- grill                 = Roast meats or vegitables
- smoker                = Preserve meats over time
- carpenter_bench       = Used for woodworking, bows, and furniture
- tanning_rack          = Dry and prepare hides
- leatherworking_table  = Craft leather armor or items
- loom                  = Weave cloth or fibers
- sawmill               = Cut logs into boards or planks
- motar_petals          = Grind Herbs or minerals
- mill                  = Process grains or seeds
- refinery              = Refine materials like oil, coal, or ore
- kiln                  = Bake clay or pottery
- fishing_station       = Repair or craft fishing gear and bait
- tailoring_table       = Sew Clothing
- mechanical_table      = Build machines and components
- jewelcrafting_table   = Set Gems, craft all types of jewlery
- none                  = Handcrafted
- any_cooking           = works at any crafting station
- magic_station         = Works at any magical crafting station
- tool_specific:item_id    = Requires a tool instead of station

For the ```tags``` category, which is used to classify recipe categories or skill groups, it can be any of these:
- blacksmithing
- carpentry
- cooking
- farming
- alchemy
- survival
- combat
- magic
- fishing
- tailoring
- mining

