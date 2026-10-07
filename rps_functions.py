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