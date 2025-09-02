# Stargazer CLI - Study Version with Monthly Constellations
import random

# Optional: colored terminal output
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    class Fore:
        BLUE = ""
        GREEN = ""
        YELLOW = ""
        RED = ""
    class Style:
        BRIGHT = ""
        RESET_ALL = ""

# Constellation data with unique constellations per month
constellations = {
    "January": [
        {"name": "Orion", "type": "Hunter", "mythology": "Greek mythology - Orion was a giant huntsman whom Zeus placed among the stars."},
        {"name": "Taurus", "type": "Bull", "mythology": "Represents Zeus transforming into a bull in Greek mythology."}
    ],
    "February": [
        {"name": "Gemini", "type": "Twins", "mythology": "Represents the twin brothers Castor and Pollux from Greek mythology."},
        {"name": "Auriga", "type": "Charioteer", "mythology": "Represents a charioteer in Greek mythology, known for bright star Capella."}
    ],
    "March": [
        {"name": "Leo", "type": "Lion", "mythology": "Represents the Nemean Lion defeated by Hercules in Greek mythology."},
        {"name": "Cancer", "type": "Crab", "mythology": "Represents the giant crab sent to distract Hercules during his labors."}
    ],
    "April": [
        {"name": "Virgo", "type": "Maiden", "mythology": "Represents Astraea, the goddess of innocence and purity in Greek mythology."},
        {"name": "Bootes", "type": "Herdsman", "mythology": "Represents a herdsman or plowman in Greek mythology."}
    ],
    "May": [
        {"name": "Libra", "type": "Scales", "mythology": "Represents balance and justice, associated with Themis or Astraea."},
        {"name": "Canes Venatici", "type": "Hunting Dogs", "mythology": "Represents the hunting dogs of Bootes the herdsman."}
    ],
    "June": [
        {"name": "Scorpius", "type": "Scorpion", "mythology": "The scorpion that killed Orion in Greek mythology."},
        {"name": "Ophiuchus", "type": "Serpent Bearer", "mythology": "Represents a healer holding a serpent, linked to Asclepius."}
    ],
    "July": [
        {"name": "Sagittarius", "type": "Archer", "mythology": "Represents a centaur archer in Greek mythology."},
        {"name": "Capricornus", "type": "Sea Goat", "mythology": "Represents the goat-fish from Greek mythology."}
    ],
    "August": [
        {"name": "Aquarius", "type": "Water Bearer", "mythology": "Represents Ganymede, a beautiful youth taken by Zeus to serve as cupbearer."},
        {"name": "Lyra", "type": "Lyre", "mythology": "Represents Orpheus's lyre in Greek mythology."}
    ],
    "September": [
        {"name": "Pegasus", "type": "Winged Horse", "mythology": "Represents the winged horse from Greek mythology."},
        {"name": "Andromeda", "type": "Princess", "mythology": "Represents the princess chained to a rock to be sacrificed to a sea monster."}
    ],
    "October": [
        {"name": "Cassiopeia", "type": "Queen", "mythology": "Represents the vain queen punished by being placed in the sky."},
        {"name": "Perseus", "type": "Hero", "mythology": "Represents the hero who saved Andromeda from the sea monster."}
    ],
    "November": [
        {"name": "Auriga", "type": "Charioteer", "mythology": "Represents a charioteer, bright star Capella."},
        {"name": "Draco", "type": "Dragon", "mythology": "Represents the dragon Ladon guarding the golden apples."}
    ],
    "December": [
        {"name": "Orion", "type": "Hunter", "mythology": "Reappears in the winter sky."},
        {"name": "Canis Major", "type": "Big Dog", "mythology": "Represents Orion’s hunting companion, features Sirius, the brightest star."}
    ]
}

# Function to display all constellations
def list_all_constellations():
    print(Fore.BLUE + Style.BRIGHT + "\nAll Constellations:")
    for month, const_list in constellations.items():
        for c in const_list:
            print(f"{Fore.GREEN}{c['name']} ({month}) - Type: {c['type']}")

# Function to display constellations for a given month
def constellations_by_month(month):
    month_cap = month.capitalize()
    if month_cap in constellations:
        print(Fore.YELLOW + Style.BRIGHT + f"\nConstellations visible in {month_cap}:")
        for c in constellations[month_cap]:
            print(f"{Fore.GREEN}{c['name']} - Type: {c['type']}")
            print(f"{Fore.BLUE}Mythology: {c['mythology']}\n")
    else:
        print(Fore.RED + "No constellations found for this month. Check spelling and try again.")

# Function to show a random constellation
def random_constellation():
    month = random.choice(list(constellations.keys()))
    c = random.choice(constellations[month])
    print(Fore.YELLOW + Style.BRIGHT + "\nRandom Constellation:")
    print(f"{Fore.GREEN}{c['name']} ({month}) - Type: {c['type']}")
    print(f"{Fore.BLUE}Mythology: {c['mythology']}\n")

# Main menu function
def main():
    print(Fore.YELLOW + Style.BRIGHT + "Welcome to Stargazer CLI!\n")
    while True:
        print(Fore.BLUE + "Menu:")
        print("1. List all constellations")
        print("2. Search constellations by month")
        print("3. Show a random constellation")
        print("4. Exit")
        choice = input(Fore.GREEN + "Enter your choice (1-4): ").strip()

        if choice == "1":
            list_all_constellations()
        elif choice == "2":
            month = input(Fore.GREEN + "Enter a month: ").strip()
            constellations_by_month(month)
        elif choice == "3":
            random_constellation()
        elif choice == "4":
            print(Fore.YELLOW + "Goodbye! Clear skies ahead.")
            break
        else:
            print(Fore.RED + "Invalid choice. Please select 1-4.\n")

if __name__ == "__main__":
    main()
