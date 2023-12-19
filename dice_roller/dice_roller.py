import random

def roll_dice():
    return random.randint(1, 6)

def display_dice(number):
    dice_lines = [
        "+-------+",
        "|       |",
        f"|   {number}   |",
        "|       |",
        "+-------+"
    ]
    return "\n".join(dice_lines)

result = roll_dice()
print(display_dice(result))
