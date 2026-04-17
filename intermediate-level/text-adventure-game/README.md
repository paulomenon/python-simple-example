# Basic Text Adventure Game

Explore a mysterious house, collect items, unlock doors, and find your way out. A classic text-based adventure game built entirely with Python fundamentals.

## How to Run

```bash
python text_adventure.py
```

## Commands

| Command | Action |
|---|---|
| `go <direction>` | Move to another room (e.g. `go east`, `go up`) |
| `take <item>` | Pick up an item in the room |
| `inventory` | Show what you're carrying |
| `look` | Repeat the current room description |
| `quit` | Exit the game |

## Tips

- Explore every room — some items are needed to progress
- Locked doors require specific items to open
- The basement is dark; you'll need a light source

## Example

```
========================================
  THE MYSTERIOUS HOUSE
  A Text Adventure
========================================

--- Entrance ---
You stand in the entrance hall of an old house. Dust covers everything.
A grand staircase leads UP and a door opens to the EAST.
You see: rusty key
Exits: UP, EAST

> take rusty key
You picked up: rusty key

> go east

--- Kitchen ---
A dimly lit kitchen. Old pots and pans hang from the ceiling.
You see: flashlight
Exits: WEST, SOUTH

> take flashlight
You picked up: flashlight

> go south
You use the rusty key to unlock the door.
...
```

## What You'll Learn

- Using dictionaries as structured data (room definitions)
- Game state management (current room, inventory)
- Parsing user input with string methods
- Conditional logic for locked doors, dark rooms, and win conditions
