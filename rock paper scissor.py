import random

choices = ["Rock", "Paper", "Scissor"]

print("Welcome to Rock-Paper-Scissors!")
print("Here is the menu:")
print("1. Rock")
print("2. Paper")
print("3. Scissor")

while True:
    # Computer chooses inside the loop so it's new every time
    computer_choice = random.choice(choices)
    
    try:
        player_choice_num = int(input("\nEnter the number: "))
        
        # Check if input is valid (1, 2, or 3)
        if player_choice_num not in [1, 2, 3]:
            print("Please choose a number from the menu (1, 2, or 3).")
            continue
            
        # Get the player's choice string
        player_choice = choices[player_choice_num - 1]
        
        print(f"\nYou chose: {player_choice}")
        print(f"I chose: {computer_choice}")
        
        # Determine the winner
        if player_choice == computer_choice:
            print("It's a tie! 🤝")
        elif (player_choice == "Rock" and computer_choice == "Scissor") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissor" and computer_choice == "Paper"):
            print("You win! 🎉")
        else:
            print("I win! 😎")
            
        # Ask to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye! 👋")
            break
            
    except ValueError:
        print("Please enter a valid integer (1, 2, or 3).")