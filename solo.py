import time
import player
import random

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
    zac_shades = player.Player("Zac Shades","Right On!", "Bummer Dude!","Zrx Echo Mark 3","12th Year in Competition. 2X Champion" )
    jade_stiks = player.Player("Jade Stiks", "Woohoo!", "Oh! Come On!", "Adirondack 750", "This years outstanding rookie. Posted fastest times in the trials this year.")
    nikki_carr = player.Player("Nikki Carr", "That's it!", "Darn it!", "1250 Firestarter", "Holds the world record for fastest time in the world ever! Back in competition after a 3 year injury break. ")
    iron_joe = player.Player("Iron Joe", "Heck Yeah", "Gimme a break man!", "Escape Speedster WRX", "Has been in the top 3 the last 3 years. Spent the last year training in the jungles of Northern Dutton.")

    players = {1:zac_shades, 2:jade_stiks, 3: nikki_carr, 4:iron_joe}

    print("Choose your player")

    # Load available players
    for x in players:
        print_speed(f"{x}: {players[x].player_name}")
        print_speed(f"Canoe: {players[x].player_canoe}")
        print_speed(f"Bio: {players[x].player_skill}")
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

# Broadcast Commentary - sets up a section that has commentary during game play
good_commentary = [f" just pulled off a great move. The skill involved in manuevering the canoe like that is superb",
                f"Wow. We've never seen that level of skill before.  must be happy with that move.",
                f"That's what we've come to expect from . Great job manuevering that.",
                f"Great move by . That was awesome.",
                f" How on earth did  pull that off. These are some top athletes for sure.",
                f" definitely wants to win this competition"]

flag_commentary = ["Nice job swooping in to get that flag", "Grabbed that flag just in time!", "Great technique to get that flag", f"worked hard for that flag"]

double_flag_commentary = ["Wow 2 flags there", "That's two flags picked up", "On a role with 2 flags picked up", "Great job!. Two flags picked up"]

bad_commentary = [f"Thats not a good look for . Let's look at that again.  paddle through but that large wave just push the canoe back.",
                f" will definitely feel that in the morning. It was a good effort but that wind was just too strong for that move.",
                f"Oh no. That's going to cost some points. The wind changed directions at the last moment.",
                f"Can make it through this? That was close. But, unfortunately that's going to cost some points",
                f"That was not a good move! What was thinking!",
                f"That's not the kind of maneuver you expect from a world class athlete.",
                f"You gotta do better than that if you want to win this competition.",
                f"I like what  was thinking there. But these waters are just too unpredictable."]

sensational_commentary = [f" has capsized!  is getting back in the canoe. But, that's a huge blow.  tried to avoid that rock!. But that last wave was just to big to handle",
                        f"Oh no. The canoe is lodged between those rocks.  is dislodging it but that going to costs big.",
                        f" has a lot of heart. Not many players would recover from their canoe being overturned by that wave.",
                        f"Does  think this competition is a joke. That could have been way more serious if the other players were not alert. That's gonna cost some points.",
                        f"It's heartbreaking to see a player's canoe get swamped like that. Hopefully,  can make up for those points deduction",
                        f"That's just a tough path to take. There's going to be some points penalty.",
                        f"The canoe must be punctured after going over those rocks"]



player_setup()
# Game Play Instructions
print_speed("Choose which line you'd like to take using 1, 2, 3, 4 or 5")
print_speed("This will advance you forward. Depending on what's under the card you choose will determine what happens as you move forward.")
print_speed("You'll need to advance 5 steps while maintaining remaining afloat to advance to the next round")



# Play game
def game_play():

    super_bad_outcome = 3
    bad_outcome = 1
    good_outcome = 0
    flag = 1
    bonus_flag = 2

    total_flags = 0
    player_life = 10

    outcomes = ["flag", "2 flags", "clear", "large swell", "sharp rocks"]
    game_board =['|A|','|B|','|C|','|D|','|E|']

    print(' '.join(game_board))


    game_tile = ""

    # Needs validation
    my_play = input("Choose Your Lane: A, B, C, D or E: ").lower()

    game_tile = random.choice(outcomes)

    if game_tile == outcomes[0]:
        print(random.choice(flag_commentary))
        total_flags = total_flags + flag
    if game_tile == outcomes[1]:
        print(random.choice(double_flag_commentary))
        total_flags = total_flags + bonus_flag
    if game_tile == outcomes[2]:
        print(random.choice(good_commentary))
    if game_tile == outcomes[3]:
        print(random.choice(bad_commentary))
        player_life = player_life - bad_outcome
    if game_tile == outcomes[4]:
        print(random.choice(sensational_commentary))
        player_life = player_life - super_bad_outcome
    
    print(total_flags)
    print(player_life)

game_play()


# welcome_screen()

