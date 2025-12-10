# Shanette Nelson
# Computer Software Assignment


# input function

def input_character_information():
    name = input("Please provide your character name: ")
    race = input("Please provide race (Elf, Dwarf, Human): ")
    role = input("Enter character role (warrior, Mage): ")
    skill_level = int(input("Please provide skill level (1-5): "))
    wealth = int(input("Please provide wealth in gold coins: "))

    character = {
        "name": name,
        "race": race,
        "role": role,
        "skill_level": skill_level,
        "wealth": wealth
    }
    return character

# output / print function


def display_character_information(character):

    print("\n--- Here's your Character details ---")
    print(f"name           : {character['name']:9}")
    print(f"race           : {character['race']:9})")
    print(f"role           : {character['role']:9})")
    print(f"skill_level    : {character['skill_level']:9}")
    print(f"wealth         : {character['wealth']:9} gold coins")

# add character


def add_character(characters):
    print("\n--- Please add a Character ---")
    new_char = input_character_information()
    characters.append(new_char)
    print(f"\nCharacter '{new_char['name']}' added perfectly!")

# list characters


def list_characters(characters):
    print("\n--- List of Characters ---")

    if not characters:
        print("No characters has been added as yet, retry")

        return
    index = 1
    for character in characters:
        print(f"\nCharacter {index}")
        display_character_information(character)
        index += 1

# search by name


def search_character(characters):
    print("\n--- Please search for a Character ---")
    search_name = input("Please enter the character name to search for ")

    found = False
    for character in characters:
        if character['name'].lower() == search_name.lower():
            display_character_information(character)
            found = True

    if not found:
        print(f"No character found with the name '{search_name}'.")

# remove a character


def remove_character(characters):
    print("\n--- Remove a Character ---")
    name_to_remove = input(
        "Please enter the name of the character to remove: ")

    removed = False
    for character in characters:
        if character['name'].lower() == name_to_remove.lower():
            characters.remove(character)
            print(f"Character '{name_to_remove}' has been removed perfectly.")
            removed = True
            break

        if not removed:
            print(f"No character found with the name '{name_to_remove}'.")

# total wealth / logic


def calculate_total_wealth(characters):
    total = 0
    for character in characters:
        total += character["wealth"]
    return total

# shows total wealth


def show_total_wealth(characters):
    print("\n--- Total wealth of all the characters ---")

    if not characters:
        print("No characters have been added as yet, retry")
        return

    total = calculate_total_wealth(characters)
    print(f"The total wealth of all the characters is: {total} gold coins")

# menu / program


def main():
    characters = []
    choice = -1

    while choice != 0:
        print("\n---- Welcome to Fantasy Character Manager ----")
        print("1. Add a Character")
        print("2. List all Characters")
        print("3. Seacch for a Character by name")
        print("4. Remove a Character")
        print("5. Show total Wealth of all Characters")
        print("0. Exit")

        try:
            choice = int(input("Please select an option:"))
        except ValueError:
            print("invalid input. Please enter a number from 0 to 5.")
            choice = -1
            continue

        if choice == 1:
            add_character(characters)
        elif choice == 2:
            list_characters(characters)
        elif choice == 3:
            search_character(characters)
        elif choice == 4:
            remove_character(characters)
        elif choice == 5:
            show_total_wealth(characters)
        elif choice == 0:
            print("Goodbye!!")
        else:
            print("Invalid choice. Enter a number from 0 to 5.")

# run the program


if __name__ == "__main__":
    main()
