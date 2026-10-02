# Stephen
# Mini Portfolio I
# Zombie Survival Simulator
# This program simulates surviving a zombie apocalypse.
# The player must manage food, water, ammunition, and health
# while making strategic decisions to survive as many days as possible.
import random

class Player:
    def __init__(self):
        self.health = 100
        self.food = 5
        self.water = 5
        self.ammo = 10
        self.day = 1

    def show_stats(self):
        print("\n===== SURVIVOR STATUS =====")
        print(f"Day: {self.day}")
        print(f"Health: {self.health}")
        print(f"Food: {self.food}")
        print(f"Water: {self.water}")
        print(f"Ammo: {self.ammo}")

    def consume_resources(self):
        self.food -= 1
        self.water -= 1

        if self.food < 0:
            self.health -= 10

        if self.water < 0:
            self.health -= 15


def scavenge(player):
    print("\nYou search abandoned buildings...")

    event = random.randint(1, 4)

    if event == 1:
        found_food = random.randint(1, 3)
        player.food += found_food
        print(f"You found {found_food} food!")

    elif event == 2:
        found_water = random.randint(1, 3)
        player.water += found_water
        print(f"You found {found_water} water!")

    elif event == 3:
        found_ammo = random.randint(2, 6)
        player.ammo += found_ammo
        print(f"You found {found_ammo} ammo!")

    else:
        print("A zombie attacks!")

        if player.ammo > 0:
            player.ammo -= 1

            if random.randint(1, 10) > 3:
                print("You defeated the zombie.")
            else:
                player.health -= 20
                print("You were injured fighting the zombie.")
        else:
            player.health -= 25
            print("You had no ammo and got badly injured.")


def rest(player):
    print("\nYou spend the day resting.")
    player.health += 10

    if player.health > 100:
        player.health = 100


def travel(player):
    print("\nYou travel to a new area.")

    if random.randint(1, 10) <= 4:
        print("A zombie horde blocks your path!")

        if player.ammo >= 2:
            player.ammo -= 2
            print("You fought through the horde.")
        else:
            player.health -= 30
            print("You were hurt escaping the horde.")
    else:
        print("The trip was uneventful.")


def game():
    player = Player()

    print("=================================")
    print("     ZOMBIE SURVIVAL SIMULATOR")
    print("=================================")

    while player.health > 0:
        player.show_stats()

        print("\nChoose an action:")
        print("1. Scavenge")
        print("2. Rest")
        print("3. Travel")
        print("4. Quit")

        choice = input("\nSelection: ")

        if choice == "1":
            scavenge(player)

        elif choice == "2":
            rest(player)

        elif choice == "3":
            travel(player)

        elif choice == "4":
            print("\nYou decided to end your journey.")
            break

        else:
            print("Invalid choice.")
            continue

        player.consume_resources()
        player.day += 1

    if player.health <= 0:
        print("\nYou did not survive the apocalypse.")

    print(f"\nYou survived {player.day} days.")
    print("Game Over.")


game()
