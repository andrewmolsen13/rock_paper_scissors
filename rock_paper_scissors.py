#rock paper scissors game!
#Custom functions to get the player choice and to determine the winner:
import random
def get_player_choice ():
    choice = input("\nEnter Rock, Paper, or Scissors: ").lower()
    while choice not in ("rock", "paper", "scissors"):
        choice = input(f"\nSorry, {choice} is not a valid answer. Please try again: ").lower()
    return choice

def determine_winner (choice, cpu_choice, rounds_played, player_win, cpu_win):
    if (choice == "rock" and cpu_choice == "paper") or (choice == "paper" and cpu_choice == "scissors") or \
        (choice == "scissors" and cpu_choice == "rock"):
        cpu_win += 1
        rounds_played += 1
        print(f"""The computer chose {cpu_choice}. You lose!""")
    elif choice == cpu_choice:
        print(f"The computer chose {cpu_choice} Tie! Try again: ")
    else:
        player_win += 1
        rounds_played += 1
        print(f"The computer chose {cpu_choice}. You win!")
    return player_win, cpu_win, rounds_played
    
#Ask the user how many games he wants to play
rounds = int(input("Welcome to Rock, Paper, Scissors! How many rounds do you want to play? "))

while rounds<= 0 or rounds % 2 == 0:
    rounds = int(input("\nInvalid input. Must enter a positive, odd number of rounds. Please try again: "))

rounds_played = 0
player_win = 0
cpu_win = 0

while rounds_played != rounds:
    cpu_choice = random.choice(["rock", "paper", "scissors"])
    player_choice = get_player_choice()
    player_win, cpu_win, rounds_played = determine_winner(player_choice, cpu_choice, rounds_played, player_win, cpu_win)
    
#Print out the final score, decide who wins
print(f"""\n--------------------------
Score: You: {player_win}| Computer: {cpu_win}
Rounds played: {rounds_played}""")


if player_win > cpu_win :
    print("\nYou win!")
else:
    print ("\nComputer wins!")

print("\nThanks for playing!")
