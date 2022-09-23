import random
import termcolor

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player_points = 0
computer_points = 0
start_game = False

while True:
    print("To start the game type: start")
    start_input = input("").lower()
    if start_input == "start":
        start_game = True
        break
    elif start_input == "stop":
        break
    else:
        print("Invalid Input!")


while start_game:
    player_points = 0
    computer_points = 0
    player_move = input("Choose [r]ock, [p]aper, [s]cissors: ")
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        print("Invalid Input. Try again...")
        continue


    computer_random_number = random.randint(1, 3)
    computer_move = ''
    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors
    print(f"The computer chose {computer_move}")


    if player_move == rock and computer_move == scissors or \
        player_move == paper and computer_move == rock or \
            player_move == scissors and computer_move == paper:
        player_points += 1
        print(termcolor.colored("You win!", "green"))
        print(f"Player: {player_points} / Player_2: {computer_points}")
    elif player_move == computer_move:
        print(termcolor.colored("Draw.", 'yellow'))
        print(f"Player: {player_points} / Player_2: {computer_points}")
    else:
        computer_points += 1
        print(termcolor.colored("You lose!", "red"))
        print(f"Player: {player_points} / Player_2: {computer_points}")


    print("Do you want to play again?")
    print("Type 'yes' to continue or 'no' to exit the game.")
    again = input('')
    if again.lower() == "yes":
        continue
    if again.lower() == "no":
        start_game = False
