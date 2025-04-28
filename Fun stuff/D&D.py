import random
charStats = []
inventory = []

# 1. Roll Dice
def rollDice(sides, count):
    dice_arr = list(range(1,sides+1))
    random_index = random.randint(0,sides-1)
    random_dice = dice_arr[random_index]
    return random_dice
# 2. Create Character
def createCharacter(charStats):
    # TODO: Ask for name, class, max HP, and set HP equal to max HP
    name = input("Input Your Character Name:")
    



# 2.5 Show Character
def showCharacter(charStats):
    pass  # TODO: Display all character attributes using f-strings

# 3. Take Damage
def takeDamage(charStats, damage):
    pass  # TODO: Subtract damage, check if HP is 0, and print "You have fallen!"

# 3.5 Death Saving Throws
def deathSavingThrows():
    pass  # TODO: Roll 3 d20s, pass if 2 rolls are 10 or higher, reset HP to 1 if successful

# 4. Heal HP
def healHP(charStats):
    pass  # TODO: Ask how many d8s to roll for healing, do not exceed max HP

# 5. Add Item
def addItem(inventory, item):
    pass  # TODO: Add an item to the inventory list

# 6. Remove Item
def removeItem(inventory, item):
    pass  # TODO: Remove an item from inventory if it exists

# 7. Show Inventory
def showInventory(inventory):
    pass  # TODO: Display all inventory items or print "Empty" if none

# Main Game Loop
def main():
    pass  # TODO: Implement game loop with user choices

# Run the game
main()
