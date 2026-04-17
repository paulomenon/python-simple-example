# Basic Text Adventure Game
# Explore rooms, collect items, and find your way out of a mysterious house.

def create_world():
    """Define the rooms, descriptions, exits, and items."""
    return {
        "entrance": {
            "description": "You stand in the entrance hall of an old house. Dust covers everything. A grand staircase leads UP and a door opens to the EAST.",
            "exits": {"up": "upstairs_hallway", "east": "kitchen"},
            "items": ["rusty key"],
        },
        "kitchen": {
            "description": "A dimly lit kitchen. Old pots and pans hang from the ceiling. There's a door to the WEST and a locked door to the SOUTH.",
            "exits": {"west": "entrance", "south": "basement"},
            "items": ["flashlight"],
            "locked": {"south": "rusty key"},
        },
        "upstairs_hallway": {
            "description": "A narrow hallway with peeling wallpaper. Doors lead NORTH and SOUTH. Stairs go DOWN.",
            "exits": {"down": "entrance", "north": "library", "south": "bedroom"},
            "items": [],
        },
        "library": {
            "description": "Shelves of dusty books line the walls. A single book sits on a pedestal. The exit is to the SOUTH.",
            "exits": {"south": "upstairs_hallway"},
            "items": ["ancient map"],
        },
        "bedroom": {
            "description": "A small bedroom with a broken window. Moonlight shines in. The exit is NORTH.",
            "exits": {"north": "upstairs_hallway"},
            "items": ["gold coin"],
        },
        "basement": {
            "description": "You descend into a cold, dark basement. In the far corner you see a door with light behind it. There's an exit NORTH and an EXIT to the EAST.",
            "exits": {"north": "kitchen", "east": "escape"},
            "items": [],
            "requires_flashlight": True,
        },
        "escape": {
            "description": "You push open the door and find yourself outside in a moonlit garden. You've escaped the house!",
            "exits": {},
            "items": [],
            "is_exit": True,
        },
    }


def play():
    world = create_world()
    current_room = "entrance"
    inventory = []

    print("=" * 40)
    print("  THE MYSTERIOUS HOUSE")
    print("  A Text Adventure")
    print("=" * 40)
    print("\nCommands: go <direction>, take <item>, inventory, look, quit\n")

    while True:
        room = world[current_room]

        if room.get("is_exit"):
            print(f"\n{room['description']}")
            print(f"\nYou escaped with: {', '.join(inventory) if inventory else 'nothing'}")
            print("CONGRATULATIONS! You win!")
            break

        if room.get("requires_flashlight") and "flashlight" not in inventory:
            print("\nIt's pitch black! You can't see anything without a flashlight.")
            print("You stumble back the way you came.")
            current_room = "kitchen"
            continue

        print(f"\n--- {current_room.replace('_', ' ').title()} ---")
        print(room["description"])

        if room["items"]:
            print(f"You see: {', '.join(room['items'])}")

        exits = ", ".join(room["exits"].keys()).upper()
        print(f"Exits: {exits}")

        command = input("\n> ").lower().strip()

        if command == "quit":
            print("Thanks for playing!")
            break

        elif command == "look":
            continue

        elif command == "inventory":
            if inventory:
                print(f"You are carrying: {', '.join(inventory)}")
            else:
                print("Your inventory is empty.")

        elif command.startswith("take "):
            item = command[5:]
            if item in room["items"]:
                inventory.append(item)
                room["items"].remove(item)
                print(f"You picked up: {item}")
            else:
                print(f"There's no '{item}' here.")

        elif command.startswith("go "):
            direction = command[3:]
            if direction in room["exits"]:
                locked_doors = room.get("locked", {})
                if direction in locked_doors:
                    required_key = locked_doors[direction]
                    if required_key in inventory:
                        print(f"You use the {required_key} to unlock the door.")
                        del locked_doors[direction]
                        current_room = room["exits"][direction]
                    else:
                        print("The door is locked. You need a key.")
                else:
                    current_room = room["exits"][direction]
            else:
                print(f"You can't go '{direction}' from here.")

        else:
            print("I don't understand that command.")
            print("Try: go <direction>, take <item>, inventory, look, quit")


play()
