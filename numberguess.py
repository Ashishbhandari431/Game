import random
def numberguesssgame():
    nguess=random.randint(1,100)
    atmp=0
    print("Welcome to number guessing game")
    print("I am writing a random number between 1 to 100 pleasee guess it correct")
    while True:
        try:
            guess=int(input("Enter your guess:"))
            atmp+=1
    
            if guess<nguess:
                print("Your guess is too low")
            elif guess>nguess:
                print("Too high! please try once more")
            else:
                print(f"congratulations! you have guessed the correct number {nguess} in {atmp} attemps. \n You are the greate man")
                exit()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
numberguesssgame()