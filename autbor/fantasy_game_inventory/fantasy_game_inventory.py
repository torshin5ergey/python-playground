"""
fantasy_game_inventory.py - Fantasy Game Inventory

Written by Sergey Torshin @torshin5ergey
Inspired by a practice project from Al Sweigart's book
"""

# Display inventory
def display_inventory(inventory: dict) -> None:
    print('Inventory:')
    # Counting total items
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total += v
    print(f'Total number of items: {item_total}')

# Add loot to the inventory
def add_to_inventory(inventory: dict, added_items: list) -> dict:
    for item in added_items:
        inventory.setdefault(item, 0) # If there's no item in the inventory, add it with value 0
        inventory[item] = inventory[item] + 1
    return inventory

def main():
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    stuff = add_to_inventory(stuff, dragon_loot)
    display_inventory(stuff)


if __name__ == '__main__':
    main()