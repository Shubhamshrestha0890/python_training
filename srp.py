import random

choices = ["r", "p", "s"]

while True:
    user = input("\nEnter r, p, or s (or 'exit' to quit): ").lower()

    if user == "exit":
        print("Game Over!")
        break

    if user not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    # Game Logic
    if user == computer:
        print("It's a tie!")
    elif (user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p"):
        print("You win!")
    else:
        print("Computer wins!")