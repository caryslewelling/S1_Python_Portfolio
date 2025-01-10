#Carys
#11/21/2024
#Pokemon Evolution Game
#This project is a game in which people can evolve, train, and battle as a pokemon

#Initial
#Global Variables
pokemon_level = 0
pokemon_name = "snorlax"

#Functions
def evolve(): #ensures the pokemon advances over time
    global pokemon_name
    if pokemon_level > 5 and pokemon_level < 10:
        pokemon_name = "mew"
    if pokemon_level >= 10:
        pokemon_name = "pichu"
def train(): #causes the pokemon level to increase by one
    global pokemon_level
    pokemon_level = pokemon_level + 1
    global pokemon_level2
    pokemon_level2 = str(pokemon_level)
    print("Your pokemon level is " + pokemon_level2)
def gym_battle(): #causes the pokemon to either win or lose in a battle
    import random
    outcome = random.randint(1,2) #50% chance to win or lose
    if outcome == 1:
        print("You win!!")
    if outcome == 2:
        print("You lose!!")
def display_info(): #shows the pokemon level
    print("Your pokemon level is " + pokemon_level2)
    print("Your pokemon name is " + pokemon_name)
def quit(): #allows the user to stop playing
    print("Play again soon!")
def pokemon(): #all the functions in one
    print("Welcome to Pokemon Evolution")
    while True:
        print("Choose today's activity: ")
        print("""1. Train
    2. Gym Battle
    3. Rest (Display Info)
    4. Quit""")
        option = int(input("Make your choice (1-4)"))
        if option == 1:
            evolve()
            train()
        if option == 2:
            gym_battle()
        if option == 3:
            evolve()
            display_info()
        if option == 4:
            quit()
            break
#Main
pokemon()











#Main



