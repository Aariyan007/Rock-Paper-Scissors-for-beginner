import random

options = ["rock", "scissors", "paper"]

user_wins = 0
comp_wins = 0
print("\n")

while True:
    inp = input("Enter Rock/Paper/Scissors or 'q' to quit: ").lower()
    if inp == "q":
        break

    if inp not in options:
        print("Enter a valid option: ")
        continue

    pick = random.randint(0, 2)
    computer_sel = options[pick]
    print(f"The computer has picked {computer_sel}.")

    if (inp == "scissors" and computer_sel == "paper") or \
       (inp == "rock" and computer_sel == "scissors") or \
       (inp == "paper" and computer_sel == "rock"):
        print("You won!")
        user_wins += 1
    elif inp == computer_sel:
        print("TIE")
    else:
        print("You lost")
        comp_wins += 1

    print("\nScore:")
    print(f"Computer score: {comp_wins}")
    print(f"User score: {user_wins}")

print("Thanks for playing!")
