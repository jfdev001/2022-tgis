"""Outline of script for text-based adventure game.

This is too long tbh
"""

from random import random


def main():

    # Get your character's name
    name = input("Enter your character's name: ")

    # Enter your character's strength modifier
    strength = int(input(
        "Enter your character's strength modifier (0 to 3): "))

    if (strength < 0 or strength > 3):
        raise

    # Enter your character's intelligence modifier
    intelligence = int(input(
        "Enter your character's intelligence modifier (0 to 3): "))

    if (intelligence < 0 or intelligence > 3):
        raise

    # Enter your character's charisma modifier
    charisma = int(input(
        "Enter your character's charisma modifier (0 to 3): "))

    if (charisma < 0 or intelligence > 3):
        raise


if __name__ == '__main__':
    main()
