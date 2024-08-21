import random

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
        
        if user_choice == "exit":
            print("Thanks for playing!")
            break
        
        if user_choice not in options:
            print("Invalid choice. feri hal ramroo herera.")
            continue
        
        computer_choice = random.choice(options)
        print(f"Computer choose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("Jitis ta mula!")
        else:
            print("Xya kaile jitna nasakne vais!")

# Run the game
rock_paper_scissors()
