import time
import player

# Print Speed - control how fast text is printed to screen
def print_speed(text,speed=0):
    print(text)
    time.sleep(speed)

# Welcome Screen
def welcome_screen():
    print_speed('Welcome to Solo')
    print_speed('Every fall, solo canoe adventurers across the world gather \n'
            'along the banks of Lake Louisa to tackle one of the worlds toughest races.', 3)
    print_speed('Do you have what it takes to survive?', 1)

# Player Section
def player_setup():
    # Players Available
    zac_shades = player.Player("Zac Shades","Right On!", "Bummer Dude!","Zrx Super Paddle","Expert Rower" )
    jade_stiks = player.Player("Jade Stiks", "Woohoo!", "Oh! Come On!", "Canoe Cart", "Fast Trail Hiker")
    nikki_carr = player.Player("Nikki Carr", "That's it!", "Darn it!", "Firestarter", "Skilled in Bushcraft")
    iron_joe = player.Player("Iron Joe", "Heck Yeah", "Gimme a break man!", "Hunting Gear", "Hunter")

    players = {1:zac_shades, 2:jade_stiks, 3: nikki_carr, 4:iron_joe}

    print("Choose your player")

    # Load available players
    for x in players:
        print_speed(f"{x}: {players[x].player_name}")
        print_speed(f"Special Skill: {players[x].player_skill}")
        print_speed(f"Backpack Extras: {players[x].player_pack}")
        print("")

    # User chooses who they want to play as
    player1 =""
    user_input = int(input("Press 1, 2, 3, or 4 to choose your player: "))

    if user_input == 1:
        player1 = players[user_input]
        print(player1.player_name)
    elif user_input == 2:
        player1 = players[user_input]
        print(player1.player_name)
    elif user_input == 3:
        player1 = players[user_input]
        print(player1.player_name)
    elif user_input == 4:
        player1 = players[user_input]
        print(player1.player_name)
    else:
        print("Wrong")


# Game Play Instructions




# Play game



# welcome_screen()

